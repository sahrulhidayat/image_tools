import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Color Splash YOLOv8", page_icon="💧", layout="centered")


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "yolo_models"


@st.cache_resource
def load_model():
    return YOLO(str(MODEL_DIR / "yolov8n-seg.pt"))


model = load_model()


if st.button("← Back to Image Tools"):
    st.switch_page("app.py")


st.title("Color Splash Effect")

uploaded = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    img = np.array(image)

    with st.spinner("⏳ Memproses..."):
        results = model.predict(img, device="cpu", conf=0.4, verbose=False)

        result = results[0]

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

        output = gray.copy()

        if result.masks is not None:
            masks = result.masks.data.cpu().numpy()

            combined_mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

            for mask in masks:
                mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

                combined_mask = np.maximum(combined_mask, (mask > 0.5).astype(np.uint8))

            output[combined_mask == 1] = img[combined_mask == 1]

        col1, col2 = st.columns(2)

        with col1:
            st.image(img, caption="Original", width="stretch")

        with col2:
            st.image(output, caption="Color Splash", width="stretch")

        download_img = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode(".png", download_img)

        st.download_button(
            "Download Hasil",
            buffer.tobytes(),
            "colorsplash-result.png",
            "image/png",
            width="stretch",
        )
else:
    st.info(
        "Upload gambar dengan kontras yang jelas antara objek dan latar belakang untuk hasil terbaik."
    )
