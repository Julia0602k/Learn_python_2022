import random
class Human:
    def __init__(self, work, temper):
        self.temper = temper
        self.work = work
    def jobs(self):
        dict_job1_temper = {'холерик': (7, 2), 'сангвиник': (10, 3), 'меланхолик': (6, 7), 'флегматик': (20, 5)}
        for key, value in dict_job1_temper.items():
            if key == self.temper:
                a = random.randint(1, value[0])
                b = random.randint(1, value[1])
                if self.work == 'Рабочий' and a == 1:
                    print(a)
                    self.work = 'Безработный'
                    print(self.work)
                elif self.work == 'Безработный' and b == 1:
                    print(b)
                    self.work = 'Рабочий'
                    print(self.work)
        return self.jobs
    def info(self):
        print(self.work, self.temper)
    def print(self):
        print(111, '\n')

dict_human1 = {}
for i in range(5):
    work = random.choice(['Рабочий', 'Безработный'])
    temper = random.choice(['холерик', 'сангвиник', 'меланхолик', 'флегматик'])
    dict_human1[i] = Human(work, temper)
print(dict_human1)
for k, v in dict_human1.items():
    v.info()
    v.jobs()
    v.print()







