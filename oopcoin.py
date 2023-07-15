class Coin:
    def __init__(self, value:int) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return f"{self.value}"

coin1 =Coin(10) 
coin2 = Coin(11)
coin3 = Coin(12)
coins = [coin1, coin2, coin3]

# print(coins)

class PaperMoney:
    
    def __init__(self, value: int) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return f"{self.value}"

papermoney1 = PaperMoney(20)
papermoney2 = PaperMoney(30)
# papermoneys = [papermoney1, papermoney2]

# print(papermoneys)

class Wallet:
    def __init__(self) -> None:
        self.all_money = []
        
    def getAllPaperMoney(self):
        s_loop = 0
        total_money = 0
        for paper in self.all_money:
            if type(paper).__name__ == 'PaperMoney':
                total_money += int(paper.value)
                s_loop +=1
        return f" {s_loop}  {total_money}"
        
  
    def getAllCoin(self):
        s_loop = 0
        total_money = 0
        result = ''
        for paper in self.all_money:
           if isinstance(paper, PaperMoney):
               total_money += int(paper.value)
               s_loop +=1
               result += f" {s_loop}  {total_money}"
        return result
    
    def getSumMoney(self):
        result = 0
        for paper in self.all_money:
            result += paper.value 
        return result
                
    def addMoney(self, d: PaperMoney|Coin):
        self.all_money.append(d)
                
a = Wallet()
a.addMoney(papermoney1)
a.addMoney(papermoney2) 
a.addMoney(coin1)
a.addMoney(coin2)
a.addMoney(coin3)
print(a.getAllPaperMoney())
print(a.getSumMoney())