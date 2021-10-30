import asyncio

from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant

from TamilVc.services.callsmusic.callsmusic import client as USER
from TamilVc.config import SUDO_USERS

@Client.on_message(filters.command(["broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐆𝐜𝐚𝐬𝐭 🥳`")
        if not message.reply_to_message:
            await wtf.edit("❗ 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐀𝐧𝐲 𝐓𝐞𝐱𝐭 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐆𝐜𝐚𝐬𝐭!")
            return
        lmao = message.reply_to_message.text
        async for dialog in USER.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                #await wtf.edit(f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
                
            
        await message.reply_text(f"`Broadcast Finished ` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
