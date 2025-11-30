# Simple Search Engine

A lightweight Python-based search engine that indexes documents and enables fast text searching across multiple files.

## Features

- **Document Crawling**: Automatically reads and indexes all `.txt` files from a directory
- **Inverted Index**: Builds an efficient word-to-document mapping for fast lookups
- **Multi-token Search**: Search using multiple terms (space-separated)
- **Interactive CLI**: Query the search engine with a simple command-line interface

## Project Structure

```
simple_search/
├── README.MD
├── requirements.txt
├── data/
│   └── documents/          # Directory containing .txt files to index
│       ├── cooking_recipes.txt
│       ├── environmental_issues.txt
│       ├── financial_advice.txt
│       ├── health_tips.txt
│       ├── history_facts.txt
│       ├── music_review.txt
│       ├── programming_basics.txt
│       ├── science_news.txt
│       ├── tech_gadgets.txt
│       └── travel_guide.txt
└── src/
    ├── search.py           # Main search engine implementation
    └── test.ipynb          # Jupyter notebook for testing
```

## Usage

### Running the Search Engine

```bash
python src/search.py
```

This starts an interactive search session:
```
Enter search term (or 'exit' to quit): python programming
Documents found: {'Programming Basics', ...}
Enter search term (or 'exit' to quit): exit
```

### Using the Search Class Programmatically

```python
from src.search import Search

# Initialize with document directory
search = Search('data/documents')

# Perform a search
results = search.search('machine learning')
print(results)  # Returns list of matching document names
```

## How It Works

1. **Crawling**: The `crawl()` method scans the specified directory for all `.txt` files
2. **Indexing**: The `build_index()` method creates an inverted index mapping each word to documents containing it
3. **Searching**: The `search()` method finds documents matching all search terms

## Requirements

See `requirements.txt` for dependencies.

## Installation

```bash
pip install -r requirements.txt
```