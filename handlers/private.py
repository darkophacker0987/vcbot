import os

import youtube_dl
from youtube_search import YoutubeSearch
import requests

from helpers.filters import command, other_filters2, other_filters
from helpers.decorators import errors

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Voice

from config import BOT_NAME as bn, PLAY_PIC


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    cyber_pic = PLAY_PIC
    hell = f"I am **{bn}** !!\nI let you play music in your group's voice chat π\nTo get all commands and their explanation do /help\n\nEnjoy Streaming Music π"
    butts = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Group π¬", url="https://t.BONDOFBESTIZZ"
                ),
                InlineKeyboardButton(
                    "Channel π£", url="https://t.me/incredible_spam_bot"
                )
            ]
        ]
    )
    await message.reply_photo(
    photo=cyber_pic,
    reply_markup=butts,
    caption=cyber,
)


@Client.on_message(command("repo") & other_filters2)
async def repo(_, message: Message):
    await message.reply_text(
        f"""π€  Hoi!!
I'm **{bn}** and below is the my source code π

Happy Streaming π
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo π", url="https://github.com/darkhacker0987/vc_bot"
                    ),
                    InlineKeyboardButton(
                        "Channel π£", url="https://t.me/incredible_spam_bot"
                    ),
                    InlineKeyboardButton (
                        "OWNERπ΅", url="https;//t.me/Itz_me_cyberking"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("ping") & other_filters)
async def ping(_, message: Message):
    cybet_pic = PLAY_PIC
    await message.reply_photo(
    photo=cyber_pic,
    caption="I'm Alive and working fine. Do /help to get commands.\n\nHappy Streaming Music π",
)


@Client.on_message(command("song") & other_filters2)
@errors
async def a(client, message: Message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    okvai = query.capitalize()
    print(query.capitalize())
    m = await message.reply(f"**{bn} :-** π Searching for {okvai}")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            m.edit(f"**{bn} :-** π Found nothing. Try changing the spelling a little.\n\n{e}")
            return
    except Exception as e:
        m.edit(
           f"**{bn} :-** π Found Nothing. Sorry.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    await m.edit(f"**{bn} :-** π₯ Downloading...\n**Query :-** {okvai}")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'πΆ **Title:** [{title[:35]}]({link})\nβ³ **Duration:** {duration}\n'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await  message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        await m.delete()
    except Exception as e:
        m.edit(f"β Error!! \n\n{e}")
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)