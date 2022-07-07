"""Modul 2"""

#1
class Pesan(object):
    def __init__(self, sebuahString):
        self.text = sebuahString
    def cetakIni(self):
        print(self.text)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.text))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.text))
    def jumKar(self):
        return len(self.text)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.text),'karakter')
    def perbaharui(self, stringBaru):
        self.text = stringBaru
    #a
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.text:
            return True
        else :
            return False
    #b
    def hitungVokal(self):
        v = ['A','I','U','E','O','a','i','u','e','o']
        hitung = 0
        for i in self.text:
            if i in v:
                hitung+=1
        return hitung
    #c
    def hitungKonsonan(self):
        k = ['A','I','U','E','O','a','i','u','e','o']
        hitung = 0
        for i in self.text:
            if i not in k:
                hitung+=1
        return hitung

#2
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self, nama):
        self.nama = nama
    def ucapSalam(self):
        print ('salam ', self.nama)
    def makan(self, s):
        print ('saya makan ', s)
        self.keadaan = 'kenyang'
    def olahraga (self, k):
        print ('sedang latihan ', k)
        self.keadaan = 'lapar'
    def kaliDua(self, n):
        return n*2

listKuliah = []
MahasiswaBaru = []
#2-    
class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.us = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + ', Tinggal di ' + self.kota \
            + ', Uang saku ' + str(self.us) \
            + ' tiap bulan.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUs(self):
        return self.us
    def makan(self, s):
        print ('makan ',s,' sambil belajar')
        self.keadaan = 'kenyang'
    #a    
    def ambilkota(self):
        return self.kota
    #b
    def perbaharuiKota(self, k):
        self.kota = k
    #c
    def tambahUs(self, u):
        return self.us + u

#3
    class MhsBaru(Mahasiswa):
        def __init__(self, nama, asal, alamat):
            self.nama = nama
            self.asal = asal
            self.alamat = alamat
        def input(self):
            MahasiswaBaru.append(self.nama)
            MahasiswaBaru.append(self.asal)
            MahasiswaBaru.append(self.alamat)
        
#4
    def ambilKuliah(self, i):
        self.i = i
        listKuliah.append(i)

#5
    def hapusmatkul(self):
        listKuliah[0:len(listKuliah)]=[]

#6
class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, alamat):
        self.nama = nama
        self.NIS = NIS
        self.alamat = alamat
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIS
    def ambilUs(self):
        return self.alamat

#7
class MhsTIF(Mahasiswa):
    def __init__(self, nama, jurusan, alamat):
        self.nama = nama
        self.jurusan = jurusan
        self.alamat = alamat
