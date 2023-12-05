from sklearn.utils import shuffle
import pandas as pd
from sklearn.linear_model import LinearRegression

def regress_performance( path, n ) :

    labels = ['democracy_eiu', 'elect_freefair_eiu', 'pol_part_eiu', 'dem_culture_eiu']

    res = {'democracy_eiu' : [],
            'elect_freefair_eiu' : [],
            'pol_part_eiu' : [],
            'dem_culture_eiu' : []
    }

    df_orig = pd.read_parquet(path)

    for i in range(n) :
        #print("try #" + str(i))

        df = shuffle( df_orig )

        df_train = df.sample( frac = 0.5 ).dropna()
        df_test = df.drop( df_train.index ).dropna()

        print("\n[iteration #" + str(i) + "]")

        for t in labels :
            # train
            model = LinearRegression()
            x = df_train[t].to_numpy().reshape(-1, 1)
            y = df_train['contributors_per_100k'].to_numpy().reshape(-1, 1)
            model.fit(x, y)

            x_test = df_test[t].to_numpy().reshape(-1, 1)
            y_test = df_test['contributors_per_100k'].to_numpy().reshape(-1, 1)

            '''
            print("score for" +
                  str(t) +
                  ":" +
                  str( model.score( x_test, y_test ) ) )
            '''
            score = model.score( x_test, y_test )

            res[t].append(score)
            print(t + ": r2=" + str(score))

    for t in labels:
        print("\n===============================================")
        print("Average for " + t + ":\n" + str( sum(res[t]) / len(res[t]) ))
