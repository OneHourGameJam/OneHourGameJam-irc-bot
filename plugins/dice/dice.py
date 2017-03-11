import plugins.pluginapi
import re, random

class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'dice'
        desc = 'Use $dice and dice notation to generate a number'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('dice', self.cmd_dice)
        self.register_command('coin', self.cmd_coin)
        self.find_dice_notation = re.compile('(\d+)d(\d+)')
    
    def cmd_dice(self, usr, cmd, chan):
        dice_num = 1
        dice_faces = 6
        results = []
        total = 0
        
        try:
            if len(cmd) == 2:
                settings = self.find_dice_notation.match(cmd[1]).groups()
                dice_num = min(int(settings[0]), 100) # Keep this bot from flooding itself off the chat
                dice_faces = min(int(settings[1]), 100) 
            
            
            for i in range(dice_num):
                result = random.randint(1, dice_faces)
                results.append(str(result))
                total += result
            
            self.send_msg('%s rolled %s for a total of %s!' % (usr, ", ".join(results), str(total)), chan)
        except:
            self.send_msg('Please use dice notation!', chan)
    
    def cmd_coin(self, usr, cmd, chan):
        options = ['heads', 'tails']
        self.send_msg('%s flipped %s!' % (usr, random.choice(options)), chan)
