from data_cleanup import cleanup
from data_plot import mattplot
from test_regress import regress_performance

path = '../data/final.parquet'

# Main Execution Script
cleanup()
mattplot(path)
regress_performance(path, 5000)
