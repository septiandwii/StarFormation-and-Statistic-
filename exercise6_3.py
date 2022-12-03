# def starFormation2(n):
#     for a in range(n, 0, -1):
#         print("*" * a)

# starFormation2(int(input("Masukkan angka: ")))

def starFormation2(n):
    for i in range (n):
        print('*' * (n-i))

starFormation2(4)