from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

#Get PDB(5681) historical price data from 2012 to 2015
start = dt(2012, 1, 1)
end = dt(2015, 1, 1)
data = DR("5681.KL", 'yahoo', start, end)

#Define a function for moving average
def moving_avg (values, days):
    weight=np.repeat(1.0, days)/days
    sma=np.convolve(values, weight,'valid')
    return sma

#Calculate 5-day moving average for PDB
closevalue = data['Close'].values #Use the closing value of PDB
ma= moving_avg(closevalue, 5)

#Plot 5-day moving average of PDB
number= len(ma)
t= p.linspace(0,number,number);
p.title('Moving average of 5 days closing price of PDB')
p.xlabel('Number of days, T')
p.ylabel('Average of stock price $')
p.plot(t,ma)
p.show()

#Find the correlation of PDB with FTSEKLCI
data_of_ftseklci= DR("^KLSE",'yahoo',start,end) #download FTSEKLCI data

x = ['5681.KL', '^KLSE']
PDB_klse_closevalue = DR(x, 'yahoo', start, end)['Close']

correlation_PDB_klci= PDB_klse_closevalue.corr()

print('Correlation of PDB with FTSEKLCI is \n ', correlation_PDB_klci)
