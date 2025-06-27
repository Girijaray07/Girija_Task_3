import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    saved = False
    
    fileName = "headlines.txt"
    filePath = os.path.abspath(fileName)

    for h in soup.find_all(["h3", "title"]):
        text = h.get_text(strip=True)
        if text:
            headlines.append(text)

    with open(fileName, "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(f"{line}\n")

    print(f"Headlines saved to '{filePath}'.")

except Exception as e:
    print("Error occurred:", e)
