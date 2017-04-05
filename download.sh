#!/bin/bash
set -e

CURRENT_DATE=`date "+%Y_%m_%d"`
DAY_OF_MONTH=`date "+%-d"`

echo 'Downloading list of newspapers for today'
mkdir -p data/$CURRENT_DATE

node ./discoverNewspapers.js > papers.txt
cat papers.txt | xargs -n 8 wget -4 --directory-prefix="data/$CURRENT_DATE"
