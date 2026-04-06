import pandas as pd
import numpy as np
from netCDF4 import Dataset

df = pd.read_csv("./tmdata_csv/tmdata_2026-03-24T20-20-56.csv", sep=",")
print(df.columns) 

nc_file = "tmdata.nc"
ds = Dataset(nc_file, "w", format="NETCDF4")
# Unlimited dimension for appending
ds.createDimension("time", None)

#Time variable
time_var = ds.createVariable("time", "f8", ("time",))
#time_var.units = "seconds since xxx UTC"

# Create data variables
# Add only columns you want and that are numeric
numeric_cols = []
for col in df.columns:
    if col != "tm_time_utc" and pd.api.types.is_numeric_dtype(df[col]):
        numeric_cols.append(col)
        var = ds.createVariable(col, "f4", ("time",), fill_value=np.nan)
        var.long_name = col

# Write numeric data
for col in numeric_cols:
    ds.variables[col][:] = df[col].to_numpy()

ds.close()