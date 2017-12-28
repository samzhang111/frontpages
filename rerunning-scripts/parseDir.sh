#!/bin/bash

DIR=$1

find $DIR -name "*.pdf" | xargs -n 1 -t -P 8 -I % timeout 15m pdf2txt.py -t xml -o %.xml %
