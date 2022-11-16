## <center> **Laporan Mingguan Praktikum Metode Komputasi** <center>
### <center> Kelompok 1: <center>
#### <center> 1. Aulia Rizqikha <center>
#### <center> 2. Iha Sakti <center>
#### <center> 3. Isma Afrianti <center>
#### <center> 4. Muhammad Raffli <center>
#### <center> 5. Olivia Salma <center>
#### <center> 6. Riva Adhista <center>
#### <center> 7. Zahra Adinda <center>

##### Pada minggu pertama ini, praktikkan diminta untuk membuat core program dari masing-masing masalah yang diminta. Untuk kelompok 1, masalah yang harus diselesaikan berupa tekanan hidrostatis pada tangki bocor. Berikut modul yang dibuat oleh kelompok kami:

import turtle

def hdr(r,g,h,hmax):
    """Menghitung Tekanan hidrostatis (massa jenis zat cair,gravitasi,kedalaman bocor (meter),tinggi tabung asli (meter) ) """
    t=turtle.Turtle()
    t.penup()
    t.goto(-100,-50)
    t.pendown()
    hdr = r*h*g
    z= hmax-h
    
    if h < 100:
            h1=h
    elif h == 100:
            h1=h
    if z == 100:
        z1=z
    elif z < 100:
        z1=z
    for i in range(1,11):
        if h > 10*10**i:
            h1=h/10**i
        if z > 10*10**i:
            z1=z/10**i 
    
    h2 = 200*(h1/(h1+z1))
    z2 = 200*(z1/(h1+z1))
        
    x=6
    t.pensize(2)
    t.pencolor('black')
    t.fillcolor('cyan')
    t.begin_fill()
    t.forward((h2+x+z2)/2)
    t.left(90)
    t.forward(z2/2)
    t.write(" "+ str(z) + "m")
    t.forward(z2/2)
    t.right(90)
    t.forward(x)
    t.penup()

    for i in range(90):
        t.forward(1)
        t.right(1)

    t.forward(1)
    t.forward(z2/2)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(z2/2)
    t.forward(x)


    for i in range(90):
        t.forward(1)
        t.left(1)
    
    t.forward(1)
    t.forward(x)
    t.pendown()
    t.forward(x)
    t.right(90)
    t.forward(h2/2)
    t.write(" "+ str(h) + "m")
    t.forward(h2/2)
    t.left(90)
    t.penup()
    t.forward((h2+x+z2)/2)
    t.left(90)
    t.pendown()
    t.forward((h2+x+z2)/2)
    t.write(" "+ str(h+z) + "m")
    t.forward((h2+x+z2)/2)
    t.end_fill()
    t.penup()
    t.goto(-100,-70)
    t.write("Tekanan Hidrosatis :"+ str(hdr) + "N/m^2")
    
    turtle.done()
    turtle.mainloop()

def hidrostatis(r,g,h,hmax):
    if h > hmax:
        print('masukan nilai yang benar')
    else:
        hdr(r,g,h,hmax)


##### Untuk modul ini kami menggunakan library turtle untuk menggambar garis, lingkaran, dan bentuk lainnya yang lebih kompleks. Library ini akan digunakan untuk menggambar tabung bocor dalam 2 dimensi. Di sini kami mendefinisikan fungsi hidrostatis dengan parameter yang diinput, diantaranya massa jenis cairan (dilambangkan dengan r), gravitasi planet (dilambangkan dengan g), tinggi tabung dari atas permukaan (dilambangkan dengan h), dan tinggi tabung keseluruhan (dilambangkan dengan hmax).

##### Setelah menginput parameter tersebut, barulah masuk ke dalam proses perhitungan tekanan hidrostatis dan pembuatan gambar dengan library turtle. Untuk memunculkan kepala tanda panah, kami menggunakan fungsi "turtle.Turtle()". Kemudian, terdapat fungsi penup dan pendown, dimana fungsi penup digunakan untuk menghilangkan tinta warna pada garis yang dibuat dan fungsi pendown digunakan untuk menampilkan tinta warna pada garis yang dibuat. 

##### Kami memulai titik pada koordinat x=-100 dan y=-50. Pada code di atas terdapat variabel z, dimana variabel z merupakan tinggi dari titik bocor ke batas bawah tabung yang didapatkan dengan mengurangi nilai hmax dan h. Saat membuat gambarnya, terdapat fungsi forward(untuk maju), left(untuk ke kiri), dan right(untuk ke kanan) untuk membantu dalam pembuatannya. Fungsi forward menggunakan parameter jarak sehingga garis bergerak maju ke depan sesuai dengan jarak yang diminta. Sedangkan, fungsi left dan right menggunakan parameter sudut sehingga dapat bergerak belok sesuai dengan arah sudut yang diinginkan