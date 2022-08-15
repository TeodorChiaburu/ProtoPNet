import sys
sys.path.append('../Augmentor')

import Augmentor
import os

datasets_root_dir = '../../data/data_lstudio/'
dir = datasets_root_dir + 'Bees_Christian_bbox_train/'
target_dir = datasets_root_dir + 'Bees_Christian_bbox_train_aug/'
# Note: There is a bug making Augmentor to fail if you try to save the files in './Bees_Christian_bbox_train_aug/'
# See https://github.com/mdbloice/Augmentor/issues/174
        
folders = [os.path.join(dir, folder) for folder in next(os.walk(dir))[1]]
target_folders = [os.path.join(target_dir, folder) for folder in next(os.walk(dir))[1]]
num_transforms = 2 # originally 10

for i in range(len(folders)):
    fd = folders[i]
    tfd = target_folders[i]
    
    # Rotation
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.rotate(probability=1, max_left_rotation=20, max_right_rotation=20)
    p.flip_left_right(probability=0.5)
    for i in range(num_transforms):
        p.process()
    del p

    # Brightness
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.random_brightness(probability=1, min_factor=0.5, max_factor=1.5)
    p.flip_left_right(probability=0.5)
    for i in range(num_transforms):
        p.process()
    del p

    # Shear
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.shear(probability=1, max_shear_left=10, max_shear_right=10)
    p.flip_left_right(probability=0.5)
    for i in range(num_transforms):
        p.process()
    del p