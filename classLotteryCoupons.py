class Coupons:
    def __init__(self, n):
        self.somaDigitos = self.SomaDigitos(n)

    def SomaDigitos(self, n):
        if n == 0:
            return 0
        
        coupons = range(1, n+1) 
        couponsMod = list(map(lambda x: abs(x) % 10, coupons)) 
        couponsDiv = list(map(lambda x: abs(x) // 10, coupons))
        couponsSum = couponsMod

        while list(filter(lambda x: x != 0, couponsDiv)): 
            couponsMod = list(map(lambda x: x % 10, couponsDiv))
            couponsDiv = list(map(lambda x: x // 10, couponsDiv))
            couponsSum = list(map(lambda x, y: x + y, couponsSum, couponsMod))

        return couponsSum

    def GetSomaDigitos(self):
        return self.somaDigitos

class Sorteio:
    def __init__(self, couponsSum):
        self.listaSorteio = self.ListaSorteio(couponsSum)

    def ListaSorteio(self, couponsSum):
        if couponsSum == 0:
            return 0
            
        maxCouponsSum = max(couponsSum) + 1
        winnersCount = list(map(lambda x: couponsSum.count(x), range(1, maxCouponsSum)))  
        maxWinnerCount = max(winnersCount) 
        s = winnersCount.count(maxWinnerCount) 
        return s

    def GetSorteio(self):
        return self.listaSorteio
        

def test():
    for i in range(0,23):
        C = Coupons(i)
        somaCoupons = C.GetSomaDigitos()
        Sort = Sorteio(somaCoupons)
        print(Sort.GetSorteio())

if __name__ == '__main__':
    test()