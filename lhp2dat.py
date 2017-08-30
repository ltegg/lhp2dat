# ################
# lhp2dat.py
# ################
#
# by ltegg@live.com
# 2017-01-23
# Version 0.1
#
# A python script which
#   a) replaces all the '.' in a *.LHP file with spaces EXCEPT for the first 
#      three, and
#   b) saves the file with a .dat extension,
# so that the file can be opened by Rietica.

print('Running lhp2dat.py...')

# Import relevant libraries
import glob # to search the pwd for *.lhp files

# Find .lhp files
lhplist=glob.glob('*.lhp') # make a list of .lhp files
print('Found',len(lhplist),'.LHP files')

# Loop through all the .lhp files found
for file in lhplist:
    print(' - Converting',file,'... ',end='')
    oldstr=open(file) # open the file as a string
    newstr=oldstr.read().replace('.',',',3) # replace the first 3 '.' with ','
    newstr=newstr.replace('.',' ') # replace all the '.' with ' '
    newstr=newstr.replace(',','.') # replace all ',' with '.'
    newfile=open(file[0:len(file)-3]+'dat','w') # write a .dat file with the same basename as the .lhp
    newfile.write(newstr) # commit the new string to the new file
    newfile.close() # close the new file
    print('Done!')

print('All done!')