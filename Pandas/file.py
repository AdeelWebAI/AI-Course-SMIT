

import pandas as pd

# data = [10, 20, 30, 40, 50]

# series = pd.Series(data, index = [ 'a', 'b', 'c', 'd', 'e'])

# print(series[0])


#------------- Data Frames--------------------



# data= {
#     "name": ["alice", "bob", "charlie", "david", "edward"],
#     "age": [25, 26, 27, 28, 29],
#     "sallary": [30000, 40000, 50000, 60000, 70000]
# }

# df = pd.DataFrame(data)


# df = pd.read_excel("data.xlsx")  # Load Excel file
# df = pd.read_json("data.json")  # Load JSON file
df = pd.read_csv("data.csv")  # Load CSV file

# df.to_csv("data.json", index=True)
# df.to_csv("data.xlsx", index=True)
# print(df)
# df.to_excel("output.xlsx", index=False)
# df.to_json("output.json")


#  -------------------data fram operations--------------------------------

#  basic inspection --------------------------------

# df = pd.read_csv("data.csv")  # Load CSV file

# print(df.head())  # print first 5 rows
# print(df.tail())  # print first 5 rows
# print(df.info())  # summary of data frame
# print(df.info())  # print first 5 rows
# print(df.describe())  # statistics of data frame
# print(df.shape)  # rows and columns count of data frame
# print(df.columns) # columns name of data frame
# print(df.dtypes) # dtype of each column


# selectng data --------------------------------
df = pd.read_csv("data.csv")  # Load CSV file

df[["Duration","Pulse"]]  # select column by name

df.iloc[0]       # First row (Index-based)
# df.loc[1]        # Row by label/index
# df.loc[df["Age"] > 30]  # Filtering rows





# print(df)





