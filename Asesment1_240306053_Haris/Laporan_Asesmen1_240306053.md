# FINAL PRACTICAL ASSIGNMENT 1: FUZZY MODELING PROJECT

## 1. JUDUL PROYEK & IDENTITAS MAHASISWA

**Judul Proyek:** Sistem Deteksi Dini Beban Server (Server Overload Warning System)

**Nama:** Lalu Muh Harista Gunawan  
**NIM:** 240306053

---

# 2. LATAR BELAKANG & DESKRIPSI PERMASALAHAN

Server merupakan salah satu komponen penting dalam sistem teknologi informasi. Ketika beban server terlalu tinggi, kinerja server dapat menurun dan menyebabkan waktu respons menjadi lebih lama. Kondisi tersebut dapat mengganggu layanan yang digunakan oleh pengguna.

Dalam kondisi nyata, penggunaan CPU dan waktu respons tidak selalu berada pada kondisi yang tegas. Sebagai contoh, penggunaan CPU sebesar 65% tidak selalu dapat langsung dikategorikan sebagai rendah atau tinggi. Oleh karena itu, digunakan logika fuzzy agar suatu nilai dapat memiliki derajat keanggotaan pada beberapa kategori sekaligus.

Proyek ini merancang model fuzzy untuk mendeteksi kondisi beban server berdasarkan dua variabel input, yaitu **Penggunaan CPU** dan **Waktu Respons Server**. Model juga memiliki satu variabel output yaitu **Risiko Overload Server**. Pada tahap ini dilakukan pemodelan fungsi keanggotaan dan fuzzifikasi menggunakan Python tanpa menggunakan library fuzzy siap pakai. Proses inferensi dan penentuan output akhir akan dikembangkan pada Modul 2.

---

# 3. PERANCANGAN SISTEM FUZZY

## 3.1 Semesta Pembicaraan dan Domain Variabel

Sistem fuzzy menggunakan dua variabel input dan satu variabel output.

| Variabel | Jenis | Semesta | Label Linguistik | Bentuk Fungsi |
|---|---|---|---|---|
| Penggunaan CPU | Input | [0, 100] % | Rendah, Normal, Tinggi | Trapesium dan Segitiga |
| Waktu Respons Server | Input | [0, 10] detik | Cepat, Sedang, Lambat | Trapesium dan Segitiga |
| Risiko Overload Server | Output | [0, 100] % | Rendah, Sedang, Tinggi | Trapesium dan Segitiga |

### A. Penggunaan CPU

- Rendah: [0, 0, 20, 40]
- Normal: [30, 50, 70]
- Tinggi: [60, 80, 100, 100]

### B. Waktu Respons Server

- Cepat: [0, 0, 2, 4]
- Sedang: [3, 5, 7]
- Lambat: [6, 8, 10, 10]

### C. Risiko Overload Server

- Rendah: [0, 0, 30, 50]
- Sedang: [40, 60, 80]
- Tinggi: [70, 85, 100, 100]

---

## 3.2 Penurunan Matematis Fungsi Keanggotaan

Fungsi keanggotaan diturunkan dari titik-titik pembentuk kurva. Persamaan garis linear diperoleh menggunakan persamaan:

$$
\frac{y-y_1}{y_2-y_1}=\frac{x-x_1}{x_2-x_1}
$$

Nilai derajat keanggotaan berada pada rentang:

$$
0\leq \mu(x)\leq 1
$$

### 3.2.1 Fungsi Keanggotaan Penggunaan CPU

#### a. CPU Rendah

Bentuk fungsi adalah trapesium bahu kiri dengan titik:

$$
A=(0,0),\quad B=(0,1),\quad C=(20,1),\quad D=(40,0)
$$

Bagian datar memiliki nilai keanggotaan 1 pada rentang 0 sampai 20. Bagian turun diperoleh dari titik C ke D:

$$
\frac{y-1}{0-1}=\frac{x-20}{40-20}
$$

$$
\frac{y-1}{-1}=\frac{x-20}{20}
$$

$$
-y+1=\frac{x-20}{20}
$$

$$
y=\frac{40-x}{20}
$$

Sehingga fungsi keanggotaannya adalah:

