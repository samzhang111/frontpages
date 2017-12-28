import os
import sys
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup

from lib.combine_textboxes import extract_textboxes

if len(sys.argv) != 4:
    print('''Usage: python {} XML_FILES_DIR OUTPUT_DB_URI OUTPUT_TABLE

This is used to ingest multiple archives of frontpages into the database. See parse_xml_to_db.py for a single-day script.

This program parses the XML files generated by pdf2txt.py into text boxes, and saves the result to a database.

All of the .xml files in XML_FILES_DIR are assumed to be parseable output from earlier stages of this process.
For example, we are assuming that the deepest directory in XML_FILES_DIR is the date of the newspaper,
and that the filename is expected to be the slug of the newspaper before the first period.

OUTPUT_DB is expected to be a sqlalchemy URI.
The output database is appended to, so subsequent runs of the same command will create duplicates.'''.format(
    __file__))
    sys.exit(1)

FILES_DIR, SQLALCHEMY_URI, OUTPUT_TABLE = sys.argv[1:]

for i, (dirname, _, fns) in enumerate(os.walk(FILES_DIR)):
    if len([fn for fn in fns if fn.endswith('.xml')]) < 5:
        continue
    if i % 50 == 0:
        print('.', end='')
        sys.stdout.flush()

    date = datetime.strptime(os.path.basename(dirname), "%Y_%m_%d")
    for fn in fns:
        if not fn.endswith('.xml'):
            continue

        slug = fn.split('.')[0]

        with open(os.path.join(dirname, fn)) as f:
            soup = BeautifulSoup(f.read(), 'lxml')
            df = extract_textboxes(soup)

        if len(df) == 0:
            continue

        df['date'] = date
        df['day_of_week'] = date.weekday()
        df['weekend'] = date.weekday() in [5, 6]
        df['slug'] = slug

        df.to_sql(OUTPUT_TABLE, SQLALCHEMY_URI, if_exists='append', index=False)
