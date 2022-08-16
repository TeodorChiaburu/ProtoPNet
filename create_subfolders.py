"""Script to cut and paste images into subfolders corresponding to their classes (similar to CUB folder structure)"""

import glob, shutil, os

classes = ['Bombus_lapidarius',
'Bombus_lucorum',
'Bombus_pascuorum',
'Anthophora_plumipes',
'Andrena_fulva',
'Osmia_bicornis',
'Xylocopa_violacea',
'Andrena_flavipes',
'Osmia_bicolor',
'Bombus_hypnorum',
'Osmia_cornuta',
'Andrena_vaga',
'Bombus_sylvarum',
'Halictus_scabiosae',
'Bombus_pratorum',
'Dasypoda_hirtipes',
'Andrena_cineraria',
'Bombus_hortorum',
'Andrena_bicolor',
'Andrena_haemorrhoa',
'Sphecodes_albilabris',
'Anthidium_manicatum']

IMG_PATH = '../../data/data_lstudio/Bees_Christian_bbox/'

# Get jpg files
jpg_files = glob.glob(IMG_PATH + '*.jpg')

# Create empty folders with class names
for cls in classes:
    if not os.path.exists(IMG_PATH + cls):
        os.makedirs(IMG_PATH + cls)

# Copy files in their corresponding class subfolders
for f in jpg_files:

    # Get file name (not the whole path)
    file_name = f[f.rfind('/') + 1:]

    # Infer class from file name
    substrs = file_name.split('_')
    cls = substrs[0] + '_' + substrs[1]

    # Compress Bombuc lucorum
    if cls in ['Bombus_cryptarum', 'Bombus_magnus', 'Bombus_terrestris']:
        cls = 'Bombus_lucorum'

    # Cut and paste file in subfolder or copy it
    shutil.move(f, IMG_PATH + cls + '/' + file_name)
    #shutil.copy(f, IMG_PATH + cls + '/' + file_name)