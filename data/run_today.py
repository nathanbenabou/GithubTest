import datetime as dt
import time

from data.savedata import saveData, load_config_key

horizon=1
count=0
for league in (  'SA', 'PPL', 'PD', 'FL1', 'PL','BL'):
  for look_back in range(0,horizon):
    timeFrameEnd=dt.datetime.now()-dt.timedelta(days=look_back)
    timeFrameStart=timeFrameEnd#-dt.timedelta(days=1)
    day_str=timeFrameStart.strftime("%Y%m%d")
    output_file = "".join(
        ("/Users/nathanbenabou/Documents/GithubTest/historical_daily_data/", league, "/", day_str, ".json"))
    saveData(league, timeFrameStart, timeFrameEnd, False, False, False, False, False, 'json', output_file, False, False, False, load_config_key())
    count+=1
    if count%35==0:
        time.sleep(60)