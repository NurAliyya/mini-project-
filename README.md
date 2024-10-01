# mini-project-
#### NurAliyya
#### 2409116094

![Untitled Diagram](https://github.com/user-attachments/assets/8f940e19-575b-498e-bf9e-c860f0f27517)
1. Penginputan harga barang dan jumlah barang serta menghitung diskon menggunakan while True
while True:
    harga_barang = int(input("masukkan angka harga barang: "))
    jumlah_pembelian = int(input("masukkan angka jumlah pembelian : "))
    total_harga_barang = harga_barang * jumlah_pembelian

2. Melakukan pengulangan hitung diskon
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
<img width="356" alt="Cuplikan layar 2024-10-01 121536" src="https://github.com/user-attachments/assets/e2f00046-7f1f-422d-bd68-f4d726ed2f0c">
    



