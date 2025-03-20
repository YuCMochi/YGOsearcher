# Yu-Gi-Oh Card Price Comparison Tool

A web application that helps users find the optimal purchasing combinations for Yu-Gi-Oh cards on the Ruten auction platform. The system compares prices across different sellers and generates purchase plans that minimize total costs, including shipping fees.

## Features

- Real-time card search with autocomplete
- Multi-card purchase optimization
- Price comparison across different sellers
- Shipping fee consideration
- Direct purchase links to seller pages
- Card database with fuzzy matching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ygosearcher.git
cd ygosearcher
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Search for cards using the search bar
4. Add desired cards to your purchase list
5. Click "Optimize Purchase" to generate optimal purchase plans
6. Follow the direct purchase links to make your purchases

## Project Structure

```
ygosearcher/
├── app.py              # Main Flask application
├── scraper.py          # Ruten auction scraping module
├── optimizer.py        # Purchase optimization logic
├── card_database.py    # Card database management
├── requirements.txt    # Python dependencies
├── data/              # Data directory
│   └── cards.json     # Card database file
└── templates/         # HTML templates
    ├── base.html      # Base template
    └── index.html     # Main page template
```

## Technical Details

### Backend
- Flask web framework
- Asynchronous web scraping with aiohttp
- Fuzzy matching for card names
- Purchase optimization algorithm

### Frontend
- Bootstrap 5 for responsive design
- jQuery for AJAX requests
- Dynamic card selection and removal
- Real-time price comparison display

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Yu-Gi-Oh! is a trademark of Konami Digital Entertainment Co., Ltd.
- Ruten is a trademark of PChome Online Inc. 