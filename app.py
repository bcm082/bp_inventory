import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="BP Inventory Search", layout="wide")

# Add a title and description
st.title("BP Inventory Search")
st.write("Inventory is from before the migration to Veeqo.")
st.write("Search for items in the inventory by SKU or name")

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("bp_Inventory.csv")

df = load_data()

# Create search functionality
search_term = st.text_input("Enter search term (searches SKU and name):")

if search_term:
    # Filter data based on partial matches in SKU or name columns
    filtered_df = df[
        df['sku'].str.contains(search_term, case=False, na=False) | 
        df['name'].str.contains(search_term, case=False, na=False)
    ]
    
    # Display results count
    st.write(f"Found {len(filtered_df)} matching items")
    
    # Display results in a table
    if not filtered_df.empty:
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.info("No matching items found. Try a different search term.")
else:
    # Show all data when no search term is entered
    st.write(f"Total inventory items: {len(df)}")
    st.write("Enter a search term above to find specific items or browse the complete inventory below.")
    st.dataframe(df, use_container_width=True)

# Add some additional information
st.sidebar.header("About")
st.sidebar.info(
    """
    This app allows you to search through the BP inventory database.

    The inventory is from before the migration to Veeqo. 
    
    Enter a partial SKU or product name in the search box to find matching items.
    
    The search is case-insensitive and will find partial matches.
    """
)
