"""
Top places by rating counts
"""


import pandas as pd

cuisine = pd.read_csv('chefmozcuisine.csv', index_col='placeID')
rating = pd.read_csv('rating_final.csv')

rating_grouped = rating.groupby('placeID').count()
rating_grouped.sort_values('rating', ascending=False, inplace=True)

top_rating = rating_grouped.head(10)

top_rating_with_place_type = top_rating.join(cuisine)
print(top_rating_with_place_type.head(10))
