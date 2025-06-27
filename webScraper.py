import requests
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

    # Find headline elements (BBC uses <h3> for many headlines)
    for h in soup.find_all("h3"):
        text = h.get_text(strip=True)
        if text:
            headlines.append(text)

    # Save to file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(f"{line}\n")

    print("Headlines saved to 'headlines.txt'.")

except Exception as e:
    print("Error occurred:", e)
