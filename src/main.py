from data_cleanup import data_cleanup
from data_calc import mattplot
import test_regress

path = '../data/final.parquet'

# Main Execution Script
data_cleanup()
mattplot(path)
test_regress.regress_performance(path, 5000)
