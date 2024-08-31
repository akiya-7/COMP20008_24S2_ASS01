def task2():
    import json
    import pandas as pd

    community = pd.read_csv('communities.csv')
    community_amount = community.shape[0]

    health_services = community[["Public Hospitals", "Private Hospitals", "Community Health Centres", "Allied Health"]]
    poorly_serviced = health_services.sum(axis=1) < 2
    poorly_serviced_amount = poorly_serviced.sum()

    poorly_serviced_percent = (poorly_serviced_amount / community_amount) * 100

    output = {
        "Percentage of suburbs poorly serviced": f"{poorly_serviced_percent:.2f}"
    }

    with open("task2_summary.json", "w") as outfile:
        json.dump(output, outfile)

    return
