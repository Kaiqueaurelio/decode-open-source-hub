#!/usr/bin/env python3
"""Generate ultra-polished, modern, unified Decode Analytics suite icons.

Every icon follows the Decode Design System:
- Dark sleek squircle base (#0d111a) with subtle inner gradient & neon rim
- The official Decode Analytics clover node mark embedded as brand hallmark
- Distinct high-contrast functional glyph for each tool:
  * photocraft: Camera aperture with focus ring
  * vectorcraft: Pen tool nib with bezier control nodes
  * filmcraft: Cinematic clapperboard / film frame with playback triangle
  * lightcraft: Sunburst aperture / color grading wheel
  * pdfcraft: Clean document sheet with folded corner & PDF vector lines
  * effectcraft: Visual FX magic wand with particle burst
  * designcraft: Layout artboards with vector guides & ruler
  * figcraft: Prototyping component diamond with smart layout flow
  * wordcraft: Typography ligature 'W' with dynamic text lines
  * soundcraft: Stereo equalizer spectrum waveform with audio jack
  * deckcraft: Presentation slide projection with rising analytics trend
  * cadcraft: Precision engineering drafting compass with crosshair snaps
  * gridcraft: Spreadsheet database table matrix with active formula cell
  * decode-craft: Neural network node matrix with generative AI spark
  * decode-craftx: Quantum AI prism with hyper-speed laser vector
  * decode-clip: Video scissors cutting filmstrip / social viral short badge
  * decode-launcher: Official Decode Analytics clover mark with orbital energy ring
"""

import math
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageOps

REPO_ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_MARK_PATH = REPO_ROOT / "launcher" / "docs" / "brand" / "decode-mark.png"

