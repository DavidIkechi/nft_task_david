
# CHIP-0007 JSON FORMAT GENERATOR

This project converts each row in a CSV into it's CHIP-0007 JSON format equivalence. for each row, a JSON file is created, and saved in your directory. Furthermore, the hash of the json file from each row of the csv is calculated and appended as a new column to an output csv.
NOTE: JSON files are generated for each row.
      a csv file is also generated with name filename.output.csv, where filename represents the name of your initial csv
## Acknowledgements

 - [HNGi9](https://internship.zuri.team/hngi9)
 

## Run Locally

Clone the project

```bash
  git clone https://github.com/DavidIkechi/nft_task_david.git
```

Go to the project directory

```bash
  cd nft_task_david
```

activate your virtual environment. for windows use the command below. for other users, please check how to activate a virtual environment on your OS.

```bash
virtualenv environment_name
```

Install the required package
```bash
pip install -r requirements.txt
```
run the code
```bash
python main.py
```


## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## Example output

```bash
{
    "format": "CHIP-0007",
    "name": "baba-ijebu-the-gambler",
    "description": "Baba Ijebu likes to spend all his money playing ayo and plays till the moon is high.",
    "minting_tool": "TEAM AXE",
    "sensitive_content": false,
    "series_number": 381,
    "series_total": 420,
    "attributes": [
        {
            "trait_type": "hair",
            "value": "none"
        },
        {
            "trait_type": "eyes",
            "value": "sky blue"
        },
        {
            "trait_type": "teeth",
            "value": "none"
        },
        {
            "trait_type": "clothing",
            "value": "none"
        },
        {
            "trait_type": "accessories",
            "value": "facemask"
        },
        {
            "trait_type": "expression",
            "value": "none"
        },
        {
            "trait_type": "strength",
            "value": "creation god"
        },
        {
            "trait_type": "weakness",
            "value": "love"
        }
    ],
    "collection": {
        "name": "Zuri NFT Tickets for Free Lunch",
        "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
        "attributes": [
            {
                "type": "description",
                "value": "Rewards for accomplishments during HNGi9."
            }
        ]
    }
}
```


## Tech Stack

**Server:** Python (Version 3.10.4)

