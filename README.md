# Country Code Lookup

A simple Python script to look up the ISO 3166-1 alpha-2 country code for a given country name. This script supports both standard country names and a set of alternative or formal names through manual mappings.

## Features

- Retrieves official ISO 3166-1 alpha-2 country codes
- Supports common alternative names (e.g., "USA", "UK", "PRC", etc.)
- Interactive prompt for repeated lookups
- Graceful error handling for unrecognized countries

## Requirements

- Python 3.6 or higher
- `iso3166` Python package

You can install the required package using pip:

```bash
pip install iso3166
```

## Usage

Run the script directly from the command line:

```bash
python country-code-lookup.py
```

You will be prompted to enter a country name:

```bash
Enter a country name (or 'exit' to quit): United States
Country code: US

Enter a country name (or 'exit' to quit): DPRK
Country code: KP

Enter a country name (or 'exit' to quit): exit
```

## Supported Alternative Names

This script includes manual support for alternative or formal country names, such as:

- "USA" → US
- "United Kingdom" / "UK" → GB
- "PRC" / "People's Republic of China" → CN
- "DPRK" / "North Korea" → KP
- "Russian Federation" → RU
- ...and more
