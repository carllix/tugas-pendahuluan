# # PROBLEM 1     
# n = int(input("Masukkan N: "))
# arr_angka = [0 for i in range(n)]
# arr_angka_reverse = [0 for i in range(n)]

# print("Masukkan angka dari kiri ke kanan: ")
# for i in range(n):
#     arr_angka[i] = int(input())

# print("Angka dari kanan ke kiri: ")
# for i in range(n):
#     arr_angka_reverse[i] = arr_angka[n-i-1]

# for i in range(n):
#     print(arr_angka_reverse[i])

# # PROBLEM 2
# n = int(input("Banyaknya barang: "))
# arr_harga = [0 for i in range(n)]

# print("Masukkan harga barang: ")
# for i in range(n):
#     arr_harga[i] = int(input())

# diskon = int(input("Masukkan diskon: "))
# for i in range(n):
#     arr_harga[i] *= (100-diskon)/100

# print("Harga barang sesudah diskon: ")
# for i in range(n):
#     print(int(arr_harga[i]))

# # PROBLEM 3
# # Cara 1
# n = int(input("Masukkan banyaknya stik Tuan Kris: "))

# arr_panjang = [0 for i in range(n)]
# arr_segitiga = [0 for i in range(100)]

# print("Masukkan panjang stik: ")
# for i in range(n):
#     arr_panjang[i] = int(input())

# x = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1,n):
#             if arr_panjang[i]+arr_panjang[j]>arr_panjang[k]:
#                 arr_segitiga[x] = [arr_panjang[i], arr_panjang[j], arr_panjang[k]]
#                 x+=1

# print("Daftar segitiga yang dapat dibuat: ")
# for i in range(100):
#     if arr_segitiga[i]!=0:
#         for j in range(3):
#             print(arr_segitiga[i][j], end=" ")
#         print()


# # Cara 2
# n = int(input("Masukkan banyaknya stik Tuan Kris: "))

# arr_panjang = [0 for i in range(n)]

# print("Masukkan panjang stik: ")
# for i in range(n):
#     arr_panjang[i] = int(input())

# print("Daftar segitiga yang dapat dibuat: ")
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1,n):
#             if arr_panjang[i]+arr_panjang[j]>arr_panjang[k] and arr_panjang[i]+arr_panjang[k]>arr_panjang[j] and arr_panjang[j]+arr_panjang[k]>arr_panjang[i]:
#                 print(arr_panjang[i], arr_panjang[j], arr_panjang[k])

# PROBLEM 4 (SURREND)

# rantai_dna = input("Masukkan rantai DNA: ")
# pola = input("Masukkan pola yang dicari: ")
# panjang_pencarian = len(rantai_dna) - len(pola)

# for i in range(panjang_pencarian+1):

# # PROBLEM 5
# n = int(input("Banyaknya nilai: "))
# arr_nilai = [0 for i in range(100)]

# print("Daftar nilai: ")
# for i in range(n):
#     nilai = int(input())
#     arr_nilai[nilai-1] += 1

# print("Daftar nilai yang dicurigai: ")
# for i in range(100):
#     if arr_nilai[i] >= 2:
#         print(i+1)

# # PROBLEM 6
# n = int(input("Masukkan n: "))
# arr = [0 for i in range(n)]
# new_arr = [0 for i in range(n)]

# for i in range(n):
#     arr[i] = int(input(f"Masukkan elemen ke {i+1}: "))

# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#             dummy = arr[i]
#             arr[i] = arr[j]
#             arr[j] = dummy

# for i in range(n):
#     if i%2 == 0:
#         new_arr[i] = arr[i//2]
#     else:
#         new_arr[i] = arr[n-1-(i//2)]

# print(new_arr)

# # PROBLEM 7
# # Cara 1
# n = int(input("Masukkan jumlah huruf pada tulisan: "))
# tulisan = input("Masukkan tulisan: ")
# is_palindrom = True
# banyak_huruf = [1 for i in range(n)]
# ganjil = 0

# if n%2==0:
#     is_palindrom = False
# else:
#     for i in range(n):
#         for j in range(n):
#             if i!=j:
#                 if tulisan[i] == tulisan[j]:
#                     banyak_huruf[i]+=1

#     for i in range(n):
#         if banyak_huruf[i]%2!=0:
#             ganjil+=1
    
#     if ganjil != 1:
#         is_palindrom = False
    
