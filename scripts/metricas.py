#!/usr/bin/env python3
"""Burndown y burnup por sprint a partir de GitHub (TravelWrap).

Convenciones (ver diagramas/COMO-USAR.md):
  - Sprint = milestone "S1".."S4". Fin = fecha del milestone; inicio = día siguiente al fin del anterior.
  - PBI   = issue cuyo título empieza por "PB-NN " (con milestone del sprint).
  - Tarea = issue cuyo título empieza por "PB-NN.x.y " (sprint: el suyo o el de su PBI).
  - Horas estimadas: línea "Estimación: 2.5 h" en el cuerpo de la tarea.
    Una PBI sin tareas cuenta como su propia tarea con su "Estimación".
  - Puntos de historia: línea "Puntos de historia: 5" en el cuerpo de la PBI.
  - Hecho = issue cerrada (si se cierra como "not planned" sale del alcance).

Histórico: diagramas/historico.json guarda una foto por día. Los días pasados no se
reescriben, así que re-estimar o añadir tareas solo afecta desde ese día (la curva sube).
Durante los primeros DIAS_PLANIFICACION días del sprint el compromiso (inicio de la
línea ideal) se ajusta solo al total actual; después queda fijo.

Variables: GITHUB_TOKEN, GITHUB_REPOSITORY, REINICIAR (sprint a reconstruir, opcional),
RECOMPROMETER (sprint cuyo compromiso se fija al total actual, opcional),
MOCK_DIR (pruebas: issues.json y milestones.json), HOY (pruebas: AAAA-MM-DD).
"""
import json
import os
import re
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

TZ = ZoneInfo("Europe/Madrid")
PRIMER_SPRINT = 2          # se empieza a medir en S2
DIAS_PLANIFICACION = 2     # días iniciales en los que el compromiso aún se ajusta
RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "diagramas"
HIST = OUT / "historico.json"

RE_PBI = re.compile(r"^PB-(\d+)\s")
RE_TAREA = re.compile(r"^PB-(\d+)(?:\.\d+)+\s")
RE_SPRINT = re.compile(r"^S(\d+)$", re.I)
_NUM = r"\**\s*[:=]\s*\**\s*(\d+(?:[.,]\d+)?)"
RE_HORAS = re.compile(r"(?im)^[\s>*_-]*estimaci[oó]n" + _NUM + r"\s*h")
RE_SP = re.compile(r"(?im)^[\s>*_-]*puntos\s+de\s+historia" + _NUM)


# ---------------------------------------------------------------- datos
def api(ruta):
    repo, token = os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"]
    res, pag = [], 1
    while True:
        sep = "&" if "?" in ruta else "?"
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/{ruta}{sep}per_page=100&page={pag}",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2022-11-28"})
        with urllib.request.urlopen(req) as r:
            lote = json.load(r)
        if not lote:
            return res
        res += lote
        pag += 1


def cargar():
    mock = os.environ.get("MOCK_DIR")
    if mock:
        return (json.load(open(Path(mock) / "issues.json", encoding="utf-8")),
                json.load(open(Path(mock) / "milestones.json", encoding="utf-8")))
    return ([i for i in api("issues?state=all") if "pull_request" not in i],
            api("milestones?state=all"))


