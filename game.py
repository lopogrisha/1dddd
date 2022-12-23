import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satiety=50
        self.job=job
        self.car=car
        self.home=home
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self,manage):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def days_indexes(self,day):
        pass
    def is_alive(self):
        pass
    def live (self,day):
        pass
class Auto:
    def __init__(self, brend_list):
        self.brend=random.choice(list(brend_list))
        self.fuel=brend_list[self.brend]["fuel"]
        self.strength=brend_list [self.brend]["strenght"]
        self.consumption=brend_list[self.brend]["consumption"]
        brends_of_car{
            "BMW":{"fuel":100,  "strenght":100, "comsumption":}: