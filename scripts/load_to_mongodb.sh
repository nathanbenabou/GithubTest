#!/bin/bash
cd `dirname $0`
#mongod

for LEAGUE in FL1 PL BL SA PPL PD; do
	for filename in ../historical_daily_data/${LEAGUE}/*; do mongoimport --db soccer --collection ${LEAGUE} --upsert --file $filename;  done
        for filename in ../historical_past_data/json/${LEAGUE}/*; do mongoimport --db soccer_past --collection ${LEAGUE} --upsert --file $filename;  done
done