$$
\mu_{CPU\_Rendah}(x)=
\begin{cases}
1, & 0 \leq x \leq20 \\
\frac{40-x}{20}, & 20 < x < 40 \\
0, & x\geq 40
\end{cases}
$$

#### b. CPU Normal

Bentuk fungsi adalah segitiga dengan titik:

$$
A=(30,0),\quad B=(50,1),\quad C=(70,0)
$$

Bagian naik dari A ke B:

$$
\frac{y-0}{1-0}=\frac{x-30}{50-30}
$$

$$
y=\frac{x-30}{20}
$$

Bagian turun dari B ke C:

$$
\frac{y-1}{0-1}=\frac{x-50}{70-50}
$$

$$
y=\frac{70-x}{20}
$$

Sehingga:

$$
\mu_{CPU\_Normal}(x)=
\begin{cases}
0, & x \leq30 \\
\frac{x-30}{20}, & 30 < x \leq50 \\
\frac{70-x}{20}, & 50 < x < 70 \\
0, & x\geq 70
\end{cases}
$$

#### c. CPU Tinggi

Bentuk fungsi adalah trapesium bahu kanan dengan titik:

$$
A=(60,0),\quad B=(80,1),\quad C=(100,1),\quad D=(100,0)
$$

Bagian naik dari A ke B:

$$
\frac{y-0}{1-0}=\frac{x-60}{80-60}
$$

$$
y=\frac{x-60}{20}
$$

Setelah x mencapai 80, derajat keanggotaan tetap 1. Jadi:

$$
\mu_{CPU\_Tinggi}(x)=
\begin{cases}
0, & x \leq 60 \\
\frac{x-60}{20}, & 60 < x < 80 \\
1, & x\geq 80
\end{cases}
$$

### 3.2.2 Fungsi Keanggotaan Waktu Respons Server

#### a. Respons Cepat

Bentuk fungsi adalah trapesium bahu kiri dengan titik:

$$
A=(0,0),\quad B=(0,1),\quad C=(2,1),\quad D=(4,0)
$$

Bagian turun dari C ke D:

$$
\frac{y-1}{0-1}=\frac{x-2}{4-2}
$$

$$
y=\frac{4-x}{2}
$$

Sehingga:

$$
\mu_{Cepat}(x)=
\begin{cases}
1, & 0\leq x\leq 2 \\
\frac{4-x}{2}, & 2 < x < 4 \\
0, & x\geq 4
\end{cases}
$$

#### b. Respons Sedang

Bentuk fungsi adalah segitiga dengan titik:

$$
A=(3,0),\quad B=(5,1),\quad C=(7,0)
$$

Bagian naik:

$$
\frac{y-0}{1-0}=\frac{x-3}{5-3}
$$

$$
y=\frac{x-3}{2}
$$

Bagian turun:

$$
\frac{y-1}{0-1}=\frac{x-5}{7-5}
$$

$$
y=\frac{7-x}{2}
$$

Sehingga:

$$
\mu_{Sedang}(x)=
\begin{cases}
0, & x\ leq3 \\
\frac{x-3}{2}, & 3 < x \ leq5 \\
\frac{7-x}{2}, & 5 < x < 7 \\
0, & x\geq 7
\end{cases}
$$

#### c. Respons Lambat

Bentuk fungsi adalah trapesium bahu kanan dengan titik:

$$
A=(6,0),\quad B=(8,1),\quad C=(10,1),\quad D=(10,0)
$$

Bagian naik dari A ke B:

$$
\frac{y-0}{1-0}=\frac{x-6}{8-6}
$$

$$
y=\frac{x-6}{2}
$$

Setelah x mencapai 8, derajat keanggotaan tetap 1. Maka:

$$
\mu_{Lambat}(x)=
\begin{cases}
0, & x\ leq 6 \\
\frac{x-6}{2}, & 6 < x < 8 \\
1, & x\geq 8
\end{cases}
$$

### 3.2.3 Fungsi Keanggotaan Risiko Overload Server

#### a. Risiko Rendah

Bentuk fungsi adalah trapesium bahu kiri dengan titik:

$$
A=(0,0),\quad B=(0,1),\quad C=(30,1),\quad D=(50,0)
$$

Bagian turun dari C ke D:

