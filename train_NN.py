import numpy as np
import matplotlib.pyplot as plt
import tables

import image_lib

# Read training images into array of shape (80, 200, 200, 1)
IMSIZE=200
train_data_onedimension = np.array([]) #np.empty([80,200,200,1])
train_labl_onedimension = np.array([])
for dataset in range(1, 9):
    for img_counter in range(1, 11):
        dataset_str = str(dataset).zfill(3)
        image_str = str(img_counter).zfill(4)
        # Samples
        filename = "data001/move" + \
                dataset_str+"_"+image_str+".gif"
        #print filename
        img, a = image_lib.image_2_array(filename)
        
        train_data_onedimension = np.append(train_data_onedimension, a)
        # Targets (labels)
        filename = "data001/move_inv_" + \
                dataset_str+"_"+image_str+".gif"
        #print filename
        img,a = image_lib.image_2_array(filename)
        train_labl_onedimension = np.append(train_labl_onedimension, a)
        
        
print train_data_onedimension.shape
print train_labl_onedimension.shape

images_in_set = train_data_onedimension.size / (IMSIZE*IMSIZE)
print images_in_set
train_data = train_data_onedimension.reshape(images_in_set, IMSIZE, IMSIZE, 1)
print train_data.shape
train_labl = train_labl_onedimension.reshape(images_in_set, IMSIZE, IMSIZE, 1)
print train_labl.shape

