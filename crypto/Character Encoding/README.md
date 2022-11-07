# [Character Encoding](https://ctflearn.com/challenge/115)

## Deskripsi Soal

In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out?

`41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D`

## Solve

1. Jika dilihat tiap-tiap karakter nya merepresentasikan sebuah angka hexadecimal (base 16)
2. Melakukan decode dari hex ke plaintext menggunakan python

```python
chiper = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"

for c in chiper.split(' '):
  print(chr(int(c, 16)), end='')
print('\n')

# output -> ABCTF{45C11_15_U53FUL}
```

as simple as that kita dapet flag nya

## Flag

`ABCTF{45C11_15_U53FUL}`
