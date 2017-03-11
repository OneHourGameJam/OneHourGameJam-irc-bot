import json, random
import plugins.pluginapi


class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'Jokes'
        desc = 'Tells user-submitted jokes. Do `$joke` to receive a random joke, and `$joke [joke]` to submit one!'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('joke', self.cmd_joke)

    def cmd_joke(self, usr, cmd, chan):
        jokesFile = open('data.json')
        jokes = json.loads(jokesFile.read())
        jokesFile.close()
        if len(cmd) == 1:
            try:
                chosen_joke = random.choice(jokes["jokes"])
                self.send_msg("\"%s\" (submitted by %s)" % (chosen_joke["joke"], chosen_joke["submitter"]), chan)
            except:
                self.send_msg("There are no jokes! Submit one yourself!", chan)
        else:
            joke = " ".join(cmd[1:])
            self.submit_joke(joke, usr, chan)

    def submit_joke(self, joke, usr, chan):
        jokesFile = open('data.json')
        jokes = json.loads(jokesFile.read())
        jokesFile.close()
        new_joke = {"submitter": usr, "joke": joke}
        jokes["jokes"].append(new_joke)
        jokesFile = open('data.json', 'w')
        jokesFile.write(json.dumps(jokes, sort_keys=True, indent=4))
        jokesFile.close()
        self.send_msg("%s: Successfully submitted joke!" % usr, chan)