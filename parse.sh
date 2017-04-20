#!/bin/bash

CURRENT_DATE=`date "+%Y_%m_%d"`

ls data/$CURRENT_DATE/*_decrypt.pdf | xargs -t -P 8 -I % timeout 2m pdf2txt.py -t xml -o %.xml %
