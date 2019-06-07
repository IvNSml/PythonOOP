class Customer():
    from random import randint
    COEFF_AGE = 9 / 13
    COEFF_MOOD = 1

    def __init__(self, name=None, mood=None, age=None):

        self.__listmoods = {'Bad': 1, 'Good': 2, 'Excellent': 3, 'Brilliant': 4}
        self.__name = name
        self.__age = age
        self.__mood = mood

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def mood(self):
        return self.__mood

    def getmark(self):
        modif_age = self.COEFF_AGE * self.__age
        modif_mood = self.COEFF_MOOD * self.__listmoods[self.__mood]
        mark = ((modif_age + modif_mood + self.randint(1, 2200)) / 33.33) + 10
        return mark
