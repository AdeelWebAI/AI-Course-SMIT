
 1. Installation


First of all we have to initialize poetry virtual invironment

  -- poetry init

  after that we have to install pandas using the command

  -- poetry add pandas

  after that we can work in all the data structures in the pandas library of python for data preprocessing


  we will use this command to run this file using pandas in poetry invironment


  -- poetry run python (file).py


2. Core Data Structures

Creating a DataFrame:

  --> df = pd.read_excel("data.xlsx")  # Load Excel file
  --> df = pd.read_json("data.json")  # Load JSON file
  --> df = pd.read_csv("data.csv")  # Load CSV file

Saving Data:

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")


3. DataFrame Operations

a. basic inspection 


df.head()       # First 5 rows
df.tail()       # Last 5 rows
df.info()       # Summary of the DataFrame
df.describe()   # Statistical summary
df.shape        # Rows and columns count
df.columns      # List of column names
df.dtypes       # Data types of columns


b. Selecting Data


column Selecting


df["Duration"]       # Single column as Series
df[["Duration", "Pulse"]]  # Multiple columns as DataFrame

Rows Selecting

df.iloc[0]       # First row (Index-based)
df.loc[1]        # Row by label/index
df.loc[df["Age"] > 30]  # Filtering rows

Data Manipulation

a. Adding and Removing Columns

df["Bonus"] = df["Salary"] * 0.10  # Add new column
df.drop("Bonus", axis=1, inplace=True)

b. Adding and Removing Rows
