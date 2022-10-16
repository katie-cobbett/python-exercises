
# im[ort statements at the top
import pandas
import matplotlib.pyplot as plt 
import numpy as np

# The panda function should make excell readable :) 
###### something = pandas.read_excel(io="car-data.XLSX")
# wriiting pip instal _______ wil cuase the downloading of libraries 
# need to write pip instal pandas and pip instal matplotlib 
# it wil go up into the cloud and instal the stuff you want it to 

# as pd is a madeup nameand allows things to be called names 
# you instal two things with the same name. Here the AS is not actually needed
data = pandas.read_excel("car-data.XLSX", sheet_name="Car data")
# data is the variable name 
print (data)
engine_size = list(data["EngineSize"])
hydrocarbons = list(data["hc"])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(engine_size,hydrocarbons,marker="+",s=100,c="black")
plt.title("Excel sheet to Scatter Plot")
plt.xlabel("Engine Size cm^3")
plt.ylabel("Hydrocarbon Emissions g/km")
z=np.polyfit(engine_size,hydrocarbons,0.1)
p=np.poly1d(z)
plt.plot(engine_size, p(engine_size), color="purple", linewidth =3, linestyle="--")
plt.show()

