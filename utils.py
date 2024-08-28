import os
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def readJson(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        data['train'] = {
            'input': [np.array(d['input'], dtype=np.int8) for d in data['train']],
            'output': [np.array(d['output'], dtype=np.int8) for d in data['train']],
        }
        data['test'] = {
            'input': [np.array(d['input'], dtype=np.int8) for d in data['test']],
            'output': [np.array(d['output'], dtype=np.int8) for d in data['test']],
        }
    return data

def readAllData(dir):
    train_file_names = [os.path.join(dir, file_name)
                        for file_name in os.listdir(dir)]
    return [readJson(file_name) for file_name in train_file_names]

cmap = ListedColormap(['#000000', '#0075d8', '#fe4036', '#2ecc40', '#ffdd01', '#ababaa', '#f113be', '#fe851a', '#7edbfe', '#860d25', ])

def show(img, ax=None):
    if ax:
        ax.imshow(img, cmap=cmap, norm=plt.Normalize(0, 9))
    else:
        plt.imshow(img, cmap=cmap, norm=plt.Normalize(0, 9))
        plt.show()