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
        if i[2] == j[2] and i[3] != j[3]:
            stat_record['changed'] = stat_record.get('changed',[])
            stat_record['changed'].append(i)
stat_record['nochanged'] = [ i for i in curr_info if (i[2],i[3]) in [(j[2],j[3]) for j in last_info]]
#stat_record['changed'] = [ i for i in curr_info if i[2]==j[2] for j in last_info] 
stat_record['new'] = [i for i in curr_info if i[2] not in [j[2] for j in last_info]]
stat_record['deleted'] = [ i for i in last_info if i[2] not in [j[2] for j in curr_info]]


print stat_record
