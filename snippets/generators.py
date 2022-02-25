
def pairs_numbers():

    for i in range(100):
        if(i%2 == 0):
            yield i

pair_n = pairs_numbers()

print(next(pair_n))
print(next(pair_n))
print(next(pair_n))
print(next(pair_n))
print(next(pair_n))