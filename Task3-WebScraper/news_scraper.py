import requests
from bs4 import BeautifulSoup

# -----------------------------
# Step 1: Define Website URL
# -----------------------------
URL = "https://www.bbc.com/news"

# -----------------------------
# Step 2: Send HTTP Request
# -----------------------------
try:
    response = requests.get(URL)
    response.raise_for_status()  # Raises error if request fails
except requests.exceptions.RequestException as e:
    print("Error fetching the website:", e)
    exit()

# -----------------------------
# Step 3: Parse HTML Content
# -----------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -----------------------------
# Step 4: Extract Headlines
# -----------------------------
headlines = []

# BBC headlines are often inside <h2> tags
for heading in soup.find_all("h2"):
    text = heading.get_text(strip=True)
    if text and len(text) > 30:  # Filter small headings
        headlines.append(text)

# Remove duplicates
headlines = list(set(headlines))

# -----------------------------
# Step 5: Save Headlines to File
# -----------------------------
file_name = "headlines.txt"

with open(file_name, "w", encoding="utf-8") as file:
    for index, headline in enumerate(headlines, start=1):
        file.write(f"{index}. {headline}\n")

print(f"\n✅ Successfully saved {len(headlines)} headlines to '{file_name}'")
