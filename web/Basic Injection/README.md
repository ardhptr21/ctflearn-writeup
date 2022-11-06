# [Basic Injection](https://ctflearn.com/challenge/88)

## Deskripsi

See if you can leak the whole database using what you know about SQL Injections.

## Solve

![Foto Web](https://i.ibb.co/Q8RXzcx/image.png)

1. Web yang akan dilakukan exploitation adalah web sederhana, dan disitu kita juga diberi tahu seperti apa query akan dieksekusi

2. Setelah melihat query tersebut, saya menggunakan basic sql injection `' OR '1' = '1`

3. Dan bingo, kita dapat hasil query dan juga didalamnya terdapat flag yang dicari

![Hasil query basic sql injection](https://i.ibb.co/1bsx5Y5/image.png)

## Flag

`CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}`
