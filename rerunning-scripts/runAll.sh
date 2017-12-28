#!/bin/bash

REMOTE_FILE=$1

aws s3 cp s3://newseum-frontpage-archive/$REMOTE_FILE $REMOTE_FILE

mkdir -p data
tar xzf $REMOTE_FILE -C data

rm $REMOTE_FILE

./parseDir.sh data/
python ../ingest_xmls_to_db.py data/ postgres:///frontpages frontpage_texts2
rm -rf data
