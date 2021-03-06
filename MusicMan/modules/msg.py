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

import os
from MusicMan.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
**Haii ๐ Selamat datang di {PROJECT_NAME}, saya bot telegram musik id.

โฃ๏ธ {PROJECT_NAME} dapat memutar lagu di voice chat group dengan cara yang mudah, bot ini juga dilengkapi dengan berbagai fitur menarik yang dapat kamu coba loh.

โฃ๏ธ Assistant Music ยป @{ASSISTANT_NAME}\n\nKlik next untuk melihat instruksi penggunaan bot.**

""",

f"""
**โ PENGATURAN**

1. Jadikan bot sebagai admin di grup.
2. Mulai/Nyalakan obrolan suara / VCG
3. Ketik `/userbotjoin` dan coba ketik /play <nama lagu>
โ  Jika Assistant Bot bergabung ke grup, selamat menikmati musik, 
โ  Jika Assistant Bot tidak bergabung Silahkan Tambahkan @{ASSISTANT_NAME} ke grup Anda secara manual dan coba lagi.


**๐ Perintah untuk semua member grup:**

 ร /playlist : Untuk Menampilkan daftar putar Lagu sekarang
 ร /current : Untuk Menunjukkan  Lagu sekarang yang sedang diputar
 ร /song <judul lagu> : Untuk Mendownload lagu di YouTube 
 ร /video <judul lagu> : Untuk Mendownload Video di YouTube dengan detail
 ร /vsong <judul lagu> : Untuk Mendownload Video di YouTube dengan detail
 ร /deezer <judul lagu> : Untuk Mendownload lagu dari deezer 
 ร /saavn <judul lagu> : Untuk Mendownload lagu dari website saavn
 ร /search <judul lagu> : Untuk Mencari Video di YouTube dengan detail

**๐ Perintah ini hanya untuk admin:**

ร /play <judul lagu> : Untuk Memutar lagu yang Anda minta melalui youtube
ร /play <link yt> : Untuk Memutar lagu yang Anda minta melalui link youtube
ร /play <reply ke audio> : Untuk Memutar lagu yang Anda minta melalui file audio
ร /dplay : Untuk Memutar lagu yang Anda minta melalui deezer
ร /splay : Untuk Memutar lagu yang Anda minta melalui jio saavn
ร /skip : Untuk Menskip pemutaran lagu ke Lagu berikutnya
ร /pause : Untuk Menjeda pemutaran Lagu
ร /resume : Untuk Melanjutkan pemutaran Lagu yang di pause
ร /end : Untuk Menghentikan pemutaran Lagu
ร /userbotjoin - Untuk Mengundang asisten ke obrolan Anda
ร /admincache - Untuk MeRefresh admin list
"""
      ]
