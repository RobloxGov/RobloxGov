import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # เปิดใช้ Intent ที่ต้องการ

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def verify(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name="Verified")  # ชื่อของ role ที่ต้องการให้เมื่อยืนยันตัวตนแล้ว
    if role:
        await member.add_roles(role)
        await ctx.send(f'{member.mention} ได้รับการยืนยันตัวตนแล้ว!')
    else:
        await ctx.send('Role "Verified" ไม่พบในเซิร์ฟเวอร์นี้')

bot.run('YOUR_BOT_TOKEN')
