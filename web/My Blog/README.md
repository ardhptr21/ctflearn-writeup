# [My Blog](https://ctflearn.com/challenge/979)

## Deskripsi Soal

Hi, I'm Noxtal! I have hidden a flag somewhere in my Cyberworld (AKA blog)... you may find a good application for your memory. ;)

Note: This is my real website (thus no deadly bug to exploit here). You might want to read some of my content (writeups, tutorials, and cheatsheets). I would be glad to receive any kind of feedback.

Hint: replace the flag{} part with CTFlearn{}.

## Solve

1. Tidak ada yang menarik dari website nya setelah dikunjungi
2. But wait, di deskripsi soal ada kata `application` dan `memory` yang di cetak tebal, seperti nya itu mengenai `browser storage`, mari kita cek dengan `Developer Tools`

![developer tools](https://i.ibb.co/cYfYSb7/image.png)

Dan benar bro, setelah buka `developer tools` terus ke `tab application` dan cek `local storage` ada flag hehe

## Flag

`flag{n7f_l0c4l_570r463_15n7_53cur3_570r463}`
