from plugins.ludumdare.update_db import *
import plugins.pluginapi
import json
import re
import random
import urllib.request

class SearchQuery(object):
    def __init__(self, cmd, args, run):
        self.cmd = cmd
        self.args = args
        self.torun = run
    
    def run(self, data, args):
        if (len(args) == self.args):
            return self.torun(data, args)

class Search(object):
    def __init__(self):
        self.queries = []
        
    def register_query(self, query):
        self.queries.append(query)
    
    def run(self, data, command):
        for query in self.queries:
            if query.cmd.lower() == command[0].lower():
                args = " ".join(command[1:]).split(",")
                return query.run(data, args)

class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'ludumdare'
        desc = 'Add LD stuff.'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('update_db', self.cmd_updatedb)
        self.register_command('findme', self.cmd_findme)
        self.register_command('find', self.cmd_find)
        self.register_command('findrandom', self.cmd_random)
        self.config = config
        self.search = Search()
        queries = [
            SearchQuery("supports", 1, self.query_supports),
            SearchQuery("novotes", 0, self.query_novotes),
            SearchQuery("notcool", 0, self.query_notcool),
            SearchQuery("jam", 0, self.query_jam),
            SearchQuery("compo", 0, self.query_compo)
        ]
        
        for query in queries:
            self.search.register_query(query)
    
    def query_supports(self, data, args):
        entry = random.choice(data["entries"])
        for x in range(300):
            if not args[0] in entry["platforms"]:
                entry = random.choice(data["entries"])
            else:
                return entry
    
    def query_novotes(self, data, args):
        entry = random.choice(data["entries"])
        for x in range(300):
            if not entry["votes"] == "0":
                entry = random.choice(data["entries"])
            else:
                return entry
    
    def query_notcool(self, data, args):
        entry = random.choice(data["entries"])
        for x in range(300):
            if not entry["coolness"] == "0":
                entry = random.choice(data["entries"])
            else:
                return entry
    
    def query_jam(self, data, args):
        entry = random.choice(data["entries"])
        for x in range(300):
            if not entry["event"] == "open":
                entry = random.choice(data["entries"])
            else:
                return entry
    
    def query_compo(self, data, args):
        entry = random.choice(data["entries"])
        for x in range(300):
            if not entry["compo"] == "compo":
                entry = random.choice(data["entries"])
            else:
                return entry

    def cmd_updatedb(self, usr, cmd, chan):
        if usr in self.config["admin"]["admins"]:
            self.send_msg("Updating DB: bot will be down for a bit", chan)
            entries = update_db()
            self.send_msg("Done. Fetched %s entries" % str(entries), chan)

    def cmd_random(self, usr, cmd, chan):
        data = json.loads(open('entries.json').read())
        
        q = " ".join(cmd[1:]).lower()
        if (len(cmd) == 1):
            entry = random.choice(data["entries"])
            self.send_msg("%s: %s by %s: %s" % (usr, entry["name"], entry["author"], "http://ludumdare.com/compo/ludum-dare-35?action=preview&uid=" + entry["uid"]), chan)
        else:
            results = self.search.run(data, cmd[1:])
            if results:
                self.send_msg("%s: %s by %s: %s" % (usr, results["name"], results["author"], "http://ludumdare.com/compo/ludum-dare-35?action=preview&uid=" + results["uid"]), chan)
        
    def cmd_findme(self, usr, cmd, chan):
        data = json.loads(open('entries.json').read())
        for entry in data["entries"]:
            if entry["author"] == usr:
                self.send_msg("%s: %s by %s: %s" % (usr, entry["name"], entry["author"], 'http://ludumdare.com/compo/ludum-dare-35?action=preview&uid=' + entry["uid"]), chan)
    
    def cmd_find(self, usr, cmd, chan):
        if len(cmd) > 1:
            data = json.loads(open('entries.json').read())
            q = " ".join(cmd[1:]).lower()
            for entry in data["entries"]:
                if entry["author"].lower() == q or entry["name"].lower().startswith(q) or entry["uid"].lower() == q:
                    self.send_msg("%s: %s by %s: %s" % (usr, entry["name"], entry["author"], 'http://ludumdare.com/compo/ludum-dare-35?action=preview&uid=' + entry["uid"]), chan)
                    break
    
    def on_message(self, msg, user, chan):
        p = re.compile('ludumdare.com\/compo\/ludum-dare-\d\d\/?\?action=preview&uid=(\d+)')
        results = p.search(msg)
        if results:
            data = json.loads(open('entries.json').read())
            print(results.group(1))
            s = False
            for entry in data["entries"]:
                if entry["uid"] == results.group(1):
                    self.send_msg("\"%s\" by %s" % (entry["name"], entry["author"]), chan)
                    s = True
                    break