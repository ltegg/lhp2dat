# ################
# refinement2csv.py
# ################
#
# by ltegg@live.com
# 2017-04-20
# Version 0.1.
#
# A python script which converts Excel/Sigma file generated by Rietica into a 
# *.csv for easy analysis.

print('Running refinement2csv.py...')

# Import relevant libraries
import glob # to search the pwd for *.lhp files
import numpy # to do numbers
import matplotlib.pyplot as pyplot # to make plots

reflist=glob.glob('*.refinement') # make a list of *.refinement files
reflist.extend(glob.glob('*refinement.txt')) # append a list of *.txt files
print('Found',len(reflist),'refinement files')

for file in reflist: # for all the files in the list...
    print(' - Converting',file,'... ',end='')
   
    fileopen=open(file) # open each file in the loop
    fileheader=fileopen.readline() # read just the headerline
            
    pattern=numpy.genfromtxt(file, # open the file
                          skip_header=1, # skip the first line
                          usecols=(0,1,2), # read only the first 3 columns
                          invalid_raise=False, # IGNORE lines with the wrong number of columns
                          loose=True, # don't raise errors for incorrect values
                          )
               
    peaks=numpy.genfromtxt(file, # open the file
                           skip_header=1, # skip the first line
                           usecols=(3,4), # read only the 4th and 5th columns
                           invalid_raise=False, # IGNORE lines with the wrong number of columns
                           loose=True, # don't raise errors for incorrect values
                           )
    
    thetadata=pattern[:,0] # the theta of the actual data and refinement
    data=pattern[:,1] # the experimental data
    refinement=pattern[:,2] # the refined pattern
    residual=data-refinement # the residual curve
    
    thetapeak=peaks[:,0]
    peakpos=peaks[:,1]
    
    peakshift = [-50000,0] # a multiplier, and a constant shift in the peak labels
    residualshift = -peakshift[0]*(max(peakpos)+2) # shift the residual curve down so that its nicely spaced with the peak list
    
    pyplot.figure(figsize=(10,6)) # figure, 10x8 inches
    
    pyplot.plot(thetadata,data,'.k',label='Data',markersize=2) # plot data points
    pyplot.plot(thetadata,refinement,'-r',label='Refinement',linewidth=0.5) # plot refinement
    pyplot.plot(thetadata,residual-residualshift,'-c',label='Residual',linewidth=0.5) # plot residual
    pyplot.plot(thetapeak,peakshift[0]*peakpos+peakshift[1],'|k',label='Peak Positions') # plot peak positions, spread out according to peakshift

    pyplot.xlim(numpy.floor(numpy.min(thetadata)/5)*5,numpy.ceil(numpy.max(thetadata)/5)*5) # set axis limits to data limits
       
    pyplot.title(file) # graph title is filename
    pyplot.xlabel(r'$2{\theta}   \  ({\degree})$') # very fancy latex
    pyplot.ylabel('Counts')
    pyplot.legend(loc='best')
    
    pyplot.savefig(file[0:-4]+'.png',dpi=200)
      
    print('Done!')

print('All done!')
