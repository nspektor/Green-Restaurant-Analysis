# combine all green ratings with yelp data

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='small or big')
parser.add_argument("--small", default=False, type=bool, help="When true, run on smaller data")
args = parser.parse_args()
small = args.small

# Get the Yelp Restaurats and Reviews data
if small:
    restaurants_and_reviews_file = "../data/small_restaurants_and_reviews.csv"
    name_review_green_file = '../data/small_restaurants_reviews_ratings.csv'
    env_term_file = '../data/small_term_based_green_rating_results.csv'
    print("smallness achieved")
else:
    restaurants_and_reviews_file = "../data/big_restaurants_and_reviews.csv"
    name_review_green_file = '../data/big_restaurants_reviews_ratings.csv'
    env_term_file = '../data/big_term_based_green_rating_results.csv'
    print("we livin large")
restaurants_and_reviews = pd.read_csv(restaurants_and_reviews_file)

# Add in the GRA data
green = pd.read_csv('../data/clean_green.csv', header=0, delimiter=',')
green = green.sort_values(['Name'])
green = green[['Name', 'rating']]

green.rename(columns={"Name": "name", "rating": "GRA_rating"}, inplace=True)

# Add in the Seafood Watch Data
seafood = pd.read_csv('../data/original_sources/SeafoodWatch.csv')
seafood_restaurants = seafood.loc[seafood['PartnerTypes'] == 'Restaurant Partner']


def clean_str(r):
    idx = r.find('(')
    if idx != -1:
        return r[0:idx]
    else:
        return r


seafood = pd.DataFrame(seafood_restaurants['Title'].apply(lambda r: clean_str(r)).unique())
seafood.rename(index=str, columns={0: 'name'}, inplace=True)
seafood['rating'] = 1
seafood = seafood[['name', 'rating']]
seafood['name'] = seafood['name'].str.upper()
seafood.rename(columns={"rating": "seafood_rating"}, inplace=True)
# green = green.append(seafood, sort=True)
# # NO! we should add points for being in both not drop duplicates
# green.drop_duplicates(subset="name", inplace=True)

# Add in the env_term_analysis data
env_terms = pd.read_csv(env_term_file, header=0, delimiter=',')
env_terms.rename(columns={"term_based_green_rating": "term_based_rating"}, inplace=True)

# All together now
# print(restaurants_and_reviews.head(2))
# print(green.head(2))
# print(seafood.head(2))
name_review_green = restaurants_and_reviews.merge(green, left_on='name', right_on='name', how='left', suffixes=['_b', '_g'])
name_review_green = name_review_green[['name', 'review_text', 'stars', 'GRA_rating']]

name_review_green = name_review_green.merge(seafood, left_on='name', right_on='name', how='left', suffixes=['_b', '_g'])
name_review_green = name_review_green.merge(env_terms, left_on='name', right_on='name', how='left', suffixes=['_b', '_g'])
name_review_green.fillna(0, inplace=True)

name_review_green['overall_rating'] = name_review_green['GRA_rating'] + name_review_green['seafood_rating'] \
                                      + name_review_green['term_based_rating']
name_review_green = name_review_green.sort_values(['overall_rating'], ascending=False)


print("head of name_review_green\n", name_review_green.head(10))
name_review_green.to_csv(name_review_green_file)