# if is_palindrom:
#     print("Tulisan tersebut dapat disusun menjadi sebuah palindrom.")
# else:
#     print("Tulisan tersebut tidak dapat disusun menjadi sebuah palindrom.")

# # Cara 2
# n = int(input("Masukkan jumlah huruf pada tulisan: "))
# tulisan = input("Masukkan tulisan: ")
# is_palindrom = True
# banyak_huruf = [1 for i in range(n)]
# ganjil = 0

# for i in range(n):
#     for j in range(n):
#         if i!=j:
#             if tulisan[i] == tulisan[j]:
#                 banyak_huruf[i]+=1

# for i in range(n):
#     if banyak_huruf[i]%2!=0:
#         ganjil+=1
    
# if ganjil != 1:
#     is_palindrom = False

# if is_palindrom:
#     print("Tulisan tersebut dapat disusun menjadi sebuah palindrom.")
# else:
#     print("Tulisan tersebut tidak dapat disusun menjadi sebuah palindrom.")

# # PROBLEM 8
# n = int(input("Masukkan jumlah bilangan: "))
# arr = [0 for i in range(n)]

# for i in range(n):
#     arr[i] = int(input(f"Masukkan bilangan ke-{i+1}: "))

# # Sort
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#             dummy = arr[i]
#             arr[i] = arr[j]
#             arr[j] = dummy

# # Mean
# total = 0
# for i in range(n):
#     total+= arr[i]
# mean = total/n

# # Median
# if n%2==0:
#     median = (arr[n//2-1]+arr[n//2])/2
# else:
#     median = arr[n//2]

# # Modus
# arr_kemunculan = [0 for i in range(arr[n-1]+1)]

# for i in range(n):
#     arr_kemunculan[arr[i]]+=1

# terbesar = arr_kemunculan[0]
# for i in range(1,arr[n-1]):
#     if arr_kemunculan[i]>terbesar:
#         terbesar = arr_kemunculan[i]
#         modus = i

# print(f"Mean: {mean}")
# print(f"Median: {median}")
# print(f"Modus: {modus}")

# # PROBLEM 9
# a = int(input("Masukkan jumlah anggota A: "))
# b = int(input("Masukkan jumlah anggota B: "))
# arr_a = [0 for i in range(a)]
# arr_b = [0 for i in range(b)]

# for i in range(a):
#     arr_a[i] = int(input(f"Masukkan anggota A ke-{i+1}: "))

# for i in range(b):
#     arr_b[i] = int(input(f"Masukkan anggota B ke-{i+1}: "))

# is_same = True
# is_subset = True
# kondisi_a_subset_b = [0 for i in range(a)]
# kondisi_b_subset_a = [0 for i in range(b)]

# if a==b:
#     for i in range(a):
#         if arr_a[i] != arr_b[i]:
#             is_same = False
# else:
#     is_same = False
#     # A subset B
#     if a<b:
#         for i in range(a):
#             for j in range(b):
#                 if arr_a[i] == arr_b[j]:
#                     kondisi_a_subset_b[i] += 1

#         for i in range(a):
#             if kondisi_a_subset_b[i] == 0:
#                 is_subset = False
#             else:
#                 himp = "A"
#                 subset_dari = "B"
#     else:
#         for i in range(b):
#             for j in range(a):
#                 if arr_b[i] == arr_a[j]:
#                     kondisi_b_subset_a[i] += 1

#         for i in range(b):
#             if kondisi_b_subset_a[i] == 0:
#                 is_subset = False
#             else:
#                 himp = "B"
#                 subset_dari = "A"

# # CEK SUBSET A ATAU B
# if is_same==True:
#     print("A sama dengan B.")
# else:
#     if is_subset == True:
#         print(f"{himp} adalah subset {subset_dari}.")
#     else:
#         print("Tidak ada relasi.")

# # PROBLEM 1 PRAK FTMD
# n = int(input("Masukkan banyak robot: "))
# config = input("Masukkan konfigurasi robot: ")
# kiri = 0
# kanan = 0

# for i in range(n//2):
#     kiri+=int(config[i])

# for i in range(n-1, n//2-1, -1):
#     kanan+=int(config[i])

# if kanan>kiri:
#     print("Sisi kanan menang!")
# elif kanan<kiri:
#     print("Sisi kiri menang!")
# else:
#     print("Berakhir seri!")

# PROBLEM 2 PRAK FTMD
