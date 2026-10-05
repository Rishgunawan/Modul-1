import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# FUNGSI KEANGGOTAAN A
# Ketersediaan Bandwidth Cukup
# Segitiga [30, 60, 90]
# ==========================================

def fungsi_A(x):
    if x <= 30 or x >= 90:
        return 0
    elif 30 <= x <= 60:
        return (x - 30) / 30
    else:
        return (90 - x) / 30


# ==========================================
# FUNGSI KEANGGOTAAN B
# Packet Loss Rendah
# Trapesium [40, 55, 75, 95]
# ==========================================

def fungsi_B(x):
    if x <= 40 or x >= 95:
        return 0
    elif 40 <= x <= 55:
        return (x - 40) / 15
    elif 55 <= x <= 75:
        return 1
    else:
        return (95 - x) / 20


# ==========================================
# OPERASI FUZZY
# ==========================================

def zadeh_min(a, b):
    return min(a, b)


def algebraic_product(a, b):
    return a * b


def zadeh_max(a, b):
    return max(a, b)


def algebraic_sum(a, b):
    return a + b - (a * b)


def komplemen(a):
    return 1 - a


# ==========================================
# PENGUJIAN
# ==========================================

data_uji = [35, 50, 65, 80]

print("HASIL EVALUASI BANDWIDTH")
print("=" * 80)

for x in data_uji:

    a = fungsi_A(x)
    b = fungsi_B(x)

    intersection_min = zadeh_min(a, b)
    intersection_product = algebraic_product(a, b)

    union_max = zadeh_max(a, b)
    union_sum = algebraic_sum(a, b)

    not_a = komplemen(a)

    print(f"\nThroughput = {x} Mbps")
    print(f"μA                 = {a:.2f}")
    print(f"μB                 = {b:.2f}")
    print(f"Intersection Min    = {intersection_min:.2f}")
    print(f"Intersection Product= {intersection_product:.2f}")
    print(f"Union Max           = {union_max:.2f}")
    print(f"Union Algebraic Sum= {union_sum:.2f}")
    print(f"Komplemen A         = {not_a:.2f}")


# ==========================================
# PLOT
# ==========================================

x = np.linspace(0, 100, 500)

A = np.array([fungsi_A(i) for i in x])
B = np.array([fungsi_B(i) for i in x])

intersection_min = np.minimum(A, B)
intersection_product = A * B

union_max = np.maximum(A, B)
union_sum = A + B - (A * B)

not_A = 1 - A


# Plot fungsi keanggotaan A dan B
plt.figure(figsize=(10, 6))
plt.plot(x, A, label="A - Bandwidth Cukup")
plt.plot(x, B, label="B - Packet Loss Rendah")

plt.xlabel("Throughput (Mbps)")
plt.ylabel("Derajat Keanggotaan")
plt.title("Fungsi Keanggotaan A dan B")
plt.grid(True)
plt.legend()
plt.show()


# Plot Intersection
plt.figure(figsize=(10, 6))
plt.plot(x, intersection_min, label="Zadeh Min")
plt.plot(x, intersection_product, label="Algebraic Product")

plt.xlabel("Throughput (Mbps)")
plt.ylabel("Derajat Keanggotaan")
plt.title("Operasi Intersection")
plt.grid(True)
plt.legend()
plt.show()


# Plot Union
plt.figure(figsize=(10, 6))
plt.plot(x, union_max, label="Zadeh Max")
plt.plot(x, union_sum, label="Algebraic Sum")

plt.xlabel("Throughput (Mbps)")
plt.ylabel("Derajat Keanggotaan")
plt.title("Operasi Union")
plt.grid(True)
plt.legend()
plt.show()


# Plot Komplemen A
plt.figure(figsize=(10, 6))
plt.plot(x, not_A, label="Komplemen A")

plt.xlabel("Throughput (Mbps)")
plt.ylabel("Derajat Keanggotaan")
plt.title("Komplemen A")
plt.grid(True)
plt.legend()
plt.show()
