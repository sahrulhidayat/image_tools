import streamlit as st
from rembg import remove
from PIL import Image
import io

# Konfigurasi halaman
st.set_page_config(page_title="Background Remover", page_icon="🖼️", layout="centered")

if st.button("← Back to Image Tools"):
    st.switch_page("app.py")

# Judul
st.title("Background Remover")

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Baca dan proses gambar
    input_image = Image.open(uploaded_file).convert("RGBA")

    with st.spinner("⏳ Memproses..."):
        output_image = remove(
            input_image,
        )

    # Tampilkan hasil
    st.success("Selesai!")

    col1, col2 = st.columns(2)
    with col1:
        st.image(input_image, caption="Asli", width="stretch")
    with col2:
        st.image(output_image, caption="Hasil", width="stretch")

    # Tombol download
    output_bytes = io.BytesIO()
    output_image.save(output_bytes, format="PNG")
    output_bytes.seek(0)

    st.download_button(
        label="Download Hasil",
        data=output_bytes,
        file_name="result.png",
        mime="image/png",
        width="stretch",
    )
else:
    st.info(
        "Upload gambar dengan kontras yang jelas antara objek dan latar belakang untuk hasil terbaik."
    )
