import discord
from discord.ext import commands
import os
from prettytable import PrettyTable

prefix = '$' # Choose the prefix
client = commands.Bot(command_prefix= f"{prefix}", case_insensitive=True)
client.remove_command('help')
client.author_id = 740700552593145876  # Change to your discord id

@client.event
async def on_ready():
	activity = discord.Game(name=f"{client.command_prefix}sug | suggestion to continue 🙃", type=1)
	await client.change_presence(status=discord.Status.online, activity=activity)
	print('==================================================')
	tap = PrettyTable(['Name Bot', 'Tag', 'Id', 'prefix'])
	tap.add_row([client.user.name, f'#{client.user.discriminator}', client.user.id, client.command_prefix])
	print(tap)
	print('==================================================')
	print('All rights reserved © HazemMeqdad 2020')

# All rights reserved © HazemMeqdad 2020

@client.command(aliases=['suggestion', 'اقتراح'])
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
async def on_command_error(ctx, error):
    pass


from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('token')

client.run(TOKEN)

# All rights reserved © HazemMeqdad 2020
# Contact with me: https://discordapp.com/channels/@me/740700552593145876
