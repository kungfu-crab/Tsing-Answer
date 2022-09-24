# 导出原始数据，线上线下分开统计
import pandas as pd

db = pd.read_json('result_order_during_20210913_20210920.json', encoding = 'utf-8')
actionRec = pd.json_normalize(db['actionRec'])
feedback = pd.json_normalize(db['feedback'])
db = pd.concat([db[['_id', 'abstract', 'courseID', 'online', 'state', 'subjectID']], actionRec, feedback], axis = 1)
order_online = db[db['online'] == True]
order_offline = db[db['online'] == False]
order_online.to_excel('order_online_during_20210913_20210920.xlsx')
order_offline.to_excel('order_offline_during_20210913_20210920.xlsx')
