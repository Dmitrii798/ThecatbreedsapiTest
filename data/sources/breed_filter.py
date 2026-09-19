# data/sources/breed_filter.py

def filter_by_name(breeds: list, name: str) -> list:
    """Фильтрует породы по имени."""
    return [b for b in breeds if b.get("name") == name]


def limit_breeds(breeds: list, limit: int) -> list:
    """Ограничивает количество пород."""
    return breeds[:limit]
