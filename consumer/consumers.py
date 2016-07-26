# -*- coding: utf-8 -*-
def getLine(text):
    leshaAnswers = text + u' и че'
    return leshaAnswers

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    answer = getLine(message.content['text'])
    message.reply_channel.send({
        "text": answer,
    })
