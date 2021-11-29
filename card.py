import random


class Card:
    def __init__(self,value,suit):
        self.cost=value
        self.value=['A','2','3','4','5','6','7','8','9','10','J','Q','K'][value-1]
        self.suit=['\u2661','\u2667','\u2664','\u2662']
        self.suit_c=random.choice(self.suit)
    def price(self):
        if self.cost>=10:
            return 10
        elif self.cost==1:
            return 11
        return self.cost
    def show(self):
        print('-----------')
        print(f'| {self.value:<2}       |')
        print('|          |')
        print(f'|    {self.suit_c}     |')
        print('|          |')
        print(f'|      {self.value:>2}  |')
        print('------------')

# obj=Card(3,'\u2661',)
# obj.price()
# obj.show()
