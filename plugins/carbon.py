from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from helper.errors import capture_err
from plugins.utils.functions import make_carbon

C = "**MADE WITH ❤️ BY >JEOL**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/beta_boTZ")
]]
)


@Client.on_message(
    filters.command("carbon")
    & ~filters.edited
)
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    m = await message.reply_text("Preparing Carbon")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
