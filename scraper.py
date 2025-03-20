import aiohttp
import asyncio
from bs4 import BeautifulSoup
from typing import List, Dict
import json

class RutenScraper:
    def __init__(self):
        self.base_url = "https://www.ruten.com.tw/search/s000.php"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    async def search_listings(self, card_name: str) -> List[Dict]:
        """
        Search for card listings on Ruten
        """
        params = {
            'q': card_name,
            'type': 'direct',
            'sort': 'price_asc'
        }

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    html = await response.text()
                    return self._parse_listings(html)
                return []

    def _parse_listings(self, html: str) -> List[Dict]:
        """
        Parse the HTML response and extract listing information
        """
        soup = BeautifulSoup(html, 'html.parser')
        listings = []

        # Find all product items
        items = soup.find_all('div', class_='product-item')
        
        for item in items:
            try:
                listing = {
                    'title': item.find('h3', class_='product-title').text.strip(),
                    'price': self._extract_price(item.find('span', class_='price').text),
                    'seller': item.find('div', class_='seller-name').text.strip(),
                    'url': item.find('a')['href'],
                    'condition': item.find('div', class_='condition').text.strip() if item.find('div', class_='condition') else 'Unknown',
                    'shipping_fee': self._extract_shipping_fee(item)
                }
                listings.append(listing)
            except Exception as e:
                print(f"Error parsing listing: {e}")
                continue

        return listings

    def _extract_price(self, price_text: str) -> float:
        """
        Extract and convert price text to float
        """
        try:
            return float(price_text.replace('NT$', '').replace(',', '').strip())
        except:
            return 0.0

    def _extract_shipping_fee(self, item) -> float:
        """
        Extract shipping fee from listing
        """
        shipping_text = item.find('div', class_='shipping-fee')
        if shipping_text:
            try:
                return float(shipping_text.text.replace('運費', '').replace('NT$', '').strip())
            except:
                return 0.0
        return 0.0 