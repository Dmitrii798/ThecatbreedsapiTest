# scripts/generate_names_file.py
import sys
import os
from pathlib import Path

# Добавляем корень проекта в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.names_gen import generate_names

# Создаём папку data, если её нет
os.makedirs("data", exist_ok=True)

names = generate_names(100)

with open("data/names.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(names))

print(f"✅ Saved {len(names)} names to data/names.txt")
print(f"📄 First 5 names:")
for name in names[:5]:
    print(f"   - {name}")
   