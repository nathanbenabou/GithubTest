#!/bin/bash

cd `dirname $0`

for date in 1617 1516 1415 1314 1213 1112 1011; do
	wget -O  ../historical_past_data/PL/${date}.csv  http://www.football-data.co.uk/mmz4281/${date}/E0.csv
done

for date in 1617 1516 1415 1314 1213 1112 1011; do
        wget -O ../historical_past_data/BL/${date}.csv http://www.football-data.co.uk/mmz4281/${date}/D1.csv
done

for date in 1617 1516 1415 1314 1213 1112 1011; do
        wget -O ../historical_past_data/SA/${date}.csv http://www.football-data.co.uk/mmz4281/${date}/I1.csv
done

for date in 1617 1516 1415 1314 1213 1112 1011; do
        wget -O ../historical_past_data/FL1/${date}.csv http://www.football-data.co.uk/mmz4281/${date}/F1.csv
done

for date in 1617 1516 1415 1314 1213 1112 1011; do
        wget -O ../historical_past_data/PD/${date}.csv http://www.football-data.co.uk/mmz4281/${date}/SP1.csv
done

for date in 1617 1516 1415 1314 1213 1112 1011; do
        wget -O ../historical_past_data/PPL/${date}.csv http://www.football-data.co.uk/mmz4281/${date}/P1.csv
done


