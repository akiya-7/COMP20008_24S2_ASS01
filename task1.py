def task1():

    import json
    import pandas as pd

    community = pd.read_csv('communities.csv')


    pop_density = community["Population Density"]
    community_amount = community.shape[0]

    output = {
        "Number of communities": community_amount,
        "Mean population density": pop_density.mean()
    }


    with open("task1_summary.json", "w") as outfile:
        json.dump(output, outfile)

    return

task1()
