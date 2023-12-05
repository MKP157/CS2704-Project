import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

def mattplot( path ) :
    ###########################################################
    # Part 2 : Plot each table as regressions                 #
    ###########################################################

    df = pd.read_parquet(path)

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='democracy_eiu',
           color='cornflowerblue')
    plt.ylabel('GitHub Contributions per 100k Inhabitants')
    plt.xlabel('Overall Democracy Index')
    plt.title('Democracy Index (x) vs. GitHub Contributions per Capita (y)')
    plt.savefig('../pngs/democracy_eiu')

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='pol_part_eiu',
           color='mediumpurple')
    plt.ylabel('GitHub Contributions per 100k Inhabitants')
    plt.xlabel('Political Participation Index')
    plt.title('Political Partitipation Index (x) vs. GitHub Contributions per Capita (y)')
    plt.savefig('../pngs/pol_part_eiu')

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='dem_culture_eiu',
           color='palevioletred')
    plt.ylabel('GitHub Contributions per 100k Inhabitants')
    plt.xlabel('Democratic Culture Index')
    plt.title('Democratic Culture Index (x) vs. GitHub Contributions per Capita (y)')
    plt.savefig('../pngs/dem_culture_eiu',)

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='elect_freefair_eiu',
           color='coral')
    plt.ylabel('GitHub Contributions per 100k Inhabitants')
    plt.xlabel('Free and Fair Elections Index')
    plt.title('Free and Fair Elections Index (x) vs. GitHub Contributions per Capita (y)')
    plt.savefig('../pngs/elect_freefair_eiu')

    plt.show()
