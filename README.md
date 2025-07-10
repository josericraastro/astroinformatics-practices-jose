# Astroinformatics I – Graded Practices

## Author
José Luis Ricra Mayorca

## Overview
This repository includes my graded practices for the Astroinformatics I course (Semester 1, 2025) at Universidad de Antofagasta.

## Contents
- Practice 1: Download and convert TESS light curves
- Practice 2: Preprocess files and classify stellar temperatures
- Practice 3: Plot light curves, detect outliers, and compute statistics
- Practice 4: GitHub submission, documentation, and test cases

## File Descriptions
Practice 1 – Download and convert TESS light curves

    tesscurl_sector_73_lc.sh: Shell script to download light curves in FITS format
    
    lista.sh: Shell script to create a text file with the list of all files in CSV format
    
    dividir.sh: Shell script to split the contents of the csv_files.txt file into three text files

Practice 2 – Preprocess files and classify stellar temperatures

    spectral.py: Python script that takes the surface temperature of a star and returns the spectral type
    
    jd.py: Python script that takes the day, month, and year to calculate the Julian day

Practice 3 – Visualization and Analysis

    script_data.sh: Shell script to convert CSV data to LC format, extracting the time, flux, and flux error columns, and replacing the comma delimiter with spaces.
    
    plot.py: Plots light curves for visual inspection and comparison
    
    outliers.py: Identifies and flags outliers in flux values
    
    stat.py: Computes basic statistics (mean, std, min, max, etc.) from the light curve data  

Practice 4 – Documentation and Testing

    test_cases.md: Describes test cases for each processing step to ensure reproducibility

## How to Reproduce
You need:
- Python 3.10+
- NumPy and Matplotlib
- TOPCAT (for initial FITS → CSV conversion)

## License
This repository is for academic purposes only.