$$
\frac{y-1}{0-1}=\frac{x-30}{50-30}
$$

$$
y=\frac{50-x}{20}
$$

Sehingga:

$$
\mu_{Risiko\_Rendah}(x)=
\begin{cases}
1, & 0\leq x\ leq 30 \\
\frac{50-x}{20}, & 30 < x < 50 \\
0, & x\geq 50
\end{cases}
$$

#### b. Risiko Sedang

Bentuk fungsi adalah segitiga dengan titik:

$$
A=(40,0),\quad B=(60,1),\quad C=(80,0)
$$

Bagian naik:

$$
\frac{y-0}{1-0}=\frac{x-40}{60-40}
$$

$$
y=\frac{x-40}{20}
$$

Bagian turun:

$$
\frac{y-1}{0-1}=\frac{x-60}{80-60}
$$

$$
y=\frac{80-x}{20}
$$

Sehingga:

$$
\mu_{Risiko\_Sedang}(x)=
\begin{cases}
0, & x\ leq40 \\
\frac{x-40}{20}, & 40 < x \ leq 60 \\
\frac{80-x}{20}, & 60 < x < 80 \\
0, & x\geq 80
\end{cases}
$$

#### c. Risiko Tinggi

Bentuk fungsi adalah trapesium bahu kanan dengan titik:

$$
A=(70,0),\quad B=(85,1),\quad C=(100,1),\quad D=(100,0)
$$

Bagian naik dari A ke B:

$$
\frac{y-0}{1-0}=\frac{x-70}{85-70}
$$

$$
y=\frac{x-70}{15}
$$

Setelah x mencapai 85, derajat keanggotaan tetap 1. Maka:

$$
\mu_{Risiko\_Tinggi}(x)=
\begin{cases}
0, & x\ leq 70 \\
\frac{x-70}{15}, & 70 < x < 85 \\
1, & x\geq 85
\end{cases}
$$

---

## 3.3 Ilustrasi Grafik Desain

Grafik fungsi keanggotaan dibuat menggunakan Python dan Matplotlib. Terdapat tiga grafik utama:

1. `cpu.png` untuk fungsi keanggotaan Penggunaan CPU.
2. `waktu_respons.png` untuk fungsi keanggotaan Waktu Respons Server.
3. `risiko_overload.png` untuk fungsi keanggotaan Risiko Overload Server.

Setiap grafik menampilkan sumbu nilai variabel pada sumbu X dan derajat keanggotaan 0 sampai 1 pada sumbu Y.

Desain fungsi dibuat saling beririsan pada daerah transisi sehingga tidak terdapat celah antara label linguistik. Hal ini memungkinkan suatu nilai berada pada lebih dari satu kategori dengan derajat keanggotaan yang berbeda.

---

# 4. IMPLEMENTASI PYTHON

## 4.1 Source Code Lengkap

