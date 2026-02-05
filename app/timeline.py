import streamlit as st

YEAR_TITLES = {
    1966: "Lines and Polygons",
}


def render_timeline() -> tuple[int, str]:
    options = sorted(YEAR_TITLES.keys())
    if len(options) < 2:
        selected_year = st.selectbox("Timeline", options=options, index=0)
    else:
        selected_year = st.select_slider(
            "Timeline",
            options=options,
            value=options[0],
        )
    title = YEAR_TITLES.get(selected_year, str(selected_year))
    return selected_year, title
