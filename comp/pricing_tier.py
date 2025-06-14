import pandas as pd

def get_pricing_tiers():
    # Load data from the specified file path
    data_file = "data/Competitor Pricing Tier Percept.csv"  # Use your provided file path
    df = pd.read_csv(data_file)

    # Ensure 'Price per 100g (INR)' is numeric, handling any non-numeric values
    df['Price per 100g (INR)'] = pd.to_numeric(df['Price per 100g (INR)'], errors='coerce')

    # Set Haldiram's price per 100g (you may need to extract from the dataset or hardcode)
    haldiram_row = df[df['Brand'] == "Haldiram's"]
    if not haldiram_row.empty:
        haldiram_price_per_100g = haldiram_row['Price per 100g (INR)'].iloc[0]
    else:
        return {"error": "Haldiram's data not found in the dataset."}

    # Define a function to categorize pricing tier relative to Haldiram
    def categorize_pricing(row):
        price_per_100g = row['Price per 100g (INR)']
        
        if price_per_100g >= 1.5 * haldiram_price_per_100g:
            return 'Premium'
        elif 0.75 * haldiram_price_per_100g <= price_per_100g < 1.5 * haldiram_price_per_100g:
            return 'Mid-Range'
        else:
            return 'Economy'

    # Apply the categorization function to all competitors
    df['Pricing Tier'] = df.apply(categorize_pricing, axis=1)

    # Create the final table to display competitor pricing tiers
    final_table = df[['Brand', 'Product', 'Size', 'Price (INR)', 'Price per 100g (INR)', 'E-commerce Platform', 'Pricing Tier']]

    return final_table.to_dict(orient="records")