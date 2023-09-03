import random


top_of_range = input("Ketik lah nomor: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("ketik angka lebih dari 0 lain kali ya! ")
        quit()
else:
    print("ketik angka lain kali ya! ")
    quit()

random_number = random.randint(0, top_of_range)
tebakan = 0

while True:
    tebakan += 1
    tamu = input("tebaklah angka yang benar dari 0 sampai angka yang kamu tulis ")
    if tamu.isdigit():
        tamu = int(tamu)
    else:
        print("ketik angka ")
        continue

    if tamu == random_number:
        print("tebakan mu benar")
        break 
    elif tamu <= random_number:
        print("angkanya naik lagi ")
    else:
        print("turunkan angkanya")

print("selamat kamu berhasil menebak sebanyak", tebakan, "kali")

