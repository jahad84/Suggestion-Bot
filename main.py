import discord
from discord.ext import commands
import os

prefix = '-'#تعديل مهم حط البرفكس حقكك
client = commands.Bot(command_prefix= f"{prefix}")
client.remove_command('help')

@client.command()
async def sug(ctx,* , sugg):
  channel = client.get_channel(741732875262623748) # id channel
  await ctx.channel.purge(limit=1)
  embed = discord.Embed(title='New Suggestion By {}'.format(ctx.author.display_name))
  embed.add_field(name='Suggestion: ', value=sugg)
  embed.set_footer(text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id, ctx.author.display_name), icon_url=ctx.author.avatar_url)
  await ctx.send('☑️ Your Suggestion Has Been Sent To <#{}> !'.format(channel.id))
  suggg = await channel.send(embed=embed)
  await suggg.add_reaction('👍')
  await suggg.add_reaction('👎')
@sug.error
async def sug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.channel.purge(limit=1)
      await ctx.send('**Please Type Your Suggestion!**')


@client.event
async def on_ready():
    print("I'am ready")

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

client.run(TOKEN)
