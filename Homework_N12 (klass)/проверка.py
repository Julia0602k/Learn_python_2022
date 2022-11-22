import random
class Human:
    year = 2022
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age
name = ''
gender = random.choice('mw')
if gender == 'm':
    name = random.choice(['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend', 'Lewis Pope'])
elif gender == 'w':
    name = random.choice(['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice', 'Ruth Rice'])
# Определение возраста, даты рождения, свадьбы, смерти
age = random.randint(18, 100)





dict_human = {i: Human(gender, name, age) for i in range(random.randint(2, 5))}
# for i in range(random.randint(2, 5)):
#     dict_human[i] = Human(gender, name, age, temper, work, capital, income, d_birth, d_death, house, car, family, d_wedding, expence)
print(dict_human)
print(len(dict_human))