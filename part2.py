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
    
    return main_df, prices_df
    
task1_load_explore()# write your code for part 2 here

# Import Pandas Library with alias pd 

import pandas as pd 

def task1_load_explore():

    # Read Both CSV Files using pd.read_csv()
    main_df = pd.read_csv("Data/modcloth_main.csv")
    prices_df = pd.read_csv("Data/modcloth_prices.csv")

    # Display First Five Rows Using .head()
    print(main_df.head())
    print(prices_df.head())

    # Display the Dimensions and Column names using .shape() and .column()

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
    
    return main_df, prices_df
    
task1_load_explore() 

def task2_merge_data(main_df, prices_df):
    pd.merge()


task2_merge_data()


def task3_analyze_merges():

task3_analyze_merges()