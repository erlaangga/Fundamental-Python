# -*- coding: utf-8 -*-
# Python membaca file dengan menganggap semua karakternya menggunakan ASCII
# menambahkan komentar di atas bersifat opsional namun perlu, sebagai persiapan agar tidak error ketika ada UTF-8 muncul :D


# ini menggunakan Python versi 2.7
# dokumentasinya dapat dilihat di help()
# Python dapat menggunakan kutip satu atau dua

print "Hallo Dunia!"
# pada Python versi 3 syntax di atas sudah dihilangkan sehingga setiap sintaks meskipun default harus menggunakan tanda kurung 
print("Hallo dunia!")
# dokumentasinya dapat dilihat di help(str)
contoh = "contoh string"
print contoh
print(contoh)

a = 15
b =7
c=9
d=a+b+c
print "Hasilnya",d
# typecasting
print "Hasilnya adalah "+str(float(d))
print type(d)
z = 4.3
print type(z)
print type(contoh)
# fungsi dir dapat melihat semua field instance yang dipunyai suatu objek
print dir(contoh)
print contoh.capitalize()
print contoh.upper()

nama = "Jajang"
print "%s nama adalah %s" %(contoh,nama)

print "Operator dan ekspresi"

bilangan1 = 5
bilangan2 = 3

print 'bil1 = ', bilangan1
print 'bil2 = ', bilangan2

print 'bil1 + bil2 = ', bilangan1 + bilangan2
print 'bil1 - bil2 = %s' % (bilangan1 - bilangan2)
print 'bil1 * bil2 = {0}'.format(bilangan1 * bilangan2)
print 'bil1 ** bil2 = ', bilangan1 ** bilangan2

bilangan1 = 5.0
print 'bil1 = ', bilangan1
print 'bil2 = ', bilangan2

print 'bil1 / bil2 = ', bilangan1 / bilangan2
print 'bil1 // bil2 = ', bilangan1 // bilangan2
print 'bil1 % bil2 = ', bilangan1 % bilangan2

print '-' * 80

bilangan1 = 5
print 'bil1 = ', bilangan1
print 'bil2 = ', bilangan2

print 'bil1 << bil2 = ', bilangan1 << bilangan2
print 'bil1 >> bil2 = ', bilangan1 >> bilangan2
print 'bil1 & bil2 = ', bilangan1 & bilangan2
print 'bil1 | bil2 = ', bilangan1 | bilangan2
print 'bil1 ^ bil2 = ', bilangan1 ^ bilangan2
print '~bil1 = ', ~bilangan1

print '-' * 80

print 'bil1 < bil2 = ', bilangan1 < bilangan2
print 'bil1 > bil2 = ', bilangan1 > bilangan2
print 'bil1 <= bil2 = ', bilangan1 <= bilangan2
print 'bil1 >= bil2 = ', bilangan1 >= bilangan2
print 'bil1 == bil2 = ', bilangan1 == bilangan2
print 'bil1 != bil2 = ', bilangan1 != bilangan2

print '-' * 80

print 'not True = ', not True
print 'True and False = ', True and False
print 'True or False = ', True or False

print 'Sifat Asosiatif' 
hasil = 2 + 3 * 4
print '2 + 3 * 4 = %s' % hasil

hasil = (2 + 3) * 4
print '(2 + 3) * 4 = %s' % hasil

hasil = 2 / 3 * 4
print '2 / 3 * 4 = %s' % hasil

hasil = 2.0 / 3 * 4
print '2.0 / 3 * 4 = %s' % hasil


# tuple
nilai = [45,213,4,123]
print nilai
#tuple dapat memiliki nilai yang berbeda dalam satu variabel
nilai.append("tambahan")
print nilai
nilai[3] = "Wow"
print nilai

# dictionary
# Anda hanya bisa menggunakan obyek immutable (seperti string) untuk key/ kunci dictionary. Anda bisa menggunakan obyek mutable atau immutable untuk value dalam dictionary.
harga_buah = {"Pisang":16000, "Mangga":10000, "Pepaya":8000}
print harga_buah
print "Harga pisang (kualitas A) %s per kg." %harga_buah["Pisang"]
harga_buah["Pisang"] = 6000
print "Harga pisang (biasa) "+str(harga_buah["Pisang"])+" per kg."

# sequence
daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
nama = 'budi'

print 'Barang 0 =', daftar_belanja[0]
print 'Barang 1 =', daftar_belanja[1]
print 'Barang 2 =', daftar_belanja[2]
print 'Barang 3 =', daftar_belanja[3]

