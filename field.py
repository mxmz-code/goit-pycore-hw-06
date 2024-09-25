# Модуль для роботи з полями контактів
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self._validate_phone(value):
            raise ValueError(f"Невірний номер телефону: {value}. Телефон повинен складатись з 10 цифр.")
        super().__init__(value)

    def _validate_phone(self, phone):
        # Перевірка на те, що номер телефону містить лише цифри та має 10 цифр
        return phone.isdigit() and len(phone) == 10
