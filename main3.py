class Human:
    def __init__ (self, name="Human"):
        self.name=name
class Auto:
    def __init__(self,brend):
        self.brend=brend
        self.passengers=[]
    def add_passenger(self,human):
        self.passengers.append(human)
    def print_passengers_names(self):
            if self.passengers!=[]:
                print(f"Імена {self.brend} пасажирів:")
                for passenger in self.passengers:
                    print(passenger.name)

            else:
                print(f"Пасажирів немає {self.brend}")
nick=Human("Nick")
kate=Human("Kate")
car=Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers_names()