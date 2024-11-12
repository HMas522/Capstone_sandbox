import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
def get_API_key():
    # Keep secrets in a .env file - load it, read the values.
    # Load environment variables from .env file
    load_dotenv()
    key = os.getenv("OPEN_FOOTBALL_API_KEY")
    return key


# Your API key from RapidAPI
api_key = get_API_key()
API_HOST = "api-football-v1.p.rapidapi.com"
API_URL = "https://api-football-v1.p.rapidapi.com/v3/standings"

# Mapping leagues to their respective league IDs (You can extend or modify this list)
LEAGUE_IDS = {
    "English Premier League": 39,
    "La Liga": 140,
    "Serie A": 135,
    "Bundesliga": 78,
    "Ligue 1": 61
}

# Function to fetch standings from the API
def get_standings(league_id):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": API_HOST
    }
    params = {
        "league": league_id,
        "season": 2024  # Modify this for the correct season if necessary
    }

    # Send GET request to API
    response = requests.get(API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        standings = data['response'][0]['league']['standings'][0]

        # Create a list of dictionaries for teams and their standings
        standings_list = []
        for team in standings:
            standings_list.append({
                "Rank": team['rank'],
                "Team": team['team']['name'],
                "Played": team['all']['played'],
                "Won": team['all']['win'],
                "Drawn": team['all']['draw'],
                "Lost": team['all']['lose'],
                "Points": team['points']
            })
        
        # Return the standings as a DataFrame
        return pd.DataFrame(standings_list)
    else:
        print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
        return None

# Function to save standings to CSV
def save_standings_to_csv(league_name, league_id, file_name):
    print(f"Fetching standings for {league_name}...")
    standings_df = get_standings(league_id)
    
    if standings_df is not None:
        # Write DataFrame to CSV
        standings_df.to_csv(file_name, index=False)
        print(f"Standings for {league_name} saved to {file_name}")
    else:
        print(f"Failed to fetch standings for {league_name}")

# Fetch and save standings for each league
for league_name, league_id in LEAGUE_IDS.items():
    # Generate a unique file name for each league's standings CSV
    file_name = f"{league_name.replace(' ', '_')}_standings.csv"
    save_standings_to_csv(league_name, league_id, file_name)
