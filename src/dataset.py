import pandas as pd

# Creating a dataframe

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Huston"],
}

df = pd.DataFrame(data)

df.head()

df = df.replace("Alice", "Alice Smith")

df.head()