# App configurations: slug, name, folder, primary_rgb, accent_rgb, type
APPS = [
    {
        "slug": "photocraft",
        "name": "Decode Photo",
        "folder": "decode-photo",
        "color": (59, 130, 246),       # #3B82F6 Vibrant Blue
        "accent": (56, 189, 248),      # #38BDF8 Sky Cyan
        "type": "photo",
    },
    {
        "slug": "vectorcraft",
        "name": "Decode Vector",
        "folder": "decode-vector",
        "color": (239, 68, 68),        # #EF4444 Crimson Red
        "accent": (249, 115, 22),      # #F97316 Bright Orange
        "type": "vector",
    },
    {
        "slug": "filmcraft",
        "name": "Decode Film",
        "folder": "decode-film",
        "color": (147, 51, 234),       # #9333EA Electric Violet
        "accent": (192, 132, 252),     # #C084FC Lavender Neon
        "type": "film",
    },
    {
        "slug": "lightcraft",
        "name": "Decode Light",
        "folder": "decode-light",
        "color": (245, 158, 11),       # #F59E0B Amber
        "accent": (253, 224, 71),      # #FDE047 Vivid Yellow
        "type": "light",
    },
    {
        "slug": "pdfcraft",
        "name": "Decode PDF",
        "folder": "decode-pdf",
        "color": (16, 185, 129),       # #10B981 Emerald
        "accent": (52, 211, 153),      # #34D399 Mint
        "type": "pdf",
    },
    {
        "slug": "effectcraft",
        "name": "Decode Effect",
        "folder": "decode-effect",
        "color": (236, 72, 153),       # #EC4899 Magenta
        "accent": (244, 114, 182),     # #F472B6 Pink
        "type": "effect",
    },
    {
        "slug": "designcraft",
        "name": "Decode Design",
        "folder": "decode-design",
        "color": (217, 70, 239),       # #D946EF Fuchsia
        "accent": (240, 171, 252),     # #F0ABFC Orchid
        "type": "design",
    },
    {
        "slug": "figcraft",
        "name": "Decode Fig",
        "folder": "decode-fig",
        "color": (20, 184, 166),       # #14B8A6 Teal
        "accent": (94, 234, 212),      # #5EEAD4 Aquamarine
        "type": "fig",
    },
    {
        "slug": "wordcraft",
        "name": "Decode Word",
        "folder": "decode-word",
        "color": (37, 99, 235),        # #2563EB Deep Blue
        "accent": (96, 165, 250),      # #60A5FA Light Blue
        "type": "word",
    },
    {
        "slug": "soundcraft",
        "name": "Decode Sound",
        "folder": "decode-sound",
        "color": (79, 70, 229),        # #4F46E5 Indigo
        "accent": (165, 180, 252),     # #A5B4FC Soft Indigo
        "type": "sound",
    },
    {
        "slug": "deckcraft",
        "name": "Decode Deck",
        "folder": "decode-deck",
        "color": (234, 88, 12),        # #EA580C Warm Tangerine
        "accent": (251, 146, 60),      # #FB923C Peach Accent
        "type": "deck",
    },
    {
        "slug": "cadcraft",
        "name": "Decode CAD",
        "folder": "decode-cad",
        "color": (14, 165, 233),       # #0EA5E9 Sky Blue
        "accent": (125, 211, 252),     # #7DD3FC Soft Cyan
        "type": "cad",
    },
    {
        "slug": "gridcraft",
        "name": "Decode Grid",
        "folder": "decode-grid",
        "color": (22, 163, 74),        # #16A34A Forest Green
        "accent": (74, 222, 128),      # #4ADE80 Lime Green
        "type": "grid",
    },
    {
        "slug": "decode-craft",
        "name": "DecodeCraft",
        "folder": "decode-craft",
        "color": (139, 92, 246),       # #8B5CF6 Purple
        "accent": (216, 180, 254),     # #D8B4FE Pastel Violet
        "type": "craft",
    },
    {
        "slug": "decode-craftx",
        "name": "DecodeCraftX",
        "folder": "decode-craftx",
        "color": (244, 63, 94),        # #F43F5E Rose Red
        "accent": (251, 113, 133),     # #FB7185 Coral
        "type": "craftx",
    },
    {
        "slug": "decode-clip",
        "name": "DecodeClip",
        "folder": "decode-clip",
        "color": (225, 29, 72),        # #E11D48 Carmine
        "accent": (253, 164, 175),     # #FDA4AF Light Rose
        "type": "clip",
    },
    {
        "slug": "decode-launcher",
        "name": "Decode Launcher",
        "folder": "launcher",
        "color": (37, 99, 235),        # #2563EB Blue
        "accent": (56, 189, 248),      # #38BDF8 Cyan
        "type": "launcher",
    },
]

def load_official_mark():
    if OFFICIAL_MARK_PATH.exists():
        return Image.open(OFFICIAL_MARK_PATH).convert("RGBA")
    return None

