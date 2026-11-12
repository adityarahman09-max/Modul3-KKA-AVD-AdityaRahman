# LATIHAN 4: Visualisasi Hubungan dengan Scatter Plot
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

DATA_FILE = Path(__file__).resolve().parent / "penjualan_nusantaramart - penjualan_nusantaramart(1).csv"
df = pd.read_csv(DATA_FILE)

plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x="jumlah",
    y="total",
    hue="kategori_produk",
    alpha=0.8,
    s=70
)
plt.title("Hubungan Jumlah Pembelian dengan Total Nilai Transaksi")
plt.xlabel("Jumlah Barang")
plt.ylabel("Total Transaksi (Rp)")
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda nilai, posisi: f"Rp{nilai:,.0f}")
)
plt.legend(title="Kategori Produk", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()

# Menghitung korelasi Pearson untuk melihat kekuatan hubungan linear
korelasi = df["jumlah"].corr(df["total"])
print("Korelasi antara jumlah barang dan total transaksi:", round(korelasi, 3))
