import sys
import telegram
import time


class BOTc():
    def __init__(self):
        super(BOTc).__init__()
        self.token = '#########:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' # enter the token of the bot
        self.bot = telegram.Bot(token = self.token)
        #self.updates = self.bot.getUpdates
        self.t_start = self.cur_time_str()
        self.chat_id = '########'# enter your telegram ID (where to send msg)

    def send(self,msg=''):
         self.bot.sendMessage(chat_id=self.chat_id,text=msg)

    def cur_time_str(self):
        _tuple = time.localtime()
        return time.strftime("%Y/%m/%d, %H:%M:%S", _tuple)

