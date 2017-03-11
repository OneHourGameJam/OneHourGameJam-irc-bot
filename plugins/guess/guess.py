import plugins.pluginapi
import random


class Plugin(plugins.pluginapi.BasicPlugin):
    def __init__(self, bot, config):
        name = 'Guess a number'
        desc = 'Do $guess <number> to guess! (between 1 and 1023)'
        plugins.pluginapi.BasicPlugin.__init__(self, name, desc, config, bot.connection)
        self.register_command('guess', self.cmd_guess)
        self.num = random.randrange(0, 1024)
        self.totalguesses = 0
        

    def cmd_guess(self, usr, cmd, chan):
        if len(cmd) > 1:
            try:
                self.totalguesses += 1
                guess = int(cmd[1])
                if guess == self.num:
                    self.send_msg("Congratulations! You guessed the number in a total of %s guesses! I'm now thinking of another number. Can you guess what it is?" % str(self.totalguesses),
                    chan)
                    self.num = random.randrange(0, 1023)
                    self.totalguesses = 0
                else:
                    if guess < self.num:
                        self.send_msg("Your number is too low! Try again!", chan)
                    elif guess > self.num:
                        self.send_msg("Your number is too high! Try again!", chan)
            except:
                self.send_msg("Please guess a number!", chan)
        else:
            self.send_msg("Please guess a number between 1 and 1023!", chan)