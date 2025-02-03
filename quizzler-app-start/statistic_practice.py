import statistics
from tracemalloc import Statistic

data_str = '''45  45  45  45  45    45  45  45  44  43 
43  43  41  41  39    38  38  38  37  37 
37  35  35  34  33    32  31  29  29  28
28  27  25  25  25    24  24  22  21  20
11   9    9    8    7       6     0'''

data = data_str.split()
int_data =[int(number) for number in data]

print(statistics.mean(int_data))
print(statistics.median(int_data))



