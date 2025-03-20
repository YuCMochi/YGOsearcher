from flask import Flask, render_template, request, jsonify
from scraper import RutenScraper
from optimizer import PurchaseOptimizer
from card_database import CardDatabase
import asyncio
import json

app = Flask(__name__)
scraper = RutenScraper()
optimizer = PurchaseOptimizer()
card_db = CardDatabase()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
async def search_cards():
    data = request.get_json()
    query = data.get('query', '')
    
    # Search card database for matches
    matches = card_db.search(query)
    
    # Get real-time prices from Ruten
    listings = await scraper.search_listings(query)
    
    return jsonify({
        'matches': matches,
        'listings': listings
    })

@app.route('/api/optimize', methods=['POST'])
async def optimize_purchase():
    data = request.get_json()
    cards = data.get('cards', [])
    
    # Get all listings for the selected cards
    all_listings = []
    for card in cards:
        listings = await scraper.search_listings(card['name'])
        all_listings.extend(listings)
    
    # Generate optimal purchase combinations
    optimal_plans = optimizer.generate_plans(cards, all_listings)
    
    return jsonify({
        'plans': optimal_plans
    })

if __name__ == '__main__':
    app.run(debug=True) 