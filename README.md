# RoaDtofuture

- `index.html` — investigación de empresas con sponsorship H-1B / OPT y mi plan de acción.
- `resume/` — mi resume como sitio web.

## Resume: cómo funciona

Todo el contenido vive en **`resume/resume.json`** (formato estándar [JSON Resume](https://jsonresume.org/schema)).
`resume/index.html` solo lo dibuja; nunca hace falta tocar el HTML.

**Para actualizarlo con Claude:** abre una sesión de Claude Code sobre este repo y pide el cambio
(“agrega mi internship en X”, “adapta el resumen para Data Analyst”). Claude edita `resume.json`,
corre `python3 scripts/check_resume.py` y hace push. GitHub Pages publica la nueva versión en ~1 minuto.

- Texto entre `[corchetes]` = pendiente de llenar; se marca en amarillo en pantalla.
- Fechas: `YYYY`, `YYYY-MM` o `YYYY-MM-DD`. `endDate` vacío = “Present”.
- **Download PDF** imprime una versión limpia en tamaño carta.
- El workflow `Check resume` valida el JSON en cada push.

## Publicar (una sola vez)

GitHub → **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*,
Branch = `main`, carpeta `/ (root)`. Queda en `https://siiick78.github.io/RoaDtofuture/resume/`.

## Ver en local

```sh
python3 -m http.server   # luego abre http://localhost:8000/resume/
```
