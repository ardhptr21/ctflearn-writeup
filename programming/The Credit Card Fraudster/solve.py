
import luhn

"""
Karena nilai Card Number nya adalah 543210******1234
berarti kita harus menebak range angka dari 5432100000001234 sampai 5432109999991234
"""

for i in range(5432100000001234, 5432109999991234, 10000):
    if i % 123457 == 0 and luhn.verify(f'{i}'):
        print(f'CTFlearn{{{i}}}')
