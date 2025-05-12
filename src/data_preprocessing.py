import pandas as pd
import numpy as np
import os

# Create folders if not exist
os.makedirs('data/processed', exist_ok=True)
os.makedirs('figures', exist_ok=True)

# Function to explore data
def explore_data(df, name):
    print(f"------------------------------- Exploring {name} -------------------------------")
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nSummary Statistics:\n{df.describe(include='all')}\n")
    print("\n")

# Load datasets
bid_df = pd.read_csv('data/raw/bids.csv')
train_df = pd.read_csv('data/raw/train.csv')
test_df = pd.read_csv('data/raw/test.csv')

# Explore data before processing
explore_data(bid_df, 'Bid Data')
explore_data(train_df, 'Train Data')
explore_data(test_df, 'Test Data')

# Merge datasets on common key:bidder_id
train_merged_df = pd.merge(train_df, bid_df, on='bidder_id', how='left')
test_merged_df = pd.merge(test_df, bid_df, on='bidder_id', how='left')

# Explore merged data
explore_data(train_merged_df, 'Merged Train Data')
explore_data(test_merged_df, 'Merged Test Data')

# Handle missing values
# The missing bid_id, auction, etc., likely happens because some bidders in train.csv or test.csv have no matching bids in bids.csv. (Meaning they never placed any bid.)
no_bid_cols = ['bid_id', 'auction', 'merchandise', 'device', 'time', 'ip', 'url']
for col in no_bid_cols:
    if train_merged_df[col].dtype == 'O':  # object type (string)
        train_merged_df[col] = train_merged_df[col].fillna('no_bid')
        test_merged_df[col] = test_merged_df[col].fillna('no_bid')
    else:  # numeric type (like bid_id, time)
        train_merged_df[col] = train_merged_df[col].fillna(-1)
        test_merged_df[col] = test_merged_df[col].fillna(-1)
# The missing country even when other bid fields exist likely means that the bidder's IP couldn’t be geolocated. So we can fill it with 'unknown'.
train_merged_df['country'] = train_merged_df['country'].fillna('unknown')
test_merged_df['country'] = test_merged_df['country'].fillna('unknown')
  
# Check for missing values again
print(f"\nMissing Values in Merged Train Data after cleaning:\n{train_merged_df.isnull().sum()}")
print(f"\nMissing Values in Merged Test Data after cleaning:\n{test_merged_df.isnull().sum()}")

# Arrange the time column to ascending order (per bidder_id)
train_merged_df.sort_values(by=['bidder_id', 'time'], inplace=True)
test_merged_df.sort_values(by=['bidder_id', 'time'], inplace=True)

# Print the first 5 rows of the cleaned data
print(f"\nFirst 5 rows:\n{train_merged_df.head()}")
print(f"\nFirst 5 rows:\n{test_merged_df.head()}")

# Save cleaned data
train_merged_df.to_csv('data/processed/cleaned_train.csv', index=False)
test_merged_df.to_csv('data/processed/cleaned_test.csv', index=False)

print("\nCleaned and sorted data saved to 'data/processed/' folder.")