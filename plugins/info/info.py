import plugins.pluginapi

# This is an example plugin. Feel free to remove it! :)
class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'info'
        desc = '$code'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('code', self.cmd_code)
        self.register_command('source', self.cmd_code)
        

    def cmd_code(self, usr, cmd, chan):
        self.send_msg("https://github.com/pta2002/paib", chan)