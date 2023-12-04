from data_cleanup import data_cleanup
from data_calc import mattplot
from test_regress import regress

# Main Execution Script
data_cleanup()
mattplot('../data/final.parquet')
regress('../data/final.parquet', 1000)