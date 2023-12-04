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
    plt.savefig('../pngs/democracy_eiu')

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='pol_part_eiu',
           color='mediumpurple')
    plt.savefig('../pngs/pol_part_eiu')

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='dem_culture_eiu',
           color='palevioletred')
    plt.savefig('../pngs/dem_culture_eiu',)

    plt.figure()
    sb.regplot(order=2,
           data=df,
           y='contributors_per_100k',
           x='elect_freefair_eiu',
           color='coral')
    plt.savefig('../pngs/elect_freefair_eiu')

    plt.show()
