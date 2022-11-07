# [Hextroadinary](https://ctflearn.com/challenge/158)

## Deskripsi Soal

Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x.

`0xc4115 0x4cf8`

## Solve

1. Disini diberi 2 karakter yaitu `0xc4115` dan `0x4cf8` yang berupa bilangan hex karena diawali dengan _0x_ tapi harus diapakan? ada kata kunci didalam deskripsi soal yaitu `ROX` atau jika dibalik menjadi `XOR`, yeahh seperti nya 2 karakter diatas perlu diberi operasi `XOR`, dan juga hasil dari operasi tersebut adalah bilangan hex yang diawali dengan _0x_

2. Proses operasi _XOR_-ing dengan python

```python
result = hex(0xc4115 ^ 0x4cf8)
print(f'CTFlearn{result}')
```

kode diatas nanti akan menghasilkan output flag nya

## Flag

`CTFlearn{0xc0ded}`
