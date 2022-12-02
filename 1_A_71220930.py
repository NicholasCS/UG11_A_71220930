print("======= Program Manipulasi String =======")
print("Pilihan Menu : ")
print("1. Hitung kata")
print("2. Ubah Kata")
pilihan = int(input("Pilihan anda : "))
def hitung_kata():
    a = input("Masukkan sebuah kalimat/kata : ")
    b = input("Masukan kata yang ingin dihitung : ")
    print("Terdapat sebanyak",a.count(b),"kata makan di dalam kalimat")
def ubah_kata():
    c = input("Masukan sebuah kalimat/kata : ")
    d = input("Masukan kata yang ingin di ubah : ")
    e = input("Masukan kata prngganti : ")
    print("Srting berhasil diubah menjadi : ",c.replace(d,e))

if pilihan==1:
    hitung_kata()

elif pilihan==2:
    ubah_kata()

else:
    input("Masukan sebuah kalimat/kata : ")
    print("pilihan yang anda input tidak terdaftar di daftar pilihan")
                              

