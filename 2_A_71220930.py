def cetak_huruf(kalimat):
    n= len(kalimat)
    if n%2==0:
        left = kalimat[0:3]
        right = kalimat[n-3-1:]
        print("Huruf yang diambil pada kata",left, "dan",right)


    else:
     tgh = round(n/2)
     o=kalimat[tgh-2:tgh+1]
     print("Huruf yang diambil pada kata",kata, "adalah",o)

     

    

kata = str(input("Masukan kata : "))
h = cetak_huruf(kata)
(h)

