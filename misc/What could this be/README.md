# [What could this be?](https://ctflearn.com/challenge/268)

## Deskripsi Soal

It seems like someone really likes special characters… Or could it mean something more? https://mega.nz/#!SDQkUYQZ!b1Fu7iZ_wGiNX0aOjez95_74TYDCnLb3YSQfRzs0J-o

## Solve

1. Kita diberi file, lalu setelah saya download dan lihat isi nyaaaa, HAHHHHH?🤯🤯🤯 isi file nya hanya berisi karakter-karakter saja, seperti ini contoh dari **sebagian** file nya

```
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]
+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]
+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]
+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])
[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]
+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]
+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[]
```

dan disini saya bingung tidak ada hint sama sekali

2. Saya mencoba melakukan copy paste sebagian string tersebut ke google, dan hasil nya? damn broo google aja ngga tau😖

![search google](https://i.ibb.co/XbP2D4v/image.png)

sudah lelah dengan semua ini, saya mencoba mencari hint dari comment di challenge ini hehe, dan saya menemukan hint yaitu katanya string itu adalah kode dari salah satu [**Esoteric Programming Language**](https://en.wikipedia.org/wiki/Esoteric_programming_language), tidak lama kemudian saya mencari tahu mengenai Esoteric Programming Language itu dan ternyata banyak sekali bahasa nya, kemudian saya mencari bahasa yang sesuai dengan string yang kita punya itu. Ternyata string yang kita punya tersebut adalah kode dari [**JSFuck Esoteric Programming Language**](https://en.wikipedia.org/wiki/JSFuck), setelah itu saya langsung cepat mencari jsfuck decoder nya, dan thanks god saya dapet web untuk melakukan decode kode tersebut

3. Melakukan decode di https://www.dcode.fr/jsfuck-language

![hasil decode jsfuck](https://i.ibb.co/6HhW38t/image.png)

woww akhirnya dapet flag nya :)

## Flag

`flag{5uch_j4v4_5crip7_much_w0w}`