print 'Barang -1 =', daftar_belanja[-1]
print 'Barang -2 =', daftar_belanja[-2]

print 'Karakter 0 =', nama[0]

# slicing pada list
print 'Barang 1 ke 3:', daftar_belanja[1:3]
print 'Barang 2 ke terakhir:', daftar_belanja[2:]
print 'Barang 1 ke -1:', daftar_belanja[1:-1]
print 'Barang dari awal ke akhir:', daftar_belanja[:]

# slicing pada string
print 'Karakter 1 ke 3:', nama[1:3]
print 'Karakter 2 ke terakhir:', nama[2:]
print 'Karakter 1 ke -1:', nama[1:-1]
print 'Karakter dari awal ke akhir:', nama[:]

print '%s pergi ke %s' % ('ibu', 'pasar')
print '{0} pergi ke {1}'.format('ibu', 'pasar')

print 'jumlah total: %10.3f' % 10.3333
print 'jumlah total: {0:10.3f}'.format(10.3333)

# bacanya dari sini aja haha
print "Python"
print("Python itu mudah")

a = "Semua bisa belajar Python"
print a*5
b = 3456
print b, a

nama = raw_input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
print "Hai "+ nama

# blok program pada Python dipisah menggunakan indentasi yang semakin menjorok ke dalam
if(umur<10):
    print "Terus belajar ya!"
elif (umur<22):
    print "Belajar terus ya!"
else:
    print "Udah nikah?"

# Operator pada Python 
# Operator     Keterangan
# +     Menambahkan dua obyek
# -     Mengurangi obyek dengan obyek yang lain
# *     Perkalian
# **     Pangkat
# /     Pembagian
# //     Pembagian bulat ke bawah
# %     Sisa hasil bagi (modulus)
# <<     
# 
# (geser kiri) Menggeser bit ke sebelah kiri sesuai dengan jumlah bit yang ditentukan.
# 
# 2 << 2 menghasilkan 8. 2 direpresentasikan 10 dalam bit (binary digit). Menggeser 2 bit kekiri akan menghasilkan 1000 yang merupakan representasi dari desimal 8.
# >>     
# 
# (geser kanan) Menggeser bit ke sebelah kanan sesuai dengan jumlah bit yang ditentukan.
# 
# 11 > 1 menghasilkan 5. 11 direpresentasikan oleh bit dengan 1011 kemudian digeser kekanan 1 bit menghasilkan 101 yang merupakan desimal angka 5.
# &     
# 
# (bit-wise AND)
# 
# Operasi bit-wise AND dari angka (bit-wise adalah operasi angka berbasis bit yakni dengan 0 dan 1). 5 & 3 menghasilkan 1.
# |     
# 
# (bit-wise OR)
# 
# Operasi bit-wise OR dari angka. 5 | 3 menghasilkan 7.
# ^     
# 
# (bit-wise XOR)
# 
# Operasi bit-wise XOR (ekslusif OR). 5 ^ 3 menghasilkan 6.
# ~     
# 
# (bit-wise invert)
# 
# Operasi membalikkan angka bitwise dari x, menghasilkan -x - 1. ~5 akan menghasilkan -6. lihat two’s complement.
# <     
# 
# (kurang dari)
# 
# Mengembalikan apakah x kurang dari y. Semua operator pembanding mengembalikan True atau False. 5 < 3 mengembalikan False, 3 < 5 mengembalikan True dan 2 < 5 < 7 mengembalikan True.
# >     
# 
# (lebih dari)
# 
# Mengembalikan apakah x lebih dari y. 5 > 3 mengembalikan True.
# <=     
# 
# (kurang dari atau sama dengan)
# 
# Mengembalikan apakah x kurang dari atau sama dengan y. 5 <= 5 mengembalikan True.
# >=     
# 
# (lebih dari atau sama dengan)
# 
# Mengembalikan apakah x lebih dari atau sama dengan y. 5 >= 5 mengembalikan True.
# ==     
# 
# (sama dengan)
# 
# Membandingkan apakah kedua obyek sama. 2 == 2 mengembalikan True, 'nama' == 'Nama' mengembalikan False, 'nama' == 'nama' mengembalikan True.
# !=     
# 
# (tidak sama dengan)
# 
# Membandingkan apakah kedua obyek berbeda. 2 != 3 mengembalikan True.
# not     
# 
# (boolean NOT)
# 
# Jika x bernilai True akan mengembalikan False. Jika x bernilai False akan mengembalikan True. x = True; not x mengembalikan False.
# and     
# 
# (boolean AND)
# 
# x and y mengembalikan False jika x bernilai False, selain itu akan mengembalikan nilai y.
# 
# x = False; y = True; x and y akan mengembalikan False karena x bernilai False. Pada kasus ini Python tidak akan mengevaluasi y karena nilai x. Hal ini disebut short-circuit evaluasi.
# or     
# 
# (boolean OR)
# 
# Jika x bernilai True, x or y akan mengembalikan True, selain itu akan mengembalikan nilai y.
# 
# x = True; y = False; x or y mengembalikan True. short-circuit evaluasi berlaku juga disini.