```python
import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# FUNGSI DASAR KEANGGOTAAN
# ==========================================================

def trapezoid(x, a, b, c, d):
    if x <= a:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 0.0


def triangle(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    else:
        return 0.0


# ==========================================================
# FUNGSI KEANGGOTAAN PENGGUNAAN CPU
# ==========================================================

def cpu_rendah(x):
    return trapezoid(x, 0, 0, 20, 40)


def cpu_normal(x):
    return triangle(x, 30, 50, 70)


def cpu_tinggi(x):
    return trapezoid(x, 60, 80, 100, 100)


# ==========================================================
# FUNGSI KEANGGOTAAN WAKTU RESPONS
# ==========================================================

def respons_cepat(x):
    return trapezoid(x, 0, 0, 2, 4)


def respons_sedang(x):
    return triangle(x, 3, 5, 7)


def respons_lambat(x):
    return trapezoid(x, 6, 8, 10, 10)


# ==========================================================
# FUNGSI KEANGGOTAAN RISIKO OVERLOAD
# ==========================================================

def risiko_rendah(x):
    return trapezoid(x, 0, 0, 30, 50)


def risiko_sedang(x):
    return triangle(x, 40, 60, 80)


def risiko_tinggi(x):
    return trapezoid(x, 70, 85, 100, 100)


# ==========================================================
# MODEL LINGUISTIK
# ==========================================================

model = {
    "Penggunaan CPU": {
        "Rendah": cpu_rendah,
        "Normal": cpu_normal,
        "Tinggi": cpu_tinggi
    },

    "Waktu Respons": {
        "Cepat": respons_cepat,
        "Sedang": respons_sedang,
        "Lambat": respons_lambat
    },

    "Risiko Overload": {
        "Rendah": risiko_rendah,
        "Sedang": risiko_sedang,
        "Tinggi": risiko_tinggi
    }
}


# ==========================================================
# FUZZIFIKASI
# ==========================================================

def fuzzifikasi(input_dict):
    cpu = input_dict["cpu"]
    respons = input_dict["respons"]

    hasil = {
        "Penggunaan CPU": {},
        "Waktu Respons": {}
    }

    for label, fungsi in model["Penggunaan CPU"].items():
        hasil["Penggunaan CPU"][label] = fungsi(cpu)

    for label, fungsi in model["Waktu Respons"].items():
        hasil["Waktu Respons"][label] = fungsi(respons)

    return hasil


# ==========================================================
# FUNGSI PLOT
# ==========================================================

def plot_variabel(nama_variabel, fungsi_dict, batas, nama_file):
    x = np.linspace(batas[0], batas[1], 500)

    plt.figure(figsize=(10, 6))

    for label, fungsi in fungsi_dict.items():
        y = np.array([fungsi(nilai) for nilai in x])
        plt.plot(x, y, linewidth=2, label=label)

    plt.xlabel("Nilai")
    plt.ylabel("Derajat Keanggotaan")
    plt.title("Fungsi Keanggotaan - " + nama_variabel)

    plt.xlim(batas[0], batas[1])
    plt.ylim(-0.05, 1.05)

    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(nama_file, dpi=300)
    plt.show()


# ==========================================================
# MEMBUAT GRAFIK
# ==========================================================

plot_variabel(
    "Penggunaan CPU",
    model["Penggunaan CPU"],
    (0, 100),
    "cpu.png"
)

plot_variabel(
    "Waktu Respons Server",
    model["Waktu Respons"],
    (0, 10),
    "waktu_respons.png"
)

plot_variabel(
    "Risiko Overload Server",
    model["Risiko Overload"],
    (0, 100),
    "risiko_overload.png"
)


# ==========================================================
# DATA PENGUJIAN
# ==========================================================

data_uji = [
    {
        "kasus": "Kondisi Normal",
        "cpu": 35,
        "respons": 3.5
    },

    {
        "kasus": "Kondisi Ringan",
        "cpu": 15,
        "respons": 1.5
    },

    {
        "kasus": "Kondisi Transisi",
        "cpu": 65,
        "respons": 6.5
    },

    {
        "kasus": "Kondisi Tinggi",
        "cpu": 80,
        "respons": 8
    },

    {
        "kasus": "Kondisi Ekstrem",
        "cpu": 95,
        "respons": 9.5
    }
]


# ==========================================================
# MENAMPILKAN HASIL FUZZIFIKASI
# ==========================================================

print("=" * 70)
print("HASIL FUZZIFIKASI")
print("=" * 70)

for nomor, data in enumerate(data_uji, start=1):

    hasil = fuzzifikasi({
        "cpu": data["cpu"],
        "respons": data["respons"]
    })

    print()
    print(f"Kasus {nomor}: {data['kasus']}")
    print(f"CPU      : {data['cpu']} %")
    print(f"Respons  : {data['respons']} detik")

    print("\nPenggunaan CPU:")

    for label, nilai in hasil["Penggunaan CPU"].items():
        print(f"  {label:<8} : {nilai:.2f}")

    print("\nWaktu Respons:")

    for label, nilai in hasil["Waktu Respons"].items():
        print(f"  {label:<8} : {nilai:.2f}")

    print("-" * 70)
```

## 4.2 Penjelasan Modul & Struktur Data

Program terdiri dari beberapa bagian utama.

### 1. Fungsi `trapezoid()`

Fungsi ini digunakan untuk menghitung derajat keanggotaan dengan bentuk trapesium. Fungsi digunakan pada kategori yang mempunyai bahu kiri atau bahu kanan.

### 2. Fungsi `triangle()`

