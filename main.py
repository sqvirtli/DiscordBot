from http.client import responses
import discord # Подключаем библиотеку discord
from discord.ext import commands
from Cybernator import Paginator
from discord.ui import Button, View
import json # Подключаем библиотеку json

file = open('config.json', 'r')
config =json.load(file)

intents = discord.Intents.all() # Подключаем "Разрешения"
intents.message_content = True
# Подгружаем префикс и интенты
bot = commands.Bot(config['prefix'], intents=intents) 

# Класс для кнопок
class MyView(discord.ui.View):

    # Кнопка "Предметы"
    @discord.ui.button(label="Предметы", style=discord.ButtonStyle.red, emoji="⚔️")
    async def button_items(self, interaction, button):
        await interaction.response.send_message("Крутой меч!")

    # Кнопка "Мобы"
    @discord.ui.button(label="Мобы", style=discord.ButtonStyle.primary, emoji="👤")
    async def button_mobs(self, interaction, button):
        await interaction.response.send_message("Крутой моб!")
        
    # Кнопка "Квесты"
    @discord.ui.button(label="Квесты", style=discord.ButtonStyle.green, emoji="🔎")
    async def button_tasks(self, interaction, button):
        await interaction.response.send_message("Крутой квест!")

# Команда "Меню"
@bot.command()
async def menu(ctx):

# Главная вкладка "Меню"
    emb = discord.Embed(title='Навигация по РП',
        description='В этом меню находятся три вкладки.\n "Предметы" - все предметы которые можно найти в РП.\n "Мобы" - Любой моб или NPS которые есть в РП.\n "Квесты" - Все возможные квесты РП',
        color=discord.Color.gold()
    )
    
# Вкладка "Предметы"
    embitems = discord.Embed(
        title='Предметы',
        description='Вкладка разбита на\n "Оружие" - любое оружие существующие в РП\n "Броня" - любая броня существующая в РП\n "Еда" - любая еда существующая в РП\n  "Расходники" - любые расходники существующие в РП',
        color=discord.Color.red()
    )
# Вкладка "Оружие"
    embweapon = discord.Embed(
        title='Оружие',
        description='Оружейная Дариуса\n \nДеревянный Щит Блок 6. Цена 1 серебряная.\nПосох-дубина Сила 20. Цена 3 серебряных.\nКороткий лук Сила 5. Цена 50 медных.\nБоевой посох Сила 10. Цена 50 медных.\n \nЖелезный Меч Сила 10. Цена 2 серебряных.\nЖелезный Топор Сила 12. Цена 2 серебряных.\nЖелезная Сабля Сила 10. Цена 2 серебряных.\nЖелезные Кинжалы Сила 7. Цена 1.5 серебряных за шт.\nДлинный лук Сила 12. Цена 2 серебряных.\nКопье с железным наконечником Сила 12. Цена 2 серебряных.\nЖелезный Двуручный меч Сила 15. Цена 3 серебряных.\nЖелезный Двуручный молот Сила 16. Цена 3 серебряных.\nЖелезный Щит Блок15. Цена 5 серебряных.\n \nСтальной Меч Сила 15. Цена 4 серебряных.\nСтальная Булава Сила 20. Цена 5 серебряных.\nСтальной Ятаган Сила 16. Цена 3 серебряных.\nСтальные Кинжалы Сила 10. Цена 3 серебряных за шт.\nЛук из костей слона Сила 25. Цена 10 серебряных.\nАлебарда со стальным наконечником Сила 20. Цена 6 серебряных.\nСтальной Двуручный меч Сила 25. Цена 10 серебряных.\nСтальная Двуручная секира Сила 24. Цена 10 серебряных.\nСтальной Щит Блок 25. Цена 12 серебряных.',
        color=discord.Color.red()
    )
# Вкладка "Броня"
    embarmor = discord.Embed(
        title='Броня',
        description='"Броня" - любая броня существующая в РП',
        color=discord.Color.red()
    )
# Вкладка "Еда"
    embfood = discord.Embed(
        title='Еда',
        description='"Еда" - любая Еда существующая в РП',
        color=discord.Color.red()
    )
# Вкладка "Расходники"
    embother = discord.Embed(
        title='Расходники',
        description='"Расходники" - любые расходники существующие в РП',
        color=discord.Color.red()
    )
# Вкладка "Мобы"
    embmobs = discord.Embed(
        title='Мобы',
        description='Вкладка разбита на\n "Враждебные" - все виды агресивных мобов в РП\n "NPS" - любой моб с которым можно как-то взаимодействовать в РП\n "Мирные" - любая моб который сразу не нападает',
        color=discord.Color.blurple()
    )
# Вкладка "Враждебные"
    embenemy = discord.Embed(
        title='Враждебные',
        description='"Враждебные" - все виды агресивных мобов в РП',
        color=discord.Color.blurple()
    )
# Вкладка "NPS"
    embnps = discord.Embed(
        title='NPS',
        description='"NPS" - любой моб с которым можно как-то взаимодействовать в РП',
        color=discord.Color.blurple()
    )
# Вкладка "Мирные"
    embpeaceful = discord.Embed(
        title='Мирные',
        description='"Мирные" - любая моб который сразу не нападает',
        color=discord.Color.blurple()
    )

# Вкладка "Квесты"
    embtasks = discord.Embed(
        title='Квесты',
        description='Вкладка разбита на\n "Боевые" - квест, основной задачей которого является победа кого-либо в РП\n "Сбор" - квест, основной задачей которого является сбор каких либо ресурсов\n "Приключения" - квест, основной задачей которого является выплнение какой либо миссии связаной с загадками и приключениями',
        color=discord.Color.green()
    )

# Вкладка "Боевые"
    embfights = discord.Embed(
        title='Боевые',
        description='"Боевые" - квест, основной задачей которого является победа кого-либо в РП',
        color=discord.Color.green()
    )
# Вкладка "Сбор"
    embfarms = discord.Embed(
        title='Сбор',
        description='"Сбор" - квест, основной задачей которого является сбор каких либо ресурсов',
        color=discord.Color.green()
    )
# Вкладка "Приключения"
    embadventures = discord.Embed(
        title='Приключения',
        description='"Приключения" - квест, основной задачей которого является выплнение какой либо миссии связаной с загадками и приключениями',
        color=discord.Color.green()
    )

    embs = [emb, [embitems, embweapon, embarmor, embfood ,embother], [embmobs, embenemy, embnps, embpeaceful],[embtasks, embfights, embfarms, embadventures]]
    

    await ctx.send(embed=emb, view=MyView())
#    page = Paginator(bot, message, only=ctx.author, use_more=True, embeds=embs, footer=False, timeout= 150, delete_message= 150)
#    await page.start()


bot.run(config['token'])
