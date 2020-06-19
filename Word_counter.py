from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

import pandas as pd
from pandas import DataFrame

f = open("Insert_text_here", "r")
data = f.read()
f.close()
word = data.split(" ")
num_word= len(word)

print ("there are " + str(num_word) + " words")
sortedlist = map(len,word)
countedlist = Counter(sortedlist)
print sortedlist
df = pd.DataFrame(countedlist.items(), columns=['letters', 'Frequency'])  # type: DataFrame
x = np.array(sorted(sortedlist))
hstd = np.std(x)
hmean = np.mean(x)
pdf = stats.norm.pdf(x,hmean,hstd)
plt.hist(x,normed=True)
plt.plot(x, pdf, '-o')
print ("standard deviation is " + str (hstd))
print ("mean is " + str(hmean))
print df
