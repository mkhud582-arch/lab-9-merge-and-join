import pandas as pd

def task_2(main_df, prices_df):
    inner_merged = pd.merge(main_df, prices_df, on="item_id", how="inner")
    print(inner_merged.head())
    print(inner_merged.shape)

    left_merged = pd.merge(main_df, prices_df, on="item_id", how="left")
    print(left_merged.head())
    print(left_merged.shape)


    right_merged = pd.merge(main_df, prices_df, on="item_id", how="right")
    print(right_merged.head())
    print(right_merged.shape)


    outer_merged = pd.merge(main_df, prices_df, on="item_id", how="outer")
    print(outer_merged.head())
    print(outer_merged.shape)

task_2(main_df, prices_df)