Fungsi ini digunakan untuk menghitung derajat keanggotaan dengan bentuk segitiga. Nilai keanggotaan meningkat sampai titik puncak bernilai 1 dan kemudian menurun kembali menjadi 0.

### 3. Fungsi Keanggotaan

Fungsi khusus dibuat untuk setiap label, yaitu:

- `cpu_rendah()`
- `cpu_normal()`
- `cpu_tinggi()`
- `respons_cepat()`
- `respons_sedang()`
- `respons_lambat()`
- `risiko_rendah()`
- `risiko_sedang()`
- `risiko_tinggi()`

### 4. Dictionary `model`

Dictionary digunakan untuk mengelompokkan variabel linguistik dan labelnya. Dengan struktur ini, fungsi keanggotaan dapat dipanggil berdasarkan nama variabel dan label.

### 5. Fungsi `fuzzifikasi()`

Fungsi ini menerima nilai crisp CPU dan waktu respons. Nilai tersebut kemudian dihitung terhadap seluruh label linguistik pada masing-masing variabel input.

### 6. Fungsi `plot_variabel()`

Fungsi ini digunakan untuk membuat grafik fungsi keanggotaan menggunakan NumPy dan Matplotlib. Grafik disimpan dalam format PNG dengan resolusi 300 dpi.

### 7. Data Pengujian

Program menggunakan lima skenario pengujian yang mewakili kondisi ringan, normal, transisi, tinggi, dan ekstrem.

Pada tahap Modul 1, variabel output Risiko Overload sudah dimodelkan dan dibuat grafiknya, tetapi belum digunakan untuk menentukan hasil akhir karena proses inferensi fuzzy akan dikembangkan pada Modul 2.

---

# 5. HASIL PENGUJIAN & EVALUASI FUZZIFIKASI

## 5.1 Tabel Pengujian 5 Skenario

Hasil fuzzifikasi dari lima skenario adalah sebagai berikut.

| Kasus | CPU (%) | CPU Rendah | CPU Normal | CPU Tinggi | Respons (detik) | Cepat | Sedang | Lambat |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Kondisi Normal | 35 | 0.25 | 0.25 | 0.00 | 3.5 | 0.25 | 0.25 | 0.00 |
| Kondisi Ringan | 15 | 1.00 | 0.00 | 0.00 | 1.5 | 1.00 | 0.00 | 0.00 |
| Kondisi Transisi | 65 | 0.00 | 0.25 | 0.25 | 6.5 | 0.00 | 0.25 | 0.25 |
| Kondisi Tinggi | 80 | 0.00 | 0.00 | 1.00 | 8.0 | 0.00 | 0.00 | 1.00 |
| Kondisi Ekstrem | 95 | 0.00 | 0.00 | 1.00 | 9.5 | 0.00 | 0.00 | 1.00 |

### Perhitungan Contoh

#### Kasus 1: CPU = 35%

Nilai berada pada daerah transisi CPU Rendah:

$$
\mu_{Rendah}(35)=\frac{40-35}{20}=0.25
$$

Untuk CPU Normal:

$$
\mu_{Normal}(35)=\frac{35-30}{20}=0.25
$$

Sehingga:

- CPU Rendah = 0.25
- CPU Normal = 0.25
- CPU Tinggi = 0

#### Kasus 2: CPU = 15%

Karena CPU 15 berada pada daerah penuh CPU Rendah:

$$
\mu_{Rendah}(15)=1
$$

Sehingga:

- CPU Rendah = 1.00
- CPU Normal = 0
- CPU Tinggi = 0

#### Kasus 3: CPU = 65%

Untuk CPU Normal:

$$
\mu_{Normal}(65)=\frac{70-65}{20}=0.25
$$

Untuk CPU Tinggi:

$$
\mu_{Tinggi}(65)=\frac{65-60}{20}=0.25
$$

Sehingga:

- CPU Rendah = 0
- CPU Normal = 0.25
- CPU Tinggi = 0.25

#### Kasus 4: CPU = 80%

Karena CPU 80 berada pada bagian penuh CPU Tinggi:

$$
\mu_{Tinggi}(80)=1
$$

Sehingga:

- CPU Rendah = 0
- CPU Normal = 0
- CPU Tinggi = 1.00

