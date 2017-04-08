#!/bin/bash
set -e

CURRENT_DATE=`date "+%Y_%m_%d"`
DAY_OF_MONTH=`date "+%-d"`

echo 'Downloading list of newspapers for today'
mkdir -p data/$CURRENT_DATE

node ./discoverNewspapers.js > frontpage.json

jq '.papers[] | .links.pdf' frontpage.json | xargs -n 8 wget -4 --directory-prefix="data/$CURRENT_DATE"
jq '.papers[] | {paperId: .paperId, city: .city, state: .state, country: .country, longitude: .longitude, latitude: .latitude, title: .title, website: .website}' frontpage.json | jq -s '.' > "data/$CURRENT_DATE-metadata.json" 