makan = True
while makan:
    print "Makan"
    konfirmasi = raw_input("Masih lapar?")
    if konfirmasi.upper() in ["NO", "N", "TDK","TIDAK","ENGGAK","ENGGA","G",'GA', "GAK"]:
        makan = False
print "cie abis makan."

# list
# sebuah list dapat berupa kumpulan data dengan tipe data yang sama maupun bervariasi (heterogen)
contoh_list = ["Ada", 3, "meong", "berumur", 1, "tahun", True]
print contoh_list[2] + "!"

print 'isi list', contoh_list
print 'cetak list'
for i in contoh_list:
    print i
    
# tuple
# perbedaannya dengan list selain tandanya adalah tuple bersifat immutable (tak bisa diganti setelah didefinisikan)
contoh_tuple = (4,23,"Yiihii",True,"haha")
print 'isi tuple', contoh_tuple
print "cetak tuple"
for i in contoh_tuple:
    print i

# dictionary
# sebuah dictionary mempunyai bentuk {kunci:nilai} dengan tipe data yang bisa bermacam-macam
contoh_dictionary = {"makan": "pisang", "sebanyak": 3, 5:90, True:9}
contoh_dictionary[True]

print 'cetak dictionary'
for a,b in contoh_dictionary.items():
    print str(a)+" bernilai "+str(b)
    
# sama aja 
for a,b in contoh_dictionary.iteritems():
    print str(a)+" bernilai "+str(b)

# menggunakan fungsi range() untuk membuat angka secara berurut
angka = range(10)
for i in angka:
    print i

for i in range(100):
    if i % 2 == 0:
        print "angka genap"
        continue
    print i
    
# bagi seorang developer fungsi dir pada Python sangat berguna karena dapat melihat isi variabel dan fungsi pada suatu objek
import datetime
print 'isi datetime'
print dir(datetime)

# fungsi eval juga sangat berguna untuk membuat suatu nilai objek dari bentuk string 
print eval("5")
jam = "datetime.datetime.now()"
print eval(jam)

# fungsi repr juga dapat digunakan untuk mengubah nilai struktu objek menjadi string
jam2 = datetime.datetime.now()
# ketika dicetak jam2 akan diubah menjadi string yang dapat dibaca manusia non-programmer
print jam2
# pada interpreter ketika variabel kita masukkan akan langsun terlihat seperti ini
print "jam2 dipanggil dengan ", repr(jam2)

# // fungsi pada Python
def inifungsi():
    print "Baru memanggil fungsi"
    
inifungsi()

def halo(nama):
    print "Hai", nama

namanya = raw_input("Masukkan namanya: ")
halo(namanya)

def kalidua(nilai):
    print nilai,"dikali dua sama dengan"
    nilai2 = nilai * 2
    return nilai2

nilainya = int(raw_input("Masukkan nilainya: "))
print kalidua(nilainya)

# fungsi di Python dapat mempunyai nilai argumen default dengan menginisialisasikannya pada parameter
# jika tidak diberi sintaks return di akhir fungsi, secara otomatis fungsi mengembalikan return kosong yang berarti mempunyai tipe None
def makan(makanan, porsi=1):
    print "Makan",makanan,"sebanyak",porsi,"porsi"
    
makan("Nasi")
makan("Nasi", 3)

# argumen juga dapat kita masukkan dengan memberi nilai terhadap nama parameter
makan(porsi=2,makanan="Sate")

# fungsi pada Python dapat mempunyai fungsi lagi di dalamnya
def minum(minuman):
    print "Minum",minuman,"memang enak"
    def lap():
        return "setelah minum "+minuman+" pasti segar"
    return lap()

print minum("Air")

# fungsi sebagai dekorator
def selamat(orang):
    print "Isi orang:",orang
    def ucapannya(dia):
        print "Isi dia:", dia
        print "Wow"
        return "Selamat "+ str(orang(dia))
    return ucapannya


def selamat2(orang): # menerima argumen berupa fungsi
    print "Isi orang luar: ", orang
    def ucapannya(dia): #menerima argumen nilai argumen parameter fungsi
        print "Isi orang dalam: ",dia
        print "Wiw"
        return "Selamat "+ dia
    return ucapannya 

