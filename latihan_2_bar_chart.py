# LATIHAN 2: Visualisasi Perbandingan dengan Bar Chart
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

DATA_FILE = Path(__file__).resolve().parent / "penjualan_nusantaramart - penjualan_nusantaramart(1).csv"
df = pd.read_csv(DATA_FILE)

# Menjumlahkan nilai penjualan untuk setiap kategori produk
total_kategori = (
    df.groupby("kategori_produk")["total"]
    .sum()
    .sort_values(ascending=False)
)

sns.set_style("whitegrid")
plt.figure(figsize=(9, 5))
sns.barplot(
    x=total_kategori.values,
    y=total_kategori.index,
    color="cornflowerblue"
)
plt.title("Total Penjualan per Kategori Produk")
plt.xlabel("Total Penjualan (Rp)")
plt.ylabel("Kategori Produk")
plt.gca().xaxis.set_major_formatter(
    FuncFormatter(lambda nilai, posisi: f"Rp{nilai:,.0f}")
)
plt.tight_layout()
plt.show()

# Menampilkan kategori dengan total penjualan tertinggi dan terendah
print("Total penjualan per kategori:")
print(total_kategori)
print("\nTertinggi:", total_kategori.idxmax(), "- Rp", format(total_kategori.max(), ",.0f"))
print("Terendah :", total_kategori.idxmin(), "- Rp", format(total_kategori.min(), ",.0f"))
