import pandas as pd
def conv( *args ):
    df = pd.read_csv(args[0])
    df = df.filter(items=[x for x in args[1:]])
    df.to_parquet(args[0].split('.csv')[0] + '.parquet', compression='snappy')