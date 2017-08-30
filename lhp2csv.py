# ################
# lhp2csv.py
# ################
#
# by ltegg@live.com
# 2017-04-04
# Version 0.1
#
# A python script which converts a *.LHP file into a *.csv for easy analysis.

print('Running lhp2csv.py...')

# Import relevant libraries
import glob # to search the pwd for *.lhp files
import numpy # to do numbers
import matplotlib.pyplot as pyplot # import regular expressions to parse the first line

# Find .lhp files
lhplist=glob.glob('*.lhp') # make a list of .lhp files
print('Found',len(lhplist),'.LHP files')

# Loop through all the .lhp files found
for file in lhplist:
    print(' - Converting',file,'... ',end='')
    firstline=numpy.genfromtxt(file,max_rows=1) # get the first line of the lhp
    data=numpy.genfromtxt(file, # open the file
                          skip_header=1, # skip the first line
                          skip_footer=1, # skip the last line
                          usecols=(0,1,2,3,4,5,6,7,8,9), # use ten columns
                          delimiter='.', # columns separated by '.'
                          )
    
    datalastline=numpy.genfromtxt(file, # open the file
                                  skip_header=data.shape[0]+1 # skip all but the last line
                                 )
    
    data=numpy.reshape(data,data.shape[0]*data.shape[1]) # reorder into a 1D array
    datalastline=numpy.reshape(datalastline,datalastline.shape[0]) # reorder into a 1D array
       
    intensity=numpy.concatenate((data,datalastline)) # append the last line to the rest of the data
        
    theta=numpy.linspace(firstline[0],firstline[2],num=intensity.shape[0]) # calculate the 2theta range based on the first line, and the length of hte intensity vector
    
    csv=numpy.stack((theta,intensity),axis=1) # stack up theta and intensity 

    numpy.savetxt(file[0:-4]+'.csv',csv,fmt='%s',delimiter=',') # save the theta.intensity as a csv
    print('Done!')

print('All done!')