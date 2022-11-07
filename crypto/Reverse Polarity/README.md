# [Reverse Polarity](https://ctflearn.com/challenge/230)

## Deskripsi Soal

I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: `01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101`

## Solve

1. Karakter diatas adalah karakter binary yang hanya terdiri **0** dan **1** dan biasanya karakter tersebut akan terpotong tiap 8 bit, jadi kita harus melakukan decode ke plaintext per 8 bit karakter

2. Proses decode menggunakan python

```python
chiper = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"

for i in range(0, len(chiper), 8):
  print(chr(int(chip[i:i+8], 2)), end='')
```

## Flag

`CTF{Bit_Flippin}`
