# [Time Traveller](https://ctflearn.com/challenge/1072)

## Deskripsi Soal

Let's take a trip to nasa.gov on December 31, 1996. If you can tell me what email NASA listed on their website, I'll provide you with 10 points. Format: `CTFlearn{email}`

## Solve

1. Dari deskripsi soal kita diperintahkan untuk melihat website nasa.gov pada tanggal `31 Desember 1996` untuk mencari `email` yang tertera di website tersebut, tapi saat ini sudah tahun `2022` _\*saat saya mengerjakan problem ini_ dan tentu saja website nasa.gov sudah berbeda jauh.

2. Lalu saya melaukan pencarian di google untuk mencari hint dengan keyword pencarian `how to see website in a specific time?`, tujuannya adalah untuk mengetahui cara melihat website di waktu tertentu, dan yahh ternyata kita perlu layanan **website archive**

3. Setelah mengetahui hint tersebut, saya mencari layanan website archive, dan saya menemukan layanan tersebut di website https://web.archive.org/, lalu saya menginputkan website `nasa.gov` ke website tersebut dan memilih tanggal `December 31, 1996`

![nasa.gov 31 desember 1996](https://i.ibb.co/DGPwyKN/image.png)

oke kita dapat website nasa.gov pada tanggal 31 Desember 1996, dan seperti tujuan awal kita yaitu mencari email yang tertara, disitu ada email `today@nasa.gov` dan hanya satu satu nya email yang tertera, berati itu adalah flag nya 😁

## Flag

`CTFlearn{today@nasa.gov}`
