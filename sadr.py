""" Sing a song... 
    Command .sadr

    By @veryhelpful"""

from telethon import events
import asyncio
import os
import sys
import random
from REBELBOT.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"sadr$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("@veryhelpful Making A Shayri for u.......")
    await asyncio.sleep(2)
    s=(random.randrange(1,10)) 
    if s==1:
        await event.edit("🙂Kehti Hain Zindagi Pyaar Kar Ke Toh Dekh ,\n Kya Pata Tha Jis Zindagi Ne Pyaar Mein Jeena Sikhaya,\n Aaj Wahi Gir Ke Samhalna Bhi Sikha Gayi☺️")
    if s==2:
        await event.edit("आज कुछ इस कदर याद आयी तेरी ..,\nआँसू गिर पड़े जैसे ...,\nनदी को नया मोड़ मिल गया !!")
    if s==3:
        await event.edit("कभी अपना कहते थे \n आज बेगाना कर गए...\n\nहमसे बात ना करने के लिए \n बहाना कर गए... \nशुक्रिया कैसे करूं तुम्हारा \nसमझ नहीं आ रहा...\nमेरे इस नियाने से दिल को \n**सयाना कर गए...* ")
    if s==4:
        await event.edit("जानती हूँ जवाब देना आसान नही \nपर कोशिश भी नही करते तुम ,\n मेरा हाल जानने की !!")
    if s==5:
        await event.edit("हम हर बिछड़न में नई मुलाकात को ढूंढते है !!\nतुम्हारे बार बार छोड़ जाने की अब ,\nआदत सी हो गयी है !!")
    if s==6:
        await event.edit("सोचते तो तब भी थे हम \nतुम मेरे नही हो सकते !!\nअब भी यकीन कहाँ है \n के तुम कभी मेरे थे !!")
    if s==7:
        await event.edit("पगला है वो ,\nना जाने इतना क्यों प्यार करता है !!\nकुछ बातें मेरी \n  कहने से पहले ही समझ जाता है !! ")    
    if s==8:
        await event.edit("आज कल हाल कुछ  \n Telephone booth की \nतरह हो गया है !!\n लोग आते है बात करते है ,\nऔर बस चले जाते है !")
    if s==9:
        await event.edit("दिल रोकना तो बहोत चाहता है \nमगर रोकेंगे नही ....!\nना तुम हमारे कुछ हो \nऔर हम भी तुम्हारे कुछ नही !!")
    if s==10:
        await event.edit("फर्क नही पड़ता सच मे ,\n कोई आये कोई जाए !!\nबस जो दिल को बार बार \n आदतें लग जाती है ना \nकिसी की ..!!\n बस छुड़ाने में कुछ देर लगती है !!")