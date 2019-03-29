#!/bin/sh

curl http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz --output "../kddcup99"
curl http://kdd.ics.uci.edu/databases/kddcup99/kddcup.testdata.unlabeled_10_percent.gz --output "../kddcup99"

gzip -d kddcup99/kddcup.data_10_percent.gz
gzip -d kddcup99/kddcup.testdata.unlabeled_10_percent.gz
