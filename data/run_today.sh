#!/bin/bash

cd `dirname $0`
TODAY=`date +%Y%m%d`
python run_today.py > ../historical_daily_data/logs/log_${TODAY}.txt
