# Головний модуль для запуску програми
from addressbook import AddressBook
from record import Record
from utils import print_menu, get_input, validate_name, validate_phone

def main():
    book = AddressBook()

    while True:
        print_menu()
        choice = get_input("Оберіть опцію (наприклад, 1): ")

        if choice == '1':
            name = get_input("Введіть ім'я (наприклад, Олег): ")
            if not validate_name(name):
                print("Невірне ім'я. Ім'я повинно містити лише букви.")
                continue

            phone = get_input("Введіть телефон (наприклад, 0987654321): ")
            if not validate_phone(phone):
                print("Невірний номер телефону. Він повинен складатись з 10 цифр.")
                continue

            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            print(f"Контакт {name} додано!")

        elif choice == '2':
            name = get_input("Введіть ім'я для пошуку (наприклад, Олег): ")
            record = book.find(name)
            if record:
                print(record)
            else:
                print(f"Контакт {name} не знайдено.")

        elif choice == '3':
            name = get_input("Введіть ім'я (наприклад, Олег): ")
            record = book.find(name)
            if not record:
                print(f"Контакт {name} не знайдено.")
                continue

            old_phone = get_input("Введіть телефон, який бажаєте змінити (наприклад, 0987654321): ")
            if not record.find_phone(old_phone):
                print("Телефон не знайдено.")
                continue

            new_phone = get_input("Введіть новий телефон (наприклад, 0671234567): ")
            if not validate_phone(new_phone):
                print("Невірний номер телефону.")
                continue

            record.edit_phone(old_phone, new_phone)
            print(f"Телефон {old_phone} змінено на {new_phone} для контакту {name}.")

        elif choice == '4':
            name = get_input("Введіть ім'я для видалення (наприклад, Олег): ")
            if book.find(name):
                book.delete(name)
                print(f"Контакт {name} видалено.")
            else:
                print(f"Контакт {name} не знайдено.")

        elif choice == '5':
            print("Ваші контакти:")
            print(book)

        elif choice == '6':
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
