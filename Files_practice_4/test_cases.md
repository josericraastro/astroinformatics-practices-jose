# Test Cases for Processing TESS Light Curves

This section outlines test cases designed to validate the individual steps involved in the processing of TESS light curve data, as implemented across Graded Practices 1–3.

---

## Test Case 1 (Practice 1): FITS to CSV Conversion

**Objective:** 
Verify that TESS FITS files are correctly converted to CSV format using TOPCAT.

**Input:** 
A TESS FITS file (e.g. `tess2023341045131-s0073-0000000001750268-0268-s_lc.fits`)

**Procedure:** 
Open the FITS file in TOPCAT → Export as CSV

**Expected Output:** 
A CSV file containing columns such as `TIME`, `PDCSAP_FLUX`, `PDCSAP_FLUX_ERR`, and other relevant metadata.

**Pass Criteria:** 
- The number of rows remains unchanged 
- Data types and column names are preserved 
- File is readable by other processing tools

---

## Test Case 2 (Practice 3): Extract relevant columns from CSV data

**Objective:** 
Verify that only the relevant light curve columns (TIME, FLUX and FLUX ERROR) are extracted, replaces commas with whitespace accurately

**Input:** 
Files `data*.csv` containing lines such as: 
`TIME,...,PDCSAP_FLUX,PDCSAP_FLUX_ERR, ...` 

**Procedure:** 
Run: `script_data.sh`

**Expected Output:** 
Files `col_data*_flux.lc` containing exactly three columns: `TIME`, `PDCSAP_FLUX` and `PDCSAP_FLUX_ERR` separated by spaces.

**Pass Criteria:** 
- All commas are replaced with single spaces 
- Output file contains three columns (TIME, FLUX and FLUX ERROR) 
- The format of the files is changed from csv to lc

---

## Test Case 3 (Practice 3): Plotting a Light Curve

**Objective:** 
Confirm that the plotting script produces clear and accurate flux vs. time graphs.

**Input:** 
A `.lc` file with three numerical columns: `TIME`, `FLUX` and `FLUX ERROR`

**Procedure:** 
Run: `plot.py` using Matplotlib

**Expected Output:** 
A plot saved as `.pdf` showing a labeled time-series of the light curve

**Pass Criteria:** 
- Axes are labeled correctly 
- Data points match original flux values 
- No runtime errors occur

---

## Test Case 4 (Practice 3): Outlier Detection

**Objective:** 
Validate the outlier detection mechanism based on the 4σ-from-median rule.

**Input:** 
A `.lc` file containing at least one anomalous data point

**Procedure:** 
Run: `outliers.py`

**Expected Output:** 
A plot highlighting outliers (e.g., using red dots or markers)

**Pass Criteria:** 
- Outliers beyond 4σ from the median are correctly flagged 
- Normal data points are not falsely flagged 
- Plot clearly distinguishes between normal and anomalous data

---

## Test Case 5 (Practice 3): Statistical Summary

**Objective:** 
Ensure that basic statistics are correctly calculated and reported.

**Input:** 
A `.lc` file with valid flux values

**Procedure:** 
Run: `stat.py`

**Expected Output:** 
Printed or saved values for:
- Minimum
- Maximum
- Mean
- Median
- Standard deviation
- Amplitude

**Pass Criteria:** 
- Computed values match NumPy or manual verification 
- Output is clear and correctly formatted

---

