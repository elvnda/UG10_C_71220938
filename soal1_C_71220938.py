print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")
bilpertama=int(input("masukkan bilangan pertama :"))
bilkedua=int(input("masukkan bilangan kedua :"))
menu= input("pilihan anda :")
if menu== "1" :
    Tambah= bilpertama+bilkedua
    print ("hasil:",Tambah)
elif menu== "2" :
    Kurang= bilpertama-bilkedua
    print ("hasil:",Kurang)
elif menu== "3" :
    Kali= bilpertama*bilkedua
    print ("hasil:", Kali)
elif menu== "4" :
    Bagi= bilpertama//bilkedua
    print ("hasil:", Bagi)
