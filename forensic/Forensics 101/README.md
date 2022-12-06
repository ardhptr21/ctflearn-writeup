# [Forensic 101](https://ctflearn.com/challenge/96)

## Deskripsi Soal

Think the flag is somewhere in there. Would you help me find it?
`https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c`

## Solve

1. Download file yang telah diberikan dan ternyata itu adalah file dengan ekstensi jpg, namun setelah dibuka tidak ada informasi apapun
2. Coba cari tau dengan `exiftool`

```bash
$ exiftool 95f6edfb66ef42d774a5a34581f19052 .jpg

ExifTool Version Number         : 12.44
File Name                       : 95f6edfb66ef42d774a5a34581f19052.jpg
Directory                       : .
File Size                       : 9.8 kB
File Modification Date/Time     : 2022:11:07 08:19:30-05:00
File Access Date/Time           : 2022:11:07 08:29:16-05:00
File Inode Change Date/Time     : 2022:11:07 08:20:16-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 236
Image Height                    : 218
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 236x218
Megapixels                      : 0.051
```
yahh tidak ada informasi juga :(

3. Yahh agak bingung disini harus kemana lagi, tapi-tapi setelah dipikir-pikir tiap file itu punya printable string, kenapa ngga dicoba yekann? okee kita coba 
ambil semua printable string dari file itu menggunakan command `strings`

```bash
$ strings 95f6edfb66ef42d774a5a34581f19052.jpg

...
xp7p
v{*{8
=k"$TW3G
1)j!
7y}U
<~0GD
n%CeoQ=m8
`"n<P
 i}\D
X`(
8kF=
~9%]Tn
flag{wow!_data_is_cool}
$lqU
AG{u
Xm*CnC
@'hnQ
ax+p
bdQG
D_ O
```
> FOR YOU: ini hanya sebgaian outputnya saja yaa gess yaaa

nahhh benar, ada flag diantara deretan string yang tidak beraturan didalamnya

## Flag

`flag{wow!_data_is_cool}`
