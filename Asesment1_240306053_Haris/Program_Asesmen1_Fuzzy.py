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
