while True:
    harga_barang = int(input("masukkan angka harga barang: "))
    jumlah_pembelian = int(input("masukkan angka jumlah pembelian : "))
    total_harga_barang = harga_barang * jumlah_pembelian

    if total_harga_barang > 250000: 
        diskon = total_harga_barang * 0.25
        print("Selamat anda mendaptkan diskon 25%")
        print("Total", total_harga_barang)
    else:
        print("Total", total_harga_barang)
        break

    pilihan = input("Apakah anda ingin menghitung lagi? (y/t): ")
    if pilihan == 't':
        break
    print("Terima kasih")