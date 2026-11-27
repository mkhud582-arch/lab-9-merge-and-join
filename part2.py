# write your code for part 2 here

# Import Pandas Library with alias pd 

import pandas as pd 

def task1_load_explore():

    # Read Both CSV Files using pd.read_csv()
    main_df = pd.read_csv("Data/modcloth_main.csv")
    prices_df = pd.read_csv("Data/modcloth_prices.csv")

    # Display First Five Rows Using .head()
    print(main_df.head())
    print(prices_df.head())

    # Display the Dimensions and Column names using .shape and .column
    print("\nMain Dataset Dimension:\n", main_df.shape)
    print("\nMain Dataset Columns:\n", main_df.columns)

    print("\nPrices Dataset Dimensions:\n", prices_df.shape)
    print("\nPrices Dataset Columns:\n", prices_df.columns)

    # Use .info() to inspect data types and non-null values
    print("\nMain Dataset Information:")
    main_df.info()

    print("\nPrices Dataset Information:")
    prices_df.info()

    # Use .isna() to identify missing values
    identify_missing_values_main = main_df.isna().sum()
    identify_missing_values_prices = prices_df.isna().sum()

    print("\nMissing Values in Main Dataset:")
    print(identify_missing_values_main)

    print("\nMissing Values in Prices Dataset:")
    print(identify_missing_values_prices)

    # Identify the common column between both datasets 
    common_columns = main_df.columns.intersection(prices_df.columns) #arg take all of the columns in main_df and find the intersection of that to find the common column in the prices_df 

    print("\nCommon Columns:")
    print(common_columns)

    # Return the Modcloth Main and Modcloth Prices DataFrames
    return main_df, prices_df


def task2_merge_data(main_df, prices_df):

   
    # Perform an Inner Merge and display the first 5 rows and dimensions of the inner merge
    inner_merged = pd.merge(main_df, prices_df, on = "item_id", how = "inner")
    print("\nFirst Five Rows:", inner_merged.head())
    print("\nDimensions:", inner_merged.shape)

    # Perform a Left Merge and display the first 5 rows and dimensions of the left merge
    left_merged = pd.merge(main_df, prices_df, on = "item_id", how = "left")
    print("\nFirst Five Rows:", left_merged.head())
    print("\nDimensions:", left_merged.shape)

    # Perform a Right Merge and display the first 5 rows and dimensions of the right merge
    right_merged = pd.merge(main_df, prices_df, on = "item_id", how = "right")
    print("\nFirst Five Rows:", right_merged.head())
    print("\nDimensions:", right_merged.shape)

    # Perform an Outer Merge and display the first 5 rows and dimensions of the outer merge
    outer_merged = pd.merge(main_df, prices_df, on = "item_id", how = "outer")
    print("\nFirst Five Rows:", outer_merged.head())
    print("\nDimensions:", outer_merged.shape)
    print()

    # Return all four merge types
    return inner_merged, left_merged, right_merged, outer_merged



def task3_analyze_merges(merge_results):
    inner_merged, left_merged, right_merged, outer_merged = merge_results

    # Compare the dimensions of all four results using .shape

    print("Inner Merge Dimensions:", inner_merged.shape)
    print("Left Merge Dimensions:", left_merged.shape)
    print("Right Merge Dimensions:", right_merged.shape)
    print("Outer Merge Dimensions:", outer_merged.shape)

    # Identify missing values using .isna().sum()

    print("\nInner Merge Missing Values:")
    print(inner_merged.isna().sum())

    print("\nLeft Merge Missing Values:")
    print(left_merged.isna().sum())

    print("\nRight Merge Missing Values:")
    print(right_merged.isna().sum())

    print("\nOuter Merge Misssing Values:")
    print(outer_merged.isna().sum())

    # Identify records (rows) that exist in both datasets, only in the main dataset, or only in the prices dataset 

    both_datasets = inner_merged

    only_main_dataset = left_merged[left_merged["price"].isna()]

    only_prices_dataset = right_merged[right_merged["size"].isna()]

    print("\nRecords in Both Datasets:")
    print(both_datasets)

    print("\nNumber of records in Both Datasets:", len(both_datasets))

    print("\nRecords in the Main Dataset:")
    print(only_main_dataset)

    print("\nNumber of records Only in the Main Dataset:", len(only_main_dataset))

    print("\nRecords only in the Prices Dataset:")
    print(only_prices_dataset)

    print("Number of records Only in Price Dataset:", len(only_prices_dataset))


    # Return all four merged DataFrames and their analysis results
    return inner_merged, left_merged, right_merged, outer_merged, both_datasets, only_main_dataset, only_prices_dataset


if __name__ == "__main__":
    main_df, prices_df = task1_load_explore()
    merge_results = task2_merge_data(main_df, prices_df)
    task3_analyze_merges(merge_results)
