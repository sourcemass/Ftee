from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
[ ](https://telegra.ph/file/c1639eddea449ba4174ae.jpg)
✶ اهلا {}

✶ انا بوت اسمي {}


✶ اختصاص هذا البوت تحويل الصورة الى رابط تيليجراف

    """


    # About Message
    ABOUT = """

✶ Dev [Mohammad](t.me/PPF22)

✶ Bot Language [Python](www.python.org)

✶ Source [RsExs](t.me/vvvznn)

"""


    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✶ RsEXS", url="https://t.me/vvvznn")],
        [InlineKeyboardButton("✶ إغلاق", callback_data="close")],
        [InlineKeyboardButton(text="✶ الصفحة الرئيسية", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✶ Team RsExs", url="https://t.me/vvvznn")
        ],
        [
            InlineKeyboardButton("✶ حول البوت", callback_data="about")
        ],
        [InlineKeyboardButton("✶ إغلاق", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("✶ Team RsExs", url="https://t.me/vvvznn")],
        [InlineKeyboardButton("✶ إغلاق", callback_data="close")],
        [InlineKeyboardButton(text="✶ الصفحة الرئيسية", callback_data="home")]
    ]
