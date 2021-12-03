# Tugas-Praktikum-4

***

#### Nama   : Amelia Diah Parwati
#### NIM    : 312110134
#### Kelas  : TI.21.CA1

---

## Bentuk program latihan di Tugas Praktikum
Berikut ini adalah screenshot programnya :

![ss lat1](https://user-images.githubusercontent.com/92660371/144609105-1ff2d5a7-b76b-4cd0-a569-7635ef779bc5.png)




## Membuat list nilai mahasiswa

1. Hal pertama yang dilakukan adalah membuat flowchart. Fungsi flowchart ini untuk memudahkan kita dalam menulis program. Berikut ini adalah gambar flowchartnya :

![flowchart praktikum4](https://user-images.githubusercontent.com/92660371/144609866-965cd798-081f-4094-beef-234d4c10b208.jpeg)


2. Kedua membuat program. Berikut ini adalah programnya :

![ss rumus](https://user-images.githubusercontent.com/92660371/144609897-f2ad372a-2e89-4acb-a755-d52de5a7097a.png)



dengan keterangan

'''python
    i=0
'''

*   diatas adalah untuk menginisiasikan variable i sama dengan 0, karena diprogram ini akan menggunakan perulangan while dan for, jadi perlu menginisiasikan agar tidak terjadi eror


'''python

    nama =[]
    nim =[]
    tugas=[]
    uts=[]
    uas=[]
    nilaiakhir=[]

'''
 

 * Program di atas untuk mendefinisikan list nya, dan untuk menampung data

 '''python

    while True:
        nama1=input("Nama  : ")
        nama.append(nama1)
        nim1=input("NIM   : ")
        nim.append(nim1)
        tugas1=input("Nilai Tugas : ")
        tugas.append(tugas1)
        uts1=input("Nilai UTS : ")
        uts.append(uts1)
        uas1=input("Nilai UAS : ")
        uas.append(uas1)
'''

* diatas adalah code untuk menginput isi dalam list tersebut, juga untuk menambahkan list jika sudah menginput 1 nama atau nilai dalam list, dengan menggunakan append dan menggunakan pengulangan while


'''python

    nilaiakhir1=(int(tugas1)*0.30)+(int(uts1)*0.35)+(int(uas1)*0.35)
    nilaiakhir.append(nilaiakhir1)

'''

* diatas adalah code untuk menghitung nilai akhir dengan kondisi nilai akhir 30% dari nilai tugas, ditambah 35% dari nilai UTS dan juga 35% dari nilai UAS, dengan kemudian diubah persentase menjadi bentuk desimal, maka terdapat 0.30, 0.35. sedangkan untuk nilai_akhir.append adalah untuk menambahkan list dari yang telah di inputkan sebelum akhirnya di tampilkan


'''python

    more=""

        while more!="y" and more!="t":
            more=input("Tambah Data(y/t) ?")
    i+=1
    if more=="t":
         break
'''

* Program diatas adalah untuk perintah menambahkan data dengan pertanyaan ya atau tidak, dengan definisi jika ya, maka ketikkan y pada keyboard, maka akan mengulang inputan list. dan jika tidak, ketikkan t paada keyboard, maka akan menampilkan hasil list yang telah di inputkan

'''python

    print("._____________________________________________________________________________________________________________.")
    print("|                                             Daftar Mahasiswa                                                |")
    print("|_____________________________________________________________________________________________________________|")
    print("|  No.  |      Nama      |      NIM        |     Tugas      |      UTS      |      UAS      |      Akhir      |")
    print("|-------------------------------------------------------------------------------------------------------------|")
'''

* untuk membuat border agar terlihat rapi dan enak dipandang

'''python

    for n in range(i):
        print("| ",n+1,"   |  ",nama[n],"  |  ",nim[n],"    |      ",tugas[n],"      |      ",uts[n],"     |     ",uas[n],"      |    ",nilaiakhir[n],"      |")
     print("|-------------------------------------------------------------------------------------------------------------|")
'''

* sedangkan ini adalah untuk menampilkan hasil dari list yang telah diinputkan, dengan menggunakan perulangan for n in renge



## Berikut hasil dari programnya

![ss tampilan akhir](https://user-images.githubusercontent.com/92660371/144609931-b729ee74-8ec1-4188-bf56-b5ba01b809b9.png)
