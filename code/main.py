import random
player_1 = random.randint(1,3)
player_2 = random.randint(1, 3)

if player_1 == 1: print("У первого - Камень")
if player_1 == 2: print("У первого - Ножницы")
if player_1 == 3: print("У первого - Бумага")
if player_2 == 1: print("У первого - Камень")
if player_2 == 2: print("У первого - Ножницы")
if player_2 == 3: print("У первого - Бумага")

if player_1 == player_2: print("Ничья")
if player_1 == 1 and player_2 == 2: print("Выиграл ПЕРВЫЙ")
if player_1 == 2 and player_2 == 3: print("Выиграл ПЕРВЫЙ")
