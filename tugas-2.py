
# Input Data
nama = input("\nMasukan Nama: ")
nik = input("Masukan NIK: ") 
status = input('Masukan Status Pegawai ("tetap" atau "honor") : ').lower()
golongan = input("Masukan Golongan A/B/C: ").upper()

# Inisialisasi Gaji dan Bonus
gaji = 0
bonus = 0

if status == "tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
    else:
        print("Golongan Tidak Valid!")
        exit()  
elif status == "honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000
    else:
        print("Golongan Tidak Valid!")
        exit()
else:
    print("Status tidak valid! Harap masukan 'tetap' atau 'honor'.")
    exit()

# Menghitung Total Gaji
total_gaji = gaji + bonus

# Output Hasil
print("\n----Hasil Perhitungan Gaji----")
print(f"Nama: {nama}")
print(f"NIK: {nik}")
print(f"Status: {'Pegawai tetap' if status == 'tetap' else 'Pegawai Honor'}")
print(f"Golongan: {golongan}")
print(f"Gaji: Rp {gaji:,}") 
print(f"Bonus: Rp {bonus:,}")
print(f"Gaji Total: Rp {total_gaji:,}")