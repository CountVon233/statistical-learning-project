import numpy as np
import pickle
import scipy
from pathlib import Path
from IO import read_in 
import run_PCA
import run_DL
import run_LR

relative_train_feature_path = "..\\..\\dataset\\train_feature.pkl"
relative_train_label_path = "..\\..\\dataset\\train_labels.npy"
relative_test_feature_path = "..\\..\\dataset\\test_feature.pkl"

TrainFeature, TrainLabel, TestFeature = read_in.read_file(relative_train_feature_path, relative_train_label_path, relative_test_feature_path)

target_dim = 233
run_PCA.run_pca(TrainFeature, TestFeature, target_dim)

train_x = np.random.rand(1000,2)
train_y = ((train_x[:,0] > train_x[:,1]) * 1).reshape(1000,1)

test_x = np.random.rand(1000,2)
test_y = ((test_x[:,0] > test_x[:,1]) * 1).reshape(1000,1)
# print(test_x)
# print(test_y.reshape(10,1))

# run_DL.run_py(test_x, test_y)
run_LR.run_lr(train_x, train_y, test_x, test_y)