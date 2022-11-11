# [RSA Noob](https://ctflearn.com/challenge/120)

## Deskripsi Soal

These numbers were scratched out on a prison wall. Can you help me decode them?
https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

## Solve

1. Download file yang disediakan
2. Nah setelah dibuka ternyata berisi 3 buah nilai

```txt
e: 1
c:9327565722767258308650643213344542404592011161659991421
n: 245841236512478852752909734912575581815967630033049838269083
```

oke seperti nama soalnya yaitu RSA Noob, brarti disini kita menggunakan algoritma RSA

untuk melakukan decode rsa yaitu bisa pake rumus `c ^ d mod n` tapi kita disini tidak memiliki nilai `d`

untungnya nilai `e` disitu adalah _1_ berarti `d` juga bernilai _1_, karena `d*e = 1 * mod tot(n)` menjadi `d = 1 * mod tot(n)`

> tot(n) = (p-1) \* p(q-1) ; p and q adalah bilangan prima

oke dari situ kita bisa melakukan decode

```python
# c ^ d mod n -> c ^ 1 mod n
bytes.fromhex(hex(pow(c, d, n))[2:]).decode()

# output : abctf{b3tter_up_y0ur_e}
```

## Flag

`abctf{b3tter_up_y0ur_e}`
