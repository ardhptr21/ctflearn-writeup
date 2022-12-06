# [Lazy Game Challenge](https://ctflearn.com/challenge/691)

## Deskripsi Soal

I found an interesting game made by some guy named "John_123". It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at: `nc thekidofarcrania.com 10001`

## Solve

1. Connect ke service dengan netcat yang ada di deskripsi soal.

![ui service](https://i.ibb.co/9gtnx4K/image.png)

dan ternyata setelah connect, service tersebut berupa sebuah game berbasis cli, yaitu mengenai game tebak angka sederhana, dan juga sudah diberikan rules dari game tersebut.

2. Mencari tahu alur program dari game tersebut dengan cara memainkannya.

Dan setelah dimainkan (sesuai dengan rules) game tersebut mengharuskan kita untuk mendapatkan uang 1000000$ dengan uang pertama yang diberikan yaitu 500$, alur sederhananya sebagai berikut

- Memasang taruhan (tidak dapat melebihi nilai uang sekarang).
- Menebak angka dari komputer dengan 10 kali kesempatan, jika berhasil maka uang akan ditambah dengan taruhan dan jika gagal uang akan dikurangi dengan taruhan.

3. Kejanggalan

Kejanggalan dari game ini adalah ketika memasukkan nilai bernilai negatif ternyata masih bisa dan diizinkan.

4. Analisa Program

Jika dianalisa harus nya game ini hanya menggunakan operasi matematika sederhana untuk menentukan nilai uang nya, yaitu

> Jika game berhasil = `uang saat ini + taruhan`

> Jika game gagal = `uang saat ini - taruhan`

5. Hacked

Oke, dengan analisa diatas seharusnya kita akan lebih mudah mendapatkan uang yang diinginkan, yaitu kita memberikan nilai negatif senilai dengan total uang yang diharuskan, dan kita akan membuat game nya gagal. Contoh

\> uang saat ini = 500$

\> taruhan = -1000000$

\> Game kalah = 500$ - (-1000000$) = 1005000$

Dari skema diatas seharusnya kita berhasil untuk mengumpulkan uang sebanyak 1000000$ bahkan bisa melebihi. Let's try it!

![hasil hacked](https://i.ibb.co/jhNhQ8x/image.png)

Hahahaha It's work! meskipun game nya gagal namun uang kita akan selalu naik akibat sifat dari operasi matematika.

## Flag

`CTFlearn{d9029a08c55b936cbc9a30_i_wish_real_betting_games_were_like_this!}`