@selamat
def untuk(nama):
    print nama
    print "hmm"
    return nama+" yeay"

@selamat2
def untuk2(nama):
    print nama
    return nama

untuk("Erlan")
# dijalankan secara berbeda
untuk2("Erlan")


def salam(pada):
    def wrapper(kamu):
        return "Assalamu'alaikum " + pada(kamu)
    return wrapper
 
def rahmat(pada):
    def wrapper(kamu):
        return "Wa rahmatullah " + pada(kamu)
    return wrapper
 
def berkah(pada):
    def wrapper(kamu):
        return "Wabarokatuh " + pada(kamu)
    return wrapper

# dekotaror dieksekusi dari bawah ke atas
@salam
@rahmat
@berkah
def pesan(name):
    print name
    return name

pesan("Erlan")


# VarArgs
def total(*bilangan, **keywords):
    hitung = 0
    for bil in bilangan:
        hitung += bil
    for key in keywords:
        hitung += keywords[key]
    return hitung

print total(1, 2, 3, 4, 5)
print total(daging=2, sayur=10, buah=3)
print total(7, 8, 5, daging=2, sayur=10, buah=3)

def katakan(pesan, jumlah=1):
    "mencetak pesan <pesan> dengan jumlah <jumlah>"
    print pesan * jumlah

print katakan.__doc__
help(katakan)


# sintaks import digunakan untuk memanggil modul (file) python lainnya
# uniknya import di Python dapat digunakan di manapun (bahkan di dalam blok program seperti fungsi) bukan di bagian atas program
# ketika kita mengimport modul di Python, maka modul akan dicompile oleh Python sehingga menghasilkan file dengan format .pyc 
import modulbuatan


a = modulbuatan
a.katakan("meong!", 10)

from modulbuatan import katakan

katakan("meongin lah!")

class Orang:
    def katakanHalo(self):
        print 'Halo, apa kabar?'

org = Orang()
org.katakanHalo()

class Orang2:
    def __init__(self, nama):
        self.nama = nama

    def katakanHalo(self):
        print 'Halo %s, apa kabar?' % self.nama

org = Orang2('Jajang')
org.katakanHalo()

# bukan contoh yang baik tapi seenggaknya begitu lah :D
class Kakek:
    def __init__(self,namanya):
        self.namakakek = namanya
    def namakakekku(self):
        print "Nama kakek",self.namakakek

class Ayah(Kakek):
    def __init__(self,namanya):
        self.namaayah = namanya
    def namaayahku(self):
        print "Nama ayah",self.namaayah
        
class Anak(Ayah):
    def __init__(self,namanya):
        self.nama = namanya
        self.namaayah = "Abu "+ namanya
        self.namakakek = "al-Jakartiy"
    def namaku(self):
        print "Nama saya %s bin %s %s" %(self.nama, self.namaayah,self.namakakek)

kamu = Anak("Jajang")
kamu.namaku()
kamu.namaayahku()

# file
teks = """Jajang mempunyai seekor kucing peliharaan bernama meong.
Meong adalah kucing yang baik."""

meongtxt = 'meong.txt'

# membuka dengan mode tulis
filemeong = open(meongtxt, 'w')
filemeong.write(teks)
filemeong.close()

# default membuka file dengan mode baca
filemeong = open(meongtxt)
bariske = 0
while True:
    baris = filemeong.readline()
    bariske+=1
    if len(baris) == 0:
        # EOF
        break
    print bariske,baris,
filemeong.close()
print
# dibaca langsung semuanya
filemeong = open(meongtxt)
print bariske, filemeong.read()
filemeong.close()

class InputPendekError(Exception):
    "exception jika input terlalu pendek"

    def __init__(self, panjang, minimal):
        Exception.__init__(self)
        self.panjang = panjang
        self.minimal = minimal


try:
    teks = raw_input('Ketikkan sesuatu: ')
    panjang = len(teks)
    minimal_panjang = 3

    if panjang < minimal_panjang:
        raise InputPendekError(panjang, minimal_panjang)
except EOFError:
    print '\nKenapa sudah EOF?'
except KeyboardInterrupt:
    print '\nAnda membatalkan operasi'
except InputPendekError as e:
    print 'input terlalu pendek: panjang input: %s, minimal: %s' % (e.panjang, e.minimal)
else:
    print 'Anda mengetikkan "%s"' % teks

# beberapa sumber diambil dari http://workshop-python-101.readthedocs.io dan https://tutorialopenerp.wordpress.com/2014/10/10/python-decorator/