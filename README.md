# This repository is not maintained and will likely need some upfront work to get it to work with the one hour game jam site API.

If applicable, please consider using the Discord Bot which is, as of this writing, maintained: https://github.com/OneHourGameJam/OneHourGameJam-discord-bot

# PAIB
PAIB is Pta's Amazing IRC Bot, although on #ludumdare it can also stand for Pta's Amazing Idea Bot (because that's what it's doing there ;))

# Installing
PAIB is an extensible IRC bot written in python3 using the IRC module. You can easily set it up:

    $ sudo pip3 install irc
    $ git clone https://github.com/pta2002/paib.git
    $ cd paib
    $ python3 paib.py

This should get you running

# Changing the config
As of now, PAIB only runs in a single channel. This is how config.json would look like for #paib on irc.afternet.org (port 6667):

      {
        "connection": {
          "server": "irc.afternet.org",
          "port": 6667,
          "nick": "paib",
          "channel": "#paib"
        },
      
        "botsettings": {
          "command_prefix": "$",
          "plugins_folder": "plugins",
          "ignored": ["bot1", "bot2"]
        },
      
        "admin": {
          "admins": ["example"]
        }
      }

The settings on the config file are meant for #ludumdare, where I (pta2002) am the paib admin and where yaib and lunabot are two other bots that we should ignore.
