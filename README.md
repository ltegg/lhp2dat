# lhp2dat
*A small set of .py scripts to convert X-ray diffraction patterns between the .LHP, .dat and.csv file formats.

## Description
Phillips X'Pert Data Collector can export diffraction pattern data in a number of file formats. One of this is the .LHP format, which is very similar in syntax to the .dat format used by the refinement program Rietica.

## Requirements
This repository contains Python (`.py`) scripts. All of the scripts were written using Python 3.6. Though each script differs slightly, the main libraries used are [numpy](http://www.numpy.org/), pyplot from [matplotlib](https://matplotlib.org/index.html), [glob](https://docs.python.org/3.5/library/glob.html), and [sys](https://docs.python.org/3.5/library/sys.html). These scripts were written using Spyder 3.1.x, using the Anaconda3 distribution.
    
## Installation
All of the scripts should work anywhere. Just download and unzip.

## Usage
The python scripts include code to search the present working directory (pwd) for the files it needs. For each file found, the relevant conversion will be performed, and the output file will be saved to the same pwd.

## Feedback
I've uploaded the scripts onto GitHub so that they may be shared, repurposed and edited freely. That said, if you find an issue with the scripts that you'd like to discuss or have fixed, you are welcome to submit a pull request or issue.
