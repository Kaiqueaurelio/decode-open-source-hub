#!/usr/bin/env python3
"""Generate complete, high-definition Decode Analytics icons for all 13 suite apps and launcher."""
import math
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

REPO_ROOT = Path(__file__).resolve().parents[1]

# App definitions: slug, name, folder, primary_rgb, accent_rgb
APPS = [
    {
        "slug": "photocraft",
        "name": "Decode Photo",
        "folder": "decode-photo",
        "color": (47, 123, 245),       # #2F7BF5
        "accent": (0, 210, 255),       # #00D2FF
        "type": "photo",
    },
    {
        "slug": "vectorcraft",
        "name": "Decode Vector",
        "folder": "decode-vector",
        "color": (232, 87, 63),        # #E8573F
        "accent": (255, 138, 112),     # #FF8A70
        "type": "vector",
    },
    {
        "slug": "filmcraft",
        "name": "Decode Film",
        "folder": "decode-film",
        "color": (139, 92, 246),       # #8B5CF6
        "accent": (182, 156, 255),     # #B69CFF
        "type": "film",
    },
    {
        "slug": "lightcraft",
        "name": "Decode Light",
        "folder": "decode-light",
        "color": (242, 165, 22),       # #F2A516
        "accent": (255, 193, 77),      # #FFC14D
        "type": "light",
    },
    {
        "slug": "pdfcraft",
        "name": "Decode PDF",
        "folder": "decode-pdf",
        "color": (18, 165, 138),       # #12A58A
        "accent": (63, 214, 184),      # #3FD6B8
        "type": "pdf",
    },
    {
        "slug": "effectcraft",
        "name": "Decode Effect",
        "folder": "decode-effect",
        "color": (224, 54, 143),       # #E0368F
        "accent": (255, 122, 184),     # #FF7AB8
        "type": "effect",
    },
    {
        "slug": "designcraft",
        "name": "Decode Design",
        "folder": "decode-design",
        "color": (236, 72, 153),       # #EC4899
        "accent": (244, 114, 182),     # #F472B6
        "type": "design",
    },
    {
        "slug": "figcraft",
        "name": "Decode Fig",
        "folder": "decode-fig",
        "color": (16, 185, 129),       # #10B981
        "accent": (52, 211, 153),      # #34D399
        "type": "fig",
    },
    {
        "slug": "wordcraft",
        "name": "Decode Word",
        "folder": "decode-word",
        "color": (59, 130, 246),       # #3B82F6
        "accent": (96, 165, 250),      # #60A5FA
        "type": "word",
    },
    {
        "slug": "soundcraft",
        "name": "Decode Sound",
        "folder": "decode-sound",
        "color": (99, 102, 241),       # #6366F1
        "accent": (129, 140, 248),     # #818CF8
        "type": "sound",
    },
    {
        "slug": "deckcraft",
        "name": "Decode Deck",
        "folder": "decode-deck",
        "color": (249, 115, 22),       # #F97316
        "accent": (251, 146, 60),      # #FB923C
        "type": "deck",
    },
    {
        "slug": "cadcraft",
        "name": "Decode CAD",
        "folder": "decode-cad",
        "color": (62, 166, 232),       # #3EA6E8
        "accent": (124, 200, 255),     # #7CC8FF
        "type": "cad",
    },
    {
        "slug": "gridcraft",
        "name": "Decode Grid",
        "folder": "decode-grid",
        "color": (31, 157, 85),        # #1F9D55
        "accent": (79, 214, 138),      # #4FD68A
        "type": "grid",
    },
    {
        "slug": "decode-craft",
        "name": "DecodeCraft",
        "folder": "decode-craft",
        "color": (168, 85, 247),       # #A855F7
        "accent": (216, 180, 254),     # #D8B4FE
        "type": "craft",
    },
    {
        "slug": "decode-craftx",
        "name": "DecodeCraftX",
        "folder": "decode-craftx",
        "color": (236, 72, 153),       # #EC4899
        "accent": (244, 114, 182),     # #F472B6
        "type": "craftx",
    },
    {
        "slug": "decode-launcher",
        "name": "Decode Launcher",
        "folder": "launcher",
        "color": (32, 85, 255),        # #2055FF
        "accent": (0, 210, 255),       # #00D2FF
        "type": "launcher",
    },
]

