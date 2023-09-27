#%% Imports -------------------------------------------------------------------

import numpy as np
from skimage import io
from pathlib import Path

#%%

# 3DHistech
channel = "488"
data_path = "D:\\local_vEMTools\\data\\3DHistech\\"
image_name = "slide-2023-07-07T15-05-22-R1-S18"
zarr_path = Path(data_path, image_name + ".ome.zarr")

image = []
for path in Path(data_path, image_name + "_TIFF").iterdir():
    image.append(io.imread(path))
image = np.stack(image)
        
#%%

# Convert a ndarray to ome.zarr and display it with napari-ome-zarr

import zarr
import ome_zarr.reader
import ome_zarr.scale
import ome_zarr.writer

image = image[None, :, None] # tczyx   
scaler = ome_zarr.scale.Scaler()
mip = scaler.local_mean(image)
loc = ome_zarr.io.parse_url(zarr_path, mode="w")
group = zarr.group(loc.store)
ome_zarr.writer.write_multiscale(mip, group)

import napari
viewer = napari.Viewer()
viewer.open(zarr_path, plugin="napari-ome-zarr")

#%%

# Open ome.zarr extract on resolution level

loc = ome_zarr.io.parse_url(zarr_path, mode="r")
zarr_reader = ome_zarr.reader.Reader(loc).zarr
res = zarr_reader.load("3")

import napari
viewer = napari.Viewer()
viewer.add_image(res)

#%% 

# Next lazy computation with dask array
# https://gist.github.com/constantinpape/69e3cb8e0401621365d814b4d6fda0bchttps://gist.github.com/constantinpape/69e3cb8e0401621365d814b4d6fda0bc