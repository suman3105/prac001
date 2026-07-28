class car:
    def op(self,brand,color):
        self.brand =  brand
        self.color = color
    def show(self):
        print(f'this car is a {self.brand}{self.color}')

car1=car()
car1.op('bmw','red')

car2=car()
car2.op('tesla','red')

car1.show()
car2.show()
