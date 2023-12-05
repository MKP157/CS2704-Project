import math

import numpy as np
import pandas as pd
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle

# Constant data
labels = ['democracy_eiu', 'elect_freefair_eiu', 'pol_part_eiu', 'dem_culture_eiu']

def regress_performance( path, n ) :

    res = {'democracy_eiu' : [],
            'elect_freefair_eiu' : [],
            'pol_part_eiu' : [],
            'dem_culture_eiu' : []
    }

    df_orig = pd.read_parquet(path)

    for i in range(n) :
        df = shuffle( df_orig )
        df_train = df.sample( frac = 0.5 ).dropna()
        df_test = df.drop( df_train.index ).dropna()

        spacing = " " * (int)((math.cos((i/(60*math.pi))+math.pi)+1)*10*math.pi)
        print(f"{spacing}[]   Iteration #{i:5d}...   []")
        for l in labels :
            # train
            model = LinearRegression()
            x = df_train[l].to_numpy().reshape(-1, 1)
            y = df_train['contributors_per_100k'].to_numpy().reshape(-1, 1)
            model.fit(x, y)

            x_test = df_test[l].to_numpy().reshape(-1, 1)
            y_test = df_test['contributors_per_100k'].to_numpy().reshape(-1, 1)

            score = model.score( x_test, y_test )
            res[l].append(score)
            #print(f"{l}: r2={score:.6f}")

    for l in labels:
        print(f"\n[Scores for {l}]")
        print(f"\t-> R-Squared = {sum(res[l]) / len(res[l]):.6f}")
        print(f"\t-> P-Value   = {regress_get_p(df_orig, l)}")


def regress_characteristics( path ) :
    df = pd.read_parquet(path).dropna()

    for col in labels :
        model = generate_linreg(df[col], df['contributors_per_100k'])
        print_linreg(col, model)

def regress_get_p( df, col ) :
    df = df.dropna()
    model = generate_linreg(df[col], df['contributors_per_100k'])
    return model.pvalue

def generate_linreg( x_col, y_col ) :
    x = x_col.to_numpy().reshape(-1, 1)
    y = y_col.to_numpy().reshape(-1, 1)

    x = x[:, 0]
    y = y[:, 0]

    model = linregress(x, y)
    return model

def print_linreg( l, model ) :
    print(f"\n[Regression on {l}]")
    print(f"P-Value   : {model.pvalue}")
    print(f"Slope     : {model.slope:.6f}")
    print(f"Std error : {model.stderr:.6f}")
