# LATIHAN 1: Eksplorasi Data & Statistika Deskriptif dengan Pandas
from pathlib import Path
import pandas as pd

# Letakkan file CSV di folder yang sama dengan file Python ini.
DATA_FILE = Path(__file__).resolve().parent / "penjualan_nusantaramart - penjualan_nusantaramart(1).csv"
df = pd.read_csv(DATA_FILE)

# 1. Melihat lima baris pertama
print("===== 5 BARIS PERTAMA =====")
print(df.head())

# 2. Melihat tipe data dan jumlah data yang terisi pada setiap kolom
print("\n===== INFORMASI DATASET =====")
df.info()

# 3. Ringkasan statistik kolom numerik
print("\n===== STATISTIK DESKRIPTIF =====")
print(df.describe())

# 4. Memeriksa jumlah missing value pada setiap kolom
print("\n===== MISSING VALUE =====")
print(df.isnull().sum())

# 5. Menghitung rata-rata nilai transaksi berdasarkan kategori produk
print("\n===== RATA-RATA TOTAL TRANSAKSI PER KATEGORI =====")
rata_kategori = df.groupby("kategori_produk")["total"].mean()
print(rata_kategori.sort_values(ascending=False))

# 6. Membandingkan mean dan median total transaksi secara keseluruhan
print("\n===== MEAN DAN MEDIAN TOTAL TRANSAKSI =====")
print("Mean   : Rp", format(df["total"].mean(), ",.2f"))
print("Median : Rp", format(df["total"].median(), ",.2f"))
