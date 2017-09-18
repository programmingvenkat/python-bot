#main setup :P
import telegram
from telegram.ext import Updater 
from telegram.ext import CommandHandler
import logging
import wikipedia
import os


updater = Updater(token='443409571:AAEUtkX0T74kJFotCl57ORJRJBl-fBeZQ-Q')
dispatcher = updater.dispatcher
#Basic setup to start the app
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

##################################################################################
'''Start command'''
def start(bot, update): #command to help new users and also remove dyno from sleep
    bot.send_message(chat_id=update.message.chat_id, text='I am here. What is your request? Type in /help to list commands')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
'''end of start command'''
def version_check_command(bot, update): #this command is solely for checking if updated or not
    bot.send_message(chat_id=update.message.chat_id, text="The Anti Spammer version 0.1")
version_check_handler = CommandHandler('version', version_check_command)
dispatcher.add_handler(version_check_handler)

'''help commad to list commands for help'''
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='/summary - Load summary from wikipedia\n/search - Seach articles on wikipedia.')
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)
'''end of help command'''
#######################################
'''Use the wikipedia library to get results and return them as a string'''
def getWikiSummary(q):
        query = q.replace('/summary', '').replace('@i_swear_i_dont_spam_bot', '') #help remove command part and username
        
        if len(query) < 2:
            return 'What would you like to get a summary about? For example /summary magnetism'
        else:
            return wikipedia.summary(query) 
            
'''Actual command to initiate /summary''' 
def wikiLink(bot, update):
    try:
        
        summaryFinal = getWikiSummary(update.message.text)
        
        bot.send_message(chat_id=update.message.chat_id, text=summaryFinal)
    except:

        bot.send_message(chat_id=update.message.chat_id, text='Sorry! Too many or no articles regarding that :\'( . Use /search to see if the article exists.')

wikiHandler = CommandHandler('summary', wikiLink)
dispatcher.add_handler(wikiHandler)
'''end'''

'''Search command /search to search wikipedia articles'''
def getWikiSearch(q):
    query = q.replace('/search', '').replace('@i_swear_i_dont_spam_bot', '') #remove command and username mention parts
    
    if len(query) < 2: #incase of no query...
        return ['What would you like to search about? For example /search magnetism']
    else:
        return  wikipedia.search(query)  


def wikiSearch(bot, update):
    try:
        finalResults = ''
        searchResults = getWikiSearch(update.message.text)
        
        finalResults = ', \n'.join(searchResults)
        #this part uses markdown for bold text
        bot.send_message(chat_id=update.message.chat_id, text='\n*'+finalResults+'\n*', parse_mode=telegram.ParseMode.MARKDOWN)
    except:  
        bot.send_message(chat_id=update.message.chat_id, text='Sorry! Couldn\'t find anything matching that :\'(. Try a more general search?')

search_handler = CommandHandler('search', wikiSearch)
dispatcher.add_handler(search_handler)


updater.start_polling()  # USE FOR LOCAL TESTING ONLY

'''And finally initiate heroku servers'''
#PORT = int(os.environ.get('PORT', '5000'))
#updater.start_webhook(listen='0.0.0.0', port=PORT, url_path='443409571:AAEUtkX0T74kJFotCl57ORJRJBl-fBeZQ-Q')
#updater.bot.setWebhook("https://the-anti-spammer.herokuapp.com/" + '443409571:AAEUtkX0T74kJFotCl57ORJRJBl-fBeZQ-Q')
#updater.idle()