class Manager:
    def __init__(self, coffeeshops, price):
        self.__coffeeshops = coffeeshops
        self.__price = price
    @property
    def coffeeshops(self):
        return self.__coffeeshops
    @property
    def price(self):
        return self.__price

    def delshop(self):
        for i in self.__coffeeshops:
            if i.getprice() > self.__price:
                print('Coffeeshop', i.name, ' is closed!')
                self.__coffeeshops.remove(i)
            if i == self.__coffeeshops[-1]:
                print('Nothing is closed!')
        # There u can insert a for loop to test this method
        return self.__coffeeshops
