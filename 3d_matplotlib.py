# practicing the matplotlib package 
# work not finalized 

from __future__ import absolute_import


import matplotlib.pyplot as plt 
from skimage import data 

from skimage import io 

import nibabel

from urllib import urlretrieve
import zipfile

import tempfile 
import os

astronaut = data.astronaut()
ihc = data.immunohistochemistry()
hubble = data.hubble_deep_field()

# create a temporary directory 
d = tempfile.mkdtemp()

# os.path.basename(u'https://www.google.com/attention.zip')

# initialize the subplot panels side by side 
fig, ax = plt.subplots(nrows=1, ncols=3)

# show an image in each subplot 
ax[0].imshow(astronaut)
ax[0].set_title(u'Natural image')
ax[1].imshow(ihc)
ax[1].set_title(u'Microscope image')
ax[2].imshow(hubble)
ax[2].set_title(u'Telescope image')


url = u'http://www.fil.ion.ucl.ac.uk/spm/download/data/attention/attention.zip'
# retrieve the data 
fn, info = urlretrieve(url, os.path.join(d, u'attention.zip'))

zipfile.ZipFile(fn).extractall(path=d)

#  list 10 first files
#[f.filename for f in zipfile.ZipFile(fn).filelist[:10]]

# read the image 
struct = nibabel.load(os.path.join(d, u'attention/structural/nsM00587_0002.hdr')
)


# get a plain NumPy array, without all the metadata 
# struct_arr = struct.get_data()

# struct_arr = io.imread(u"https://s3.amazonaws/com/assets.datacamp.com/blog_assets/attention-mri.tif")

# plt.imshow(struct_arr[75])