def dia(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(TZ).date() if iso else None


def num(rx, texto):
    m = rx.search(texto or "")
    return float(m.group(1).replace(",", ".")) if m else None


def sprints_de(milestones):
    fines = {}
    for m in milestones:
        k = RE_SPRINT.match(m["title"].strip())
        if k and m.get("due_on"):
            fines[int(k.group(1))] = dia(m["due_on"])
    res = {}
    for n in sorted(fines):
        if n >= PRIMER_SPRINT and n - 1 in fines:
            res[f"S{n}"] = (fines[n - 1] + timedelta(1), fines[n])
    return res


def modelo(issues):
    pbis, tareas = {}, []
    for i in issues:
        t = i["title"].strip()
        base = {"num": i["number"], "titulo": t, "creada": dia(i["created_at"]),
                "cerrada": dia(i["closed_at"]) if i["state"] == "closed" else None,
                "descartada": i["state"] == "closed" and i.get("state_reason") == "not_planned",
                "sprint": (i.get("milestone") or {}).get("title", "").strip().upper() or None,
                "horas": num(RE_HORAS, i.get("body")), "sp": num(RE_SP, i.get("body"))}
        if RE_PBI.match(t):
            base["id"] = int(RE_PBI.match(t).group(1))
            pbis[base["id"]] = base
        elif RE_TAREA.match(t):
            base["pbi"] = int(RE_TAREA.match(t).group(1))
            tareas.append(base)
    for ta in tareas:
        if not ta["sprint"] and ta["pbi"] in pbis:
            ta["sprint"] = pbis[ta["pbi"]]["sprint"]
    return pbis, tareas


def foto(sp, pbis, tareas, d, usar_creacion):
    """Estado del sprint al final del día d."""
    def existe(x):
        return not x["descartada"] and (not usar_creacion or x["creada"] <= d)

    def hecha(x):
        return x["cerrada"] is not None and x["cerrada"] <= d

    p_sp = [p for p in pbis.values() if p["sprint"] == sp and existe(p)]
    con_tareas = {t["pbi"] for t in tareas if t["sprint"] == sp and existe(t)}
    trabajo = [t for t in tareas if t["sprint"] == sp and existe(t)]
    trabajo += [p for p in p_sp if p["id"] not in con_tareas]
    total = sum(x["horas"] or 0 for x in trabajo)
    return {
        "total_h": round(total, 2),
        "restante_h": round(sum(x["horas"] or 0 for x in trabajo if not hecha(x)), 2),
        "sp_objetivo": sum(p["sp"] or 0 for p in p_sp),
        "sp_hecho": sum(p["sp"] or 0 for p in p_sp if hecha(p)),
    }, trabajo, p_sp


# ---------------------------------------------------------------- gráficas
def ejes(ax, ini, n):
    ax.set_xticks(range(1, n + 1))
    ax.set_xticklabels([f"{k}\n{ini + timedelta(k - 1):%d/%m}" for k in range(1, n + 1)], fontsize=7.5)
    ax.set_xlim(0.5, n + 0.5)
    ax.set_xlabel("Días dentro del sprint")
    ax.grid(axis="y", alpha=0.3)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def graficas(sp, ini, fin, h, hoy):
    n = (fin - ini).days + 1
    dias = sorted(h["dias"])
    xs = [(date.fromisoformat(d) - ini).days + 1 for d in dias]
    comp = h.get("compromiso_h", 0)

    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax.plot([1, n], [comp, 0], "--", color="#9aa0a6", lw=1.2, label=f"Ideal (compromiso {comp:g} h)")
    ax.plot(xs, [h["dias"][d]["restante_h"] for d in dias], "-o", color="#1f5fd6", lw=2.6,
            ms=6, mfc="#0b2a66", label="Restante")
    ax.set_ylabel("Horas estimadas restantes")
    ax.set_ylim(bottom=0)
    ejes(ax, ini, n)
    ax.set_title(f"Burndown {sp} ({ini:%d/%m} - {fin:%d/%m})")
    ax.legend(frameon=False)
    fig.tight_layout(); fig.savefig(OUT / f"burndown_{sp}.png", dpi=130); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 4.6))
    obj = [h["dias"][d]["sp_objetivo"] for d in dias]
    ax.step(xs + [n + 0.5], obj + obj[-1:], where="post", color="black", lw=2, label="Objetivo")
    ax.plot(xs, [h["dias"][d]["sp_hecho"] for d in dias], "-o", color="#1f3fbf", lw=2.6, ms=6,
            mfc="#8ab4f8", label="Completado")
    ax.set_ylabel("Puntos de historia")
    ax.set_ylim(0, max(obj + [1]) * 1.15)
    ejes(ax, ini, n)
    ax.set_title(f"Burnup {sp} ({ini:%d/%m} - {fin:%d/%m})")
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout(); fig.savefig(OUT / f"burnup_{sp}.png", dpi=130); plt.close(fig)


