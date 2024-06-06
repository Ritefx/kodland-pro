
import random
harfler = "+-/*!&#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parolanızın uzunluğunu girin: "))
parola = ""
for _ in range(uzunluk):
    parola += random.choice(harfler)

print("şifren:", parola)