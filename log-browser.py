#!/usr/bin python3
# -*- coding: utf-8 -*-

import sqlite3 as sql
import time
from datetime import datetime

logs = 'logs.db'
file = 'logs.txt'
db = sql.connect(logs)

with db:
	db.row_factory = sql.Row
	cur = db.cursor()

def gen_logs(file):
	logsFile = open(file, 'w')
	with db:
		try:
			cur.execute("SELECT * FROM Logs")
			print("Grabbed logs")
			logs = cur.fetchall()
			toWrite = []
			for log in logs:
				toWrite.append("[%s] <%s> %s" % (
					datetime.fromtimestamp(log["time"]),
					log["user"],
					log["message"]
				))
				print("[%s] <%s> %s" % (
					datetime.fromtimestamp(log["time"]),
					log["user"],
					log["message"]
				))
			logsFile.write("\n".join(toWrite))
			logsFile.close()
			toWrite = None
		except: pass

def get_logs_by(file, user):
	logsFile = open(file, 'w')
	with db:
		cur.execute("SELECT * FROM Logs WHERE `user` = '%s'" % user)
		print("Grabbed logs")
		logs = cur.fetchall()
		toWrite = []
		for log in logs:
			toWrite.append("[%s] <%s> %s" % (
				datetime.fromtimestamp(log["time"]),
				log["user"],
				log["message"]
			))
			print("[%s] <%s> %s" % (
				datetime.fromtimestamp(log["time"]),
				log["user"],
				log["message"]
			))
		logsFile.write("\n".join(toWrite))
		logsFile.close()
		toWrite = None


gen_logs("logs.txt")