# ---------------------------------------------------------------- principal
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    issues, milestones = cargar()
    hoy = date.fromisoformat(os.environ["HOY"]) if os.environ.get("HOY") else datetime.now(TZ).date()
    pbis, tareas = modelo(issues)
    sprints = sprints_de(milestones)
    hist = json.loads(HIST.read_text(encoding="utf-8")) if HIST.exists() else {}
    reiniciar = (os.environ.get("REINICIAR") or "").strip().upper()
    if reiniciar in hist:
        del hist[reiniciar]
    recomprometer = (os.environ.get("RECOMPROMETER") or "").strip().upper()

    avisos, bloques = [], []
    for sp, (ini, fin) in sprints.items():
        if ini > hoy:
            continue
        nuevo = sp not in hist
        h = hist.setdefault(sp, {"dias": {}})
        ultimo = min(hoy, fin)
        d = ini
        while d <= ultimo:
            k = d.isoformat()
            if d == hoy or k not in h["dias"]:
                # hoy: estado actual. Huecos: reconstrucción con fechas de cierre
                # (al crear el histórico de un sprint se asume que todo existía desde el día 1).
                f, _, _ = foto(sp, pbis, tareas, d, usar_creacion=not nuevo and d != hoy)
                h["dias"][k] = f
            d += timedelta(1)
        if hoy < ini + timedelta(DIAS_PLANIFICACION) or sp == recomprometer:
            h["compromiso_h"] = h["dias"][ultimo.isoformat()]["total_h"]   # aún planificando / reajuste manual
        elif "compromiso_h" not in h:
            h["compromiso_h"] = h["dias"][ini.isoformat()]["total_h"]

        _, trabajo, p_sp = foto(sp, pbis, tareas, ultimo, usar_creacion=False)
        sin_h = [f"#{x['num']}" for x in trabajo if x["horas"] is None]
        sin_sp = [f"#{p['num']}" for p in p_sp if p["sp"] is None]
        if sin_h:
            avisos.append(f"- {sp}: sin «Estimación: X h» → {', '.join(sin_h)}")
        if sin_sp:
            avisos.append(f"- {sp}: PBIs sin «Puntos de historia: N» → {', '.join(sin_sp)}")

        graficas(sp, ini, fin, h, hoy)
        u = h["dias"][ultimo.isoformat()]
        estado = "en curso" if hoy <= fin else "terminado"
        bloques.append(
            f"### {sp} ({ini:%d/%m} - {fin:%d/%m}, {estado})\n\n"
            f"Quedan **{u['restante_h']:g} h** de {u['total_h']:g} h estimadas · "
            f"**{u['sp_hecho']:g} / {u['sp_objetivo']:g}** puntos de historia hechos\n\n"
            f"![Burndown {sp}](diagramas/burndown_{sp}.png)\n![Burnup {sp}](diagramas/burnup_{sp}.png)\n")

    HIST.write_text(json.dumps(hist, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")

    texto = ["<!-- METRICAS:START -->", "## Métricas del sprint", "",
             f"_Actualizado automáticamente el {datetime.now(TZ):%d/%m/%Y %H:%M}._", ""]
    texto += list(reversed(bloques)) or ["Aún no ha empezado ningún sprint medido."]
    if avisos:
        texto += ["", "**Pendiente de estimar:**", ""] + avisos
    texto.append("<!-- METRICAS:END -->")
    bloque = "\n".join(texto)
    readme = RAIZ / "README.md"
    txt = readme.read_text(encoding="utf-8") if readme.exists() else "# Gestión\n"
    if "<!-- METRICAS:START -->" in txt:
        txt = re.sub(r"<!-- METRICAS:START -->.*?<!-- METRICAS:END -->", lambda _: bloque, txt, flags=re.S)
    else:
        txt = txt.rstrip() + "\n\n" + bloque + "\n"
    readme.write_text(txt, encoding="utf-8")
    print("\n".join(bloques + avisos) or "Nada que medir todavía")


if __name__ == "__main__":
    main()