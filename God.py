class God:
    # I'm doing everything I wanna to do!!!!

    from random import randint

    # Customer

    __names = ['Ivan', 'Mishka', 'Petka', 'Vaska', 'Kolka', 'Mitka', 'Dashka', 'Mashka', 'Natashka', 'Anka', 'Yanka']
    __moods = ['Bad', 'Good', 'Excellent', 'Brilliant']

    # CoffeeShop

    __places = ['Mogilevskaya', 'Uručča', 'Hrušaŭka', 'Plošča Jakuba Kolasa', 'Kastryčnickaja', 'Niamiha']
    __name_shops = ['MyCoffee', 'YourCoffee', 'TheirCoffee', 'BananaHouse', 'SvetlanaHouse']

    def define_Visitor(self):
        name = self.__names[self.randint(0, len(self.__names) - 1)]
        mood = self.__moods[self.randint(0, len(self.__moods) - 1)]
        ages = self.randint(10, 80)
        return name, mood, ages

    def define_CoffeeShop(self):
        place = self.__places[self.randint(0, len(self.__places) - 1)]  # define a random place
        name = self.__name_shops[self.randint(0, len(self.__name_shops) - 1)]
        return place, name
