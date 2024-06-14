"""
Helper functions for the cell_counter script.

Each function:
    - Must have a path directory as an input
    - Must return an integer (Sum of cell counts)
    - Must have an example GEO accession that yields this kind of matrix

"""

import os

def tenx_mex_format(path_to_dir):
    """
    GSE130430
    :param path_to_dir:
    :return:
    """
    files = [f for f in os.listdir(path_to_dir) if "matrix.mtx" in f]
    third_rows = []
    for file in files:
        with open(f"{path_to_dir}/{file}", 'r') as f:
            # Third row contains line number for matrix, barcode and genes files
            f.readline()
            f.readline()
            third_rows.append(f.readline())
    cell_numbers = [int(r.split(" ")[1]) for r in third_rows]
    return sum(cell_numbers)

def h5(path_to_dir):
    """
    GSE118127
    :param path_to_dir:
    :return:
    """
    files = [f for f in os.listdir(path_to_dir) if ".h5" in f]



