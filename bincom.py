from collections import Counter
monday = sorted(["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED",
          "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"])

tuesday = sorted(["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED",
           "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"])

wednesday = sorted(["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED",
             "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"])

thursday = sorted(["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED",
            "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"])

friday = sorted(["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED",
          "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"])

"""
def count(n):
    m = Counter(n)
    print(m)

mo = count(monday)
tu = count(tuesday)
we = count(wednesday)
th = count(thursday)
fr = count(friday)"""
length = len(monday)
add = sorted(set(monday))
mid = []

for s in add:
    print(s)
    



'''
mean = length / sum
print(mean)'''