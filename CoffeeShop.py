class CoffeeShop:
    COEFF_PRICE = 1

    def __init__(self, place, name, visitors_mark):
        # Why have I created THIS init???
        self.__place = place
        self.__places = {'Mogilevskaya': 1, 'Uručča': 1, 'Hrušaŭka': 2, 'Plošča Jakuba Kolasa': 3, 'Kastryčnickaja': 4,
                       'Niamiha': 5}
        self.__mark_place = self.__places[self.__place]
        self.__visitors_mark = visitors_mark
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def visitors_mark(self):
        return self.__visitors_mark

    @property
    def place(self):
        return self.__place



    def getprice(self):
        price = self.__mark_place * self.COEFF_PRICE * self.__visitors_mark
        return price.__round__()


