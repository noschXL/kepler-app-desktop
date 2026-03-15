from string import Template
from PySide6 import QtGui

# the colors are from claude.ai, i am not a graphics designer.

def adjust(hex_color: str, value: int = 0, saturation: int = 0) -> str:
    color = QtGui.QColor(hex_color)
    h, s, v, a = color.getHsv()
    color.setHsv(
        h,
        max(0, min(255, s + saturation)),
        max(0, min(255, v + value)),
        a,
    )
    return color.name()


# ── Brand ────────────────────────────────────────────────────────────────────

YELLOW = "#fed44c"
ORANGE = "#ff7c00"
BLUE   = "#4a8aba"

# ── Theme ────────────────────────────────────────────────────────────────────

THEME = {

    # Brand — yellow
    "yellow":               YELLOW,
    "yellow_dark":          adjust(YELLOW, -40),
    "yellow_light":         adjust(YELLOW, +40),
    "yellow_tint":          adjust(YELLOW, +70, -80),
    "text_on_yellow":       "#7a6200",

    # Brand — orange
    "orange":               ORANGE,
    "orange_dark":          adjust(ORANGE, -40),
    "orange_light":         adjust(ORANGE, +40),
    "orange_tint":          adjust(ORANGE, +70, -80),
    "text_on_orange":       "#ffffff",

    # Brand — blue
    "blue":                 BLUE,
    "blue_dark":            adjust(BLUE, -40),
    "blue_light":           adjust(BLUE, +40),
    "blue_tint":            adjust(BLUE, +70, -80),
    "text_on_blue":         "#ffffff",

    # Backgrounds — light
    "bg":                   "#fdf6e3",
    "bg_card":              "#ffffff",
    "bg_hover":             adjust(BLUE, +70, -80),
    "bg_input":             "#ffffff",

    # Backgrounds — dark
    "bg_dark":              "#1e2535",
    "bg_card_dark":         "#242d3f",
    "bg_hover_dark":        "#2e3a50",
    "bg_input_dark":        "#1a2030",

    # Text
    "text_primary":         "#1a1a2e",
    "text_secondary":       "#4b5563",
    "text_muted":           "#9ca3af",
    "text_on_dark":         "#ffffff",
    "text_muted_dark":      "#6b7280",

    # Borders — light
    "border":               "#e5e7eb",
    "border_hover":         adjust(BLUE, +20),
    "border_focus":         BLUE,

    # Borders — dark
    "border_dark":          "#2a3a52",
    "border_dark_hover":    "#3a4a62",
    "border_dark_focus":    BLUE,

    # Semantic — success
    "success":              "#22c55e",
    "success_dark":         "#16a34a",
    "success_tint":         "#dcfce7",
    "text_on_success":      "#ffffff",

    # Semantic — warning (uses brand yellow)
    "warning":              YELLOW,
    "warning_dark":         adjust(YELLOW, -40),
    "warning_tint":         adjust(YELLOW, +70, -80),
    "text_on_warning":      "#7a6200",

    # Semantic — error
    "error":                "#ef4444",
    "error_dark":           "#dc2626",
    "error_tint":           "#fee2e2",
    "text_on_error":        "#ffffff",

    # Semantic — info (uses brand blue)
    "info":                 BLUE,
    "info_dark":            adjust(BLUE, -40),
    "info_tint":            adjust(BLUE, +70, -80),
    "text_on_info":         "#ffffff",

    # Grays
    "gray_100":             "#f3f4f6",
    "gray_200":             "#e5e7eb",
    "gray_400":             "#9ca3af",
    "gray_600":             "#4b5563",
    "gray_800":             "#1f2937",

    # Sidebar
    "sidebar_bg":           "#1e2535",
    "sidebar_button":       "#2a3347",
    "sidebar_button_hover": "#303d56",
    "sidebar_active":       BLUE,
    "sidebar_active_hover": adjust(BLUE, +20),
    "sidebar_text":         "#ffffff",
    "sidebar_text_muted":   "#9ca3af",
    "sidebar_border":       "#2a3a52",

}

class AtTemplate(Template):
    delimiter = "@"

def apply_colors(stylesheet: str):
    tpl = AtTemplate(stylesheet)
    tpl = tpl.safe_substitute(THEME)
    return tpl