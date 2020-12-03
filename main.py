import discord 
from discord.ext import commands
import random

def test():
    print("hello")


#generrating the bot
client = commands.Bot(command_prefix = '.')


#Event
@client.event
async def on_ready():
    print('Bot is ready :0 ')

@client.event
async def on_member_join(member):
    print(f"{member} a rejoint le serveur.")
    print(f"Bonjour {member} !")

@client.event
async def on_member_remove(member):
    print(f"Bye Bye {member}")

#HELP command
@client.command(aliases=["what"])
async def help_me(ctx):
    help_command = ['ping: -> Renvoie le ping du serveur.',
                    'salutation: -> Dit bonjour au serveur.',
                    '_8ball: -> Répond à vos questions!',
                    'clear:  -> supprime les messages',
                    '** spécifier le nombre']

    await ctx.send("utiliser le point pour appeler les fonctions suivantes: \n")

    for x in range(len(help_command)):
        await ctx.send(f"\n {help_command[x]}")

#command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def salutation(ctx):
    await ctx.send("Hello world!")

@client.command(aliases=["8ball", "realy"])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'Without a doubt.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Ask again later.',
                 'My sources say no.',
                 'Very doubtful.',
                 'Yes.',
                 'You may rely on it.',
                 'Maybe',
                 'Of course!',
                 'Are you retarded',
                 'Nope sorry',
                 'hahahahahahahahahahahahaha!!!',
                 'Defenitly!']

    await ctx.send(f"Question : {question} \nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount=10):
    if amount > 500:
        await ctx.send("calme toi c'est pas un programme de la NASA")
    else:
        await ctx.channel.purge(limit=amount)



#Run
client.run('Nzg0MDgxNTAwMTg2MzQ1NTQ0.X8kGzQ.2GgJbKRBS3D1VKg53l4u9kJ2Wb0')

