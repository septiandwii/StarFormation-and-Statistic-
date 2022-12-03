# def isPythagoras(a, b, c):
#     sisiMiring = a**2 + b**2
#     pythagoras = sisiMiring == c**2
#     print(pythagoras)

# isPythagoras(3, 4, 5)
# isPythagoras(5, 9, 12)
# isPythagoras(8, 6, 10)
# isPythagoras(7, 8, 11)

def isPythagoras(a, b, c):
    if c**2 == a**2 + b**2:
        result = True
    else:
        result = False
    return result
print(isPythagoras(6, 8 , 9))