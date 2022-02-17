import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# 'D:\\Uppsala\\Sem2_Spr22\\ACA\\lab1\\avdark-cache\\json_data.json'
json_file = open('json_data.json')
data = json.load(json_file)

plt.figure(1)

df = pd.DataFrame(data)
pd.to_numeric(df.missRatio)

plt.plot(df[(df['cacheSize'] == 16384) & (df['associativity'] == 1)].blockSize, df[(df['cacheSize'] == 16384) & (df['associativity'] == 1)].missRatio, color = 'r', label="Size = 16384; assoc = 1")
plt.plot(df[(df['cacheSize'] == 16384) & (df['associativity'] == 2)].blockSize, df[(df['cacheSize'] == 16384) & (df['associativity'] == 2)].missRatio, color = 'r', label="Size = 16384; assoc = 2", linestyle = 'dashed')
plt.plot(df[(df['cacheSize'] == 32768) & (df['associativity'] == 1)].blockSize, df[(df['cacheSize'] == 32768) & (df['associativity'] == 1)].missRatio, color = 'g', label="Size = 32768; assoc = 1")
plt.plot(df[(df['cacheSize'] == 32768) & (df['associativity'] == 2)].blockSize, df[(df['cacheSize'] == 32768) & (df['associativity'] == 2)].missRatio, color = 'g', label="Size = 32768; assoc = 2", linestyle = 'dashed')
plt.plot(df[(df['cacheSize'] == 65536) & (df['associativity'] == 1)].blockSize, df[(df['cacheSize'] == 65536) & (df['associativity'] == 1)].missRatio, color = 'b', label="Size = 65536; assoc = 1")
plt.plot(df[(df['cacheSize'] == 65536) & (df['associativity'] == 2)].blockSize, df[(df['cacheSize'] == 65536) & (df['associativity'] == 2)].missRatio, color = 'b', label="Size = 65536; assoc = 2", linestyle = 'dashed')

plt.legend()
plt.show()

print(df)