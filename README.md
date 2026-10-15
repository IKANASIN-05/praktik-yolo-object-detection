# Praktik Object Detection Menggunakan YOLO

## Deskripsi

Praktik object detection menggunakan Ultralytics YOLO pada dataset sendiri (botol dan box, 100 gambar beranotasi). Praktik meliputi persiapan lingkungan Python, pelatihan model (eksperimen E1 dan E3), penyimpanan hasil, analisis metrik evaluasi, dan pengujian model pada gambar.

## Lingkungan

- Sistem operasi: Ubuntu
- Bahasa pemrograman: Python
- Framework: Ultralytics YOLO
- Library pendukung: OpenCV dan Pandas
- Dataset: botol dan box (100 gambar, anotasi bounding box manual)
- Perangkat pemrosesan: CPU

## Struktur Pengumpulan

- `pengumpulan/data_proyek.txt`: deskripsi data yang dipakai (Tahap 1-2).
- `pengumpulan/E1/` dan `pengumpulan/E3/`: `results.png` dan `results.csv` (Tahap 3).
- `pengumpulan/hasil_praktik_4222401030.csv` dan `.txt`: data dan analisis gabungan (Tahap 4-6).
- `pengumpulan/prediksi/`: hasil deteksi E1 dan E3 pada data validasi.
- `dataset_yolo/`: dataset botol/box beranotasi format YOLO (gambar, label, data.yaml).
- `pengumpulan/Read.Me`: laporan praktik.

## Menjalankan Praktik

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install ultralytics opencv-python pandas
    python anotasi.py      # gambar bounding box (butuh folder dataset/ lokal)
    python split_yolo.py   # bagi train/val dan buat data.yaml
    bash latih.sh          # latih E1 dan E3

Hasil training tersimpan di `runs/detect/hasil/`, lalu `results.png` dan `results.csv` disalin ke `pengumpulan/E1/` dan `pengumpulan/E3/`.

## Hasil Eksperimen

| Eksperimen | Epoch | Precision | Recall | mAP50 | mAP50-95 | Train box loss |
|---|---|---|---|---|---|---|
| E1 | 5 | 0.838 | 1.000 | 0.973 | 0.585 | 1.178 |
| E3 | 10 | 0.973 | 0.950 | 0.987 | 0.560 | 1.013 |

E3 lebih presisi dan memiliki loss lebih rendah, tetapi recall dan mAP50-95 sedikit turun. Dengan validasi hanya 20 gambar, selisihnya belum cukup untuk menyimpulkan satu model pasti lebih baik. Detail lengkap ada di `pengumpulan/Read.Me`.

## Hasil Test

Model diuji pada 20 gambar validasi. Hasil deteksi tersimpan di `pengumpulan/prediksi/hasil_E1_data/` dan `pengumpulan/prediksi/hasil_E3_data/`.

## Referensi

- <https://docs.ultralytics.com/datasets/detect/coco>
- <https://academy.ultralytics.com/courses/train-your-first-yolo/prepare-a-dataset>
- <https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html>
