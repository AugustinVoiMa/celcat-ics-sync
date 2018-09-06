#!/usr/bin/env bash

LOCAL=/usr/local/bin/
SUB=celcat_ics_sync/

mkdir -p $LOCAL$SUB

cp celcat_ics_sync/*.py $LOCAL$SUB
cp conf.json /etc/celcat_ics_sync.conf.json

cp celcat_ics_sync.py $LOCAL/celcat2ics
