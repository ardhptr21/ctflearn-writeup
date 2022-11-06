# [Don't Bump Your Head(er)](https://ctflearn.com/challenge/109)

## Deskripsi Soal

Try to bypass my security measure on this site!

# Solve

1. Kunjungi web nya dulss

![Tampilan web](https://i.ibb.co/HqpXBGg/image.png)

Dan kita dapat respone seperti itu, wait wait ada informasi dari respone itu, seperti nya kita perlu memodifikasi `user agent` untuk bisa masuk, tapi `value` nya apa? Let's go to next step

2. Seperti biasa lihat source page nya dulu

![hasil page source](https://i.ibb.co/mvh0bHD/image.png)

Huhh lagi dan lagi ada value yang di comment, sepertinya itu adalah value untuk `user agent` nya, Let's try

3. Kita akan request menggunakan `curl` untuk memodifikasi `user agent` nya, dengan value yang udah kita dapat sebelumnya

![hasil curl modifikasi user agent](https://i.ibb.co/jhx0b7r/image.png)

Masih belum ternyata, tapi kita dapat response yang beda dan ada hint lagi, seperti nya kita harus memodifikasi request agar berasal dari `awesomesauce.com` yaitu kita harus memodifikasi `referer` nya, Let's try again with `curl`

4. Modifikasi referer dengan `curl`

![hasil curl modifikasi referer](https://i.ibb.co/s1VDqNC/image.png)

that's it kita dapet flagnya

## Flag

`flag{did_this_m3ss_with_y0ur_h34d}`
