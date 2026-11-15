# from tugas import PengelolaTugas

# pengelola = PengelolaTugas()

# print("sakura-tasks. Perintah: add JUDUL, list, done NOMOR, stats, keluar")
# while True:
#     perintah = input("> ")
#     if perintah == "keluar":
#         break
#     elif perintah == "list":
#         pengelola.tampilkan()
#     elif perintah == "stats":
#         pengelola.ringkasan()
#     elif perintah.startswith("add "):
#         pengelola.tambah(perintah[4:])
#     elif perintah.startswith("done "):
#         nomor = perintah[5:]
#         if nomor.isdigit():
#             pengelola.selesai(int(nomor))
#         else:
#             print("Nomor harus angka")
#     elif perintah.startswith("hapus "):
#         nomor = perintah[6:]
#         if nomor.isdigit():
#             pengelola.hapus(int(nomor))
#         else:
#             print("Nomor harus angka")
#     else:
#         print("Perintah tidak dikenal") 

# tugas = []


# def tambah(judul):
#     judul = judul.strip()
#     if judul == "":
#         print("Judul tidak boleh kosong")
#         return
#     tugas.append({"judul": judul, "selesai": False})
#     print(f"Ditambahkan: {judul}")


# def tampilkan():
#     for nomor, item in enumerate(tugas, start=1):
#         tanda = "x" if item["selesai"] else " "
#         print(f"{nomor}. [{tanda}] {item['judul']}")


# def selesai(nomor):
#     if nomor < 1 or nomor > len(tugas):
#         print("Nomor tidak ada")
#         return
#     tugas[nomor - 1]["selesai"] = True
#     print(f"Selesai: {tugas[nomor - 1]['judul']}")


# def ringkasan():
#     total = len(tugas)
#     jumlah_selesai = 0
#     for item in tugas:
#         if item["selesai"]:
#             jumlah_selesai += 1
#     print(f"Total {total} | selesai {jumlah_selesai} | belum {total - jumlah_selesai}")

# def update(nomor, judul_baru):
#     if nomor < 1 or nomor > len(tugas):
#         print("Nomor tidak ada")
#         return
#     elif nomor.isdigit() == False:
#         print("Nomor harus angka")
#         return
#     elif judul_baru.strip() == "":
#         print("Judul baru tidak boleh kosong")
#         return
#     tugas[nomor - 1]["judul"] = judul_baru.strip()
#     print(f"Diubah: {tugas[nomor - 1]['judul']} -> {judul_baru.strip()}")


# print("sakura-tasks. Perintah: add JUDUL, list, done NOMOR, stats, keluar")

# while True:
#     perintah = input("> ")
#     if perintah == "keluar":
#         break
#     elif perintah == "list":
#         tampilkan()
#     elif perintah == "stats":
#         ringkasan()
#     elif perintah.startswith("add "):
#         tambah(perintah[4:])
#     elif perintah.startswith("done "):
#         nomor = perintah[5:]
#         if nomor.isdigit():
#             selesai(int(nomor))
#         else:
#             print("Nomor harus angka")
#     elif perintah.startswith("update "):
#         parts = perintah.split(" ", 2)
#         if len(parts) < 3:
#             print("Perintah update harus diikuti nomor dan judul baru")
#             continue
#         nomor = parts[1]
#         judul_baru = parts[2]
#         if nomor < 1 or nomor > len(tugas):
#             print("Nomor tidak ada")
#         elif nomor.isdigit() == False:
#             print("Nomor harus angka")
#         elif judul_baru.strip() == "":
#             print("Judul baru tidak boleh kosong")
#         tugas[nomor - 1]["judul"] = judul_baru.strip()
#         print(f"Diubah: {tugas[nomor - 1]['judul']} -> {judul_baru.strip()}")
        
#         if nomor.isdigit():
#             update(int(nomor), judul_baru)
#         elif nomor < 1 or nomor > len(tugas):
#             print("Nomor tidak ada")
#         elif nomor.isdigit() == False:
#             print("Nomor harus angka")
#         elif judul_baru.strip() == "":
#             print("Judul baru tidak boleh kosong")
#     else:
#         print("Perintah tidak dikenal")

from tugas import PengelolaTugas

pengelola = PengelolaTugas()

print("sakura-tasks. Perintah: add JUDUL, list, done NOMOR, stats, keluar")

while True:
    perintah = input("> ")
    if perintah == "keluar":
        break
    elif perintah == "list":
        pengelola.tampilkan()
    elif perintah == "stats":
        pengelola.ringkasan()
    elif perintah.startswith("add "):
        pengelola.tambah(perintah[4:])
    elif perintah.startswith("done "):
        nomor = perintah[5:]
        if nomor.isdigit():
            pengelola.selesai(int(nomor))
        else:
            print("Nomor harus angka")
    else:
        print("Perintah tidak dikenal")