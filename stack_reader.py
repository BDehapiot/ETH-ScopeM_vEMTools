#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io
from pathlib import Path

#%% Paths ---------------------------------------------------------------------



# FIB-SEM_agb
data_path = "D:\\local_vEMTools\\data\\3DHistech\\"
image_name = "slide-2023-07-07T15-05-22-R1-S18"
zarr_path = Path(data_path, image_name + ".ome.zarr")