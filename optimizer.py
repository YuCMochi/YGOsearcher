from typing import List, Dict
from itertools import combinations
import math

class PurchaseOptimizer:
    def __init__(self):
        self.max_sellers_per_plan = 3  # Limit the number of sellers per plan

    def generate_plans(self, cards: List[Dict], listings: List[Dict]) -> List[Dict]:
        """
        Generate optimal purchase plans for the given cards
        """
        # Group listings by seller
        seller_listings = self._group_by_seller(listings)
        
        # Generate all possible combinations of sellers
        seller_combinations = self._generate_seller_combinations(seller_listings)
        
        # Generate purchase plans
        plans = []
        for seller_combo in seller_combinations:
            plan = self._create_purchase_plan(cards, seller_combo)
            if plan:
                plans.append(plan)
        
        # Sort plans by total cost
        plans.sort(key=lambda x: x['total_cost'])
        
        return plans[:5]  # Return top 5 plans

    def _group_by_seller(self, listings: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Group listings by seller
        """
        seller_listings = {}
        for listing in listings:
            seller = listing['seller']
            if seller not in seller_listings:
                seller_listings[seller] = []
            seller_listings[seller].append(listing)
        return seller_listings

    def _generate_seller_combinations(self, seller_listings: Dict[str, List[Dict]]) -> List[List[str]]:
        """
        Generate combinations of sellers
        """
        sellers = list(seller_listings.keys())
        combinations_list = []
        
        for r in range(1, min(self.max_sellers_per_plan + 1, len(sellers) + 1)):
            combinations_list.extend(list(combinations(sellers, r)))
        
        return [list(combo) for combo in combinations_list]

    def _create_purchase_plan(self, cards: List[Dict], sellers: List[str]) -> Dict:
        """
        Create a purchase plan for the given cards and sellers
        """
        plan = {
            'sellers': [],
            'total_cost': 0,
            'cards': []
        }
        
        total_cost = 0
        remaining_cards = cards.copy()
        
        for seller in sellers:
            seller_plan = {
                'name': seller,
                'cards': [],
                'subtotal': 0,
                'shipping_fee': 0
            }
            
            # Find best matches for remaining cards from this seller
            for card in remaining_cards[:]:
                best_listing = self._find_best_listing(card, seller)
                if best_listing:
                    seller_plan['cards'].append({
                        'name': card['name'],
                        'price': best_listing['price'],
                        'url': best_listing['url']
                    })
                    seller_plan['subtotal'] += best_listing['price']
                    remaining_cards.remove(card)
            
            if seller_plan['cards']:
                # Add shipping fee for this seller
                seller_plan['shipping_fee'] = self._calculate_shipping_fee(seller_plan['subtotal'])
                plan['sellers'].append(seller_plan)
                total_cost += seller_plan['subtotal'] + seller_plan['shipping_fee']
        
        if remaining_cards:
            return None  # Could not find all cards
        
        plan['total_cost'] = total_cost
        return plan

    def _find_best_listing(self, card: Dict, seller: str) -> Dict:
        """
        Find the best listing for a card from a specific seller
        """
        # This would be implemented based on your specific requirements
        # For now, return the first matching listing
        return None

    def _calculate_shipping_fee(self, subtotal: float) -> float:
        """
        Calculate shipping fee based on subtotal
        """
        # This would be implemented based on Ruten's shipping fee rules
        # For now, return a fixed shipping fee
        return 60.0  # NT$60 fixed shipping fee 