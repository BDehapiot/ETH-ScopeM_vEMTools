#%% Imports -------------------------------------------------------------------

import tifffile
import numpy as np
from skimage import io
from pathlib import Path

#%% Parameters ----------------------------------------------------------------

# Paths
stack_name = "WS_agb-02" 
# stack_name = "SEM_singles_agb-01"  
data_path = "D:\\local_vEMTools\\data\\"

#%% Initialize ----------------------------------------------------------------

from natsort import natsorted, index_natsorted

img_names, img_shapes = [], []
for path in Path(data_path, stack_name).iterdir():
    if path.suffix == ".tif":
        img_names.append(path.name)
        with tifffile.TiffFile(path) as tif:
            img_shapes.append(tif.pages[0].shape)
        
order = index_natsorted(img_names)
sorted_other_list = [other_list[i] for i in order]

# # Open stack
# stack = []
# img_shapes = set()
# for path in Path(data_path, stack_name).iterdir():
#     if path.suffix == ".tif":
#         img = io.imread(path)
#         img_shapes.add(img.shape)
#         stack.append((path.name, img))
        
# # Correct image shapes
# y_max = np.max([shape[0] for shape in img_shapes])
# x_max = np.max([shape[1] for shape in img_shapes])
# for i in range(len(stack)):
#     y, x = stack[i].shape
#     if y < y_max:
#         stack[i] = np.vstack((stack[i], np.zeros((y_max - y, x), dtype=int))) 
#     y, x = stack[i].shape
#     if x < x_max:
#         stack[i] = np.hstack((stack[i], np.zeros((y, x_max - x), dtype=int))) 

#%% Display -------------------------------------------------------------------

# import napari
# viewer = napari.Viewer()
# viewer.add_image(np.stack(stack))
    