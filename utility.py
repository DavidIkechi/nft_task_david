import pandas as pd
import numpy as np
import hashlib
import json

def load_csv_file(filename):
    return pd.read_csv(filename)


def hash_data(data):    
    return hashlib.sha256(password.encode()).hexdigest()

def get_valid_row_count(df) -> int:
    return len(df)

def generate_attribute_list(attribute) -> list:
    empty_list = []
    split_attr = attribute.split(";")
    # loop thru the split attributes.
    for i in split_attr:
        # split the attribute again, as they are seperated by :.
        split_again = i.split(":")
        if len(split_again) < 2:
            continue 
        empty_list.append({
            "trait_type": split_again[0].strip(),
            "value": split_again[1].strip()
        })
        
    return empty_list

def update_header(header_dict, name, desc, series, total, team_name) -> dict:
    header_dict['name'] = name
    header_dict['description'] = desc
    header_dict['minting_tool'] = team_name
    header_dict['series_number'] = int(series)
    header_dict['series_total'] = int(total)
    
    return header_dict


def get_columns(df) -> list:
    """
    This function returns the number of columns in the loaded file.
    """
    return df.columns

def sha256digest(fname):
    return hashlib.sha256(open(fname, 'rb').read()).hexdigest()


def add_extra_column(df_name, column_name):
    df_name[column_name] = ""
    return df_name


def combine_all(header, attributes, collections) -> dict:
    """
    This functions combines all necessary components of the CHIP JSON.
    """
    header['attributes'] = attributes
    header['collection'] = collections
    
    return header

def make_json(f_name, j_data):
    """
    This function converts a dictionary into it's json format, and stores it in a file
    Args:
        f_name (str): represents the filename to save the json data as
        j_data (dict): represents the dict data
    """
    with open(f_name, 'w') as write_json:
        json.dump(j_data, write_json, indent=4)
        
def process_data(valid_nfts, all_columns, loaded_file, CHIP_HEADER, COLLECTION_TEMPLATE):
    """
    This function processes the data to make the CHIP-JSON format file.
    Args:
        valid_nfts (int): The number of valid nfts we have.
        all_columns (int): The number of columns in the data
        loaded_file (dataframe): The loaded data frame.
    """  
    team_name = "" 
    for i in range(valid_nfts):
        if not pd.isnull(loaded_file.loc[i, 'TEAM NAMES']) and loaded_file.loc[i, 'TEAM NAMES'] != team_name:
            team_name = loaded_file.loc[i, 'TEAM NAMES'].strip()
            changed = True
        
        for j in all_columns:
            if j == 'TEAM NAMES':
                continue
            get_name = loaded_file.loc[i, 'Filename'].strip()
            get_desc = loaded_file.loc[i, 'Description'].strip()
            get_attr = loaded_file.loc[i, 'Attributes']
            get_serial = loaded_file.loc[i, 'Series Number']
            
            # derive the name to be used as the name of the nft json file
            filename = "nft_"+team_name.replace(" ", "_").lower()+str(get_serial)+".json"
            # format the attributes mainly splitting ; and :
            formatted_attr = generate_attribute_list(get_attr)
            # update the CHIP header with the series number and other attributes we got.
            formatted_json_header = update_header(CHIP_HEADER, get_name, get_desc, get_serial, valid_nfts, team_name)
            # combine both the header, attributes and collections to form the chip json
            json_file = combine_all(formatted_json_header, formatted_attr, COLLECTION_TEMPLATE)
            # make the json file and save it.
            make_json(filename, json_file)
            # generate the hash key (sha) for the json file
            a = sha256digest(filename)
            # update the sha256 column with the hash key
            loaded_file.loc[i, ['sha256']]= a
    
    return loaded_file