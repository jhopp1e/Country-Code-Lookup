# country-code-lookup.py

from iso3166 import countries

# Manual mapping for alternative/formal names
ALT_NAMES = {
    "north korea": "KP",
    "democratic people's republic of korea": "KP",
    "dprk": "KP",
    "south korea": "KR",
    "republic of korea": "KR",
    "china": "CN",
    "people's republic of china": "CN",
    "prc": "CN",
    "united states": "US",
    "usa": "US",
    "united kingdom": "GB",
    "uk": "GB",
    "russia": "RU",
    "russian federation": "RU",
    "iran": "IR",
    "islamic republic of iran": "IR",
    "syria": "SY",
    "syrian arab republic": "SY",
    "vietnam": "VN",
    "socialist republic of vietnam": "VN",
    "venezuela": "VE",
    "bolivarian republic of venezuela": "VE",
}

def get_country_code(country_name: str) -> str:
    country_name_lower = country_name.strip().lower()

    if country_name_lower in ALT_NAMES:
        return ALT_NAMES[country_name_lower]

    try:
        return countries.get(country_name).alpha2
    except KeyError:
        return "Country not found."

if __name__ == "__main__":
    while True:
        user_input = input("Enter a country name (or 'exit' to quit): ")
        if user_input.strip().lower() == "exit":
            break
        code = get_country_code(user_input)
        print(f"Country code: {code}")
