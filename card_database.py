import json
from typing import List, Dict
from fuzzywuzzy import fuzz
import os

class CardDatabase:
    def __init__(self):
        self.cards = []
        self.load_database()

    def load_database(self):
        """
        Load card database from JSON file
        """
        try:
            with open('data/cards.json', 'r', encoding='utf-8') as f:
                self.cards = json.load(f)
        except FileNotFoundError:
            # Create default database if file doesn't exist
            self.cards = self._create_default_database()
            os.makedirs('data', exist_ok=True)
            with open('data/cards.json', 'w', encoding='utf-8') as f:
                json.dump(self.cards, f, ensure_ascii=False, indent=2)

    def search(self, query: str) -> List[Dict]:
        """
        Search for cards matching the query
        """
        if not query:
            return []

        matches = []
        query = query.lower()

        for card in self.cards:
            # Check exact matches first
            if query in card['name'].lower():
                matches.append(card)
                continue

            # Check aliases
            for alias in card.get('aliases', []):
                if query in alias.lower():
                    matches.append(card)
                    break

            # Check fuzzy matches if no exact match found
            if not matches:
                ratio = fuzz.ratio(query, card['name'].lower())
                if ratio > 80:  # 80% similarity threshold
                    matches.append(card)

        return matches[:10]  # Return top 10 matches

    def add_card(self, card_data: Dict):
        """
        Add a new card to the database
        """
        self.cards.append(card_data)
        self._save_database()

    def _save_database(self):
        """
        Save the current database to file
        """
        with open('data/cards.json', 'w', encoding='utf-8') as f:
            json.dump(self.cards, f, ensure_ascii=False, indent=2)

    def _create_default_database(self) -> List[Dict]:
        """
        Create a default card database with some common cards
        """
        return [
            {
                "name": "Blue-Eyes White Dragon",
                "aliases": ["BEWD", "Blue-Eyes", "青眼白龍"],
                "card_number": "89631139",
                "type": "Monster",
                "attribute": "Light",
                "level": 8,
                "race": "Dragon"
            },
            {
                "name": "Dark Magician",
                "aliases": ["DM", "黑魔導"],
                "card_number": "46986414",
                "type": "Monster",
                "attribute": "Dark",
                "level": 7,
                "race": "Spellcaster"
            },
            {
                "name": "Red-Eyes Black Dragon",
                "aliases": ["REBD", "Red-Eyes", "真紅眼黑龍"],
                "card_number": "74677422",
                "type": "Monster",
                "attribute": "Dark",
                "level": 7,
                "race": "Dragon"
            }
        ] 