def task3():
    import pandas as pd
    import matplotlib.pyplot as plt

    community = pd.read_csv('communities.csv')

    # Group by Suburb
    suburb_dataframe = community[["Community Name", "Population Density"]]
    # Group by Town
    town_dataframe = community[["LGA", "Population Density"]].copy
    town_dataframe = town_dataframe.groupby("LGA").sum()

    suburb_dataframe["Category"] = "Community Name"
    town_dataframe["Category"] = "LGA"

    # Rename the columns for consistency
    suburb_dataframe.rename(columns={"Community Name": "Name"}, inplace=True)
    town_dataframe.rename(columns={"LGA": "Name"}, inplace=True)

    # Concatenate the two DataFrames
    combined_df = pd.concat([suburb_dataframe, town_dataframe])
    # Create the boxplot
    plt.figure(figsize=(12, 6))
    boxplot = combined_df.boxplot(column="Population Density", by="Category", grid=False)

    return
