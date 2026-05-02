from functools import reduce

def royxat_elementlari_ko_paytmasini_hisoblang(royxat):
    return reduce(lambda x, y: x * y, royxat)

# Misol:
ro'yhat = [1, 2, 3, 4, 5]
print(royxat_elementlari_ko_paytmasini_hisoblang(ro'yhat))
