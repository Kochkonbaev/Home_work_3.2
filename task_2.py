class Employee:

    def __init__(self, first_name, last_name, salary):
        self.fullname = f'{first_name} {last_name}'
        self.salary = salary

    def day_off(self, day, month, year):
         print(f'Я {self.fullname}, хочу взять отгул '
              f'на {day}.{month}.{year} число.')


class Frontend(Employee):
    def __init__(self, firstname, secondname, salary, experience):
        super().__init__(firstname, secondname, salary)
        self.experience = experience

    @staticmethod
    def visualize():
        print(f'Making visual appearance of project')

class Backend(Employee):
    def __init__(self, firstname, secondname, salary, experience):
        super().__init__(firstname, secondname, salary)
        self.experience = experience

    @staticmethod
    def set_up_db():
        print(f'Setting up database of project')

class Management(Employee):
    def __init__(self, firstname, secondname, salary, rank):
        super().__init__(firstname, secondname, salary)
        self.rank = rank
    
    def sheet(self, worker):
        if type(worker) == Management:
            print(f'Работник {worker.fullname} является менеджером')
        else:
            print(f'Работник {worker.fullname} уволен.')
            del worker

class Project:
    def __init__(self, workers):
        self.workers = workers

    def check_backend(self):
        for worker in self.workers:
            if type(worker) == Backend:
                worker.set_up_db()
                print(f'{worker.fullname}')
        

    def check_frontend(self):
        for worker in self.workers:
            if type(worker) == Frontend:
                worker.visualize()
                print(f'{worker.fullname}')
       

backend_1 = Backend('John', 'MacTavish', 3000, 'Senior')
backend_1.day_off(12, 3, 2021)

backend_2 = Backend('Victor', 'Alexandrov', 1500, 'Middle')
backend_2.day_off(21, 7, 2021)

backend_3 = Backend('Jim', 'Artemov', 900, 'Junior')
backend_3.day_off(5, 4, 2021)

frontend_1 = Frontend('Akira', 'Sato', 2500, 'Senior')
frontend_1.day_off(10, 11, 2021)

frontend_2 = Frontend('Izumi', 'Vatanabe', 1000, 'Middle')
frontend_2.day_off(23, 4, 2021)

frontend_3 = Frontend('Mark', 'Taylor', 500, 'Junior')
frontend_3.day_off(9, 9, 2021)

management_1 = Management('Vladimir', 'Kryukov', 4500, 'CEO')
management_1.sheet(frontend_3)
management_1.day_off(31, 12, 2021)

management_2 = Management('Oleg', 'Vetkin', 4400, 'HR-manager')
management_2.day_off(1, 1, 2022)

management_3 = Management('Kirill', 'Petrov', 4300, 'Project-manager')
management_3.day_off(1, 2, 2022)

project_workers = [backend_1, backend_2, backend_3,
                   frontend_1, frontend_2, frontend_3,
                   management_1
                   ]

project = Project(project_workers)

project.check_backend()
project.check_frontend()
