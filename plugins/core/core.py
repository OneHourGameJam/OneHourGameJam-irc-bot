import plugins.pluginapi
import time


class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'core'
        desc = 'Core plugin, made for admins.'
        self.bot = bot
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('reload', self.reload)
        self.register_command('help', self.help)

    def reload(self, usr, cmd, chan):
        if usr in self.config["admin"]["admins"]:
            try:
                self.bot.plugins = []
                self.bot.load_plugins(self.config["botsettings"]["plugins_folder"])
                self.send_msg("Successfully reloaded plugins.", usr)
            except:
                self.send_msg("Failed to reload plugins.", usr)
        else:
            self.send_msg("Insufficient permissions.", usr)

    def help(self, usr, cmd, chan):
        for plugin in self.bot.plugins:
            self.send_msg("%s - %s" % (plugin.name, plugin.description), usr)
