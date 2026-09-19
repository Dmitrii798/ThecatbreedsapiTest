# generators/string_gen.py
import random
import string


def generate_string(min_length: int = 12) -> str:
    """
    Генерирует строку с условиями:
    - минимум 10 символов
    - минимум 1 строчная буква
    - минимум 1 прописная буква
    - минимум 1 цифра
    - минимум 1 специальный символ
    """
    if min_length < 10:
        raise ValueError("min_length must be >= 10")

    specials = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Гарантированно добавляем по одному символу каждого типа
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(specials),
    ]

    # Добиваем до min_length случайными символами
    all_chars = string.ascii_letters + string.digits + specials
    chars.extend(random.choices(all_chars, k=min_length - len(chars)))

    # Перемешиваем
    random.shuffle(chars)
    return "".join(chars)
