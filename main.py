from utility import *
import pandas as pd

FILENAME = "hngcsv.csv"

# create a header for the chip-0007 format
CHIP_HEADER = {
    "format": "CHIP-0007",
    "name": "",
    "description": "",
    "minting_tool": "",
    "sensitive_content": False,
    "series_number": 0,
    "series_total": 0
}

#define the collection part
COLLECTION_TEMPLATE = {
    "name": "Zuri NFT Tickets for Free Lunch",
    "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
    "attributes": [
        {
            "type": "description",
            "value": "Rewards for accomplishments during HNGi9."
        }
    ]
}

# load the file at this point 
loaded_file = load_csv_file(FILENAME)
# add extra column to be used in storing the hash (sha256)
loaded_file = add_extra_column(loaded_file, "sha256")
# count the rows with non missing column values for the 
# rows, these correlates to the valid number of nfts we have.
valid_nfts = get_valid_row_count(loaded_file)
# get all the columns in the file
all_columns = get_columns(loaded_file)
# process the file
loaded_file = process_data(valid_nfts, all_columns, loaded_file, CHIP_HEADER, COLLECTION_TEMPLATE)
# make the new CSV.
file_name = FILENAME.split('.')[0]
loaded_file.to_csv(file_name+".output.csv", index = False, encoding='utf-8')