def draw_decode_badge(draw, cx, cy, size, color, accent):
    """Draw the signature Decode 'D' mark at position (cx, cy)."""
    r = size // 2
    # Outer D contour
    left = cx - r
    top = cy - r
    right = cx + r
    bottom = cy + r
    
    # Stem
    stem_w = max(4, size // 4)
    draw.rounded_rectangle([left, top, left + stem_w, bottom], radius=stem_w//2, fill=accent)
    
    # Curve
    curve_box = [left, top, right, bottom]
    draw.arc(curve_box, -90, 90, fill=color, width=stem_w)
    draw.line([(left + stem_w//2, top), (cx, top)], fill=color, width=stem_w)
    draw.line([(left + stem_w//2, bottom), (cx, bottom)], fill=color, width=stem_w)

def draw_glyph(draw, app_type, center, radius, color, accent):
    """Draw a distinct, modern vector glyph representing the tool."""
    cx, cy = center
    c_col = color + (255,)
    a_col = accent + (255,)
    white = (255, 255, 255, 230)
    
    if app_type == "photo":
        # Aperture / Lens: concentric rings + shutter petals
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline=a_col, width=12)
        inner_r = radius * 0.6
        draw.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r], fill=c_col, outline=white, width=4)
        center_r = radius * 0.25
        draw.ellipse([cx - center_r, cy - center_r, cx + center_r, cy + center_r], fill=(11, 15, 25, 255))
        # Glare
        draw.ellipse([cx - radius*0.35, cy - radius*0.35, cx - radius*0.15, cy - radius*0.15], fill=(255, 255, 255, 180))

    elif app_type == "vector":
        # Vector Pen Tip & Bezier Node
        points = [
            (cx, cy - radius),
            (cx + radius*0.7, cy + radius*0.4),
            (cx + radius*0.3, cy + radius*0.7),
            (cx, cy + radius*0.2),
            (cx - radius*0.3, cy + radius*0.7),
            (cx - radius*0.7, cy + radius*0.4),
        ]
        draw.polygon(points, fill=c_col, outline=a_col)
        # Pen nib slit
        draw.line([(cx, cy - radius*0.5), (cx, cy + radius*0.1)], fill=white, width=6)
        # Anchor handles
        draw.ellipse([cx - radius*0.8, cy - radius*0.8, cx - radius*0.5, cy - radius*0.5], fill=a_col)
        draw.ellipse([cx + radius*0.5, cy - radius*0.8, cx + radius*0.8, cy - radius*0.5], fill=a_col)
        draw.line([(cx - radius*0.65, cy - radius*0.65), (cx + radius*0.65, cy - radius*0.65)], fill=white, width=4)

    elif app_type == "film":
        # Cinema Clapperboard / Film Frame
        w, h = radius * 1.3, radius * 1.0
        x0, y0 = cx - w//2, cy - h//2
        draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=16, fill=(20, 24, 38, 255), outline=a_col, width=8)
        # Clapper top bar
        draw.rectangle([x0, y0, x0 + w, y0 + h*0.35], fill=c_col)
        # Stripes
        for sx in range(int(x0) + 15, int(x0 + w) - 10, 32):
            draw.line([(sx, y0 + 4), (sx + 14, y0 + h*0.32)], fill=white, width=6)
        # Play triangle
        tri = [(cx - 10, cy + 5), (cx - 10, cy + h*0.35), (cx + 20, cy + h*0.2)]
        draw.polygon(tri, fill=a_col)

    elif app_type == "light":
        # Sunburst / Shutter Blades / RAW Crystal
        draw.ellipse([cx - radius*0.8, cy - radius*0.8, cx + radius*0.8, cy + radius*0.8], outline=a_col, width=8)
        # Radial rays
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = cx + math.cos(rad) * radius * 0.45
            y1 = cy + math.sin(rad) * radius * 0.45
            x2 = cx + math.cos(rad) * radius * 0.95
            y2 = cy + math.sin(rad) * radius * 0.95
            draw.line([(x1, y1), (x2, y2)], fill=c_col, width=7)
        draw.ellipse([cx - radius*0.3, cy - radius*0.3, cx + radius*0.3, cy + radius*0.3], fill=a_col)

    elif app_type == "pdf":
        # Document Fold & Shield Lock
        w, h = radius * 1.0, radius * 1.3
        x0, y0 = cx - w//2, cy - h//2
        # Page body
        draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=14, fill=c_col, outline=white, width=6)
        # Lines
        line_w = w * 0.6
        draw.line([(cx - line_w//2, cy - radius*0.3), (cx + line_w//2, cy - radius*0.3)], fill=white, width=8)
        draw.line([(cx - line_w//2, cy), (cx + line_w//2, cy)], fill=white, width=8)
        draw.line([(cx - line_w//2, cy + radius*0.3), (cx + line_w*0.2, cy + radius*0.3)], fill=white, width=8)
        # Secure badge
        draw.ellipse([cx + w*0.1, cy + h*0.2, cx + w*0.55, cy + h*0.65], fill=a_col, outline=white, width=3)

    elif app_type == "effect":
        # Dynamic Starburst VFX Spark
        for i in range(8):
            ang = i * (math.pi / 4)
            r_out = radius * (1.1 if i % 2 == 0 else 0.55)
            x = cx + math.cos(ang) * r_out
            y = cy + math.sin(ang) * r_out
            if i == 0:
                poly = [(x, y)]
            else:
                poly.append((x, y))
        draw.polygon(poly, fill=c_col, outline=a_col)
        draw.ellipse([cx - radius*0.3, cy - radius*0.3, cx + radius*0.3, cy + radius*0.3], fill=white)

    elif app_type == "design":
        # Layout Columns & Grid Frames
        w, h = radius * 1.3, radius * 1.1
        x0, y0 = cx - w//2, cy - h//2
        # Left column
        draw.rounded_rectangle([x0, y0, cx - 10, y0 + h], radius=10, fill=c_col, outline=a_col, width=4)
        # Right top block
        draw.rounded_rectangle([cx + 10, y0, x0 + w, cy - 8], radius=8, fill=a_col, outline=white, width=3)
        # Right bottom block
        draw.rounded_rectangle([cx + 10, cy + 8, x0 + w, y0 + h], radius=8, fill=(20, 24, 38, 255), outline=a_col, width=4)

    elif app_type == "fig":
        # UI Nodes / Interface Components
        draw.ellipse([cx - radius*0.7, cy - radius*0.7, cx - radius*0.1, cy - radius*0.1], fill=a_col)
        draw.ellipse([cx + radius*0.1, cy - radius*0.7, cx + radius*0.7, cy - radius*0.1], fill=c_col)
        draw.ellipse([cx - radius*0.7, cy + radius*0.1, cx - radius*0.1, cy + radius*0.7], fill=c_col)
        draw.ellipse([cx + radius*0.1, cy + radius*0.1, cx + radius*0.7, cy + radius*0.7], fill=white)
        # Frame connector lines
        draw.line([(cx - radius*0.4, cy - radius*0.4), (cx + radius*0.4, cy + radius*0.4)], fill=white, width=4)

    elif app_type == "word":
        # Serif Typographic W / Pen Calligraphy
        p1 = (cx - radius*0.8, cy - radius*0.6)
        p2 = (cx - radius*0.4, cy + radius*0.6)
        p3 = (cx, cy - radius*0.2)
        p4 = (cx + radius*0.4, cy + radius*0.6)
        p5 = (cx + radius*0.8, cy - radius*0.6)
        draw.line([p1, p2, p3, p4, p5], fill=c_col, width=16, joint="curve")
        draw.line([p1, p2, p3, p4, p5], fill=a_col, width=8, joint="curve")
        # Underline
        draw.line([(cx - radius*0.7, cy + radius*0.8), (cx + radius*0.7, cy + radius*0.8)], fill=white, width=8)

    elif app_type == "sound":
        # Equalizer Waveform Bars & Fader Knob
        bars = [-0.7, -0.4, -0.1, 0.2, 0.5, 0.8]
        heights = [0.35, 0.75, 1.0, 0.6, 0.85, 0.4]
        for b, h in zip(bars, heights):
            bx = cx + b * radius
            bar_h = h * radius
            draw.line([(bx, cy - bar_h*0.8), (bx, cy + bar_h*0.8)], fill=a_col, width=12)
            draw.ellipse([bx - 8, cy - 8, bx + 8, cy + 8], fill=white)

    elif app_type == "deck":
        # Layered Keynote Slides in Isometric 3D
        w, h = radius * 1.1, radius * 0.75
        # Bottom back slide
        draw.rounded_rectangle([cx - w*0.45, cy - h*0.8, cx + w*0.55, cy - h*0.1], radius=8, fill=(40, 50, 75, 255), outline=c_col, width=3)
        # Middle slide
        draw.rounded_rectangle([cx - w*0.5, cy - h*0.45, cx + w*0.5, cy + h*0.25], radius=10, fill=c_col, outline=a_col, width=4)
        # Front slide
        draw.rounded_rectangle([cx - w*0.55, cy - h*0.1, cx + w*0.45, cy + h*0.6], radius=12, fill=(15, 20, 32, 255), outline=a_col, width=6)
        # Trend graph on front slide
        draw.line([(cx - w*0.4, cy + h*0.4), (cx - w*0.1, cy + h*0.2), (cx + w*0.1, cy + h*0.3), (cx + w*0.35, cy)], fill=a_col, width=6)

    elif app_type == "cadcraft" or app_type == "cad":
        # Isometric Blueprint Cube & Precision Crosshair
        r = radius * 0.75
        # Top face
        top_pts = [
            (cx, cy - r),
            (cx + r * 0.866, cy - r * 0.5),
            (cx, cy),
            (cx - r * 0.866, cy - r * 0.5),
        ]
        draw.polygon(top_pts, fill=a_col, outline=white)
        # Left face
        left_pts = [
            (cx - r * 0.866, cy - r * 0.5),
            (cx, cy),
            (cx, cy + r),
            (cx - r * 0.866, cy + r * 0.5),
        ]
        draw.polygon(left_pts, fill=c_col, outline=white)
        # Right face
        right_pts = [
            (cx, cy),
            (cx + r * 0.866, cy - r * 0.5),
            (cx + r * 0.866, cy + r * 0.5),
            (cx, cy + r),
        ]
        draw.polygon(right_pts, fill=(15, 30, 55, 255), outline=white)
        # Crosshair axes
        draw.line([(cx - radius, cy), (cx + radius, cy)], fill=a_col, width=2)
        draw.line([(cx, cy - radius), (cx, cy + radius)], fill=a_col, width=2)

    elif app_type == "grid":
        # Data Matrix Spreadsheet & Analytics Bars
        w, h = radius * 1.2, radius * 1.1
        x0, y0 = cx - w//2, cy - h//2
        draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=12, fill=(18, 25, 35, 255), outline=a_col, width=6)
        # Header bar
        draw.rectangle([x0 + 4, y0 + 4, x0 + w - 4, y0 + h*0.32], fill=c_col)
        # Grid lines
        draw.line([(cx - w*0.1, y0), (cx - w*0.1, y0 + h)], fill=a_col, width=4)
        draw.line([(cx + w*0.2, y0), (cx + w*0.2, y0 + h)], fill=a_col, width=4)
        draw.line([(x0, cy + h*0.1), (x0 + w, cy + h*0.1)], fill=a_col, width=4)
        # Highlight cell
        draw.rectangle([cx - w*0.08, cy + h*0.12, cx + w*0.18, y0 + h - 6], fill=a_col)

    elif app_type == "craft":
        # Generative AI Sparkle & Neural 3D Splat
        draw.ellipse([cx - radius*0.8, cy - radius*0.8, cx + radius*0.8, cy + radius*0.8], outline=a_col, width=4)
        draw_decode_badge(draw, cx, cy, int(radius * 1.05), color, accent)

    elif app_type == "craftx":
        # Multimodal AI Prism & Kinetic Lightning
        draw.rectangle([cx - radius*0.75, cy - radius*0.75, cx + radius*0.75, cy + radius*0.75], outline=a_col, width=4)
        draw_decode_badge(draw, cx, cy, int(radius * 1.15), color, accent)
    elif app_type == "launcher":
        # Large signature Decode D Mark with orbital power ring
        draw.ellipse([cx - radius*1.05, cy - radius*1.05, cx + radius*1.05, cy + radius*1.05], outline=a_col, width=6)
        draw_decode_badge(draw, cx, cy, int(radius * 1.3), color, accent)


def create_app_icon(app, size=1024):
    """Generate high-resolution PNG image for an app."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    pad = int(size * 0.05)
    inner_pad = int(size * 0.065)
    r = int(size * 0.22)
    
    # Outer squircle border glow
    border_color = app["color"] + (255,)
    accent_color = app["accent"] + (255,)
    
    # Deep obsidian background
    bg_color = (11, 15, 25, 255)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=bg_color, outline=border_color, width=max(4, size // 100))
    
    # Subtle inner gradient frame
    draw.rounded_rectangle([inner_pad, inner_pad, size - inner_pad, size - inner_pad], radius=r - 10, outline=accent_color, width=max(2, size // 250))
    
    # Tool Glyph
    center = (size // 2, size // 2)
    glyph_radius = int(size * 0.30)
    draw_glyph(draw, app["type"], center, glyph_radius, app["color"], app["accent"])
    
    # Decode mini-monogram badge in top right (except launcher which has full mark)
    if app["type"] != "launcher":
        badge_cx = size - pad - int(size * 0.16)
        badge_cy = pad + int(size * 0.16)
        badge_size = int(size * 0.18)
        draw_decode_badge(draw, badge_cx, badge_cy, badge_size, app["color"], app["accent"])
        
    return img


def main():
    print("Generating official Decode Analytics icons across repository...")
    launcher_icons_dir = REPO_ROOT / "launcher" / "assets" / "app-icons"
    root_icons_dir = REPO_ROOT / "assets" / "app-icons"
    launcher_icons_dir.mkdir(parents=True, exist_ok=True)
    root_icons_dir.mkdir(parents=True, exist_ok=True)
    
    for app in APPS:
        slug = app["slug"]
        print(f" -> Rendering icon for {app['name']} ({slug})...")
        
        # Master 1024x1024 image
        master_img = create_app_icon(app, size=1024)
        
        # 128x128 for launcher/assets/app-icons and root/assets/app-icons
        img_128 = master_img.resize((128, 128), Image.Resampling.LANCZOS)
        img_128.save(launcher_icons_dir / f"{slug}.png", optimize=True)
        img_128.save(root_icons_dir / f"{slug}.png", optimize=True)
        
        # Also handle specific folder under apps/
        if app["type"] != "launcher":
            app_folder = REPO_ROOT / "apps" / app["folder"]
            icon_dir = app_folder / "assets" / "app-icon"
            icon_dir.mkdir(parents=True, exist_ok=True)
            
            # Save master 1024
            master_img.save(icon_dir / f"{slug}-1024.png", optimize=True)
            
            # Save 256
            img_256 = master_img.resize((256, 256), Image.Resampling.LANCZOS)
            img_256.save(icon_dir / f"{slug}.png", optimize=True)
            
            # Save standard sizes under hicolor
            for s in [16, 24, 48, 64, 128, 256, 512]:
                hicolor_dir = icon_dir / "hicolor" / f"{s}x{s}" / "apps"
                hicolor_dir.mkdir(parents=True, exist_ok=True)
                resized = master_img.resize((s, s), Image.Resampling.LANCZOS)
                # removed legacy ai.storyteller save
                resized.save(hicolor_dir / f"com.decode.{app['folder']}.png", optimize=True)
                
            # Generate .ico file
            ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            master_img.save(icon_dir / f"{slug}.ico", format="ICO", sizes=ico_sizes)
            
    print("Done! All 14 Decode app icons successfully generated and installed!")

if __name__ == "__main__":
    main()
