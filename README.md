# pyTelegram_Alarm
Python implementation to text to you while training some deep network.

Before the clone this git repository,
you need to generate the telegram bot to send you the msg.
You need the followings for your implementation:

1.token of your bot

2.Your telegram ID ( digits )

--------------------------------
-- necessary libraries --
pip3 install python-telegram-bot



------------------------------
How to Use.

example#1 :
python3 bot.py 'Hello, world'

example#2 :
~~~~~~~~~~~~~~( your_main_code.py )~~~~~~~~~~~~~
...
from BOTc import BOTc
myBot = BOTc()
...

myBot.send('%d epoch : Train Accuracy : %.4f' %(iEpoch, acc_train) )
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



