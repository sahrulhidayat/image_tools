import streamlit as st

st.set_page_config(
    page_title="Image Tools",
    page_icon="✨",
    layout="wide",
)

# ---------------------------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------------------------
st.markdown(
    """
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f3ff 0%, #fdf2f8 50%, #eff6ff 100%);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 3rem;
        max-width: 1200px;
    }

    /* Header */
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

    /* Card */
    div[class*="st-key-tool-card"] {
        background-color: #ffffff;
        border-radius: 16px;
        border: 1px solid #f0f0f0;
        
        /* Shadow menyatu untuk satu kartu penuh */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 
                    0 4px 6px -2px rgba(0, 0, 0, 0.03);
                    
        /* Aktifkan Flexbox vertikal */
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    div[class*="st-key-tool-card-content"] {
        padding: 1.5rem;
        border: none;
        box-shadow: none;
    }

    .icon-box {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        font-size: 1.5rem;
        margin-bottom: 12px;
    }

    .tool-desc {
        color: #6b7280;
        font-size: 0.92rem;
        margin-bottom: 14px;
        line-height: 1.4;
        min-height: 42px;
    }

    /* Footer strip */
    .footer-strip {
        text-align: center;
        color: #6b7280;
        margin-top: 5rem;
        font-size: 0.9rem;
    }

    /* Buttons per tool color */
    div[class*="st-key-tool-card"] .stButton {
        margin-top: auto; 
    }

    div[class*="st-key-tool-card"] .stButton > button {
        width:100%;
        background-color: slateblue;
        color:white;
        border-radius:0 0 18px 18px;
        border:none;
        padding:0.8rem 1rem;
        font-weight:600;
        transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
    }
 
    div[class*="st-key-tool-card"] .stButton > button:hover {
        background-color: yellowgreen;
    }

    div[class*="st-key-tool-card"] .stButton > button::after {
        content: " →";
        margin-left: 8px;
        font-weight: 700;
    }

    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------------
st.markdown('<div class="hero-sparkle">✨</div>', unsafe_allow_html=True)
st.markdown(
    '<h1 class="hero-title" style="color:black">Image Tools</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="hero-subtitle">Powerful tools to edit your images easily and quickly.<br>'
    "Choose a tool below to get started.</p>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# TOOL DATA
# ---------------------------------------------------------------------------
tools = [
    {
        "icon": "🖼️",
        "icon_bg": "linear-gradient(135deg, #7c3aed, #4f46e5)",
        "title": "Background<br>Remover",
        "desc": "Remove background from any image instantly.",
        "button": "Use Background Remover",
        "page": "pages/bg_remover.py",
    },
    {
        "icon": "🔢",
        "icon_bg": "linear-gradient(135deg, #10b981, #059669)",
        "title": "Object<br>Counter",
        "desc": "Count objects in your image automatically.",
        "button": "Use Object Counter",
        "page": "pages/object_counter.py",
    },
    {
        "icon": "🕵️",
        "icon_bg": "linear-gradient(135deg, #3b82f6, #2563eb)",
        "title": "Anonymizer<br>Tool",
        "desc": "Blur faces or sensitive information for privacy.",
        "button": "Use Anonymizer Tool",
        "page": "pages/anonymizer.py",
    },
    {
        "icon": "💧",
        "icon_bg": "linear-gradient(135deg, #ec4899, #db2777)",
        "title": "Color Splash<br>Effect",
        "desc": "Make your image pop with a color splash effect.",
        "button": "Use Color Splash Effect",
        "page": "pages/color_splash.py",
    },
]

# ---------------------------------------------------------------------------
# CARDS
# ---------------------------------------------------------------------------
cols = st.columns(4, gap="medium")

for index, (col, tool) in enumerate(zip(cols, tools)):
    with col:
        with st.container(key=f"tool-card-{index}"):
            with st.container(key=f"tool-card-content-{index}"):
                # Render icon box using HTML
                st.markdown(
                    f'<div class="icon-box" style="background:{tool["icon_bg"]}">{tool["icon"]}</div>',
                    unsafe_allow_html=True,
                )

                # Title (allow simple HTML like <br>)
                st.markdown(
                    f'<h4 style="margin:8px 0; color:black">{tool["title"]}</h4>',
                    unsafe_allow_html=True,
                )

                # Description and button
                st.markdown(
                    f'<p style="color:black; font-size:0.92rem">{tool["desc"]}</p>',
                    unsafe_allow_html=True,
                )

            if st.button(tool["button"], key=f"btn-{tool['page']}", width="stretch"):
                st.switch_page(tool["page"])

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="footer-strip">Fast &nbsp;•&nbsp; Easy &nbsp;•&nbsp; Secure &nbsp;•&nbsp; High Quality Results</p>',
    unsafe_allow_html=True,
)
