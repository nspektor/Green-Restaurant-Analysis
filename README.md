# Green Restaurant Analysis
## Data Sources
- Yelp: https://www.yelp.com/dataset
    - Businesses and Reviews files downloaded from the link above
- Seafood Watch: https://www.seafoodwatch.org/
    - csv file provided by a representative of the organization containing their restaurant partners
- Green Restaurant Association: http://www.dinegreen.com/
    - csv file provided by a representative of the organization containing the restaurants they have rated
## Results
[Correlations](Correlations.png)
[Graph](Graph.png)

## To run any of the python scripts you must have the above data in `data/original_sources` in files named: 
- `YelpBusiness.csv` - generated by `json_to_csv.py` from json file downloaded from yelp
- `YelpReview.csv` - generated by `json_to_csv.py` from json file downloaded from yelp
- `GRA.csv`
- `SeafoodWatch.csv`

## Code
1. [json_to_csv.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts)
   - Imports: pandas
   - Converts JSON files downloaded from Yelp dataset challenge into csv files.    
2. [clean_yelp_businesses.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/clean_yelp_businesses.py)
    - Imports: pandas 
    - Removes unwanted columns and rows from yelp businesses csv file
        - Yelp data contains businesses in addition to restaurants,
         so we filter the categories column for these words: `['RESTAURANTS','BARS','FOOD','BREAKFAST & BRUNCH','DESSERTS','BAKERIES, DELIS, SANDWICHES', 'COFFEE & TEA', 'DINERS', 'CAFES']`
    - files required: `data/original_sources/YelpBusiness.csv`
    - files generated: `data/clean_yelp_restaurants.csv`
3. [clean_GRA_data.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/clean_GRA_data.py)
   - Imports: pandas
   - Removes unnecessary columns and standardizes text
   - files required: `data/original_sources/GRA.csv`
   - files generated: `data/clean_green.csv`
4. [merge_GRA_with_yelp_restaurants.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/merge_GRA_with_yelp_restaurants.py)
    - Imports: pandas
    - Merges yelp business and review data into one pandas dataframe by combining the text from each review about a restaurant into one large block of text
    - Merges entries for separate locations of the same franchise into one row in our dataset. 
    - Added a column to indicate whether the restaurant appeared in the 
    lists we got from the Green Restaurant Association and Seafood Watch.
   - files required:  `data/original_sources/YelpReview.csv`, 
                      `data/clean_yelp_restaurants.csv`, 
                      `data/original_sources/SeafoodWatch.csv`,
                      `data/clean_green.csv`
   - files generated: `data/big_restaurants_and_reviews.csv`, 
                      `data/small_restaurants_and_reviews.csv`,
                      `data/big_name_review_green.csv`,
                      `data/small_name_review_green.csv`
5. [environmental_term_analysis.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/environmental_term_analysis.py)
    - Imports:  pandas, NLTK to pre-process review text
    - Create a green rating for each restaurant based on whether it’s reviews contains “environmental” terms. 
        - Examples of environmental terms: compost, recycle, green, local, vegan, vegetarian
        - If 1% or more of the total words in the reviews were environmental words, the restaurant got a score of 3, the rest got scores of 0, 1, or 2 but in our final dataset we only counted those with a score of 3 as “green”
    - files required: `data/helper_files/environmentalTerms.txt`, 
                      `data/big_name_review_green.csv`, 
                      `data/small_name_review_green.csv`,
   - files generated: `data/big_term_based_green_rating_results.csv`, 
                      `data/small_term_based_green_rating_results.csv`,
                      `data/big_comprehensive_results.csv`,
                      `data/small_comprehensive_results.csv`
                      
## Plan
- Analyze current data from all green sources, compare with yelp stars as a success metric
- Run better stemming and lemmatization algorithms on the reviews and determine topics for green restaurant reviews and non green restaurant reviews. 
- Expand list of green restaurants by using more alternative data sources (such as blogs or web scraping)
- Use nyc open data in addition to yelp stars to measure if green restaurants are more successful

##### This project stems partially from the NYU Big Data Science course project by Nellie Spektor, Valerie Angulo, and Andrea Waxman. [here](https://github.com/nspektor/Environmental-Consciousness-in-the-Restaurant-Business)
##### Nellie Spektor has since continued working on this project under Professor Anasse Bari






