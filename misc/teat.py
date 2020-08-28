from typing import List, Tuple, Dict


class Person:
    def __init__(self, first_name: str, last_name: str, gender: str = "male"):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.__private_value = "im private"

    def get_private_value(self):
        return self.__private_value

    @staticmethod
    def solve_fib_dynamic(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        fib_table = [0] * (n + 1)
        fib_table[0] = 0
        fib_table[1] = 1
        fib_table[2] = 1

        for i in range(3, n + 1):
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        return fib_table[n]

    @staticmethod
    def solve_fib_recursive(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return Person.solve_fib_recursive(n - 1) + Person.solve_fib_recursive(n - 2)


p = Person("Michael", "Wu")

import time
start = time.time()
print(Person.solve_fib_dynamic(n=100))
end = time.time()
print(f"used {end-start} seconds")
