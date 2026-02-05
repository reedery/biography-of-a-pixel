import streamlit as st

from app.render import Display
from app.timeline import render_timeline
from app.ui import render_sidebar


def run_app() -> None:
    selected_year, year_title = render_timeline()
    st.divider()
    st.subheader(f"{selected_year} — {year_title}")     

    res, style, ss_level, shape_type = render_sidebar(selected_year)

    st.markdown(
        "Introductory body text goes here before the first display."
    )

    display0 = Display(res)
    display0.set_supersampling(ss_level)
    color = (255, 255, 255)

    if shape_type == "Line":
        display0.draw_line(
            5 * ss_level,
            5 * ss_level,
            (res - 5) * ss_level,
            (res - 5) * ss_level,
            color,
        )
    # TODO: polygon 
    # elif shape_type == "Polygon":
    #     pts = [
    #         (int(res * 0.5) * ss_level, int(res * 0.1) * ss_level),
    #         (int(res * 0.9) * ss_level, int(res * 0.8) * ss_level),
    #         (int(res * 0.1) * ss_level, int(res * 0.8) * ss_level),
    #     ]
    #     display.draw_polygon(pts, color)
    final_img = display0.downsample()

    st.image(
        final_img,
        caption=f"Resolution: {res}x{res} | SSAA: {ss_level}x",
        width=512,
        clamp=True,
    )
    st.markdown(
        "Additional body text goes here before the second display."
    )
    # TODO: break up into new section of UI
    display1 = Display(res)
    display1.set_supersampling(ss_level)
    display1.draw_line(
        5 * ss_level,
        (res - 5) * ss_level,
        (res - 5) * ss_level,
        5 * ss_level,
        color,
    )
    secondary_img = display1.downsample()
    st.image(
        secondary_img,
        caption=f"Alternate Display — Resolution: {res}x{res} | SSAA: {ss_level}x",
        width=512,
        clamp=True,
    )
    st.markdown(
        "Use the sidebar to test how **Logical Resolution** differs from **Sub-pixel Rendering**."
    )
