from abc import ABC, abstractmethod
import csv 
from pprint import pprint


class Cupcake(ABC):
    size = 'regular'
    def __init__(self, name : str,price : float, flavor : str,frosting : str):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name: str, price: float, flavor: str, frosting: str):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Large(Cupcake):
    size = 'Large'
    def __init__(self, name: str, price: float, flavor: str, frosting: str, filling: str):
        super().__init__(name, price, flavor, frosting)
        self.filling = filling
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Regular(Cupcake):
    size = 'Regular'
    def __init__(self, name: str, price: float, flavor: str, frosting: str, filling: str):
        super().__init__(name, price, flavor, frosting)
        self.filling = filling
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

def read_csv(file_name):

    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile) 
        cupcake_lst = []
        for row in reader:
            cupcake_lst.append(row)
        return cupcake_lst   

def find_cupcake(file, name):
    for cupcake in read_csv(file):
        if cupcake["name"].lower() == name.lower():
            return cupcake
        else:
            print('not the right cake, checking next')

def find_cupcake_csv(file_name, cupcake_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["name"].lower() == cupcake_name.lower():
                return row


def write_csv(file_name, cupcakes):
    with open(file_name, 'w', newline="\n") as csvfile:
        fieldnames = ['size','name','price','flavor','frosting','sprinkles','filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({'size': cupcake.size ,'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'sprinkles': cupcake.sprinkles,'filling': cupcake.filling})
            else:
                writer.writerow({'size': cupcake.size ,'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'sprinkles': cupcake.sprinkles, 'filling': None})

def append_csv(file_name, cupcakes):
    with open(file_name, 'a', newline="\n") as csvfile:
        fieldnames = ['size','name','price','flavor','frosting','sprinkles','filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({'size': cupcake.size ,'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'sprinkles': cupcake.sprinkles,'filling': cupcake.filling})
            else:
                writer.writerow({'size': cupcake.size ,'name': cupcake.name,'price': cupcake.price,'flavor': cupcake.flavor,'frosting': cupcake.frosting,'sprinkles': cupcake.sprinkles, 'filling': None})

def add_cupcake_dictionary(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames= ['size','name','price','flavor','frosting','sprinkles','filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
        pprint(cupcake["name"] + ' added to csv')

def calculate_total(file):
    order_total = 0.0
    for cupcake in read_csv(file):
        order_total += float(cupcake['price'])
    return order_total




# display_1 = Mini('Small Fry', .89, 'vanilla', 'vanilla')
# display_2 = Mini('Teeny Cake', .89, 'vanilla', 'chocolate')
# display_3 = Mini('lil Coco', .89, 'chocolate', 'chocolate')
# display_5 = Regular('Average Joe', 1.49, 'vanilla', 'vanilla', None)
# display_4 = Regular('Main Attraction', 1.79, 'Chocolate', 'vanilla', 'vanilla')
# display_6 = Regular('Triple Chocolate', 1.79, 'chocolate', 'chocolate', 'chocolate')
# display_7 = Large('Big Chocolate', 2.99, 'chocolate', 'chocolate', 'chocolate')
# display_8 = Large('Cookies n Creme', 2.99, 'chocolate', 'Vanilla', None)
# display_9 = Large('Americas Cup', 2.99, 'Red Velvet', 'Vanilla', None)
# display_9.add_sprinkles('red', 'white', 'blue')
# display_3.add_sprinkles('brown')
# display_8.add_sprinkles('oreo crumbs')
# my_mini_cake = Mini('small fry', .89, 'vanilla', 'vanilla')
# my_cupcake = Mini("Cookies and Cream", 2.99, "Chocolate", "Oreo")
# my_cupcake.add_sprinkles('Oreo crumbs', 'chocolate', 'vanilla')
# display_cupcakes = [display_1,display_2,display_3,display_4,display_5,display_6,display_7,display_8,display_9]
# orders = []
# write_csv('current', display_cupcakes)
# pprint(read_csv('display.csv'))
# print(find_cupcake_csv('display.csv', 'lil Coco'))

