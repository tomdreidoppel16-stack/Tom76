# Video-Skills – TikTok / Reels / Shorts (v8)

## Skills

### 1. VIRAL_STORY_DIRECTOR (kostenlos)
Storyboards für 9:16-Videos: starker Einstieg in <1 Sekunde, eine klare Handlung pro Clip, konsistente Figuren, Spannungswechsel bei ca. 75 %, sauberer Loop-Schluss. Für ChatGPT als KI-Direktor nutzbar.

### 2. FREE_MOTION_CLIP (kostenlos, funktioniert)
`supercore_video_create_free(prompt, style, seconds, resolution)` erstellt eine MP4 mit animierten Originalzeichnungen (bei `fruit_drama` z.B. Erdbeere/Zitrone), Effekten, Captions und selbst synthetisiertem Beat. **Ist kein generiertes Live-Action- oder 3D-KI-Filmvideo.** Auf Render Free nur kurze Videos; generative Modelle laufen dort nicht.

### 3. CHARACTER_CONSISTENCY (kostenlos)
Lege vor mehreren KI-Clips eine Figurenbibel fest: Name, Farben, Augen, Kleidung, Merkmale, Beleuchtung. Verwende bei jedem Clip dieselben Hauptfiguren und Referenzbilder. Prüfe, ob Gesichter und Farben von Szene zu Szene konsistent bleiben.

### 4. AI_VIDEO_PROMPT (kostenlos vorbereitbar, GPU nötig)
`supercore_video_prepare_ai` erzeugt detaillierte text-to-video / image-to-video Prompts für das Open-Source-Modell **LTX-2.5 Fast** in LTX Desktop/ComfyUI. Es führt die KI-Inferenz **nicht** automatisch auf Render Free aus. LTX Desktop nennt für lokale Videos gewöhnlich 24 GB NVIDIA-VRAM und 32 GB RAM als Voraussetzung. Keine Cloud-Free-Unlimited-Zusage.

### 5. COMFYUI_AI_VIDEO_START (echte KI mit eigener oder gemieteter GPU)
`supercore_video_start_ai(workflow_json, prompt, confirm_external_job=True)` übergibt einen **echten** exportierten ComfyUI-API-Workflow an den vom Betreiber als `TOMGPT_COMFYUI_URL` konfigurierten Server. Workflow: LTX-2.5 Text/Bild-zu-Video in ComfyUI laden, im Textfeld `{{PROMPT}}` hinterlegen, **Export API Format** wählen. Rückgabe enthält die Job-ID; Video wird danach in ComfyUI gerendert. **Auf Render Free ohne externe GPU funktioniert das nicht.** Eine gemietete GPU könnte Geld kosten; ausdrückliche Zustimmung notwendig.

### 6. VIDEO_QUALITY_GATE (kostenlos für die Planung)
Prüfe vor dem Hochladen: Hook, Seitenverhältnis 9:16, keine abgeschittene Schrift, kein Wasserzeichen, legale Musik, keine fehlerhaften Figuren, Bewegung pro Szene, lesbare Untertitel und guter Schluss. Dies ist **eine redaktionelle Checkliste**, keine automatisierte KI-Bildprüfung.

## Gute Prompts

**KI-Früchte-Liebesdrama:**
> Originelle animierte 3D-Erdbeere mit großen braunen Augen und kleinen Blättern verliebt sich in eine schüchterne Zitrone. Kamera in extremen Nahaufnahmen, 9:16, filmisches warmes Licht. In der Mitte entdeckt sie eine herzförmige Nachricht eines anderen Charakters. Große emotionale Reaktion, konsistente Gesichter/Blätter/Farben, saubere Charakteranimation. Starker Hook in der ersten Sekunde; Ende mit emotionalem Cliffhanger. Keine generierte Schrift im Bild.

**Anime-Kampf:**
> Zwei originale Anime-Kämpfer mit klar unterscheidbaren Silhouetten kämpfen nachts auf einer verlassenen Dachterrasse. Dynamische Bewegungen, kurzer Stillstand vor dem Einschlag, deutliche Impact-Frames, hochwertiges 2D-Compositing, Lichtblitze und Kameraschwenks. Figuren bleiben über alle Einstellungen gleich. 9:16, 6 Sekunden, keine bestehenden Anime-Charaktere kopieren.

**Cyberpunk:**
> Eine einzelne Figur läuft durch eine neonbeleuchtete Regenstraße. Reflektierender Asphalt, volumetrischer Nebel, ruhige Dolly-Bewegung, klare Blickrichtung, ein markanter visueller Reveal am Ende, 9:16, hochwertige Filmkomposition.

## Kostenlose vs. hochwertige generative Videos

- Die Open-Source-Modelle lassen sich gratis lizenzrechtlich nutzen, benötigen aber beträchtliche **GPU-Leistung**.
- Auf einem eigenen geeigneten PC mit GPU kann LTX lokal Videoframes generieren (je nach Modellbedingungen).
- Kostenlose Web-Demos haben oft Warteschlangen, Wasserzeichen oder Nutzungsgrenzen; keine unbegrenzte kostenlose Erstellung versprechen.
- Render Free hat keinen für diese großen Modelle vorgesehenen GPU-Dienst. Der CPU-Skill ist die tatsächlich kostenfreie, dort grundsätzlich ausführbare Alternative.

Offizielle Informationen: https://docs.ltx.io/open-source-model/getting-started/quick-start und https://github.com/Lightricks/LTX-Desktop
