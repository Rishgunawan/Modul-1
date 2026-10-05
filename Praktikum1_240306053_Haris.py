import numpy as np
import matplotlib.pyplot as plt

# 1. FUNGSI CRISP

def crisp_kritis(waktu, threshold=8):
    """
    Fungsi karakteristik Crisp.

    Jika waktu tunggu >= 8 jam:
        nilai = 1 (Kritis)
    Jika waktu tunggu < 8 jam:
        nilai = 0 (Tidak Kritis)
    """
    return np.where(waktu >= threshold, 1.0, 0.0)

# 2. FUNGSI FUZZY

def fuzzy_kritis(waktu, a=4, b=12):
    """
    Fungsi keanggotaan Fuzzy Linear Naik.

    x < 4       -> 0
    4 <= x <= 12 -> (x - 4) / (12 - 4)
    x > 12      -> 1
    """

    derajat = (waktu - a) / (b - a)

    return np.clip(derajat, 0.0, 1.0)

# 3. DATA PENGUJIAN

data_uji = np.array([
    2,
    4,
    6,
    7.9,
    8.0,
    8.1,
    10,
    12,
    16,
    24
])

# 4. MENAMPILKAN TABEL HASIL

print("=" * 60)
print("PERBANDINGAN CRISP VS FUZZY")
print("=" * 60)

print(
    f"{'Waktu':<10}"
    f"{'Crisp':<10}"
    f"{'Fuzzy':<15}"
    f"{'Interpretasi':<20}"
)

print("-" * 60)

for waktu in data_uji:

    crisp = float(crisp_kritis(waktu))
    fuzzy = float(fuzzy_kritis(waktu))

    interpretasi = f"{fuzzy * 100:.1f}%"

    print(
        f"{waktu:<10.1f}"
        f"{crisp:<10.1f}"
        f"{fuzzy:<15.3f}"
        f"{interpretasi:<20}"
    )

# 5. DATA UNTUK GRAFIK

waktu = np.linspace(0, 24, 500)

y_crisp = crisp_kritis(waktu)
y_fuzzy = fuzzy_kritis(waktu)

# 6. MEMBUAT GRAFIK

plt.figure(figsize=(10, 6))

# Grafik Crisp
plt.step(
    waktu,
    y_crisp,
    label="Crisp (Threshold = 8 jam)",
    linewidth=2.5,
    where="post"
)

# Grafik Fuzzy
plt.plot(
    waktu,
    y_fuzzy,
    label="Fuzzy (Linear Naik [4, 12])",
    linewidth=2.5
)

# Garis batas Crisp
plt.axvline(
    x=8,
    linestyle="--",
    linewidth=1.5,
    label="Batas Crisp = 8 jam"
)

# Garis batas Fuzzy
plt.axvline(
    x=4,
    linestyle=":",
    linewidth=1.5,
    label="Awal Fuzzy = 4 jam"
)

plt.axvline(
    x=12,
    linestyle=":",
    linewidth=1.5,
    label="Akhir Fuzzy = 12 jam"
)

# 7. PENGATURAN GRAFIK

plt.title(
    "Perbandingan Logika Crisp vs Fuzzy\n"
    "Prioritas Tiket Helpdesk TI"
)

plt.xlabel("Waktu Tunggu Tiket (Jam)")

plt.ylabel(
    "Derajat Keanggotaan / Nilai Kebenaran"
)

plt.xlim(0, 24)
plt.ylim(-0.05, 1.1)

plt.grid(
    True,
    linestyle=":",
    alpha=0.6
)

plt.legend()

plt.tight_layout()

# 8. SIMPAN GRAFIK

plt.savefig(
    "praktikum1_crisp_vs_fuzzy.png",
    dpi=300
)

plt.show()
