import streamlit as st

BASE_CSS = """
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f3ff 0%, #fdf2f8 50%, #eff6ff 100%);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .block-container {
        padding-top: 2.5rem;
        max-width: 1200px;
    }

    .hero-sparkle {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: -10px;
    }
    .hero-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 800;
        color: #111827;
        margin: 0;
    }
    .hero-subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.05rem;
        margin-top: 0.6rem;
        margin-bottom: 2.5rem;
        line-height: 1.6;
    }

    .tool-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 22px 22px 18px 22px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.06);
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .icon-box {
        width: 56px;
        height: 56px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        margin-bottom: 12px;
    }
    .tool-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #111827;
        margin: 0 0 6px 0;
        line-height: 1.25;
    }
    .tool-desc {
        color: #6b7280;
        font-size: 0.92rem;
        margin-bottom: 14px;
        line-height: 1.4;
        min-height: 42px;
    }
    .tool-img {
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 16px;
    }
    .tool-img img {
        width: 100%;
        height: 170px;
        object-fit: cover;
        display: block;
    }
    .footer-strip {
        text-align: center;
        color: #6b7280;
        margin-top: 2.5rem;
        font-size: 0.9rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
        font-size: 0.95rem;
    }
</style>
"""


def apply_base_style():
    st.markdown(BASE_CSS, unsafe_allow_html=True)


def apply_button_color(gradient_or_color):
    """Inject a color for the single primary button on a page (call after apply_base_style)."""
    st.markdown(f"""
    <style>
        div.stButton > button:first-child {{
            background: {gradient_or_color};
            color: white;
        }}
    </style>
    """, unsafe_allow_html=True)
