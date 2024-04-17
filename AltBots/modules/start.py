from telethon import version, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [
        Button.inline("COMMNDS", data="help_back")
    ],
    [
        Button.url("CHANNEL", "https://t.me/MRITYUY"),
        Button.url("SUPPORT", "https://t.me/MRITYUY")
    ],
    [
        Button.url("REPO", "https://t.me/MRITYUY")
    ]
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = (
            f"Hey [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nI am [{bot_name}](tg://user?id={bot_id})\n"
            f"My developer: [NOBITA](https://t.me/MRITYUY)\n"
            f"Xbots version: M3.3\n"
            f"Python version: 3.11.3\n"
            f"Telethon version: {version}\n"
        )
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/451182063e3670fa369d9.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
