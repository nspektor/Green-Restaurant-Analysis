# Green Restaurant Analysis
<<<<<<< HEAD
=======
#### By: Nellie Spektor
#### Advisor: Professor Anasse Bari
>>>>>>> adfc9b1ad79ab5a44afab1f4a23e18ab4aa0335a

## Data Sources
- Yelp: https://www.yelp.com/dataset
    - Businesses and Reviews files downloaded from the link above
- Seafood Watch: https://www.seafoodwatch.org/
    - csv file provided by a representative of the organization containing their restaurant partners
- Green Restaurant Association: http://www.dinegreen.com/
    - csv file provided by a representative of the organization containing the restaurants they have rated

## Code
1. [json_to_csv.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts)
<<<<<<< HEAD
   - Imports: pandas
   - Converts JSON files downloaded from Yelp dataset challenge into csv files.    
2. [clean_yelp_businesses.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/clean_yelp_businesses.py)
    - Imports: pandas 
    - Removes unwanted columns and rows from yelp businesses csv file
        - Yelp data contains businesses in addition to restaurants,
         so we filter the categories column for these words: `['RESTAURANTS','BARS','FOOD','BREAKFAST & BRUNCH','DESSERTS','BAKERIES, DELIS, SANDWICHES', 'COFFEE & TEA', 'DINERS', 'CAFES']`
3. [clean_GRA_data.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/clean_GRA_data.py)
   - Imports: pandas
=======
   - Imports: pandas
   - Converts JSON files downloaded from Yelp dataset challenge into csv files.    
2. [clean_yelp_businesses.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/clean_yelp_businesses.py)
    - Imports: pandas 
    - Removes unwanted columns and rows from yelp businesses csv file
        - Yelp data contains businesses in addition to restaurants,
         so we filter the categories column for these words: `['RESTAURANTS','BARS','FOOD','BREAKFAST & BRUNCH','DESSERTS','BAKERIES, DELIS, SANDWICHES', 'COFFEE & TEA', 'DINERS', 'CAFES']`
3. [clean_GRA_data.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/clean_GRA_data.py)
   - Imports: pandas
>>>>>>> adfc9b1ad79ab5a44afab1f4a23e18ab4aa0335a
   - Removes unnecessary columns and standardizes text
4. [merge_GRA_with_yelp_restaurants.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/merge_GRA_with_yelp_restaurants.py)
    - Imports: pandas
    - Merges yelp business and review data into one pandas dataframe by combining the text from each review about a restaurant into one large block of text
    - Merges entries for separate locations of the same franchise into one row in our dataset. 
    - Added a column to indicate whether the restaurant appeared in the 
    lists we got from the Green Restaurant Association and Seafood Watch.
5. [environmental_term_analysis.py](https://github.com/nspektor/Green-Restaurant-Analysis/tree/master/pythonScripts/environmental_term_analysis.py)
    - Imports:  pandas, NLTK to pre-process review text
    - Create a green rating for each restaurant based on whether it’s reviews contains “environmental” terms. 
        - Examples of environmental terms: compost, recycle, green, local, vegan, vegetarian
        - If 1% or more of the total words in the reviews were environmental words, the restaurant got a score of 3, the rest got scores of 0, 1, or 2 but in our final dataset we only counted those with a score of 3 as “green”
<<<<<<< HEAD
=======

##### Note: This project stems partially from the NYU Big Data Science course project by Nellie Spektor, Valerie Angulo, and Andrea Waxman. This project can be seen [here](https://github.com/nspektor/Environmental-Consciousness-in-the-Restaurant-Business)
>>>>>>> adfc9b1ad79ab5a44afab1f4a23e18ab4aa0335a

##### This project stems partially from the NYU Big Data Science course project by Nellie Spektor, Valerie Angulo, and Andrea Waxman. This project can be seen [here](https://github.com/nspektor/Environmental-Consciousness-in-the-Restaurant-Business)
##### Nellie Spektor has since continued working on this project under Professor Anasse Bari






