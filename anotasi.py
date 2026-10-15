"""Anotasi bounding box sederhana (1 objek per gambar) -> format YOLO."""
import cv2, shutil
from pathlib import Path

SUMBER = Path("dataset")            # berisi folder botol/ dan box/
KELAS = {"botol": 0, "box": 1}      # nama folder -> id kelas
OUT_IMG = Path("dataset_yolo/images_all")
OUT_LBL = Path("dataset_yolo/labels_all")
OUT_IMG.mkdir(parents=True, exist_ok=True)
OUT_LBL.mkdir(parents=True, exist_ok=True)

daftar = []
for nama, cid in KELAS.items():
    for p in sorted((SUMBER / nama).glob("*.jpg")):
        daftar.append((p, cid, nama))

print(f"Total gambar: {len(daftar)}")
print("Cara pakai: tarik kotak dengan mouse -> ENTER/SPASI = simpan gambar ini.")
print("Keluar kapan saja: tekan 'c' atau ESC tanpa membuat kotak (progres tersimpan).")
print("Salah gambar? hapus file labelnya di dataset_yolo/labels_all/, jalankan ulang.")

for i, (p, cid, nama) in enumerate(daftar, 1):
    lbl = OUT_LBL / (p.stem + ".txt")
    if lbl.exists():
        continue
    img = cv2.imread(str(p))
    h, w = img.shape[:2]
    skala = 900 / w
    tampil = cv2.resize(img, None, fx=skala, fy=skala)
    judul = f"[{i}/{len(daftar)}] kelas: {nama} - {p.name}"
    x, y, bw, bh = cv2.selectROI(judul, tampil, showCrosshair=False)
    if bw == 0 or bh == 0:
        print("Keluar. Jalankan lagi untuk melanjutkan.")
        break
    x, y, bw, bh = x / skala, y / skala, bw / skala, bh / skala
    xc, yc = (x + bw / 2) / w, (y + bh / 2) / h
    lbl.write_text(f"{cid} {xc:.6f} {yc:.6f} {bw / w:.6f} {bh / h:.6f}\n")
    shutil.copy(p, OUT_IMG / p.name)
    print(f"  tersimpan: {lbl.name}")

cv2.destroyAllWindows()
print("Selesai. Lanjut: python split_yolo.py")
