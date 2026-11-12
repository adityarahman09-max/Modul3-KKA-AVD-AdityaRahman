# LATIHAN 3: Visualisasi Tren dengan Line Chart
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

DATA_FILE = Path(__file__).resolve().parent / "penjualan_nusantaramart - penjualan_nusantaramart(1).csv"
df = pd.read_csv(DATA_FILE)

# Mengubah kolom tanggal menjadi tipe datetime
df["tanggal"] = pd.to_datetime(df["tanggal"])

# Mengelompokkan total penjualan berdasarkan bulan
tren_bulanan = df.groupby(df["tanggal"].dt.to_period("M"))["total"].sum()

plt.figure(figsize=(9, 5))
plt.plot(
    tren_bulanan.index.astype(str),
    tren_bulanan.values,
    marker="o",
    color="crimson"
)
plt.title("Tren Penjualan Bulanan")
plt.xlabel("Bulan")
plt.ylabel("Total Penjualan (Rp)")
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda nilai, posisi: f"Rp{nilai:,.0f}")
)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Menampilkan bulan dengan penjualan tertinggi
bulan_tertinggi = tren_bulanan.idxmax()
print("Total penjualan per bulan:")
print(tren_bulanan)
print("\nBulan dengan penjualan tertinggi:", bulan_tertinggi, "- Rp", format(tren_bulanan.max(), ",.0f"))
