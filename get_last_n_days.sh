#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
		exit -1
fi

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
source "${BASE_DIR}"/download.sh

seq 1 "${1}" | \
	xargs -I {} date -v -{}d +%Y-%m-%d | \
	sort -u | \
	xargs -P4 -I{} bash -c "download_newspapers {}"
