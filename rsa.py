class Key():
    def __init__(self):
        self.p = 5 # one prime
        self.q = 7 # another prime
        self.n = self.p*self.q # the modulo
        self.totient = (self.p-1)*(self.q-1) # totient
        self.e = 3
        if self.gcd(self.e, self.totient) == 1:
            self.e = 3
    def gcd(self, one, two):
        while two:
            one = two
            two = one%two
            return one
    def phi(self, n):
        amount = 0
        for k in range(1, n + 1):
            if self.gcd(n, k) == 1:
                amount += 1
        return amount
myKey = Key()