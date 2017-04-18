#!/bin/bash
set -e

download_newspapers() {
CURRENT_DATE=${1}
echo "Downloading list of newspapers for ${CURRENT_DATE}"

TMP_DIR=$(mktemp -d)
FRONTPAGE_PATH=${TMP_DIR}/frontpage.json

mkdir -p data/"${CURRENT_DATE}"

node ./discoverNewspapers.js > "${FRONTPAGE_PATH}"

jq '.papers[] | .links.pdf' "${FRONTPAGE_PATH}" | \
	xargs -n 8 wget -4 --random-wait --directory-prefix="data/$CURRENT_DATE"


METADATA_SELECTOR="{paperId: .paperId, city: .city, state: .state, country: .country, longitude: .longitude, latitude: .latitude, title: .title, website: .website}"
jq ".papers[] | ${METADATA_SELECTOR}"  "${FRONTPAGE_PATH}" | \
	jq -s '.' > "data/$CURRENT_DATE-metadata.json" 
}

export -f download_newspapers
