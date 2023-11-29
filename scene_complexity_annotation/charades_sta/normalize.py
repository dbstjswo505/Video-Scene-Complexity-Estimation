import json
import math

with open("./raw/train_data_redundancy.json", 'r') as fget:
    data = json.load(fget)

for i in range(len(data)):
    sce = data[i][-1]
    if sce > 5:
        nsce = 1.0
    else:
        nsce = round(sce*(0.1), 2)
    data[i][-1] = nsce

with open("./out_data/train_data_complexity.json", 'w') as fput:
    json.dump(data, fput)


with open("./raw/test_data_redundancy.json", 'r') as fget:
    data = json.load(fget)

for i in range(len(data)):
    sce = data[i][-1]
    if sce > 5:
        nsce = 1.0
    else:
        nsce = round(sce*(0.1), 2)
    data[i][-1] = nsce

with open("./out_data/test_data_complexity.json", 'w') as fput:
    json.dump(data, fput)

