# [Git Is Good](https://ctflearn.com/challenge/104)

## Deskripsi Soal

The flag used to be there. But then I redacted it. Good Luck.
`https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc`

## Solve

1. Kita diberi file berupa file zip, oke langkah pertama kita melakukan unzip file tersebut dengan command `unzip gitIsGood.zip` maka nanti akan teroutput 
folder `gitIsGood` kita akan masuk ke situ

2. Setelah masuk ke dalam folder tersebut dan lakukan command `ls` ada file `flag.txt` tapi isinya adalah `flag{REDACTED}`, hmm brarti kita perlu cari tau value nya

3. Karena dari judul soal saja kita sudah dapet hint yaitu mengenai `Git` sebagai version control system, artinya kita bisa cari tau history file tersebut, mari kita selami tiap-tiap history dan log nya

4. Cari tau dulu log atau history commit nya

```bash
$ git log --oneline

d10f77c (HEAD -> master) Edited files
195dd65 Edited files
6e824db edited files
```

okee ternyata hanya ada 3 commit saja, mempermudah pencarian kita.
jadi karena cuma ada 3 commit saja kita coba lihat perbandingan file commit sebelumnya dengan commit saat ini (default) yaitu menggunakan `git show`

```bash
$ git show

commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index 8684e68..c5250d0 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{protect_your_git}
+flag{REDACTED}
```

mantapp kita dapat flag dari perbandingan 2 commit terakhir, simple ygy

## Flag

`flag{protect_your_git}`
