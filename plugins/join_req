from utils import temp
from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from database.users_chats_db import db
from Script import script
from info import DELETE_TIME, AUTH_CHANNEL, ADMINS, OWNER_LINK, MOVI_CHNL, MOVI_GRP
from database.ia_filterdb import get_file_details
from utils import get_settings, get_size
import asyncio


@Client.on_chat_join_request()
async def join_reqs(client, join_req):
    rfsub_id = await db.get_rfsub_id()
    channel_id = rfsub_id if rfsub_id else int(AUTH_CHANNEL)
    if join_req.chat.id != channel_id:
        return

    user_id = join_req.from_user.id
    # Add user to req collection
    await db.add_join_req(user_id)

    # Check if there's a pending file request
    if str(user_id) in temp.AUTO_ACCEPT:
        file_id = temp.AUTO_ACCEPT[str(user_id)]['file_id']
        grp_id = temp.AUTO_ACCEPT[str(user_id)]['grp_id']
        mode = temp.AUTO_ACCEPT[str(user_id)]['mode']

        try:
            files_ = await get_file_details(file_id)
            if not files_:
                await client.send_message(user_id, '<b>⚠️ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ⚠️</b>')
                return
            files = files_[0]

            settings = await get_settings(int(grp_id))
            CAPTION = settings.get('caption', '')
            f_caption = CAPTION.format(
                file_name=files.file_name,
                file_size=get_size(files.file_size)
            )

            msg = await client.send_cached_media(
                chat_id=user_id,
                file_id=file_id,
                caption=f_caption,
                protect_content=settings.get('file_secure', False),
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("• പുതിയ സിനിമകൾ •", url=MOVI_CHNL)
                    ],[
                        InlineKeyboardButton("• മൂവീസ് ഗ്രൂപ്പ് •", url=MOVI_GRP)
                    ]
                ])
            )

            try:
                await asyncio.sleep(DELETE_TIME)
                await msg.delete()
            except Exception as delete_error:
                await client.send_message(
                    LOG_CHANNEL,
                    f"Error deleting file for user {user_id}, file_id {file_id}: {delete_error}"
                )
        except Exception as e:
            await client.send_message(
                LOG_CHANNEL,
                f"Error sending file to user {user_id}, file_id {file_id}: {e}"
            )
            await client.send_message(
                user_id,
                "<b>⚠️ Error sending file. Please try again later.</b>"
            )
        finally:
            if str(user_id) in temp.AUTO_ACCEPT:
                del temp.AUTO_ACCEPT[str(user_id)]


@Client.on_message(filters.command("delete_requests") & filters.private & filters.user(ADMINS))
async def delete_requests(client, message):
    await db.del_join_req()
    await message.reply("<b>⚙ Successfully deleted all channel join requests</b>")
