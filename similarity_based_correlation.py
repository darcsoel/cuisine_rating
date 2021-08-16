import pandas as pd

cuisine = pd.read_csv('chefmozcuisine.csv', index_col='placeID')
rating = pd.read_csv('rating_final.csv')
geo_data = pd.read_csv('geoplaces2.csv')

x=0
