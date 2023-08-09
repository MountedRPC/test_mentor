import random

def get_user_city(previous_city):
    while True:
        user_city = input("Введите название города: ").strip().title()
        
        if not user_city.isalpha():
            print("Название города должно состоять только из букв.")
        elif user_city in used_cities:
            print("Этот город уже был назван.")
        elif user_city[0].lower() != previous_city[-1].lower():
            print(f"Город должен начинаться на букву '{previous_city[-1].upper()}'.")
        else:
            used_cities.add(user_city)
            return user_city

def get_computer_city(previous_city):
    last_letter = previous_city[-1].lower()
    for city in cities_list:
        if city[0].lower() == last_letter and city not in used_cities:
            used_cities.add(city)
            return city
    for city in cities_list:
        if city[0] not in used_cities:
            used_cities.add(city)
            return city
    return None


with open('cities.txt', 'r', encoding='utf-8') as file:
    cities_list = [line.strip() for line in file]

used_cities = set()
user_attempts = 5

print("Игра в города начинается!")
previous_city = random.choice(cities_list)

while user_attempts > 0:
    print(f"Предыдущий город: {previous_city}")
    user_city = get_user_city(previous_city)
    
    if user_city not in cities_list:
        print("Такого города нет в списке.")
        continue
    
    computer_city = get_computer_city(user_city)
    
    if computer_city:
        print(f"Компьютер: {computer_city}")
        previous_city = computer_city
    else:
        print("Компьютер не смог найти подходящий город.")
        print("Вы победили!")
        break
    
    user_attempts -= 1

if user_attempts == 0:
    print("У вас закончились попытки. Вы проиграли!")
