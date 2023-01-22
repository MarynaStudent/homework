#Задание 1
#Напишите программу с пустым классом Country. 
#Опишите наследуемые от класса Country классы Russia, Canada, Germany. 
#Добавьте каждому классу поле population и опишите метод setPopulation и getPopulation.
class Country:
    def __init__(self, language, currency, capital_of_country):
        self.language = language
        self.currency = currency
        self.capital_of_country = capital_of_country
    def info(self):
        return f'{self.language}, {self.currency}, {self.capital_of_country}'
class Russia(Country):
    def __init__(self, language, currency, capital_of_country, population=143000000):
        super().__init__(language, currency, capital_of_country)
        self.population = population
    def info(self):
        return f'{self.language}, {self.currency}, {self.capital_of_country}'
    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, value):
        self._population = value

class Canada(Country):
    def __init__(self, language, currency, capital_of_country, population=38000000):
        super().__init__(language, currency, capital_of_country)
        self.population = population
    def info(self):
        return f'{self.language}, {self.currency}, {self.capital_of_country}'
    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, value):
        self._population = value
class Germany(Country):
    def __init__(self, language, currency, capital_of_country, population=83000000):
        super().__init__(language, currency, capital_of_country)
        self.population = population
    def info(self):
        return f'{self.language}, {self.currency}, {self.capital_of_country}'
    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, value):
        self._population = value

r1 = Russia('Russian', 'RUB', 'Moscow')
c1 = Canada('English', 'USD', 'Ottawa')
g1 = Germany('Deutsch', 'EUR', 'Berlin')
print(g1.info())
print(g1.population)
