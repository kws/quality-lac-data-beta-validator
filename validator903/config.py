from .validators import *

"""
Column names for each 903 file.

These are used in two places:
- Checking that the uploaded files match and identifying which CSV file is which (when CSVs are selected).
- Constructing CSV files from provided XML (when XML is selected)
"""
column_names = {
    'Header': ['CHILD', 'SEX', 'DOB', 'ETHNIC', 'UPN', 'MOTHER', 'MC_DOB'],
    'Episodes': ['CHILD', 'DECOM', 'RNE', 'LS', 'CIN', 'PLACE', 'PLACE_PROVIDER', 'DEC', 'REC', 'REASON_PLACE_CHANGE', 'HOME_POST', 'PL_POST', 'URN'],
}

"""
List of all configured errors for validation.

These all should have return type (Error, Dict[str, DataFrame])
"""
tested_errors = [fake_error, fake_error2]