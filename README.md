# BP Inventory Search App

A simple Streamlit application that allows you to search through the BP inventory database.

## Features

- Search by SKU or product name (partial matches supported)
- Case-insensitive search
- Displays matching results in a table
- Shows inventory count for each item

## Installation

1. Make sure you have Python installed (3.7 or higher recommended)
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Enter a search term in the search box
3. View the matching results in the table

## Data

The app uses the `bp_Inventory.csv` file which contains the following columns:
- sku: Product SKU/ID
- name: Product name/description
- inventory: Current inventory count
