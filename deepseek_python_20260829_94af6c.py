import os
import sys
import time

def clear_screen():
    """Очищает экран терминала"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    """Выводит ASCII-арт"""
    art = r"""
                       /$$                               /$$                           /$$      
                      | $$                              | $$                          | $$      
  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$         /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$
 |____  $$| $$  | $$|_  $$_/   /$$__  $$       /$$_____/| $$__  $$ /$$__  $$ /$$_____/| $$  /$$/
  /$$$$$$$| $$  | $$  | $$    | $$  \ $$      | $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ 
 /$$__  $$| $$  | $$  | $$ /$$| $$  | $$      | $$      | $$  | $$| $$_____/| $$      | $$_  $$ 
|  $$$$$$$|  $$$$$$/  |  $$$$/|  $$$$$$/      |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
 \_______/ \______/    \___/   \______/        \_______/|__/  |__/ \_______/ \_______/|__/  \__/
                                                                                                
                                                                                                
                                                                                                
"""
    print(art)

def print_menu():
    """Выводит меню"""
    print("\n" + "="*50)
    print("[ 1 ] Проверить пк")
    print("[ 2 ] Почистить пк от читов")
    print("[ 3 ] Создатель")
    print("[ 4 ] Выход")
    print("="*50)

def check_pc():
    """Функция проверки ПК с задержками"""
    print("\nОткрываем папку game...")
    time.sleep(1)
    print("Проверяем папку mods...")
    time.sleep(1)
    print("Проверяем папку versions...")
    time.sleep(1)
    print("Проверяем папку config...")
    time.sleep(3)
    # Зеленый текст
    print("\033[92mНа вашем пк нету читов!\033[0m")
    input("\nНажмите Enter чтобы продолжить...")

def creator():
    """Показывает создателя"""
    clear_screen()
    print_ascii_art()
    print("\n" + "="*50)
    print("YukiKawaii")
    print("="*50)
    input("\nНажмите Enter чтобы выйти в главное меню...")

def main():
    """Главная функция"""
    while True:
        clear_screen()
        print_ascii_art()
        print_menu()
        
        choice = input("\nВведите ваш выбор: ").strip()
        
        if choice == "1":
            clear_screen()
            print_ascii_art()
            check_pc()
        elif choice == "2":
            # Ничего не происходит
            continue
        elif choice == "3":
            creator()
        elif choice == "4":
            print("\nВыход из программы...")
            time.sleep(1)
            sys.exit(0)
        else:
            print("\n\033[91mНеверный ввод! Попробуйте снова.\033[0m")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nВыход из программы...")
        sys.exit(0)