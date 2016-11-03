
# coding: utf-8

# In[2]:

# Using h5py to import HDF5 files

# Hierarchical Data Format (HDF) is a set of file formats (HDF4, HDF5) 
# designed to store and organize large amounts of data

# Import packages
import numpy as np
import h5py

# Assign filename: file
file ='LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)




# In[6]:

# Extracting data from your HDF5 file

# Import packages
import numpy as np
import matplotlib.pyplot as plt
import h5py

# Assign filename: file
file ='LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Get the HDF5 group: group
group= data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain= data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples=10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()


# In[18]:

# Importing MATLAB file

# Import package
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load Albeck gen expression data MATLAB file: mat
mat = scipy.io.loadmat('Albeck_gen_data.mat')

# Print the datatype type of mat
print(type(mat))

# Print the keys of the MATLAB dictionary
for key in mat.keys():
    print(key)

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()


