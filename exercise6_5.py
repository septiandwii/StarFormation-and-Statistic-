# def suma(*angka):
#     data = []
#     print(data)
#     print(angka)
#     for i in angka:
#         print(i)
#         data.append(i)
#     jumlah = sum(data)
#     print(jumlah)

# def average(*angka):
#     data = []
#     print(angka)
#     for i in angka:
#         print(i)
#         data.append(i)
#     jumlah = sum(data)
#     print(jumlah / data)

# suma(9, 8, 7, 6)
# average(9, 8, 7, 6)


#fungsi untuk mencari jumlah sum dari data
def sum(*data):
    result = 0 
    for x in data:
        result += x
    return result

#fungsi untuk mencari rata-rata dari data
def average(*data):
    jum = 0
    for x in data:
        jum += x
    result = jum / len(data)
    return result

#fungsi untuk mencari nilai maksimal
def findMax(*data):
    return max(data)

#fungsi untuk mencari nilai maksimal
def findMin(*data):
    return min(data)


print(sum(3, 4, 5))
print(average(3, 4, 5))
print(findMax(3, 4, 5))
print(findMin(3, 4, 5))