def draw_glyph(draw, app_type, center, radius, color, accent):
    cx, cy = center
    c_col = color + (255,)
    a_col = accent + (255,)
    white = (255, 255, 255, 255)
    
    if app_type == "photo":
        # Professional Camera with lens aperture rings & focus reflection
        w = radius * 1.3
        h = radius * 0.95
        # Camera body
        draw.rounded_rectangle([cx - w, cy - h*0.7, cx + w, cy + h*0.9], radius=16, outline=c_col, width=6)
        # Top prism
        draw.polygon([(cx - w*0.35, cy - h*0.7), (cx + w*0.35, cy - h*0.7), (cx + w*0.2, cy - h), (cx - w*0.2, cy - h)], fill=c_col)
        # Big central lens
        lens_r = radius * 0.58
        draw.ellipse([cx - lens_r, cy - lens_r*0.8, cx + lens_r, cy + lens_r*1.2], outline=a_col, width=8)
        inner_r = lens_r * 0.55
        draw.ellipse([cx - inner_r, cy - inner_r*0.6 + 6, cx + inner_r, cy + inner_r*1.4 + 6], fill=c_col)
        # Glint
        draw.ellipse([cx - inner_r*0.4, cy - inner_r*0.2, cx + inner_r*0.2, cy + inner_r*0.4], fill=white)
        # Shutter button
        draw.rounded_rectangle([cx + w*0.5, cy - h*0.85, cx + w*0.8, cy - h*0.7], radius=4, fill=a_col)

    elif app_type == "vector":
        # Precision Pen Tool Nib & Bezier vector control handles
        # Pen Nib
        nib = [
            (cx, cy - radius * 1.15),
            (cx + radius * 0.7, cy + radius * 0.5),
            (cx + radius * 0.35, cy + radius * 0.5),
            (cx, cy + radius * 0.8),
            (cx - radius * 0.35, cy + radius * 0.5),
            (cx - radius * 0.7, cy + radius * 0.5),
        ]
        draw.polygon(nib, fill=c_col, outline=a_col)
        # Center split
        draw.line([(cx, cy - radius * 0.4), (cx, cy + radius * 0.8)], fill=white, width=5)
        draw.ellipse([cx - 8, cy - radius * 0.45 - 8, cx + 8, cy - radius * 0.45 + 8], fill=white)
        # Control handle dots
        draw.line([(cx - radius*1.1, cy + radius*0.85), (cx + radius*1.1, cy + radius*0.85)], fill=a_col, width=4)
        draw.rectangle([cx - radius*1.1 - 7, cy + radius*0.85 - 7, cx - radius*1.1 + 7, cy + radius*0.85 + 7], fill=white)
        draw.rectangle([cx + radius*1.1 - 7, cy + radius*0.85 - 7, cx + radius*1.1 + 7, cy + radius*0.85 + 7], fill=white)

    elif app_type == "film":
        # Hollywood Film Clapperboard with cinema play indicator
        w = radius * 1.15
        h = radius * 0.85
        # Lower board
        draw.rounded_rectangle([cx - w, cy - h*0.1, cx + w, cy + h*1.1], radius=14, outline=c_col, width=6)
        # Clapper stripes on upper tilted bar
        top_bar = [(cx - w*1.05, cy - h*0.8), (cx + w*1.05, cy - h*0.35), (cx + w*1.02, cy - h*0.1), (cx - w*1.08, cy - h*0.55)]
        draw.polygon(top_bar, fill=c_col, outline=a_col)
        # Play button in center
        play = [(cx - radius*0.25, cy + radius*0.2), (cx - radius*0.25, cy + radius*0.8), (cx + radius*0.4, cy + radius*0.5)]
        draw.polygon(play, fill=a_col)

    elif app_type == "light":
        # Dynamic Sunburst / Aperture Ring & Shutter Ray
        draw.ellipse([cx - radius*0.45, cy - radius*0.45, cx + radius*0.45, cy + radius*0.45], fill=a_col)
        draw.ellipse([cx - radius*0.7, cy - radius*0.7, cx + radius*0.7, cy + radius*0.7], outline=c_col, width=6)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = cx + math.cos(rad) * radius * 0.85
            y1 = cy + math.sin(rad) * radius * 0.85
            x2 = cx + math.cos(rad) * radius * 1.15
            y2 = cy + math.sin(rad) * radius * 1.15
            draw.line([(x1, y1), (x2, y2)], fill=a_col, width=6)

    elif app_type == "pdf":
        # Clean Document Sheet with 3D folded corner & Vector Page Lines
        w = radius * 0.85
        h = radius * 1.15
        fold = radius * 0.4
        doc_pts = [
            (cx - w, cy - h),
            (cx + w - fold, cy - h),
            (cx + w, cy - h + fold),
            (cx + w, cy + h),
            (cx - w, cy + h),
        ]
        draw.polygon(doc_pts, outline=c_col, width=6)
        # Fold corner
        draw.polygon([(cx + w - fold, cy - h), (cx + w - fold, cy - h + fold), (cx + w, cy - h + fold)], fill=a_col)
        # Document lines
        draw.line([(cx - w*0.65, cy - h*0.1), (cx + w*0.65, cy - h*0.1)], fill=a_col, width=6)
        draw.line([(cx - w*0.65, cy + h*0.25), (cx + w*0.65, cy + h*0.25)], fill=white, width=6)
        draw.line([(cx - w*0.65, cy + h*0.6), (cx + w*0.25, cy + h*0.6)], fill=white, width=6)

    elif app_type == "effect":
        # Magic Wand with luminous particle stars
        draw.line([(cx - radius*0.8, cy + radius*0.8), (cx + radius*0.4, cy - radius*0.4)], fill=c_col, width=12)
        draw.line([(cx + radius*0.1, cy - radius*0.1), (cx + radius*0.4, cy - radius*0.4)], fill=a_col, width=14)
        # Star sparks
        for sx, sy in [(cx + radius*0.7, cy - radius*0.7), (cx + radius*0.2, cy - radius*0.9), (cx + radius*0.9, cy - radius*0.3)]:
            draw.line([(sx - 12, sy), (sx + 12, sy)], fill=a_col, width=4)
            draw.line([(sx, sy - 12), (sx, sy + 12)], fill=a_col, width=4)

    elif app_type == "design":
        # Precision Canvas Artboards with Layout Ruler & Guides
        w = radius * 0.95
        draw.rectangle([cx - w, cy - w*0.7, cx + w, cy + w*0.7], outline=c_col, width=6)
        draw.rectangle([cx - w*0.7, cy - w*0.45, cx + w*0.7, cy + w*0.45], outline=a_col, width=4)
        # Grid snap cross
        draw.line([(cx, cy - w*0.7), (cx, cy + w*0.7)], fill=white, width=2)
        draw.line([(cx - w, cy), (cx + w, cy)], fill=white, width=2)

    elif app_type == "fig":
        # Modern UI Component Diamond with Dynamic Vector Corner Nodes
        d = radius * 0.95
        diamond = [(cx, cy - d), (cx + d, cy), (cx, cy + d), (cx - d, cy)]
        draw.polygon(diamond, outline=c_col, width=7)
        inner = [(cx, cy - d*0.5), (cx + d*0.5, cy), (cx, cy + d*0.5), (cx - d*0.5, cy)]
        draw.polygon(inner, fill=a_col)
        # Corner nodes
        for pt in diamond:
            draw.rectangle([pt[0]-6, pt[1]-6, pt[0]+6, pt[1]+6], fill=white)

    elif app_type == "word":
        # Typography Monogram Ligature 'W' with Editorial Serifs
        w = radius * 0.95
        h = radius * 0.9
        pts = [
            (cx - w, cy - h),
            (cx - w*0.55, cy + h),
            (cx, cy - h*0.2),
            (cx + w*0.55, cy + h),
            (cx + w, cy - h),
        ]
        draw.line(pts, fill=c_col, width=12, joint="curve")
        draw.line([(cx - w*0.55, cy + h), (cx, cy - h*0.2)], fill=a_col, width=12)
        # Base baseline rule
        draw.line([(cx - w*1.05, cy + h + 16), (cx + w*1.05, cy + h + 16)], fill=white, width=4)

    elif app_type == "sound":
        # High-Fidelity Audio Equalizer Waveform & Beats
        bars = [0.35, 0.65, 1.1, 0.75, 1.3, 0.9, 0.45]
        bar_w = 12
        spacing = 26
        start_x = cx - (len(bars) * spacing) // 2 + 6
        for i, h_factor in enumerate(bars):
            bh = int(radius * h_factor)
            bx = start_x + i * spacing
            col = a_col if i in (2, 4) else c_col
            draw.rounded_rectangle([bx - bar_w//2, cy - bh//2, bx + bar_w//2, cy + bh//2], radius=6, fill=col)

    elif app_type == "deck":
        # Presentation Canvas with Projection Screen & Upward Trend Bar
        w = radius * 1.1
        h = radius * 0.75
        draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h*0.7], radius=12, outline=c_col, width=6)
        # Stand
        draw.line([(cx, cy + h*0.7), (cx, cy + h*1.15)], fill=c_col, width=6)
        draw.line([(cx - w*0.4, cy + h*1.15), (cx + w*0.4, cy + h*1.15)], fill=c_col, width=6)
        # Upward arrow trend
        draw.line([(cx - w*0.6, cy + h*0.3), (cx, cy - h*0.1), (cx + w*0.6, cy - h*0.45)], fill=a_col, width=7)
        draw.polygon([(cx + w*0.6, cy - h*0.45), (cx + w*0.35, cy - h*0.45), (cx + w*0.6, cy - h*0.2)], fill=a_col)

    elif app_type == "cad":
        # Precision Drafting Compass & Coordinate Crosshairs
        draw.ellipse([cx - radius*0.9, cy - radius*0.9, cx + radius*0.9, cy + radius*0.9], outline=c_col, width=4)
        draw.ellipse([cx - radius*0.45, cy - radius*0.45, cx + radius*0.45, cy + radius*0.45], outline=a_col, width=6)
        # Crosshair axes
        draw.line([(cx - radius*1.15, cy), (cx + radius*1.15, cy)], fill=white, width=3)
        draw.line([(cx, cy - radius*1.15), (cx, cy + radius*1.15)], fill=white, width=3)
        # Precision snap tick boxes
        draw.rectangle([cx - 8, cy - radius*0.45 - 8, cx + 8, cy - radius*0.45 + 8], fill=a_col)
        draw.rectangle([cx - 8, cy + radius*0.45 - 8, cx + 8, cy + radius*0.45 + 8], fill=a_col)
        draw.rectangle([cx - radius*0.45 - 8, cy - 8, cx - radius*0.45 + 8, cy + 8], fill=a_col)
        draw.rectangle([cx + radius*0.45 - 8, cy - 8, cx + radius*0.45 + 8, cy + 8], fill=a_col)

    elif app_type == "grid":
        # Professional Matrix Grid & Dynamic Formula Cell
        w = radius * 1.05
        h = radius * 0.95
        draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], radius=10, outline=c_col, width=6)
        # Header bar
        draw.rectangle([cx - w, cy - h, cx + w, cy - h*0.45], fill=c_col)
        # Matrix lines
        draw.line([(cx - w*0.3, cy - h), (cx - w*0.3, cy + h)], fill=c_col, width=4)
        draw.line([(cx + w*0.35, cy - h), (cx + w*0.35, cy + h)], fill=c_col, width=4)
        draw.line([(cx - w, cy + h*0.25), (cx + w, cy + h*0.25)], fill=c_col, width=4)
        # Selected cell highlight
        draw.rectangle([cx - w*0.28, cy - h*0.4, cx + w*0.33, cy + h*0.22], fill=a_col)

    elif app_type == "craft":
        # Generative AI Sparkle Core & Neural Orbit
        draw.ellipse([cx - radius*0.9, cy - radius*0.9, cx + radius*0.9, cy + radius*0.9], outline=c_col, width=4)
        # 4-point star in center
        for factor, col in [(1.0, a_col), (0.5, white)]:
            s = radius * factor
            star = [
                (cx, cy - s), (cx + s*0.25, cy - s*0.25),
                (cx + s, cy), (cx + s*0.25, cy + s*0.25),
                (cx, cy + s), (cx - s*0.25, cy + s*0.25),
                (cx - s, cy), (cx - s*0.25, cy - s*0.25)
            ]
            draw.polygon(star, fill=col)

    elif app_type == "craftx":
        # Futuristic Multimodal Quantum Core
        d = radius * 0.95
        draw.polygon([(cx, cy - d), (cx + d*0.9, cy - d*0.45), (cx + d*0.9, cy + d*0.45), (cx, cy + d), (cx - d*0.9, cy + d*0.45), (cx - d*0.9, cy - d*0.45)], outline=c_col, width=6)
        # Inner energy beam
        draw.polygon([(cx, cy - d*0.5), (cx + d*0.45, cy - d*0.25), (cx + d*0.45, cy + d*0.25), (cx, cy + d*0.5), (cx - d*0.45, cy + d*0.25), (cx - d*0.45, cy - d*0.25)], fill=a_col)
        # Energy laser cross
        draw.line([(cx - radius*1.1, cy), (cx + radius*1.1, cy)], fill=white, width=3)

    elif app_type == "clip":
        # Video Viral Clip Scissors Cutting Filmstrip & Audio Spikes
        w = radius * 1.05
        h = radius * 0.8
        # Filmstrip outline
        draw.rounded_rectangle([cx - w, cy - h, cx + w, cy + h], radius=12, outline=c_col, width=6)
        # Perforation notches
        for px in [-w*0.7, -w*0.3, 0, w*0.3, w*0.7]:
            draw.rectangle([cx + px - 8, cy - h + 4, cx + px + 8, cy - h + 18], fill=c_col)
            draw.rectangle([cx + px - 8, cy + h - 18, cx + px + 8, cy + h - 4], fill=c_col)
        # Scissors cutting the strip
        draw.line([(cx - radius*0.5, cy - radius*0.35), (cx + radius*0.5, cy + radius*0.35)], fill=a_col, width=8)
        draw.line([(cx - radius*0.5, cy + radius*0.35), (cx + radius*0.5, cy - radius*0.35)], fill=a_col, width=8)
        draw.ellipse([cx - radius*0.65, cy - radius*0.5, cx - radius*0.35, cy - radius*0.2], outline=a_col, width=6)
        draw.ellipse([cx - radius*0.65, cy + radius*0.2, cx - radius*0.35, cy + radius*0.5], outline=a_col, width=6)
        # Central viral spark
        draw.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=white)

    elif app_type == "launcher":
        # Master Launcher: Central orbital power ring around official clover mark
        draw.ellipse([cx - radius*1.05, cy - radius*1.05, cx + radius*1.05, cy + radius*1.05], outline=a_col, width=6)
        draw.ellipse([cx - radius*0.75, cy - radius*0.75, cx + radius*0.75, cy + radius*0.75], outline=c_col, width=4)


