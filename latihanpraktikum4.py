# Buat sebuah list sebanyak 5 elemen dengan nilai bebas
a = ['Bandung', 'Bekasi', 'Jakarta', 'Solo', 'Klaten']

# Akses list
print("Tampilkan element ke-3 : ", a[3])
print("ambil nilai elemen ke 2 sampai elemen ke-4 :", a[2:4])
print("ambil elemen terakhir :", a[-1])

# Ubah elemen list:
a[4] = 'Malang'
print("ubah elemen ke 4 dengan nilai lainnya :", a[4])

a[4:] = 'Jogja', 'Bali'
print("Ubah elemen ke 4 sampai dengan elemen terakhir = ", a[4:])

# Tambah elemen list
a =[1,2,3,4,5]
b =[6,7,8,9,10]

# Ambil 2 buah bagian list A ke ist B
b.append(a[1:3])
print("2 bagian dari list A dijadikan list B: ", b)

# Tambah list B dengan nilai string
b.append("amel")
print("Tambah list B dengan string: ",b)

# Tambah list B dengan 3 nilai
print("Tambah list B dengan 3 nilai: ", b+[11,12,13])

# Menggabungkan list B dengan list A
c = b+a
print("Gabungan dari list B dan list A: ", c)
