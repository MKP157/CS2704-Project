import pandas as pd
def data_cleanup () :
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
    df_eiu.drop(columns=['year'])
    print(df_eiu)

    # Import GitHub csv, convert to parquet, and filter for countries and contributors
    conv('../data/world_countries_2021.csv',
         'country',
         'contributors_per_100k')

    # .dropna() helps remove NaN values. Important for regression calcs.
    df_git = pd.read_parquet('../data/world_countries_2021.parquet').dropna()

    # * Montenegro was an obvious outlier in the GitHub data.
    df_git = df_git.query("`country` != 'Montenegro'")

    print(df_git)

    df_joined = pd.merge(left = df_git,
                         right = df_eiu,
                         how="right",
                         left_on='country',
                         right_on='country_name')
    print(df_joined)
    df_joined.to_parquet('../data/final.parquet')


# Convert a CSV file to Parquet.
# First arg is path to CSV, all else are names of columns to include
def conv( *args ) :
    df = pd.read_csv(args[0]).dropna()
    df = df.filter(items=[x for x in args[1:]])
    df.to_parquet(args[0].split('.csv')[0] + '.parquet', compression='snappy')