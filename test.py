#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root',password='xiaofang',database='test')
cursor1 = conn.cursor()
cursor1.execute('select * from stat_last')
last_info = cursor1.fetchall()
cursor1.close()
cursor2 = conn.cursor()
cursor2.execute('select * from stat')
curr_info = cursor2.fetchall()
cursor2.close()
conn.close()

stat_record = {}
for i in curr_info:
    for j in last_info: 
        if (i[2],i[3]) == (j[2],j[3]):
            stat_record['nochanged'] = stat_record.get('nochanged',[])
            stat_record['nochanged'].append(i)
        elif i[2] == j[2] and i[3] != j[3]:
            stat_record['changed'] = stat_record.get('changed',[])
            stat_record['changed'].append(i)
    if i[2] not in [sn[2] for sn in last_info]:
        stat_record['new'] = stat_record.get('new',[])
        stat_record['new'].append(i)

for i in last_info:
    if i[2] not in [sn[2] for sn in curr_info]:
        stat_record['deleted'] = stat_record.get('deleted',[])
        stat_record['deleted'].append(i)

print stat_record
