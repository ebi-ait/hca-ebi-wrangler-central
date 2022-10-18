import pandas as pd
import argparse

def main():

        parser = argparse.ArgumentParser()
        parser.add_argument('-r_file', type=str, help='Tab-delimited txt file with file names and associated run accessions.')
        parser.add_argument('-v_file', type=str, help='Tab-delimited txt file with file names and validation states.')

        args = parser.parse_args()

        file_to_run_accession = args.r_file
        validation_states = args.v_file

        r_data = pd.read_csv(file_to_run_accession,sep="\t")
        v_data = pd.read_csv(validation_states,sep="\t")

        v_data.columns = ["index","file","state","error"]
        for i in range(0,v_data.shape[0]):
                file = list(v_data["file"])[i]
                if file in list(r_data["file"]):
                        accession = r_data[r_data["file"] == file]["accession"].values[0]
                        error = list(v_data["error"])[i]
                        if error == "FILE_NOT_UPLOADED":
                                print(accession)

if __name__ == "__main__":
    main()
