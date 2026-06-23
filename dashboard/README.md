# Creta dashboards

- `creta_3d_dashboard.yaml` — sections dashboard with a rotatable 3D car hero (iframe -> /local/creta3d/index.html) plus controls, 360 camera, status, map, diagnostics.
- `creta_dashboard.yaml` — simpler list dashboard (no 3D).
- `creta3d/index.html` — model-viewer page. Deploy to HA `www/creta3d/` (served at `/local/creta3d/`).

## 3D model
Drop a `creta.glb` next to `index.html` in `www/creta3d/`. Placeholder used: Khronos CC0 "ToyCar"
(https://github.com/KhronosGroup/glTF-Sample-Assets). Replace with a real Creta `.glb` for an exact look.
