# data/sources/breed_dict.py

def breed_to_dict(breed) -> dict:
    """Преобразует объект Breed (или dict) в словарь."""
    if isinstance(breed, dict):
        return {
            "id": breed.get("id"),
            "name": breed.get("name"),
            "origin": breed.get("origin"),
        }
    return {
        "id": breed.id,
        "name": breed.name,
        "origin": breed.origin,
    }
