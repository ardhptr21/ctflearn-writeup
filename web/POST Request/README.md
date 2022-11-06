# [POST Request](https://ctflearn.com/challenge/114)

## Deskripsi Soal

This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate?

# Solve

1. Buka website nya, dan ternyata hanya menampilkan response seperti ini

![Request awal](https://i.ibb.co/b24k8gg/image.png)

2. Mari lihat apakah ada sesuatu di page source nya. Dan boom ternyata ada credentials disitu yang dijadikan sebuah comment sehingga tidak ter render

![Page Source](https://i.ibb.co/420PXpt/image.png)

3. Kirim request dengan method `POST` menggunakan `curl` dengan payload `username=admin` dan `password=71urlkufpsdnlkadsf`

![Hasil Curl](https://i.ibb.co/2kWqn7Q/image.png)

It's work broo, dapet flag nya

## Flag

`flag{p0st_d4t4_4ll_d4y}`
