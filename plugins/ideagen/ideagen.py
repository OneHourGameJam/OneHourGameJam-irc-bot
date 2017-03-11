import plugins.pluginapi
import random, json, urllib.request, locale


class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'Game Idea Generator'
        desc = 'Generates a random idea for a game! (List by sorceress)'
        self.dataFile = "data.json"
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('idea', self.cmd_idea)
        self.register_command('name', self.cmd_name)
        self.register_command('submitidea', self.cmd_submitidea)
        

    def cmd_idea(self, usr, cmd, chan):
        self.data = json.loads(open(self.dataFile).read())["idea-generator"]
        choice1 = random.choice(self.data["list1"]).lower()
        choice2 = random.choice(self.data["list2"]).lower()
        choice3 = random.choice(self.data["list3"]).lower()
        
        #self.send_msg("Make a%s %s %s about Christmas!" % (self.add_n(choice1), choice1, choice2), chan)
        self.send_msg("Make a%s %s %s %s!" % (self.add_n(choice1), choice1, choice2, choice3), chan)
    
    def cmd_name(self, usr, cmd, chan):
        self.send_msg(self.gen_name(), chan)
    
    def cmd_submitidea(self, usr, cmd, chan):
        ideas = ' '.join(cmd[1:]).split('/')
        if len(ideas) != 3:
            self.send_msg('Please submit 3 ideas, one for each part, separated by slashes (/)', chan)
        else:
            for idea in range(len(ideas)):
                if ideas[idea].strip() != '':
                    self.submit_idea(ideas[idea], idea+1)
            self.send_msg('Your idea was successfully submitted. It will be reviewed and may soon be in the bot!', chan)
    
    def submit_idea(self, idea, part):
        try:
            data = json.loads(open(self.dataFile).read())
            data["idea-generator"]["suggestions"]["part" + str(part)].append(idea)
            open(self.dataFile, 'w').write(json.dumps(data, sort_keys=True, indent=4))
        except:
            pass
    
    def add_n(self, text):
        if text[0].lower() == "a" or text[0].lower() == "e" or text[0].lower() == "i" or text[0].lower() == "o" or text[0].lower() == "u":
            return 'n'
        else:
            return ''
    
    def gen_name(self, fil='https://videogamena.me/video_game_names.txt'):
        name_file = urllib.request.urlopen("http://videogamena.me/video_game_names.txt")
        encoding = locale.getdefaultlocale()[1]
        
        ideas = []
        similar = {}
        
        tmp = []
        for x in name_file.read().decode(encoding).split("----"):
            for y in x.split("\n"):
                i = y.split("^")
                if len(i) > 1:
                    j = i[1].split('|')
                    similar[i[0]] = j
                    tmp.append(i[0])
                elif y != '':
                    tmp.append(y)
            ideas.append(tmp)
            tmp = []
            
        name = []
        
        name.append(random.choice(ideas[0]))
        if name[0] in similar:
            for x in similar[name[0]]:
                for idea_list in range(len(ideas)):
                    if x in ideas[idea_list]:
                        ideas[idea_list].remove(x)
                        
        name.append(random.choice(ideas[1]))
        if name[1] in similar:
            for x in similar[name[1]]:
                for idea_list in range(len(ideas)):
                    if x in ideas[idea_list]:
                        ideas[idea_list].remove(x)
        
        name.append(random.choice(ideas[1]))
        if name[1] in similar:
            for x in similar[name[1]]:
                for idea_list in range(len(ideas)):
                    if x in ideas[idea_list]:
                        ideas[idea_list].remove(x)
        
        return "\"%s %s %s\"" % (name[0], name[1], name[2])