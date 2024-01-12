# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

best_math_schools = schools[schools["average_math"] >=  640][["school_name", "average_math"]].sort_values(by="average_math", ascending=False)

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

top_10_schools = schools[["school_name" ,"total_SAT"]].sort_values("total_SAT", ascending=False).head(10)

largest_std_dev = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).rename(columns={"count" : "num_schools", "mean" : "average_SAT", "std" : "std_SAT" }).round(2).sort_values("std_SAT", ascending= False).head(1)


# Add as many cells as you like...
