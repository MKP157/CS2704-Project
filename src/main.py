from convert import conv
import pandas as pd
import os

# Defines
CURRENT_DIR = os.getcwd()

###########################################################
#  Part 1 : Data Cleansing                                #
###########################################################
# Import EIU csv, convert to parquet, and filter for required columns
# Then query for years as a filter
conv('../data/eiu_cleaned.csv',
     'country_name',
     'year',
     'democracy_eiu',
     'elect_freefair_eiu',
     'pol_part_eiu',
     'dem_culture_eiu')

df_eiu = pd.read_parquet('../data/eiu_cleaned.parquet')

df_eiu = df_eiu.query("`year` == 2021")
print(df_eiu)

# Import GitHub csv, convert to parquet, and filter for countries and contributors
conv('../data/world_countries_2021.csv',
     'country',
     'contributors_per_100k')

df_git = pd.read_parquet('../data/world_countries_2021.parquet')
df_git = df_git.query("`country` != 'Montenegro'")

print(df_git)

df_joined = pd.merge(left = df_git,
                     right = df_eiu,
                     how="right",
                     left_on='country',
                     right_on='country_name')
print(df_joined)
###########################################################
# Part 2 : Plot each table as regressions                 #
###########################################################
import matplotlib.pyplot as plt
import seaborn as sb

plt.figure()
sb.regplot(order=2,
           data=df_joined,
           y='contributors_per_100k',
           x='democracy_eiu',
           color='cornflowerblue')

plt.figure()
sb.regplot(order=2,
           data=df_joined,
           y='contributors_per_100k',
           x='pol_part_eiu',
           color='mediumpurple')

plt.figure()
sb.regplot(order=2,
           data=df_joined,
           y='contributors_per_100k',
           x='dem_culture_eiu',
           color='palevioletred')

plt.figure()
sb.regplot(order=2,
           data=df_joined,
           y='contributors_per_100k',
           x='elect_freefair_eiu',
           color='coral')

plt.show()