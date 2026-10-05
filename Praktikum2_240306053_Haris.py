import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# FUNGSI KEANGGOTAAN CPU
# ==========================================================

# 1. Fungsi Keanggotaan Rendah - Bahu Kiri
def mf_rendah(x):
    kondisi = [
        x <= 20,
        (x > 20) & (x < 40),
        x >= 40
    ]

    pilihan = [
        1.0,
        (40 - x) / (40 - 20),
        0.0
    ]

    return np.select(kondisi, pilihan)


# 2. Fungsi Keanggotaan Normal - Segitiga
def mf_normal(x):
    kondisi = [
        x <= 30,
        (x > 30) & (x <= 50),
        (x > 50) & (x < 70),
        x >= 70
    ]

    pilihan = [
        0.0,
        (x - 30) / (50 - 30),
        (70 - x) / (70 - 50),
        0.0
    ]

    return np.select(kondisi, pilihan)


# 3. Fungsi Keanggotaan Tinggi - Bahu Kanan
def mf_tinggi(x):
    kondisi = [
        x <= 60,
        (x > 60) & (x < 80),
        x >= 80
    ]

    pilihan = [
        0.0,
        (x - 60) / (80 - 60),
        1.0
    ]

    return np.select(kondisi, pilihan)


# ==========================================================
# VARIABEL LINGUISTIK
# ==========================================================

variabel_cpu = {
    "nama": "Penggunaan CPU Server",
    "satuan": "%",
    "semesta": (0, 100),
    "label": {
        "Rendah": mf_rendah,
        "Normal": mf_normal,
        "Tinggi": mf_tinggi
    }
}


# ==========================================================
# FUZZIFIKASI
# ==========================================================

def fuzzifikasi(nilai_cpu, variabel):
    hasil = {}

    batas_min, batas_max = variabel["semesta"]

    if not (batas_min <= nilai_cpu <= batas_max):
        raise ValueError(
            f"Input harus berada pada [{batas_min}, {batas_max}]"
        )

    for nama_label, fungsi_mf in variabel["label"].items():
        derajat = float(fungsi_mf(np.array([nilai_cpu]))[0])
        hasil[nama_label] = round(derajat, 2)

    return hasil


# ==========================================================
# PENGUJIAN CPU = 10%
# ==========================================================

nilai_cpu = 10

hasil = fuzzifikasi(nilai_cpu, variabel_cpu)

print("HASIL FUZZIFIKASI PENGGUNAAN CPU SERVER")
print("=" * 45)
print(f"Input CPU = {nilai_cpu}%")
print(f"Rendah    = {hasil['Rendah']:.2f}")
print(f"Normal    = {hasil['Normal']:.2f}")
print(f"Tinggi    = {hasil['Tinggi']:.2f}")


# ==========================================================
# MEMBUAT GRAFIK
# ==========================================================

x = np.linspace(0, 100, 500)

y_rendah = mf_rendah(x)
y_normal = mf_normal(x)
y_tinggi = mf_tinggi(x)

plt.figure(figsize=(10, 6))

plt.plot(
    x, y_rendah,
    label="Rendah",
    linewidth=2.5
)

plt.plot(
    x, y_normal,
    label="Normal",
    linewidth=2.5
)

plt.plot(
    x, y_tinggi,
    label="Tinggi",
    linewidth=2.5
)

plt.title("Fungsi Keanggotaan Penggunaan CPU Server")
plt.xlabel("Penggunaan CPU (%)")
plt.ylabel("Derajat Keanggotaan μ(x)")

plt.xlim(0, 100)
plt.ylim(-0.05, 1.05)

plt.grid(True, linestyle=":")
plt.legend()
plt.tight_layout()

# Menyimpan grafik
plt.savefig(
    "grafik_fungsi_keanggotaan_cpu.png",
    dpi=300
)

plt.show()
