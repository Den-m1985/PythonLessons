'''
python -m venv .folder
Создает папку куда будут устанавливатся pip
'''
#pip install progress  создает загрузчика в консоле в процентах или условных еденицах  при установке
from progress.bar import Bar
import time

bar = Bar('Processing', max=3)
for i in range(20):
    time.sleep(1)
    # Do some work
    bar.next()
bar.finish()


# pip install emoji

import emoji
print(emoji.emojize('Python is :thumbs_up:'))


#pip install matplotlib   Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()