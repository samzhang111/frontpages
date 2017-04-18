#!/bin/bash
set -e

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
source "${BASE_DIR}"/download.sh


CURRENT_DATE=$(date "+%Y_%m_%d")

source venv/bin/activate

download_newspapers "${CURRENT_DATE}"
./decrypt.sh
./parse.sh || true

python ingest_newspaper_metadata.py "data/$CURRENT_DATE-metadata.json" postgres:///frontpages newspapers
python parse_xml_to_db.py "data/$CURRENT_DATE/" postgres:///frontpages frontpage_texts
