import requests
import pandas as pd
import os
from pathlib import Path

# Параметры
url = "https://api.sportradar.com/nhl/trial/v7/en/league/2025/01/06/changes.json"
headers = {
    "accept": "application/json",
    "x-api-key": "CeXhos0BrVXkbashsgsFiGZyXct0CBnhNeeSQ1h6"
}

# Каталог для сохранения
output_dir = Path(__file__).resolve().parent / "changes"
output_dir.mkdir(parents=True, exist_ok=True)

# Отправляем запрос
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"❌ Error {response.status_code}: {response.text}")
    exit()

# Преобразуем ответ в JSON
data = response.json()
print(f"✅ Получено {len(data)} верхнеуровневых ключей")

# Обрабатываем каждую секцию
for key, value in data.items():
    try:
        if isinstance(value, list):
            print(f"📥 Обработка списка: '{key}'")
            df = pd.json_normalize(value)
            df.to_csv(output_dir / f"{key}.csv", index=False)
            print(f"✅ Сохранено: {key}.csv ({len(df)} строк)")

        elif isinstance(value, dict):
            print(f"📥 Обработка словаря: '{key}'")
            df = pd.json_normalize(value)
            df.to_csv(output_dir / f"{key}.csv", index=False)
            print(f"✅ Сохранено: {key}.csv")

        else:
            print(f"⚠️ Пропущен ключ '{key}' (тип: {type(value).__name__})")

    except Exception as e:
        print(f"❌ Ошибка при обработке '{key}': {e}")
