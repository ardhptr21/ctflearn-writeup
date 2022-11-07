# [Binwalk](https://ctflearn.com/challenge/108)

## Deskripsi Soal

Here is a file with another file hidden inside it. Can you extract it?
`https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY`

## Solve

1. Diberi sebuah file ketika didownload ternyata itu adalah file gambar jpeg, dan tidak ada informasi apapun ketika dibuka

2. Langsung saja karena dari judul soalnya kita sudah dapet hint yaitu `Binwalk` jadi kita perlu menggunakan stego tools `binwalk` untuk mencari flag nya

3. okee kita lakukan `binwalk` terhadap file nya

```bash
$ binwalk PurpleThing.jpeg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 780 x 720, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
153493        0x25795         PNG image, 802 x 118, 8-bit/color RGBA, non-interlaced
```

okee disitu kita dapat informasi kalo ada 2 file lainnya didalam file kita saat ini, yaitu file `zlib` dan `png`, soo selanjutnya mari kita ektract semua data tersebut, lalu kita lihat hasil nya

4. Ekstrak **semua data** nya tidak terkecuali dengan command `binwalk --extract --dd=".*" PurpleThing.jpeg`, setelah diekstrak akan menghasilkan folder baru hasil ekstrak nya, dan ketika kita masuk ada 4 file yang berhasil diekstrak

![hasil ekstrak](https://i.ibb.co/cwc1cnJ/image.png)

dann setelah dibuka satu-persatu, file `25795` berisi sebuah flag

![hasil dari file 25795](https://i.ibb.co/923gC3k/image.png) 

horayyy!!!!

## Flag

`ABCTF{b1nw4lk_is_us3ful}`