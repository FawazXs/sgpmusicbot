# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from MusicMan.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicMan.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Haii π{message.from_user.first_name}, saya adalah {PROJECT_NAME}.\n
Saya bot musik yang dapat memutar lagu di voice chat group dengan cara yang mudah, saya memiliki banyak fitur praktis seperti:\n
βββββββββββββββ
β  memutar Musik.
β  mendownload Lagu.
β  mencari lagu untuk diputar & di unduh.
β  Gunakan perintah /help untuk melihat fitur lengkap saya.
βββββββββββββββ
π Created by: {OWNER}
π Thanks To [SaΝ₯α΄pΝ£oΝ«erΕaα΄iβd ΰ¦ΰ§£Ν‘ssid](https://t.me/NeetflixHD)
βββββββββββββββ
Silahkan tambahkan saya dan @asistenSgpmusik ke dalam grup anda agar dapat memutar musik di vcg.
</b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Tambahkan Saya Ke Grup Anda β", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "π£ CHANNEL", url=f"https://t.me/joinchat/m0igZdtuGl81MTll"), 
                    InlineKeyboardButton(
                        "π¬ GROUP", url=f"https://t.me/joinchat/NTSKWi0Syhs2NzAx")
                ],[
                    InlineKeyboardButton(
                        "π OWNER", url=f"https://t.me/NeetflixHD")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next Β»', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("β Tambahkan Saya Ke Grup Anda β", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = 'π£ CHANNEL', url=f"https://t.me/joinchat/m0igZdtuGl81MTll"),
             InlineKeyboardButton(text = 'π¬ GROUP', url=f"https://t.me/joinchat/NTSKWi0Syhs2NzAx")],
            [InlineKeyboardButton(text = 'π OWNER', url=f"https://t.me/NeetflixHD")],
            [InlineKeyboardButton(text = 'Β« back', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'Β«', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'Β»', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "ππ»ββοΈ **apakah anda ingin mencari link youtube ?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "β YA", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β TIDAK", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**tekan tombol dibawah untuk melihat panduan menggunakan bot.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Cara Menggunakan BOT π", url="https://telegra.ph/command-list-05-18"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""β Bot **berhasil dimulai ulang!**\n\nβ’ **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π¬ GROUP", url=f"https://t.me/joinchat/NTSKWi0Syhs2NzAx"
                    ),
                    InlineKeyboardButton(
                        "π OWNER", url=f"https://t.me/NeetflixHD"
                    )
                ]
            ]
        )
   )

