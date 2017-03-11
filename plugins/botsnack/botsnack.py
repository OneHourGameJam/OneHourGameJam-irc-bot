import plugins.pluginapi
import random
import urllib, json
import requests
from io import StringIO
import math


class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'time'
        desc = "Time to jam"
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('time', self.cmd_botsnack)
        self.register_command('theme', self.cmd_botsnack)
        self.botsnack_messages = [
            "Mmmmm!",
            "Tasty!",
            "Thanks!",
        ]

    def cmd_botsnack(self, usr, cmd, chan):
        url = "http://onehourgamejam.com/api/nextjam/"
        page = requests.get(url)
        content = page.content.decode('UTF-8')
        thing = StringIO(content)
        lst = json.loads(content)
        msg = ""
        mintime = 999999999
        for jam in lst["current_jams"]:
            msg = "The jam is on! The theme is " + jam["theme"]
            self.send_msg(msg,chan)
            return
        for jam in lst["upcoming_jams"]:
            time =    int(jam["timediff"])
            if(time < mintime):
                mintime = time
                days =    math.floor(time / (60 * 60 * 24))
                time = time - days * (60 * 60 * 24)
                hours =   math.floor(time / (60 * 60))
                time = time - hours * (60 * 60)
                minutes = math.floor(time / (60))
                time = time - minutes * (60)
                seconds = time
                msg = "The next 1 hour game jam will start in"
                if days > 0:
                    msg = msg + " " + str(days)+" days"
                if hours > 0:
                    msg = msg + " " + str(hours)+" hours"
                if minutes > 0:
                    msg = msg + " " + str(minutes)+" minutes"
                if seconds > 0:
                    msg = msg + " " + str(seconds)+" seconds"
        if msg == "":
            self.send_msg("No jam scheduled yet. Next jam on Saturday at 20:00 UTC",chan)
        else:
            self.send_msg(msg,chan)