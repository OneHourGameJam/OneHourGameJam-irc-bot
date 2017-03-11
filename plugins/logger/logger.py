import plugins.pluginapi
import sqlite3
import time


class Plugin(plugins.pluginapi.BasicPlugin):
	def __init__(self, bot, config):
		name = 'Logger'
		desc = 'Keeps logs'
		db = sqlite3.connect('logs.db')
		c = db.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS Logs(`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `time` INTEGER, `channel` TEXT, `user` TEXT, `message` TEXT)")
		db.commit()
		db.close()
		plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)

	def on_message(self, msg, usr, chan):
		print("[%s] (%s) <%s> %s" % (str(int(time.time())), chan, usr, msg))
		db = sqlite3.connect('logs.db')
		c = db.cursor()
		c.execute('INSERT INTO Logs(`time`, `channel`, `user`, `message`) VALUES (?, ?, ?, ?)', (int(time.time()), chan, usr, msg))
		db.commit()
		db.close()