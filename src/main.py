from data_cleanup import data_cleanup
from data_calc import mattplot
import test_regress

# Main Execution Script
data_cleanup()
mattplot('../data/final.parquet')
test_regress.regress_performance('../data/final.parquet', 1000)