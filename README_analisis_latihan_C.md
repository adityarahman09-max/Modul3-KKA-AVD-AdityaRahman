# Analisis Latihan C 

## Analisis Latihan 1 – Eksplorasi Data & Statistika Deskriptif

Kategori **Elektronik** memiliki rata-rata nilai transaksi tertinggi, yaitu sekitar **Rp363.541,67** per transaksi. Posisi berikutnya adalah Fashion sekitar Rp353.900,00, sedangkan rata-rata terendah terdapat pada Makanan & Minuman, sekitar Rp70.441,86.

Berdasarkan pemeriksaan data, tidak ada kolom yang memiliki nilai kosong. Hal ini terlihat dari jumlah `Non-Null Count` pada `df.info()` yang sama dengan jumlah baris, yaitu 220 untuk setiap kolom. Pemeriksaan `df.isnull().sum()` juga menghasilkan nilai 0 pada seluruh kolom.

Mean kolom `total` adalah sekitar **Rp238.486,36**, sedangkan mediannya **Rp125.000,00**. Mean yang jauh lebih besar daripada median menunjukkan sebaran transaksi cenderung menceng ke kanan (*right-skewed*). Artinya, terdapat sejumlah transaksi bernilai besar yang menaikkan nilai rata-rata.

## Analisis Latihan 2 – Bar Chart

Kategori dengan total penjualan tertinggi adalah **Fashion**, sebesar **Rp17.695.000**. Elektronik berada sangat dekat di posisi kedua dengan Rp17.450.000. Sementara itu, total penjualan terendah berasal dari kategori **Makanan & Minuman**, sebesar **Rp3.029.000**.

Berdasarkan grafik, Nusantara Mart dapat menjaga ketersediaan stok produk Fashion dan Elektronik karena kedua kategori tersebut memberikan kontribusi penjualan terbesar. Untuk Makanan & Minuman, perusahaan dapat mengevaluasi pilihan produk, harga, dan strategi promosi. Evaluasi lebih lanjut diperlukan sebelum mengurangi atau menambah stok secara besar-besaran.

## Analisis Latihan 3 – Line Chart

Bulan dengan total penjualan tertinggi adalah **Mei 2026**, sebesar **Rp13.585.000**. Total penjualan bulanan meningkat dari Januari (Rp6.147.000) hingga mencapai puncak pada Mei. Pada Juni, penjualan turun menjadi **Rp6.992.000**.

Dengan demikian, tren penjualan tidak terus meningkat, melainkan naik dari Januari sampai Mei lalu turun cukup tajam pada Juni. Data yang tersedia tidak mencantumkan informasi promosi, perubahan stok, atau musim belanja, sehingga penyebab kenaikan dan penurunan tersebut belum dapat dipastikan. Manajemen sebaiknya memeriksa catatan promosi, stok, dan aktivitas penjualan pada bulan-bulan tersebut.

## Analisis Latihan 4 – Scatter Plot

Scatter plot memperlihatkan kecenderungan hubungan **positif** antara jumlah barang dan total nilai transaksi: semakin banyak barang yang dibeli, umumnya semakin besar total transaksinya. Nilai korelasi Pearson pada dataset sekitar **0,854**, yang menunjukkan hubungan linear positif yang kuat.

Terdapat sejumlah titik yang jauh dari kumpulan transaksi umum, terutama pada jumlah pembelian yang tinggi. Contohnya, kategori Elektronik memiliki transaksi 40 unit dengan total Rp3.400.000 dan dua transaksi 25 unit. Kategori Olahraga juga memiliki transaksi 25 dan 40 unit. Titik-titik tersebut dapat diperiksa lebih lanjut sebagai transaksi dalam jumlah besar. Namun, data ini belum membuktikan bahwa transaksi tersebut berasal dari reseller.

## Analisis Latihan 5 – Histogram & Boxplot

Distribusi rating pelanggan cenderung **tinggi**. Rating 4 muncul sebanyak 92 kali dan rating 5 sebanyak 83 kali. Jika digabungkan, rating 4–5 berjumlah 175 dari 220 transaksi atau sekitar **79,55%**. Rating 3 muncul 41 kali, sedangkan rating 2 muncul 4 kali. Rata-rata rating pelanggan adalah sekitar 4,15 dari 5.

Berdasarkan boxplot jumlah pembelian per kategori dan aturan IQR, potensi outlier ditemukan pada kategori **Elektronik (3 data)**, **Fashion (1 data)**, **Kesehatan (1 data)**, dan **Olahraga (3 data)**. Tidak ditemukan outlier pada kategori Makanan & Minuman. Nilai yang menonjol antara lain pembelian 25–40 unit pada Elektronik dan Olahraga, serta 25 unit pada Kesehatan. Kemungkinan penyebabnya dapat berupa pembelian grosir, reseller, atau pesanan khusus, tetapi hal tersebut perlu diverifikasi dengan informasi transaksi tambahan.

## Analisis Latihan 6 – Dashboard Sederhana

Dashboard menggabungkan empat grafik dalam satu tampilan sehingga manajer dapat membandingkan beberapa aspek bisnis secara bersamaan. Bar chart menunjukkan kategori penyumbang penjualan, line chart memperlihatkan perubahan penjualan bulanan, histogram merangkum rating pelanggan, dan boxplot memperlihatkan sebaran jumlah pembelian serta potensi outlier. Penyajian ini memudahkan pembaca melihat keterkaitan antartemuan tanpa berpindah-pindah grafik.

Sebagai manajer Nusantara Mart, keputusan yang dapat dipertimbangkan adalah menjaga stok Fashion dan Elektronik, meninjau strategi kategori Makanan & Minuman, serta menelusuri penyebab penurunan penjualan pada Juni 2026. Perusahaan juga dapat mempertahankan hal-hal yang mendukung kepuasan pelanggan karena mayoritas rating berada pada angka 4–5. Transaksi dengan jumlah pembelian yang menjadi outlier sebaiknya diperiksa untuk memastikan kebutuhan stok dan pola pemesanan. Keputusan akhir perlu didukung data tambahan, seperti catatan promosi, stok, dan tipe pelanggan.
