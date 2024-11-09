import pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn

# download dataset
url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

# output info about dataset
movies_df.info()
print(movies_df.head())

print(movies_df.describe())


