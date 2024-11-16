import pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import ast

# download dataset
url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

# output info about dataset
# movies_df.info()
# print(movies_df.head())

# print(movies_df.describe())


# ------------------------------------------

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre['name'] for genre in genres]
    except ValueError:
        return []

# print(movies_df['genres'])
movies_df['genres'] = movies_df['genres'].apply(extract_genres)

# print(movies_df['genres'])

# ----------------------------------------

movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')

movies_df.dropna(subset=['budget', 'revenue'], inplace=True)

# print(movies_df['budget'])
# print(movies_df['revenue'])


# --------------------------------

# print(movies_df['release_date'])
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
# print(movies_df['release_date'])

# ------------------------------------------------

