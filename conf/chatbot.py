#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import dependencies
import json
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
						  BaseFilter, ConversationHandler)
from emoji import emojize
import logging
import config
import certifi
import urllib3

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

# Filter compare YunoHost Apps
class FilterStar(BaseFilter):
	def filter(self, message):
		return 'ynh' in message.text

# Remember to initialize the class.
filter_star = FilterStar()

def start(bot, update):
	logger.info("start")

def aide(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="RTFM")

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def bonjour(bot, update):
	user = update.message.from_user
	logger.info("Bonjour de %s: %s" % (user.first_name, update.message.text))
	bot.sendMessage(chat_id=update.message.chat_id, text="Salut !")

def merci(bot, update):
	user = update.message.from_user
	logger.info("Biere de %s: %s" % (user.first_name, update.message.text))
	bot.sendMessage(chat_id=update.message.chat_id, text="Je vous en pris !")

def biere(bot, update):
	user = update.message.from_user
	logger.info("Biere de %s: %s" % (user.first_name, update.message.text))
	bot.sendMessage(chat_id=update.message.chat_id, text="A la votre !")

def star(bot, update):

	message = update.message.text
	mylist = message.split(" ")
	nameapp1 = mylist[1]
	nameapp2 = mylist[2]
	score_result = []

	for name in mylist[1:]:
		user_agent = {'user-agent': 'Telegram-bot/0.0.1 (Windows NT 6.3; rv:36.0)'}
		http = urllib3.PoolManager(10, headers=user_agent, cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		url_github = 'https://' + config.user_github + ':' + config.token_github + '@api.github.com/repos/YunoHost-Apps/' + name + '_ynh'
		app = http.urlopen('GET', url_github)
		japp = json.loads(app.data.decode('utf-8'))
		if ('stargazers_count' in japp):
			score = japp['stargazers_count']
			score_result.append(score)

	if len(score_result) == 2:
		if (score_result[0] == score_result[1]):
			result = emojize("{0} ({2}) est égale à {1} ({3}) :thumbsup:".format(nameapp1, nameapp2, score_result[0], score_result[1]), use_aliases=True)
		elif (score_result[0] > score_result[1]):
			result = emojize("{0} ({2}) :thumbsup: est mieux que {1} ({3}) :thumbsdown:".format(nameapp1, nameapp2, score_result[0], score_result[1]), use_aliases=True)
		else:
			result = emojize("{1} ({2}) :thumbsdown: est moins bien que {0} ({3}) :thumbsup:".format(nameapp2, nameapp1, score_result[0], score_result[1]), use_aliases=True)
	else:
		result = emojize("Une ou les deux applications n'ont pas été trouvées :confused:", use_aliases=True)

	if result:
		bot.sendMessage(chat_id=update.message.chat_id, text=result)


def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
	# Create the EventHandler and pass it your bot's token.
	updater = Updater(token=config.token_telegram, workers=32)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# This enables the '/start' command
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", aide))

	# Send message if ...
	dp.add_handler(RegexHandler('^.*(?i)(coucou|salut|bonjour|yop|hello).*$', bonjour))
	dp.add_handler(RegexHandler('^.*(?i)(mer(.*)ci|ci(.*)mer).*$', merci))
	dp.add_handler(RegexHandler('^.*(?i)bière.*$', biere))
	dp.add_handler(MessageHandler(filter_star, star))
	# dp.add_handler(RegexHandler('^\/view(\d+).*', view.item, pass_groups=True))

	# on noncommand i.e message - echo the message on Telegram
	# dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()

if __name__ == '__main__':
	main()