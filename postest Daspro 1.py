#Login Sederhana menggunakan Nama, Nim, Password, dan Captcha

#Masukkan Nama
nama = input("Masukan nama anda: ")

#Memasukkan NIM (wajib menggunakan angka)
while True:
    nim = input("Masukan NIM anda: ")
    if nim.isdigit():
        break #Keluar dari loop jika NIM benar
    else:
        print("NIM tidak sesuai, NIM wajib menggunakan angka")

#Memasukan password sesuai dengan NIM
while True :
    password = input("Masukan password anda: ")
    if nim == password:
        print("Login Berhasil")
        break #Keluar dari loop jika Password benar
    else:
        print("Password tidak sesuai dengan NIM")

#capcha
captchabenar = "2k24"

#Memasukkan capcha yang sesuai
while True:
    captcha = input("Masukan capcha: ")
    if captcha == captchabenar:
        print("Login Berhasil")
        break
    else:
        print("Captcha tidak sesuai")

#Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian.


#Memasukkan harga barang dan jumlah pembelian
while True:
    hargabarang  = float(input("Masukkan harga barang: "))
    jumlahbarang = int(input("Masukkan jumlah barang: "))

#Menghitung total harga
    totalharga = hargabarang * jumlahbarang

#Menentukan apakah mendapatkan diskon atau tidak
    if totalharga > 250000:
        # Mendapat diskon 25%
        diskon = 0.25 * totalharga
        totalhargasetelahdiskon = totalharga - diskon
    
#Menampilkan harga
    if totalharga > 250000 :
        print("Total harga sebelum diskon= Rp " + str(totalharga))
        print("Total Diskon 25%= Rp " + str(diskon))
        print("Total harga setelah diskon= Rp " + str(totalhargasetelahdiskon))
    else:
        print("Total harga: Rp " + str(totalharga))

#Menentukan apakah ingin menghitung lagi atau tidak
    pilihan = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if pilihan == 'tidak':
        print("Terima kasih")
        break
