# pyTelegram_Alarm
Python implementation to text to you while training some deep network.

Before the clone this git repository,
you need to generate the telegram bot to send you the msg.
You need the followings for your implementation:

1.token of your bot

2.Your telegram ID ( digits )


---- Necessary library ------

python-telegram-bot

---- How to use ----------------

First, edit the token of your bot and your telegram ID in bot.py/BOTc.py


Example for bot.py :

python3 bot.py 'Hello, world'

Example for BOTc.py :

~~~~~~~~~~~~~~( your_main_code.py )~~~~~~~~~~~~~

...

from BOTc import BOTc

myBot = BOTc()

...

myBot.send('%d epoch : Train Accuracy : %.4f' %(iEpoch, acc_train) )

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



