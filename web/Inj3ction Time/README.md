# [Inj3ction Time?](https://ctflearn.com/challenge/149)

## Deskripsi Soal

I stumbled upon this website: http://web.ctflearn.com/web8/ and I think they have the flag in their somewhere. UNION might be a helpful command

## Solve

1. Website yang diberikan adalah website untuk menampilkan sebuah data anjing dengan cara memasukkan ID nya yang tepat. Dan tentu kita dapat melakukan SQL Injection pada input ID tersebut.

2. Dari deskripsi soal terdapat hint yaitu UNION, artinya kita bisa menggunakan teknik UNION dan digabungkan dengan SELECT untuk mencari flag nya. Nah karena UNION SELECT ini membutuhkan jumlah kolom yang sama dengan kolom sebelum nya (kolom dari data anjing) maka kita akan mencari jumlah kolom yang diambil terlebih dahulu.

3. Pertama kita cari terlebih dahullu banyaknya kolom yang diambil dari data anjing tersebut.

Setelah mencoba satu persatu, ternyata query ini `1 UNION SELECT 1,2,3,4` lah yang berhasil mengembalikan value, artinya ada 4 kolom yang diambil dari data anjing tersebut.

4. Mengambil informasi table dari database tersebut.

`NULL UNION SELECT table_name, NULL, NULL, NULL FROM information_schema.tables WHERE table_schema=database()`

![hasil query](https://i.ibb.co/dpz03Zk/image.png)

dari query diatas ada 2 nilai tabel, yaitu **w0w_y0u_f0und_m3** dan **webheight**

5. Sepertinya tabel **w0w_y0u_f0und_m3** menarik, selanjutnya cari tahu nama kolom-kolom nya dari tabel tersebut.

`NULL UNION SELECT column_name, table_name, NULL, NULL FROM information_schema.columns WHERE table_schema=database()`

![hasil query](https://i.ibb.co/RN1Pw49/image.png)

dari query diatas kita berhasil mendapatkan kolom yang ada di tabel **w0w_y0u_f0und_m3** yaitu **f0und_m3**

6. Selanjutnya kita akan query untuk mengambil data dari kolom **f0und_m3** di tabel **w0w_y0u_f0und_m3**.

`NULL UNION SELECT f0und_m3, NULL, NULL, NULL from w0w_y0u_f0und_m3`

![hasil query](https://i.ibb.co/KjHb4Lk/image.png)

that's it, kita berhasil mendapatkan flag nya.

## Flag

`abctf{uni0n_1s_4_gr34t_c0mm4nd}`
