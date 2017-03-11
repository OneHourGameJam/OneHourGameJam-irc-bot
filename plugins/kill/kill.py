import plugins.pluginapi

# This is an example plugin. Feel free to remove it! :)
class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'kill'
        desc = 'Do `kill <user>` to kill that user. If you don\'t specify a user, you die!'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('kill', self.cmd_kill)
        

    def cmd_kill(self, usr, cmd, chan):
        if len(cmd) > 1:
            self.send_msg("*kills %s*" % cmd[1], chan)
        else:
            self.send_msg("*kills %s*" % usr, chan)