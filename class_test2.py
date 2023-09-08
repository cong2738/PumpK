class A:    
    def __init__(self,id,n,p):
        self.name = id
        self.num = n
        self.price = p

    def test(self):
        print(f'{self.name}:{self.num}:{self.price}')
    

class B(A):
    def __init__(self):
        super().__init__('참외',10,3000)
        self.test()

        
b = B()