"""Bagi dataset beranotasi jadi train/val (80/20 per kelas) + buat data.yaml."""
import random, shutil
from pathlib import Path

ROOT = Path("dataset_yolo")
IMG = ROOT / "images_all"
LBL = ROOT / "labels_all"
random.seed(42)

per_kelas = {0: [], 1: []}
for l in sorted(LBL.glob("*.txt")):
    cid = int(l.read_text().split()[0])
    per_kelas[cid].append(l.stem)

for sub in ("images/train", "images/val", "labels/train", "labels/val"):
    d = ROOT / sub
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)

for cid, nama in per_kelas.items():
    random.shuffle(nama)
    n_val = max(1, round(len(nama) * 0.2))
    for i, stem in enumerate(nama):
        split = "val" if i < n_val else "train"
        shutil.copy(IMG / f"{stem}.jpg", ROOT / f"images/{split}/{stem}.jpg")
        shutil.copy(LBL / f"{stem}.txt", ROOT / f"labels/{split}/{stem}.txt")
    print(f"kelas {cid}: {len(nama) - n_val} train, {n_val} val")

(ROOT / "data.yaml").write_text(
    "train: images/train\nval: images/val\n"
    "names:\n  0: botol\n  1: box\n"
)
print("data.yaml ditulis:", ROOT / "data.yaml")
