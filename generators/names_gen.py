# generators/names_gen.py
from faker import Faker

fake = Faker()


def generate_names(count: int = 100) -> list[str]:
    """
    Генерирует список имён (минимум 2 слова).
    Использует faker.
    """
    names = []
    while len(names) < count:
        name = fake.name()
        # Проверяем, что минимум 2 слова
        if len(name.split()) >= 2:
            names.append(name)
    return names
