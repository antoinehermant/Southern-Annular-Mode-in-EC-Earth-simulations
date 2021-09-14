#create netcdf from scratch using data in txt file

import netCDF4 as nc
import numpy as np

from numpy import loadtxt
data = loadtxt("/mnt/d/DMI/data/durville_mod.txt", comments="#", delimiter=",", unpack=False)

data = np.where(data == 99999, None, data)

year = data[:, 0]
data = np.delete(data, 0, 1)
#print (data)
#print (year)

n = len(data)
m = len(data[0])
#print (n, m)

data_line = np.zeros(shape=(n*m))
p = len(data_line)
#print (data_line, p)

i = 0
y = 0
k = 0
for y in range (n):
	tempo = data[y]
	for i in range(m):
		data_line[k] = tempo[i]
		k = k + 1
	i = 0




fn = '/mnt/d/DMI/data/test.nc'
ds = nc.Dataset(fn, 'w', format='NETCDF4')

ds.createDimension('time', None)
ds.createDimension('lat', 1)
ds.createDimension('lon', 1)

time = ds.createVariable('time', 'i4', 'time')
latitude = ds.createVariable('latitude', 'f4', 'lat')
longitude = ds.createVariable('longitude', 'f4', 'lon')
psl = ds.createVariable('psl', 'f4', ('time', 'lon', 'lat'))

psl.units = 'Pa'
psl.standard_name = 'air_pressure_at_mean_sea_level'
psl.long_name = 'Sea Level Pressure'
psl.comment = 'Sea Level Pressure at Dumont d Urville'

longitude.units = 'degrees east'
latitude.units = 'degrees north'
time.units = 'months since 1956-01-01'



latitude[0] = 66.7
longitude[0] = 140.0
time[:] = np.arange(1, (m*n + 1))

#print (data_line)
i = 0
t = 0
for t in range(n*m):
        psl[t,:,:] = data_line[i]
        i = i + 1
print (psl)

#from datetime import datetime
#today = datetime.today()
#time_num = today.toordinal()
#time[0] = time_num




ds.close()
