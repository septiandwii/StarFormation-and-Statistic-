
def starFormation1(n):
    for i in range(n+1):
        print("*" * i)

def starFormation2(n):
    for i in range (n):
        print('*' * (n-i))

def starFormation3(n):
    starFormation1(n)
    starFormation2(n-1)
starFormation3(int(input("Masukkan N: ")))
