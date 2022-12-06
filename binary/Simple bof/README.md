# [Simple bof](https://ctflearn.com/challenge/1010)

## Deskripsi Soal

Want to learn the hacker's secret? Try to smash this buffer!

You need guidance? Look no further than to [Mr. Liveoverflow](https://old.liveoverflow.com/binary_hacking/protostar/stack0.html). He puts out nice videos you should look if you haven't already

`nc thekidofarcrania.com 35235`

## Solve

1. Melihat source code service yang diberikan

Seperti yang sudah bisa dibayangkan pada source code nya menggunakan function `gets()` dimana function tersebut adalah vulnerable nya, karena function tersebut tidak melakukan pengecekan apakah input yang dimasukkan melebihi batas buffer yang telah ditentukan atau tidak, sehingga kita bisa melakukan buffer overflow.

Dan didalam source code tersebut tugas kita adalah bagaimana melakukan overwrite variable `secret` agar bisa menjalankan function `print_flag()` untuk mendapatkan flag nya.

Jika dilihat kita juga dibeirikan hint berupa visualize buffer kita, yang seharus nya dapat lebih memudahkan kita untuk melakukan exploit nya.

2. Menjalankan program dan melakukan exploit

![tampilan program](https://i.ibb.co/CzFyK0w/image.png)

terlihat visualize buffer kita, ada 48 byte junk yang harus kita isi sebelum kita bisa mendapatkan variable `secret` dan melakukan overwrite nya.

3. Melakukan exploit

Karena ini sangat simple kita tidak perlu membuat program python yang kompleks, tapi kita hanya perlu mengenerate payload exploitasi nya saja di terminal menggunakan **python2** dan meneruskan output nya ke service.

```bash
$ python2 -c "print 'A'*48 + '\x66\x6c\x61\x67'" | nc thekidofarcrania.com 35235
```

![hasil exploit](https://i.ibb.co/7WzTLG8/image.png)

We did it bro!

## Flag

`CTFlearn{buffer_0verflows_4re_c00l!}`
