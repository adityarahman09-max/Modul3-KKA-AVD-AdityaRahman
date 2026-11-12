# LATIHAN 5: Visualisasi Distribusi & Deteksi Outlier
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE = Path(__file__).resolve().parent / "penjualan_nusantaramart - penjualan_nusantaramart(1).csv"
df = pd.read_csv(DATA_FILE)
sns.set_style("whitegrid")

# 1. Histogram distribusi rating pelanggan
plt.figure(figsize=(7, 5))
sns.histplot(
    data=df,
    x="rating_pelanggan",
    bins=[1.5, 2.5, 3.5, 4.5, 5.5],
    color="seagreen",
    edgecolor="white"
)
plt.title("Distribusi Rating Pelanggan")
plt.xlabel("Rating Pelanggan")
plt.ylabel("Frekuensi")
plt.xticks([2, 3, 4, 5])
plt.tight_layout()
plt.show()

# 2. Boxplot jumlah pembelian untuk setiap kategori produk
plt.figure(figsize=(9, 5))
sns.boxplot(
    data=df,
    x="kategori_produk",
    y="jumlah"
)
plt.title("Sebaran Jumlah Pembelian per Kategori Produk")
plt.xlabel("Kategori Produk")
plt.ylabel("Jumlah Barang")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# 3. Menampilkan frekuensi rating dan nilai di luar batas IQR per kategori
print("Frekuensi rating pelanggan:")
print(df["rating_pelanggan"].value_counts().sort_index())

print("\nPotensi outlier jumlah pembelian berdasarkan aturan IQR:")
for kategori, data_kategori in df.groupby("kategori_produk"):
    q1 = data_kategori["jumlah"].quantile(0.25)
    q3 = data_kategori["jumlah"].quantile(0.75)
    iqr = q3 - q1
    batas_bawah = q1 - 1.5 * iqr
    batas_atas = q3 + 1.5 * iqr

    outlier = data_kategori[
        (data_kategori["jumlah"] < batas_bawah) |
        (data_kategori["jumlah"] > batas_atas)
    ]

    print(f"\n{kategori}: {len(outlier)} outlier")
    if not outlier.empty:
        print(outlier[["order_id", "nama_produk", "jumlah", "total"]].to_string(index=False))
