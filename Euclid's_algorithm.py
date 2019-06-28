#Euclid's algorithm
#11-22-17

def gcd(p, q):
    if(q == 0):
        return p
    r = p % q
    return gcd(q, r)

print(gcd(20, 6))