def create_app_icon(app, official_mark, size=1024):
    """Generate high-resolution PNG image for an app."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    pad = int(size * 0.05)
    inner_pad = int(size * 0.065)
    r = int(size * 0.22)
    
    # Outer squircle border glow
    border_color = app["color"] + (255,)
    accent_color = app["accent"] + (255,)
    
    # Deep obsidian background (#090D16)
    bg_color = (9, 13, 22, 255)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=bg_color, outline=border_color, width=max(6, size // 90))
    
    # Subtle inner gradient frame
    draw.rounded_rectangle([inner_pad, inner_pad, size - inner_pad, size - inner_pad], radius=r - 12, outline=accent_color, width=max(2, size // 250))
    
    center = (size // 2, size // 2)
    glyph_radius = int(size * 0.30)
    
    if app["type"] == "launcher":
        # Launcher showcases the official Decode clover mark full center
        if official_mark:
            mark_size = int(size * 0.68)
            mark_resized = official_mark.resize((mark_size, mark_size), Image.Resampling.LANCZOS)
            draw_glyph(draw, "launcher", center, glyph_radius, app["color"], app["accent"])
            img.alpha_composite(mark_resized, ((size - mark_size)//2, (size - mark_size)//2))
    else:
        # Draw specialized tool glyph
        draw_glyph(draw, app["type"], center, glyph_radius, app["color"], app["accent"])
        
        # Stamp the official Decode clover mark in the top-right badge
        if official_mark:
            badge_size = int(size * 0.22)
            badge_x = size - pad - badge_size - int(size * 0.03)
            badge_y = pad + int(size * 0.03)
            
            # Circular dark pill behind badge for supreme clarity
            b_cx = badge_x + badge_size // 2
            b_cy = badge_y + badge_size // 2
            b_r = badge_size // 2 + 6
            draw.ellipse([b_cx - b_r, b_cy - b_r, b_cx + b_r, b_cy + b_r], fill=(13, 17, 28, 240), outline=accent_color, width=3)
            
            mark_badge = official_mark.resize((badge_size, badge_size), Image.Resampling.LANCZOS)
            img.alpha_composite(mark_badge, (badge_x, badge_y))
            
    return img


def main():
    print("Generating official unified Decode Analytics suite icons...")
    official_mark = load_official_mark()
    if official_mark:
        print(f" -> Loaded official Decode mark from {OFFICIAL_MARK_PATH}")
    else:
        print(" -> Warning: official mark not found, proceeding with fallback geometry.")

    launcher_icons_dir = REPO_ROOT / "launcher" / "assets" / "app-icons"
    root_icons_dir = REPO_ROOT / "assets" / "app-icons"
    root_apps_dir = REPO_ROOT / "assets" / "apps"
    launcher_icons_dir.mkdir(parents=True, exist_ok=True)
    root_icons_dir.mkdir(parents=True, exist_ok=True)
    root_apps_dir.mkdir(parents=True, exist_ok=True)
    
    for app in APPS:
        slug = app["slug"]
        print(f" -> Rendering icon for {app['name']} ({slug})...")
        
        # Master 1024x1024 image
        master_img = create_app_icon(app, official_mark, size=1024)
        
        # 128x128 for launcher/assets/app-icons and root/assets/app-icons
        img_128 = master_img.resize((128, 128), Image.Resampling.LANCZOS)
        img_128.save(launcher_icons_dir / f"{slug}.png", optimize=True)
        img_128.save(root_icons_dir / f"{slug}.png", optimize=True)
        
        # Also save to root/assets/apps/ (e.g. decode-cad.png, decode-clip.png)
        img_256 = master_img.resize((256, 256), Image.Resampling.LANCZOS)
        img_256.save(root_apps_dir / f"{slug}.png", optimize=True)
        if slug.endswith("craft"):
            equiv_slug = f"decode-{slug[:-5]}"
            img_256.save(root_apps_dir / f"{equiv_slug}.png", optimize=True)
        
        # Also handle specific folder under apps/
        if app["type"] != "launcher":
            app_folder = REPO_ROOT / "apps" / app["folder"]
            icon_dir = app_folder / "assets" / "app-icon"
            icon_dir.mkdir(parents=True, exist_ok=True)
            
            # Save master 1024
            master_img.save(icon_dir / f"{slug}-1024.png", optimize=True)
            
            # Save 256
            img_256.save(icon_dir / f"{slug}.png", optimize=True)
            img_256.save(icon_dir / f"{slug}-256.png", optimize=True)
            
            # Save standard sizes under hicolor
            for s in [16, 24, 32, 48, 64, 128, 256, 512]:
                hicolor_dir = icon_dir / "hicolor" / f"{s}x{s}" / "apps"
                hicolor_dir.mkdir(parents=True, exist_ok=True)
                resized = master_img.resize((s, s), Image.Resampling.LANCZOS)
                resized.save(hicolor_dir / f"com.decode.{app['folder']}.png", optimize=True)
                
            # Generate .ico file
            ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            master_img.save(icon_dir / f"{slug}.ico", format="ICO", sizes=ico_sizes)
        else:
            # Launcher specific icons
            master_img.save(REPO_ROOT / "launcher" / "assets" / "app-icon" / "decode-launcher-1024.png", optimize=True)
            img_256.save(REPO_ROOT / "assets" / "launcher-icon" / "decode-launcher-256.png", optimize=True)
            master_img.save(REPO_ROOT / "launcher" / "assets" / "app-icon" / "decode-launcher.ico", format="ICO", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
            
    print("Done! All Decode suite app icons successfully stylized and rendered!")

if __name__ == "__main__":
    main()
