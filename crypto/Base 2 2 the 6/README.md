# [Base 2 2 to 6](https://ctflearn.com/challenge/192)

## Deskripsi Soal

There are so many different ways of encoding and decoding information nowadays... One of them will work!

`Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9`

## Solve

1. Ini adalah karakter encode dari Base64 bisa dilihat dari judul yaitu `Base 2 2 the 6` atau bisa saya terjemahkan ke `Base 4 the 6`, nahh disitu kita dapet hint, karena `Base46` itu ngga ada brarti kita gunakan kebalikannya yaitu `Base64`

2. Kita decode karakter tersebut dari Base64 ke plaintext, disini saya menggunakan terminal saja

```bash
> echo "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9" | base64 -d
> CTF{FlaggyWaggyRaggy}
```

that's it gaess

## Flag

`CTF{FlaggyWaggyRaggy}`
