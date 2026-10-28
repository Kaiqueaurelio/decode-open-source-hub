import json
import re

hub = "/home/decodeanalytics/.gemini/antigravity/scratch/decode-hub"
with open(f"{hub}/data/software.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

cards_html = []
for item in catalog:
    slug = item["slug"]
    name = item["name"]
    tagline = item.get("tagline", "")
    desc = item.get("description", tagline)
    source = item.get("sourceUrl", "")
    download = item.get("downloadWindowsExe") or item.get("downloadUrl", "")
    accent = "#2563eb"
    if slug == "decode-craft": accent = "#a855f7"
    elif slug == "decode-craftx": accent = "#ec4899"
    elif slug == "decode-clip": accent = "#06b6d4"
    elif slug == "decode-launcher": accent = "#fbbf24"

    clean = name.replace("Decode ", "").replace("Decode", "")
    card = f"""      <div class="software-card app-{slug}" id="card-{slug}" data-slug="{slug}">
        <span aria-hidden="true" class="card-hover-accent" style="background:{accent};"></span>
        <div class="card-header-bar">
          <span class="card-version-badge" style="color:{accent};">v0.8.3</span>
          <a class="card-github-link" href="{source}" target="_blank" rel="noopener noreferrer">GITHUB ↗</a>
        </div>
        <div class="card-main-content">
          <div class="card-icon-box" style="background:rgba(255,255,255,0.06); border-color:{accent}33;">
            <img class="card-app-icon-img" src="assets/app-icons/{slug}.png" alt="{name}" loading="lazy">
          </div>
          <div class="card-title-group">
            <h3 class="card-title">
              <span class="brand-prefix">Decode</span><span class="craft-suffix" style="color:{accent};">{clean}</span>
            </h3>
            <p class="card-tagline">{tagline}</p>
          </div>
        </div>
        <p class="card-description">{desc}</p>
        <p class="card-last-updated">Última atualização: 28 de out. de 2026</p>
        <div class="card-action-bar">
          <a class="card-btn-download" href="{download}" target="_blank" rel="noopener noreferrer">
            <span>ABRIR / BAIXAR</span>
          </a>
          <button type="button" class="card-explore-trigger" data-open-modal="{slug}" title="Mais opções para {name}">
            <span>···</span>
          </button>
        </div>
      </div>"""
    cards_html.append(card)

static_grid_content = "\n" + "\n".join(cards_html) + "\n    "

for repo_path in [
    "/home/decodeanalytics/.gemini/antigravity/scratch/decode-hub/index.html",
    "/home/decodeanalytics/.gemini/antigravity/scratch/decodecad-upstream/index.html",
    "/home/decodeanalytics/decode-open-source-hub/index.html"
]:
    with open(repo_path, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = r'(<div class="software-grid" id="software-grid" aria-live="polite">)[\s\S]*?(</div>\s*</main>)'
    replacement = r"\1" + static_grid_content + r"\2"
    new_html = re.sub(pattern, replacement, html)

    with open(repo_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Updated static fallback cards in {repo_path}")
