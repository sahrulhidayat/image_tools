# Image Tools

Aplikasi ini adalah kumpulan tool pemrosesan citra berbasis Streamlit untuk tugas UAS Pengolahan Citra Digital. Fitur yang tersedia:

- Background Remover
- Object Counter
- Anonymizer
- Color Splash

## Teknologi

- Streamlit sebagai antarmuka web
- OpenCV (`cv2`) untuk pemrosesan citra
- YOLOv8n untuk deteksi objek
- Virtual environment (`venv`) untuk lingkungan Python terisolasi

## Instalasi

1. Buat virtual environment:

```bash
python -m venv venv
```

2. Aktifkan virtual environment:
   - Windows:

   ```bash
   venv\Scripts\activate
   ```

   - macOS / Linux:

   ```bash
   source venv/bin/activate
   ```

3. Instal dependensi:

```bash
pip install -r requirements.txt
```

## Penggunaan

Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

Lalu buka alamat yang ditampilkan di browser.

## Deskripsi Fitur

- **Background Remover**: Menghapus latar belakang dari gambar dan menyimpan hasil sebagai PNG transparan.
- **Object Counter**: Menghitung jumlah objek pada gambar menggunakan model YOLOv8n.
- **Anonymizer**: Menyamarkan wajah atau objek sensitif dengan blur atau kotak.
- **Color Splash**: Menyisakan satu warna dominan pada gambar sementara bagian lainnya diubah menjadi hitam putih.

## Catatan

Pastikan file model YOLOv8n tersedia dan kompatibel dengan implementasi deteksi objek.

--

Dokumen ini dibuat untuk proyek Image Tools UAS Pengolahan Citra Digital.
