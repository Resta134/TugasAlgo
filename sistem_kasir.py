# sistem kasir

nama_produk = str(input("Masukan Nama Produk : "))
banyak_produk = int(input("Masukan Banyak Produk : "))
harga_satuan = int(input("Masukan Harga Satuan : "))
total = banyak_produk * harga_satuan
print("Total : " , total)
bayar = int(input("Bayar : "))
kembali = bayar - total

print("\n")
print("Total Belanja")
print("Nama Produk : " , nama_produk)
print("Total : " , total)
print("Bayar : " , bayar)
print("Kembali : " , kembali)