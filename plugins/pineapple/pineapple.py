import plugins.pluginapi

class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'pineapple'
        desc = 'Blame Ajay.'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('pineapple', self.cmd_pineapple)
        

    def cmd_pineapple(self, usr, cmd, chan):
        self.send_msg("http://imgur.com/a/bjk88", chan)