#!/usr/bin/env python3
"""Turn research/empresas-h1b.csv into research/empresas-h1b.json for the panel.

Adds a salary flag: values above 1,000,000 are almost certainly unit errors and are
blanked (None) in the panel data; the raw value is kept in salario_max_fuente.
Values above 500,000 are flagged for manual review. Nothing is corrected silently.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "research" / "empresas-h1b.csv"
DST = ROOT / "research" / "empresas-h1b.json"


def num(value):
    try:
        return int(float(value)) if value not in ("", None) else 0
    except ValueError:
        return 0


def flag(row):
    top = max(num(row["salario_max"]), 0)
    if top > 1_000_000:
        return "error_probable"
    if top > 500_000:
        return "revisar"
    return ""


def wage(value, row):
    # Wages flagged as probable unit errors are blanked, not used in the panel.
    return None if flag(row) == "error_probable" else num(value)


rows = []
with SRC.open(encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        rows.append({
            "empresa": r["empresa"],
            "nombres_legales": r["nombres_legales_usados"],
            "soc": r["SOC"],
            "fy2024": num(r["LCA_FY2024"]),
            "fy2025": num(r["LCA_FY2025"]),
            "fy2026": num(r["LCA_FY2026"]),
            "titulo": r["titulo_puesto"],
            "ciudad": r["ciudad"],
            "salario_min": wage(r["salario_min"], r),
            "salario_mediana": wage(r["salario_mediana"], r),
            "salario_max": wage(r["salario_max"], r),
            "salario_max_fuente": r["salario_max"],
            "salario_flag": flag(r),
            "e_verify": r["E-Verify"],
            "url_carreras": r["URL_carreras"],
            "patrocinio": r["lenguaje_patrocinio"],
            "practicas_f1": r["practicas_F1"],
            "confianza": r["nivel_confianza"],
            "fecha_consulta": r["fecha_consulta"],
        })

DST.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {len(rows)} rows to {DST.name}; flagged salaries:",
      sum(1 for r in rows if r["salario_flag"]))
