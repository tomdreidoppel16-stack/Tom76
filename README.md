# TomGPT SuperCore v8 · Video Skills · Flat GitHub Deploy

Dieses Repository funktioniert absichtlich **ohne Unterordner im GitHub-Hauptverzeichnis**. Beim Docker-Build erzeugt `boot.py` die interne Python-Ordnerstruktur aus `core_bundle.py`.

## Handy: In GitHub hochladen

1. `TomGPT_SuperCore_FLAT_VideoSkills_v8.zip` herunterladen und mit der Android-Datei-App **entpacken**.
2. Die **acht Dateien darin** (nicht die ZIP-Datei selbst!) auswählen.
3. Im Repository `Tom76` unter **Add file → Upload files** ins Hauptverzeichnis hochladen und **Commit changes** drücken. GitHub muss `Dockerfile`, `render.yaml`, `boot.py`, `core_bundle.py`, `requirements.txt`, `README.md`, `VIDEO_SKILLS.md`, `START_HIER.txt` anzeigen.
4. Render Dashboard → **New → Blueprint** oder **New Web Service → GitHub → Tom76** auswählen. Für Web Service Docker-Runtime und **Free** wählen. Die `render.yaml`-Blueprint-Variante erzeugt ein langes Zugriffstoken automatisch.
5. Render `/health` prüfen; `/mcp` benötigt weiterhin das geheime Zugriffstoken. Für ChatGPT ist zusätzlich eine zugelassene Verbindung erforderlich.

**Wichtig:** Das bloße Hochladen **nur der ZIP-Datei** reicht NICHT. GitHub/Render entpackt ZIP-Dateien im Repository nicht automatisch. Du brauchst aber keine Ordner manuell anzulegen.

## Video-Skills

- `supercore_video_skills`: ehrlich anzeigen, was kostenlos möglich ist.
- `supercore_video_plan`: Storybeats, Hook, konsistente Charaktere und einen Generierungs-Prompt erzeugen.
- `supercore_video_create_free`: tatsächliche originale animierte **MP4** in 9:16, mit Text, Figuren/Effekten und synthetischem Beat. **Kein KI-Diffusionsmodell** und keine fotorealistische Filmsequenz.
- `supercore_video_prepare_ai`: generatives Text-/Bild-zu-Video mit LTX/ComfyUI vorbereiten; der **KI-Render selbst** erfordert eine geeignete GPU/einen externen Dienst.
- `supercore_video_start_ai`: mit expliziter Bestätigung echten ComfyUI-GPU-Auftrag auslösen, falls `TOMGPT_COMFYUI_URL` gesetzt ist; kann GPU-Kosten verursachen.

Video-Ausgabe: serverseitig unter `TOMGPT_VIDEO_OUTPUT`; über einen **auf 1 Stunde begrenzten signierten Download-Link** abrufbar, wenn Hostname und Token konfiguriert sind.

## Technische Sicherheitsregeln

- `TOMGPT_MCP_TOKEN` nie in GitHub veröffentlichen. Es wird bei Render im Blueprint automatisch erzeugt.
- Ohne mindestens 32 Zeichen geheimes Token startet der MCP-Server nicht.
- Der freie Video-Renderer nutzt keine Fremd-APIs und keine urheberrechtlich geschützten Musikdateien.
- Render Free ist nicht für dauerhaften produktiven Betrieb ausgelegt: Dienst schläft ein, lokales Dateisystem ist flüchtig. Backup außerhalb des Servers nötig.
- 44.101 Agentenrollen sind verwaltet; **keine 44.101 gleichzeitig laufenden KI-Modelle**.
- ChatGPT ist die zentrale KI **während eines aktiven Chats**; der Server enthält keine unbegrenzte, autonome ChatGPT-Instanz.

## Lokal prüfen

```bash
python boot.py --verify
python boot.py --extract
pip install -r requirements.txt
python -m pytest tests
```

`pytest` ist nur für die lokale Entwicklung notwendig. Zum Start `TOMGPT_MCP_TOKEN` als sichere Umgebungsvariable definieren und `python -m tomgpt.server` ausführen.
