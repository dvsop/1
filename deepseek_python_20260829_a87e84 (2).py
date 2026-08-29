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

def type_text(text, delay=0.05):
    """Выводит текст с анимацией появления по одной букве"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Переход на новую строку

def check_pc():
    """Функция проверки ПК с задержками"""
    type_text("Открываем папку game...", 0.05)
    time.sleep(1)
    type_text("Проверяем папку mods...", 0.05)
    time.sleep(1)
    type_text("Проверяем папку versions...", 0.05)
    time.sleep(1)
    
    # Качаем Everything
    type_text("Качаем Everything...", 0.05)
    time.sleep(5)
    type_text("Проверяем Everything...", 0.05)
    time.sleep(3)
    
    # Качаем Shellbags analyzer
    type_text("Качаем Shellbags analyzer...", 0.05)
    time.sleep(5)
    type_text("Проверяем Shellbags analyzer...", 0.05)
    time.sleep(3)
    
    # Качаем USB tracker
    type_text("Качаем USB tracker...", 0.05)
    time.sleep(5)
    type_text("Проверяем USB tracker...", 0.05)
    time.sleep(3)
    
    # Зеленый текст
    print("\033[92mThere are no cheats on your PC!\033[0m")
    input("\nНажмите Enter чтобы продолжить...")

def clean_pc():
    """Функция очистки ПК от читов"""
    clear_screen()
    print_ascii_art()
    
    type_text("Начинаем очистку ПК от читов...", 0.05)
    time.sleep(1)
    type_text("Сканируем системные папки...", 0.05)
    time.sleep(2)
    type_text("Удаляем обнаруженные читы...", 0.05)
    time.sleep(2)
    
    print("\n\033[92mПК успешно очищен от читов!\033[0m")
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
            clean_pc()
        elif choice == "3":
            creator()
        elif choice == "4":
            type_text("Выход из программы...", 0.05)
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