#### Kasus 5: CPU = 95%

Karena CPU 95 berada pada bagian penuh CPU Tinggi:

$$
\mu_{Tinggi}(95)=1
$$

Sehingga:

- CPU Rendah = 0
- CPU Normal = 0
- CPU Tinggi = 1.00

---

## 5.2 Interpretasi Hasil Derajat Keanggotaan

Pada kondisi normal dengan CPU 35% dan waktu respons 3,5 detik, nilai berada pada daerah transisi sehingga CPU memiliki derajat keanggotaan 0,25 pada kategori Rendah dan Normal. Waktu respons juga memiliki derajat 0,25 pada kategori Cepat dan Sedang.

Pada kondisi ringan dengan CPU 15% dan waktu respons 1,5 detik, kedua variabel berada pada kategori rendah/cepat dengan derajat keanggotaan 1,00. Hal ini menunjukkan kondisi server masih ringan.

Pada kondisi transisi dengan CPU 65% dan waktu respons 6,5 detik, CPU memiliki derajat 0,25 pada Normal dan Tinggi. Waktu respons memiliki derajat 0,25 pada Sedang dan Lambat. Kondisi ini menunjukkan server mulai memasuki daerah transisi menuju kondisi yang lebih berat.

Pada kondisi tinggi dengan CPU 80% dan waktu respons 8 detik, CPU memiliki derajat 1,00 pada Tinggi dan waktu respons memiliki derajat 1,00 pada Lambat. Kondisi ini menunjukkan karakteristik beban server yang tinggi.

Pada kondisi ekstrem dengan CPU 95% dan waktu respons 9,5 detik, CPU tetap memiliki derajat 1,00 pada Tinggi dan waktu respons memiliki derajat 1,00 pada Lambat. Kondisi tersebut merupakan kondisi yang sangat berat dan menjadi dasar untuk pengembangan aturan risiko overload pada Modul 2.

Hasil pengujian menunjukkan bahwa fungsi keanggotaan dapat menghasilkan nilai pada rentang 0 sampai 1 dan dapat menunjukkan kondisi transisi antar kategori. Hal ini merupakan karakteristik utama dari pemodelan fuzzy.

---

# 6. KESIMPULAN & RENCANA PENGEMBANGAN MODUL 2

## Kesimpulan

Pada proyek ini telah dibuat model fuzzy untuk Sistem Deteksi Dini Beban Server. Model menggunakan dua variabel input, yaitu Penggunaan CPU dan Waktu Respons Server, serta satu variabel output yaitu Risiko Overload Server.

Setiap variabel memiliki tiga label linguistik. Fungsi keanggotaan menggunakan kombinasi fungsi trapesium dan segitiga. Implementasi dilakukan menggunakan Python, NumPy, dan Matplotlib tanpa menggunakan library fuzzy siap pakai.

Hasil pengujian terhadap lima skenario menunjukkan bahwa sistem dapat mengubah nilai crisp menjadi derajat keanggotaan antara 0 dan 1. Pada daerah transisi, satu nilai dapat memiliki derajat keanggotaan pada dua kategori sekaligus. Hal ini menunjukkan bahwa model mampu merepresentasikan ketidakpastian kondisi server.

## Rencana Pengembangan Modul 2

Pada Modul 2, model akan dikembangkan dari tahap fuzzifikasi menuju proses inferensi fuzzy. Beberapa aturan yang dapat digunakan sebagai dasar antara lain:

1. **IF CPU Rendah AND Waktu Respons Cepat THEN Risiko Overload Rendah.**
2. **IF CPU Normal AND Waktu Respons Sedang THEN Risiko Overload Sedang.**
3. **IF CPU Tinggi AND Waktu Respons Lambat THEN Risiko Overload Tinggi.**
4. **IF CPU Tinggi AND Waktu Respons Sedang THEN Risiko Overload Tinggi.**
5. **IF CPU Normal AND Waktu Respons Lambat THEN Risiko Overload Tinggi.**

Selanjutnya akan dilakukan proses evaluasi aturan, agregasi, dan defuzzifikasi untuk memperoleh nilai risiko overload server. Model tersebut dapat menjadi dasar pengembangan sistem peringatan dini beban server pada tahap berikutnya.
