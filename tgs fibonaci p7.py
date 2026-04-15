while True:
    print("\nmenu")
    print("1. A pangkat B")
    print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        a = int(input("Masukkan suatu bilangan bulat: "))
        b = int(input("Masukkan pangkat yang diinginkan: "))
        for i in range(1, b + 1):
            hasil = a ** i
            print(f"Hasil {a} pangkat {i} adalah {hasil}")

    elif pilihan == "2":
        n = int(input("Masukkan jumlah N: "))
        total = 0

        pembilang1, pembilang2 = 1, 2
        penyebut1, penyebut2 = 1, 3

        for i in range(n):
            if i == 0:
                suku = pembilang1 / penyebut1
            elif i == 1:
                suku = pembilang2 / penyebut2
            else:
                pembilang_baru = 2 * pembilang2 + pembilang1
                penyebut_baru = 2 * penyebut2 + penyebut1

                pembilang1, pembilang2 = pembilang2, pembilang_baru
                penyebut1, penyebut2 = penyebut2, penyebut_baru

                suku = pembilang2 / penyebut2

            if i % 2 == 0:
                total += suku
            else:
                total -= suku

        print("Hasil =", total)

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
