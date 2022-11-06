# [Gobustme?](https://ctflearn.com/challenge/1116)

## Deskripsi Soal

Some ghosts made this site ?, it's a little spooky but theres a bunch of stuff hidden around.

## Solve

1. Setelah mengunjungi website dan melihat source page tidak ada hint apapun, tapi disitu banyak sekali kata yang merujuk ke `gobuster` yang adalah tools untuk melakukan bruteforce, dan juga ada link mengenai `wordlist` dan link yang menuju ke cara penggunaan tools `gobuster`. Fix sepertinya kita bisa menggunakan `gobuster` untuk menyelesaikannya

2. Download file wordlist dan seperti ini lah hasil nya

![wordlist](https://i.ibb.co/RC1TK4P/image.png)

3. Kita lakukan bruteforce dir dengan gobuster

![hasil gobuster](https://i.ibb.co/Zhh0t50/image.png)

nahh dari hasil bruteforce nya kita dapat beberapa link yang aktif, mari akses satu persatu

4. Setelah diakses satu persatu ternyata flag sebenarnya tersimpan di dalam path `/hide` bukan `/flag`, but yeahh kita dapet flag nya

![hasil path /hide](https://i.ibb.co/GWxfMy5/image.png)

## Flag

`CTFlearn{gh0sbu5t3rs_4ever}`
