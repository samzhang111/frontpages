import os
import sys
import json

import pandas as pd
import numpy as np

if len(sys.argv) != 4:
    print('''Usage: python {} METADATA_FILE DB_URI OUTPUT_TABLE

The metadata file should be JSON extracted from the newseum website (schema as of 4/6/17).

The DB_URI should be in sqlalchemy format.

Newspaper metadata from the file will be combined with existing newspapers in the output table.
'''.format(__file__))
    sys.exit(1)

METADATA_FILE, DB_URI, OUTPUT_TABLE = sys.argv[1:]

try:
    existing_metadata = pd.read_sql_table(OUTPUT_TABLE, DB_URI)
except ValueError:
    existing_metadata = pd.DataFrame()

print('Previous number of newspapers in DB: {}'.format(existing_metadata.shape[0]))

with open(METADATA_FILE) as f:
    metadata = json.load(f)

metadata_df = pd.DataFrame(metadata)
metadata_df['longitude'] = metadata_df['longitude'].apply(float)
metadata_df['latitude'] = metadata_df['latitude'].apply(float)
metadata_df.rename(columns={'paperId': 'slug'}, inplace=True) # To avoid capitalization issues with postgres

df = pd.concat([metadata_df, existing_metadata], ignore_index=True).drop_duplicates(subset=['slug'])
print('Current number of newspapers in DB: {}'.format(df.shape[0]))

df.to_sql(OUTPUT_TABLE, DB_URI, if_exists='replace', index=False)
