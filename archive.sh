#!/bin/bash
set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CURRENT_DATE=`date "+%Y_%m_%d"`
FILENAME="$CURRENT_DATE.tar.gz" 

find $DIR/data -name '*.xml' | xargs rm -f
tar czf $FILENAME $DIR/data

aws s3 cp $FILENAME s3://newseum-frontpage-archive/$FILENAME
rm $FILENAME
rm -rf $DIR/data/*
