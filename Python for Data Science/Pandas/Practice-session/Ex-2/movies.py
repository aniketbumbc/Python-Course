import pandas as pd

movies_data = pd.read_csv('Movies.csv')

print(movies_data.head())

# 1.  1: How many rows and columns are present in the dataframe?

# print(movies_data.shape)

# 2. How many columns have null values present in them

# print(movies_data.isnull().any().value_counts())

# 3. What is the count of columns in the new dataframe? after drop

new_movies = movies_data.drop(['color',
                               'director_facebook_likes',
                               'actor_1_facebook_likes',
                               'actor_2_facebook_likes',
                               'actor_3_facebook_likes',
                               'actor_2_name',
                               'cast_total_facebook_likes',
                               'actor_3_name',
                               'duration',
                               'facenumber_in_poster',
                               'content_rating',
                               'country',
                               'movie_imdb_link',
                               'aspect_ratio',
                               'plot_keywords'], axis=1)

# print(new_movies.shape[1])

# 4 . Which column has the highest percentage of null values?

count_null_value = (movies_data.isnull().sum().sum())
count_null_column = (movies_data.isnull().sum())

# print(count_null_value)
# print(count_null_column)


# 5. you will see that it is safe to replace all the missing values with 'English'.

# movies_data['language'] = movies_data['language'].replace(['NaN'], 'English')
movies_data.loc[pd.isnull(movies_data['language']), ['language']] = 'English'


# print((movies_data['language'] == 'English').sum())

# 6 .  profit movie

movies_data['profit'] = movies_data['gross'] - movies_data['budget']
sort_movies = movies_data.sort_values(by=['profit'], ascending=False)
# sort_movies.columns.values
# print(sort_movies[['movie_title', 'profit']].head())

# 7 .  Suppose movies are divided into 5 buckets based on the IMDb ratings:

# https://jovian.com/ratan/practiceexercise2movies
