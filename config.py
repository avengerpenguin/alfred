##########################################################################
#                                                                        #
#  This is the config-template for Err. This file should be copied and   #
#  renamed to config.py, then modified as you see fit to run Err the way #
#  you like it.                                                          #
#                                                                        #
#  As this is a regular Python file, note that you can do variable       #
#  assignments and the likes as usual. This can be useful for example if #
#  you use the same values in multiple places.                           #
#                                                                        #
#  Note: Various config options require a tuple to be specified, even    #
#  when you are configuring only a single value. An example of this is   #
#  the BOT_ADMINS option. Make sure you use a valid tuple here, even if  #
#  you are only configuring a single item, else you will get errors.     #
#  (So don't forget the trailing ',' in these cases)                     #
#                                                                        #
##########################################################################

import os
import re
import logging

import os, errno


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

##########################################################################
# Core Err configuration                                                 #
##########################################################################

mkdir_p('data')
BOT_DATA_DIR = 'data'
BOT_EXTRA_PLUGIN_DIR = 'plugins'
BOT_LOG_FILE = None
BOT_LOG_LEVEL = logging.INFO
BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL
BOT_ASYNC = True

##########################################################################
# Account and chatroom (MUC) configuration                               #
##########################################################################

irc_uri = os.environ['IRC_URI'].strip()
irc_host, irc_port, irc_channel = re.match('irc://(.+):(\d+)/(.+)', irc_uri).groups()

bot_name = os.getenv('BOT_NAME', 'alfred-bot')

BOT_IDENTITY = {
    'nickname' : bot_name,
    'username' : bot_name,
    'server' : irc_host,
    'port': int(irc_port),
    'ssl': False,
}
CHATROOM_PRESENCE = (irc_channel,)
CHATROOM_FN = bot_name

# Set the admins of your bot. Only these users will have access
# to the admin-only commands.
#
# Note: With campfire this should be the full name of a person, like so: 
# BOT_ADMINS = ('Guillaume Binet',)
#
BOT_ADMINS = tuple(s.strip() for s in os.getenv('BOT_ADMINS', '').split(','))

# Chatrooms your bot should join on startup. For the IRC backend you 
# should include the # sign here. For XMPP rooms that are password
# protected, you can specify another tuple here instead of a string,
# using the format (RoomName, Password).

# The FullName, or nickname, your bot should use. What you set here will
    # be the nickname that Err shows in chatrooms. Note that some XMPP
# implementations, notably HipChat, are very picky about what name you
# use. In the case of HipChat, make sure this matches exactly with the
# name you gave the user.

##########################################################################
# Prefix configuration                                                   #
##########################################################################

# Command prefix, the prefix that is expected in front of commands directed
# at the bot.
#
# Note: When writing plugins,you should always use the default '!'.
# If the prefix is changed from the default, the help strings will be
# automatically adjusted for you.
#
BOT_PREFIX = '!'

# Uncomment the following and set it to True if you want the prefix to be
# optional for normal chat.
# (Meaning messages sent directly to the bot as opposed to within a MUC)
#BOT_PREFIX_OPTIONAL_ON_CHAT = False

# You might wish to have your bot respond by being called with certain
# names, rather than the BOT_PREFIX above. This option allows you to
# specify alternative prefixes the bot will respond to in addition to
# the prefix above.
#BOT_ALT_PREFIXES = ('Err',)

# If you use alternative prefixes, you might want to allow users to insert
# separators like , and ; between the prefix and the command itself. This
# allows users to refer to your bot like this (Assuming 'Err' is in your
# BOT_ALT_PREFIXES):
# "Err, status" or "Err: status"
#
# Note: There's no need to add spaces to the separators here
#
#BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')

# Continuing on this theme, you might want to permit your users to be
# lazy and not require correct capitalization, so they can do 'Err',
# 'err' or even 'ERR'.
#BOT_ALT_PREFIX_CASEINSENSITIVE = True

##########################################################################
# Access controls and message diversion                                  #
##########################################################################

# Access controls, allowing commands to be restricted to specific users/rooms.
# Available filters (you can omit a filter or set it to None to disable it):
#   allowusers: Allow command from these users only
#   denyusers: Deny command from these users
#   allowrooms: Allow command only in these rooms (and direct messages)
#   denyrooms: Deny command in these rooms
#   allowprivate: Allow command from direct messages to the bot
#   allowmuc: Allow command inside rooms
# Rules listed in ACCESS_CONTROLS_DEFAULT are applied when a command cannot 
# be found inside ACCESS_CONTROLS
#
# Example:
#ACCESS_CONTROLS_DEFAULT = {} # Allow everyone access by default
#ACCESS_CONTROLS = {'status': {'allowrooms': ('someroom@conference.localhost',)},
#                   'about': {'denyusers': ('baduser@localhost',), 'allowrooms': ('room1@conference.localhost', 'room2@conference.localhost')},
#                   'uptime': {'allowusers': BOT_ADMINS},
#                   'help': {'allowmuc': False},
#                  }

# Uncomment and set this to True to hide the restricted commands from
# the help output.
#HIDE_RESTRICTED_COMMANDS = False

# Uncomment and set this to True to ignore commands from users that have no
# access for these instead of replying with error message.
#HIDE_RESTRICTED_ACCESS = False

# A list of commands which should be responded to in private, even if
# the command was given in a MUC. For example:
# DIVERT_TO_PRIVATE = ('help', 'about', 'status')
DIVERT_TO_PRIVATE = ()

# Chat relay
# Can be used to relay one to one message from specific users to the bot
# to MUCs. This can be useful with XMPP notifiers like for example  the
# standard Altassian Jira which don't have native support for MUC.
# For example: CHATROOM_RELAY = {'gbin@localhost' : (_TEST_ROOM,)}
CHATROOM_RELAY = {}

# Reverse chat relay
# This feature forwards whatever is said to a specific user.
# It can be useful if you client like gtalk doesn't support MUC correctly
# For example: REVERSE_CHATROOM_RELAY = {_TEST_ROOM : ('gbin@localhost',)}
REVERSE_CHATROOM_RELAY = {}
