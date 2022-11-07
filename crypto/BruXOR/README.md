# [BruXOR](https://ctflearn.com/challenge/227)

## Deskripsi Soal

There is a technique called bruteforce. Message: `q{vpln'bH_varHuebcrqxetrHOXEj` No key! Just brute .. brute .. brute ... :D

## Solve

1. Dari judul soal dan deskripsi soal diberitahu bahwa kita perlu menggunakan teknik `Brute Force XOR` untuk melakukan percobaan terhadap enkripsi message agar bisa mendapatkan string aslinya, disini saya menggunakan kode python untuk melakukan brute force xor terhadap untuk tiap karakter message dengan bilangan hex antara `0x00 - 0xff` satu persatu

2. Kode bruteforce python bisa cek di file [./solve.py](./solve.py), kode tersebut akan melakukan semua kemungkinan percobaan dan akan menampilkan semua percobaan decode nya

> FOR YOU: Tolong pahami kode nya terlebih dahulu dan tidak hanya melakukan submit flag!

## Flag

`flag{y0u_Have_bruteforce_XOR}`
