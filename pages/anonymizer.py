import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "yolo_models"


@st.cache_resource
def load_models():
    # Face Detector Model
    face_model = YOLO(str(MODEL_DIR / "yolov8x-face-lindevs.pt"))
    # License Plate Detector Model
    plate_model = YOLO(str(MODEL_DIR / "yolov8n_license_plate.pt"))

    return face_model, plate_model


face_model, plate_model = load_models()


def detect_face(image):
    results = face_model.predict(image, device="cpu", conf=0.15, verbose=False)

    faces = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            faces.append((int(x1), int(y1), int(x2 - x1), int(y2 - y1)))

    return faces


def detect_plate(image):

    results = plate_model.predict(image, device="cpu", conf=0.4, verbose=False)

    plates = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            plates.append((int(x1), int(y1), int(x2 - x1), int(y2 - y1)))

    return plates


def blur(image, boxes):

    for x, y, w, h in boxes:
        roi = image[y : y + h, x : x + w]

        roi = cv2.GaussianBlur(roi, (99, 99), 30)

        image[y : y + h, x : x + w] = roi

    return image


def pixelate(image, boxes):

    for x, y, w, h in boxes:
        roi = image[y : y + h, x : x + w]

        temp = cv2.resize(roi, (10, 10))

        roi = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)

        image[y : y + h, x : x + w] = roi

    return image


st.set_page_config(page_title="Image Anonymizer", page_icon="🕵️", layout="centered")

if st.button("← Back to Image Tools"):
    st.switch_page("main.py")

st.title("Image Anonymizer")

uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

target = st.multiselect(
    "Objek yang dianonimkan", ["Face", "License Plate"], default=["Face"]
)

method = st.selectbox("Metode", ["Blur", "Pixelate"])

if uploaded:
    image = Image.open(uploaded)

    img = np.array(image)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    boxes = []

    if "Face" in target:
        boxes.extend(detect_face(img))

    if "License Plate" in target:
        boxes.extend(detect_plate(img))

    st.write("Objek terdeteksi :", len(boxes))

    if st.button("Process"):
        result = img.copy()

        if method == "Blur":
            result = blur(result, boxes)

        else:
            result = pixelate(result, boxes)

        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

        col1, col2 = st.columns(2)

        with col1:
            st.image(image, width="stretch", caption="Gambar Asli")

        with col2:
            st.image(result, width="stretch", caption="Hasil Anonimisasi")

        download_img = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode(".png", download_img)

        st.download_button(
            "Download Hasil",
            buffer.tobytes(),
            "hasil.png",
            "image/png",
            width="stretch",
        )
