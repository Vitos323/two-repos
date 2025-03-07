
user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:
    user_choice = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
    computer_choice = random.choice(['камень', 'ножницы', 'бумага'])

    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
            (user_choice == 'ножницы' and computer_choice == 'бумага') or \
            (user_choice == 'бумага' and computer_choice == 'камень'):
        user_wins += 1
        print("Вы выиграли этот раунд!")
    else:
        computer_wins += 1
        print("Компьютер выиграл этот раунд!")

print(f"\nИтог игры: Вы {user_wins} - {computer_wins} Компьютер")

if user_wins == 3:
    print("Поздравляем! Вы победили в игре!")
else:
    print("Компьютер победил в игре.")
