# Astroinformatics I – Graded Practices

## Author
José Luis Ricra Mayorca

## Overview
This repository includes my graded practices for the Astroinformatics I course (Semester 1, 2025) at Universidad de Antofagasta.

## Contents
- Practice_1.pdf: Download and convert TESS light curves
- Files_practice_1: Folder with the files used in that practice 1.
- Practice_2.pdf: Preprocess files and classify stellar temperatures
- Files_practice_2: Folder with the files used in that practice 2.
- Practice_3.pdf: Plot light curves, detect outliers, and compute statistics
- Files_practice_3: Folder with the files used in that practice 3.
- Practice_4.pdf: GitHub submission, documentation, and test cases
- Files_practice_4: Folder with the files used in that practice 4.

## File Descriptions
For each practice there is a folder with the files used in that practice (mainly scripts).

Files_practice_1

    tesscurl_sector_73_lc.sh: Shell script to download light curves in FITS format
    
    lista.sh: Shell script to create a text file with the list of all files in CSV format
    
    dividir.sh: Shell script to split the contents of the csv_files.txt file into three text files

Files_practice_2

    spectral.py: Python script that takes the surface temperature of a star and returns the spectral type
    
    jd.py: Python script that takes the day, month, and year to calculate the Julian day

Files_practice_3 

    script_data.sh: Shell script to convert CSV data to LC format, extracting the time, flux, and flux error columns, and replacing the comma delimiter with spaces.
    
    plot.py: Plots light curves for visual inspection and comparison
    
    outliers.py: Identifies and flags outliers in flux values
    
    stat.py: Computes basic statistics (mean, std, min, max, etc.) from the light curve data  

Files_practice_4 

    test_cases.md: Describes test cases for each processing step to ensure reproducibility
    
    README.md: Description of the contents of the repository.

## How to Reproduce
You need:
- Python 3.10+
- NumPy and Matplotlib
- TOPCAT (for initial FITS → CSV conversion)

## License
This repository is for academic purposes only.
