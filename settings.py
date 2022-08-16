base_architecture = 'resnet50_inat' #'resnet50_inat' or 'resnet50'
img_size = 224
num_classes = 22
prototype_shape = (num_classes*10, 128, 1, 1) # first dimension needs to be a multiple of num_classes
prototype_activation_function = 'log'
add_on_layers_type = 'regular'

experiment_run = 'Bees_bbox'

data_path = '../../data/data_lstudio/'
train_dir = data_path + 'Bees_bbox' #'Bees_Christian_bbox_train_aug/'
test_dir = data_path + 'Bees_Christian_bbox' #'Bees_Christian_bbox_val/'
train_push_dir = data_path + 'Bees_bbox' #'Bees_Christian_bbox_train/'
train_batch_size = 64
test_batch_size = 16
train_push_batch_size = 64

# Learning rates for pretrained weights, extra conv. layers and proto layers
joint_optimizer_lrs = {'features': 1e-4,
                       'add_on_layers': 3e-3,
                       'prototype_vectors': 3e-3}

joint_lr_step_size = 5 # number of steps after which to divide lr by gamma (main.py, line 123)

# Learning rates during frozen epochs for extra conv. layers and proto layers
warm_optimizer_lrs = {'add_on_layers': 3e-3,
                      'prototype_vectors': 3e-3}

last_layer_optimizer_lr = 1e-4

coefs = {
    'crs_ent': 1,  # cross entropy
    'clst': 0.8,   # cluster cost
    'sep': -0.08,  # separation cost
    'l1': 1e-4,    # reg. term
}

num_train_epochs = 51
num_warm_epochs = 10 # number of frozen epochs

push_start = 5
push_epochs = [i + push_start for i in range(num_train_epochs) if i % 10 == 0] # in which epochs to learn projections (starts with 20)
