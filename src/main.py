from data_cleanup import cleanup
from data_plot import mattplot
import test_regress

path = '../data/final.parquet'

# Main Execution Script
cleanup()
mattplot(path)
test_regress.regress_performance(path, 1000)
