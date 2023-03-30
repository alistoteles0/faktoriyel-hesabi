#Bir sayının faktoriyelini hesaplama
while True:
    try:
        n = int(input("Lütfen pozitif bir tam sayı giriniz: "))
        break
    except ValueError:
        print("Geçersiz değer.")
faktoriyel = 1        
if n > 0:
    for i in range(1,n+1):
        faktoriyel = faktoriyel * i
    print(i,"! = ", faktoriyel)
elif n == 0:
    print("0! = 1")
else:
    print("Lütfen geçerli bir değer giriniz.")
        
         
        
        

        