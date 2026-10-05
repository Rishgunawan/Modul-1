# ==========================================
# FUNGSI KEANGGOTAAN USIA
# ==========================================

# 1. Bayi / Anak Usia Dini
def fungsi_bayi_naik(x):
    return (x - 0) / 2

def fungsi_bayi_turun(x):
    return (5 - x) / 2


# 2. Anak-anak
def fungsi_anak_naik(x):
    return (x - 5) / 1

def fungsi_anak_turun(x):
    return (9 - x) / 1


# 3. Remaja
def fungsi_remaja_naik(x):
    return (x - 10) / 3

def fungsi_remaja_turun(x):
    return (24 - x) / 4


# 4. Pemuda
def fungsi_pemuda_naik(x):
    return (x - 16) / 3

def fungsi_pemuda_turun(x):
    return (30 - x) / 3


# 5. Dewasa
def fungsi_dewasa_naik(x):
    return (x - 18) / 7

def fungsi_dewasa_turun(x):
    return (59 - x) / 7


# 6. Lanjut Usia
def fungsi_lansia_naik(x):
    return (x - 60) / 5


# ==========================================
# KONEKSI DATABASE MYSQL
# ==========================================

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hrsgnw31",
    database="fuzzy_modul1"
)

cursor = db.cursor()


# ==========================================
# DAFTAR TABEL USIA
# ==========================================

tabel_usia = {
    "Bayi / Anak Usia Dini": "usia_bayi",
    "Anak-anak": "usia_anak",
    "Remaja": "usia_remaja",
    "Pemuda": "usia_pemuda",
    "Dewasa": "usia_dewasa",
    "Lanjut Usia": "usia_lansia"
}


# ==========================================
# MENCARI INTERVAL DARI DATABASE
# ==========================================

def cari_interval(nama_tabel, usia):

    query = f"""
        SELECT usia_min, usia_max, nilai_fuzzy
        FROM {nama_tabel}
        WHERE %s >= usia_min
        AND (
            %s < usia_max
            OR (%s = 150 AND usia_max = 150)
        )
    """

    cursor.execute(query, (usia, usia, usia))

    hasil = cursor.fetchone()

    return hasil


# ==========================================
# DAFTAR FUNGSI
# ==========================================

fungsi = {
    "fungsi_bayi_naik": fungsi_bayi_naik,
    "fungsi_bayi_turun": fungsi_bayi_turun,

    "fungsi_anak_naik": fungsi_anak_naik,
    "fungsi_anak_turun": fungsi_anak_turun,

    "fungsi_remaja_naik": fungsi_remaja_naik,
    "fungsi_remaja_turun": fungsi_remaja_turun,

    "fungsi_pemuda_naik": fungsi_pemuda_naik,
    "fungsi_pemuda_turun": fungsi_pemuda_turun,

    "fungsi_dewasa_naik": fungsi_dewasa_naik,
    "fungsi_dewasa_turun": fungsi_dewasa_turun,

    "fungsi_lansia_naik": fungsi_lansia_naik
}


# ==========================================
# MENGHITUNG NILAI KEANGGOTAAN
# ==========================================

def hitung_keanggotaan(nama_tabel, usia):

    hasil = cari_interval(nama_tabel, usia)

    if hasil is None:
        return 0

    usia_min, usia_max, nilai_fuzzy = hasil

    # Jika nilai di database adalah 0
    if nilai_fuzzy == "0":
        return 0

    # Jika nilai di database adalah 1
    elif nilai_fuzzy == "1":
        return 1

    # Jika nilai di database berupa nama fungsi
    elif nilai_fuzzy in fungsi:

        nilai = fungsi[nilai_fuzzy](usia)

        # Membatasi nilai 0 sampai 1
        nilai = max(0, min(1, nilai))

        return nilai

    else:
        return 0


# ==========================================
# INPUT USIA
# ==========================================

usia = float(input("Masukkan usia (0-150): "))

if usia < 0 or usia > 150:

    print("Usia harus berada antara 0 sampai 150 tahun.")

else:

    # ==========================================
    # PROSES FUZZIFIKASI
    # ==========================================

    print("\n==========================================")
    print("HASIL FUZZIFIKASI USIA")
    print("==========================================")
    print("Usia :", usia, "tahun")
    print("------------------------------------------")

    for kategori, tabel in tabel_usia.items():

        nilai = hitung_keanggotaan(tabel, usia)

        print(f"{kategori:<25} : {nilai:.2f}")


# ==========================================
# MENUTUP KONEKSI DATABASE
# ==========================================

cursor.close()
db.close()
