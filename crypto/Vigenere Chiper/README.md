# [Vigenere Chiper](https://ctflearn.com/challenge/305)

## Deskripsi Soal

The vignere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.<br />

I’m not sure what this means, but it was left lying around: `blorpy`

`gwox{RgqssihYspOntqpxs}`

## Solve

1. Kata `gwox{RgqssihYspOntqpxs}` ini adalah flag nya, tapi flag ini masih terenkripsi menggunakan teknik vigenere, tapi tenang disini kita sudah punya kunci (key) nya yaitu `blorpy`, agar lebih mudah kita pakai saja tools online

2. Proses decode Vigenere menggunakan website https://gchq.github.io/CyberChef dengan memilih operasi **Vigenere Decode** lalu memasukkan kata / string terenkripsi nya tadi dan juga key nya

![hasil decode](https://i.ibb.co/nLLj3GF/image.png)

sipp kita dapat flag nya ygyy

## Flag

`flag{CiphersAreAwesome}`
