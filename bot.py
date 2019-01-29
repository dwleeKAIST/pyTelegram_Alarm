import sys
import telegram
import time

token = '#########:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' # enter the token of the bot
chat_id = '########' # enter your telegram ID ( where to send msg )

def cur_time_str():
    _tuple = time.localtime()
    return time.strftime("%Y/%m/%d, %H:%M:%S", _tuple)
    
if __name__ == "__main__":
    bot = telegram.Bot(token = token)
    cur_t = cur_time_str()
    if len(sys.argv)>1:
        out_str = cur_t + '--> ' + sys.argv[1]
    else:
        out_str = cur_t
    bot.sendMessage(chat_id = chat_id, text=out_str)
