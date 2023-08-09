class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class Book(Publication):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre
    
    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"

class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number
    
    def get_info(self):
        return f"{super().get_info()}, Issue Number: {self.issue_number}"

class Newspaper(Publication):
    def __init__(self, title, author, year, publisher):
        super().__init__(title, author, year)
        self.publisher = publisher
    
    def get_info(self):
        return f"{super().get_info()}, Publisher: {self.publisher}"

################################################################################# #2

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}"

class Product(Item):
    def __init__(self, name, price, brand, category):
        super().__init__(name, price)
        self.brand = brand
        self.category = category
    
    def get_brand(self):
        return self.brand

class Food(Product):
    def __init__(self, name, price, brand, category, expiry_date, weight):
        super().__init__(name, price, brand, category)
        self.expiry_date = expiry_date
        self.weight = weight
    
    def get_expiry_date(self):
        return self.expiry_date

class Beverage(Product):
    def __init__(self, name, price, brand, category, volume, carbonated):
        super().__init__(name, price, brand, category)
        self.volume = volume
        self.carbonated = carbonated
    
    def is_carbonated(self):
        return self.carbonated






