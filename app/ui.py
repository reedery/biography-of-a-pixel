import streamlit as st


YEAR_UI_CONFIG = {
    1966: {
        "res_labels": ["8x8", "16x16", "32x32", "64x64", "128x128", "256x256"],
        "styles": ["Standard", "Monocolour"],
        "ss_options": [1, 2],
        "shapes": ["Line"],
        "defaults": {
            "res_label_index": 2,
            "style_index": 0,
            "ss_value": 1,
            "shape_index": 0,
        },
    },
}


def _parse_resolution_label(label: str) -> int:
    return int(label.split("x", maxsplit=1)[0])


def render_sidebar(selected_year: int) -> tuple[int, str, int, str]:
    config = YEAR_UI_CONFIG.get(selected_year, YEAR_UI_CONFIG[1966])
    res_label_map = {label: _parse_resolution_label(label) for label in config["res_labels"]}

    with st.sidebar:
        st.header("Settings")
        res_label = st.selectbox(
            "Logical Resolution",
            list(res_label_map.keys()),
            index=config["defaults"]["res_label_index"],
        )
        res = res_label_map[res_label]
        style = st.selectbox(
            "Pixel Architecture",
            config["styles"],
            index=config["defaults"]["style_index"],
        )
        ss_level = st.selectbox(
            "Supersampling",
            options=config["ss_options"],
            index=0,
        )

        st.header("Geometry")
        shape_type = st.radio(
            "Draw Shape",
            config["shapes"],
            index=config["defaults"]["shape_index"],
        )

    return res, style, ss_level, shape_type
