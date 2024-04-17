import discord
from discord.ext import commands
import googletrans
import os

translator = googletrans.Translator()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Transranto is on")

#Translator start

languages = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chichewa": "ny",
    "Chinese": "zh-cn",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Kurdish": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Odia (Oriya)": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala (Sinhalese)": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}

reverse_language = {value: key for key, value in languages.items()}

@client.command()
async def translate(ctx,*, text):
    if not text:
        await ctx.send("Please provide a message to translate.")
        return
    
    # Translate the text to the specified language
    translated = translator.translate(text, dest="en")
    detection = translator.detect(text)
    detected_language = detection.lang
    
    embed = discord.Embed(title = "Translation",description=translated.text,color = 0xdb3dfb)
    embed.add_field(name = "Detected language:",value = reverse_language[detected_language])

    # Send the translated message
    await ctx.send(embed = embed)

@client.command()
async def translateTo(ctx,lang,*, text):
    if not text:
        await ctx.send("Please provide a message to translate.")
        return
    
    # Translate the text to the specified language
    translated = translator.translate(text, dest=languages[lang.capitalize()])
    
    embed = discord.Embed(title = translated.text,color = 0xdb3dfb)

    # Send the translated message
    await ctx.send(embed = embed)

#Translator end
    
# @client.event
# async def on_message(message):
#     await client.process_commands(message)
#     author = message.author.name
#     channel = message.channel.name
#     output = client.get_channel(1214885269874937866)
#     translated = translator.translate(message.content, dest="pt")
#     if channel != "portuguese":
#         await output.send(embed = discord.Embed(title = f"{author} says on {channel}",description = translated.text,color = 0x6aa84f))

client.run(os.environ.get("token"))
