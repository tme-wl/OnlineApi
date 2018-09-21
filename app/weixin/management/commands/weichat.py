from django.core.management.base import BaseCommand
from itchat.content import *
from weixin.models import Message

import itchat

myself = '大吉'


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    nickname = msg.actualNickName
    if not nickname:
        nickname = myself
    text = msg.text
    obj = Message()
    obj.name = nickname
    obj.text = text
    obj.save()


class Command(BaseCommand):
    def run(self):
        itchat.auto_login(enableCmdQR=2)
        itchat.run()

    def handle(self, *args, **options):
        self.run()
