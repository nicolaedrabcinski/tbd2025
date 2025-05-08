import requests
import pandas as pd

# URL и заголовки
url = "https://api.sportradar.com/nhl/trial/v7/en/league/2025/01/06/changes.json"
headers = {
    "accept": "application/json",
    "x-api-key": "CeXhos0BrVXkbashsgsFiGZyXct0CBnhNeeSQ1h6"
}

# Запрос
response = requests.get(url, headers=headers)

# Проверка статуса
if response.status_code != 200:
    print(f"Error: {response.status_code} — {response.text}")
    exit()

# Преобразуем в JSON
data = response.json()
print(data)

for key, value in data.items():
    if isinstance(value, list):
        print(f"Found list in key: '{key}', saving as CSV...")
        df = pd.json_normalize(value)
        df.to_csv(f"{key}.csv", index=False)
        print(f"Saved {key}.csv ({len(df)} rows)")
    elif isinstance(value, dict):
        print(f"Found nested dict in key: '{key}', flattening and saving...")
        df = pd.json_normalize(value)
        df.to_csv(f"{key}.csv", index=False)
        print(f"Saved {key}.csv")
    else:
        print(f"Skipping non-list/dict key: '{key}'")

# Например, сохраняем только список игр
# if "games" in data:
#     games_df = pd.json_normalize(data["games"])
#     games_df.to_csv("nhl_changes_2025_01_06.csv", index=False)
#     print("Saved to nhl_changes_2025_01_06.csv")
# else:
#     print("No 'games' field found in response")
