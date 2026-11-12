# LATIHAN 6: Menggabungkan Grafik dalam Dashboard Sederhana
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

DATA_FILE = Path(__file__).resolve().parent / "penjualan_nusantaramart - penjualan_nusantaramart(1).csv"
df = pd.read_csv(DATA_FILE)
df["tanggal"] = pd.to_datetime(df["tanggal"])

# Data yang diperlukan untuk grafik dashboard
total_kategori = (
    df.groupby("kategori_produk")["total"]
    .sum()
    .sort_values(ascending=False)
)
tren_bulanan = df.groupby(df["tanggal"].dt.to_period("M"))["total"].sum()

sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Dashboard Analisis Penjualan Nusantara Mart", fontsize=16)

# Grafik 1: Bar chart total penjualan per kategori
sns.barplot(
    x=total_kategori.values,
    y=total_kategori.index,
    color="cornflowerblue",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Total Penjualan per Kategori")
axes[0, 0].set_xlabel("Total Penjualan (Rp)")
axes[0, 0].set_ylabel("Kategori Produk")
axes[0, 0].xaxis.set_major_formatter(
    FuncFormatter(lambda nilai, posisi: f"Rp{nilai:,.0f}")
)

# Grafik 2: Line chart tren penjualan bulanan
axes[0, 1].plot(
    tren_bulanan.index.astype(str),
    tren_bulanan.values,
    marker="o",
    color="crimson"
)
axes[0, 1].set_title("Tren Penjualan Bulanan")
axes[0, 1].set_xlabel("Bulan")
axes[0, 1].set_ylabel("Total Penjualan (Rp)")
axes[0, 1].yaxis.set_major_formatter(
    FuncFormatter(lambda nilai, posisi: f"Rp{nilai:,.0f}")
)
axes[0, 1].tick_params(axis="x", rotation=35)

# Grafik 3: Histogram rating pelanggan
sns.histplot(
    data=df,
    x="rating_pelanggan",
    bins=[1.5, 2.5, 3.5, 4.5, 5.5],
    color="seagreen",
    edgecolor="white",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Distribusi Rating Pelanggan")
axes[1, 0].set_xlabel("Rating Pelanggan")
axes[1, 0].set_ylabel("Frekuensi")
axes[1, 0].set_xticks([2, 3, 4, 5])

# Grafik 4: Boxplot jumlah pembelian per kategori
sns.boxplot(
    data=df,
    x="kategori_produk",
    y="jumlah",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Sebaran Jumlah Pembelian per Kategori")
axes[1, 1].set_xlabel("Kategori Produk")
axes[1, 1].set_ylabel("Jumlah Barang")
axes[1, 1].tick_params(axis="x", rotation=20)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
