#!/bin/bash

CURRENT_DATE=`date "+%Y_%m_%d"`

ls data/$CURRENT_DATE/* | grep -v '_decrypt.pdf' | xargs -t -P8 -I % qpdf --password='' --decrypt % %_decrypt.pdf
ls data/$CURRENT_DATE/* | grep -v '_decrypt.pdf' | xargs rm
