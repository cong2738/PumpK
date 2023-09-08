class discount_policy:
    def pay_discount(self):        
        if self.used_money > 5000:
            self.discount = 0.1
        elif self.used_money > 3000:
            self.discount = 0.05
        elif self.used_money > 1000:
            self.discount = 0.02
        else:
            self.discount = 0
        return self.discount
    
class member(discount_policy):
    def __init__(self,name,age,purchase = 0):
        self.name = name
        self.age = age
        self.purchase = purchase
        self.used_money = purchase

m1 = member('Lee',57,1500)
print(m1.pay_discount())

members:list[member] = [m1]
members.append(member('Park',47,4000))
members.append(member('Kim',50,6000))

print(members)

for m in members:
    print(m.pay_discount())