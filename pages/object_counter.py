import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Object Counter", page_icon="🔢", layout="centered")

if st.button("← Back to Image Tools"):
    st.switch_page("app.py")

st.title("Object Counter")

uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    # Membaca gambar
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    with st.spinner("⏳ Memproses..."):
        # Konversi RGB ke BGR
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # Grayscale
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

        # Blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Morphological operations untuk mengurangi noise
        kernel = np.ones((3, 3), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

        # Cari contour
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Filter berdasarkan luas area
        object_count = 0

        h, w = thresh.shape
        image_area = h * w

        for contour in contours:
            area = cv2.contourArea(contour)

            if 500 < area < image_area * 0.8:
                object_count += 1
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Konversi kembali ke RGB
        result = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Gambar Asli", width="stretch")

    with col2:
        st.image(result, caption="Hasil Deteksi", width="stretch")

    st.success(f"Jumlah objek terdeteksi: {object_count}")

    st.download_button(
        "Download Hasil",
        cv2.imencode(".png", cv2.cvtColor(result, cv2.COLOR_RGB2BGR))[1].tobytes(),
        "objectcounter-result.png",
        "image/png",
        width="stretch",
    )

else:
    st.info(
        "Upload gambar dengan background terang, kontras tinggi, dan objek yang jelas untuk hasil akurat."
    )
