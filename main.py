#main setup :P
import telegram
from telegram.ext import Updater 
from telegram.ext import CommandHandler
import logging
import wikipedia
import os


updater = Updater(token='443409571:AAEUtkX0T74kJFotCl57ORJRJBl-fBeZQ-Q')
dispatcher = updater.dispatcher
#now for lazy copy paste
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

##################################################################################

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='I am here. What is your request? Type in /help to list commands')
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='/summary - Load summary from wikipedia\n/search - Seach articles on wikipedia.')
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)
#######################################
def getWikiSummary(q):
        query = q.replace('/summary', '')
        qeury = q.replace('@i_swear_i_dont_spam_bot', '')
        if len(query) < 2:
            return 'What would you like to get a summary about? For example /summary magnetism'
        else:
            return wikipedia.summary(query)
   
def wikiLink(bot, update):
    try:
        summaryFinal = getWikiSummary(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=summaryFinal)
    except:
        bot.send_message(chat_id=update.message.chat_id, text='Sorry! Too many or no articles regarding that :\'( . Use /search to see if the article exists.')

wikiHandler = CommandHandler('summary', wikiLink)
dispatcher.add_handler(wikiHandler)

def getWikiSearch(q):
    query = q.replace('/search', '') #remove command and username mention parts
    qeury = q.replace('@i_swear_i_dont_spam_bot', '')
    if len(query) < 2:
        return ['What would you like to search about? For example /search magnetism']
    else:
        return '*\n'+wikipedia.search(query)+'*\n'
def wikiSearch(bot, update):
    try:
        finalResults = ''
        searchResults = getWikiSearch(update.message.text)
        
        finalResults = ', \n'.join(searchResults)
        bot.send_message(chat_id=update.message.chat_id, text='_RESULTS:_'+finalResults+'Use /summary for example to get a summary', parse_mode=telegram.ParseMode.MARKDOWN)
    except:  
        bot.send_message(chat_id=update.message.chat_id, text='Sorry! Couldn\'t find anything matching that :\'(. Try a more general search?')
search_handler = CommandHandler('search', wikiSearch)
dispatcher.add_handler(search_handler)


PORT = int(os.environ.get('PORT', '5000'))
updater.start_webhook(listen='0.0.0.0', port=PORT, url_path='443409571:AAEUtkX0T74kJFotCl57ORJRJBl-fBeZQ-Q')
updater.bot.setWebhook("https://the-anti-spammer.herokuapp.com/" + '443409571:AAEUtkX0T74kJFotCl57ORJRJBl-fBeZQ-Q')
updater.idle()