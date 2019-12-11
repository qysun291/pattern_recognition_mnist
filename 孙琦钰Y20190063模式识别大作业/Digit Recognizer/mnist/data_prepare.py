import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import os
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split


# Load the data
train = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")


Y_train = train["label"]

# Drop 'label' column
X_train = train.drop(labels = ["label"],axis = 1) 
X_test = test

# Normalize the data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Reshape image in 3 dimensions (height = 28px, width = 28px , canal = 1)
X_train = X_train.values.reshape(-1,28,28,1)
X_test = X_test.values.reshape(-1,28,28,1)

#Encoder labels to one hot vectors
Y_train = to_categorical(Y_train, num_classes = 10)

#Set the random seed
random_seed = 2
#Split the train and the validation set for fitting
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size = 0.1, random_state=random_seed)


 
# fig, ax = plt.subplots(
#     nrows=2,
#     ncols=5,
#     sharex=True,
#     sharey=True, )
 
# ax = ax.flatten()
# for i in range(10):
#     img = X_train[y_train == i][:,:,0]
#     ax[i].imshow(img, cmap='Greys', interpolation='nearest')
 
# ax[0].set_xticks([])
# ax[0].set_yticks([])
# plt.tight_layout()
# plt.show()