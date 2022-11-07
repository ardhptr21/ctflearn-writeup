# [QR Code](https://ctflearn.com/challenge/228)

## Deskripsi soal

Do you remember something known as QR Code? Simple. Here for you :
https://mega.nz/#!eGYlFa5Z!8mbiqg3kosk93qJCP-DBxIilHH2rf7iIVY-kpwyrx-0

## Solve

![qrcode](./qrcode.png)

1. Masuk ke link file, dan ternyata itu adalah file qr code, kemudian saya download

2. Lalu saya melakukan scanning melalui website https://webqr.com/

![hasil scan](https://i.ibb.co/WKtBGfT/image.png)

dan yahh hasilnya seperti string yang diencode, dan saya kira itu adalah _base64_ karena diakhiri dengan tanda `=`

3. Melakukan decode base64 dari string tersebut

![hasil decode](https://i.ibb.co/bJfz8wb/image.png)

dari hasil decode ada string `synt vf : a0_obql_s0etrg_de_pbqr` yang saya kira adalah flag, tapi setelah saya submit masih incorrect, dan ternyata string tersebut masih diencode, kalau dilihat dari karakteristik string tersebut sepertinya tidak ada teknik encode yang rumit, dan mungkin string itu diencode menggunakan teknik `ROT13`, jadi selanjutnya saya mencoba melakukan decode menggunakan teknik itu

4. Decode string `synt vf : a0_obql_s0etrg_de_pbqr` dengan teknik `ROT13`

![hasil decode rot13](https://i.ibb.co/0Qdn3Bb/image.png)

dan mantap ternyata benar hasil dari decode nya adalah `flag is : n0_body_f0rget_qr_code` tinggal kita masukkan ke format submit flag nya dan selesai

## Flag

`CTFlearn{n0_body_f0rget_qr_code}`
