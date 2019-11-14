# Combine reviews with businesses
import pandas as pd

yelp_reviews = pd.read_csv('../data/original_sources/YelpReview.csv', header=0)
yelp_businesses = pd.read_csv('../data/clean_yelp_restaurants.csv', header=0)

# Yelp Business and Review Data
yelp_businesses = yelp_businesses.drop_duplicates(subset=['business_id'])
yelp_businesses['categories'] = yelp_businesses['categories'].str.replace(',', ' ')

yelp_reviews = yelp_reviews[['business_id', 'text']]
yelp_reviews['text'] = yelp_reviews['text'].str.replace(',', ' ')

yelp_reviews = yelp_reviews.groupby('business_id')['text'].apply(list).to_frame().reset_index()

# merge restaurants with their reviews
restaurants_and_reviews = yelp_businesses.merge(yelp_reviews, left_on='business_id', right_on='business_id',
                                                how='inner', suffixes=['_biz', '_test'])
restaurants_and_reviews = restaurants_and_reviews.groupby('name')['text'].apply(list).to_frame().reset_index()
restaurants_and_reviews = restaurants_and_reviews.sort_values(['name'])
restaurants_and_reviews.to_csv('../data/big_restaurants_and_reviews.csv', index=False)
small_businesses_and_reviews = restaurants_and_reviews.head(5000)
small_businesses_and_reviews.to_csv('../data/small_restaurants_and_reviews.csv', index=False)
