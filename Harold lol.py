import discord
from discord import Embed, Member
from discord.ext.commands import Bot
from discord.ext import commands
import random
import random as dice
import time
import inspect
import pip
from typing import Type

client = commands.Bot("h%")
client.remove_command("help")
messages = ["All hail Miso", "Harold is god", "Fookie"]

@client.event
async def on_ready():
    print('Guys We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='hiding the pain|h%help'))


@client.event
async def on_member_join(member):
    await member.guild.get_channel('456444044915245058').send
    (random.choice([f"Your mom gay <@{member.id}> <:XD:456984087513530389> .",
                    f"Your ancestor incestors <@{member.id}> lol.",
                    f"Your mom a flaming homosexual <@{member.id}> <:Thonk:458454352726720513> .",
                    f"Your mom and dad gay together <@{member.id}> tbh",
                    f"Yer nanny a homo <@{member.id}> lul",
                    f"Tbh you are as gay as your mom <@{member.id}> XDDDD",
                    f"Your nana a banana <@{member.id}>", ]))



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Fuckin retard, There is no command like that do h%help")
    else:
        embed = discord.Embed(title="Error:",
                              description=f"{error}",
                              colour=0xe73c24)
        await ctx.send(embed=embed)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if 'DESPACITO' in message.content.upper():
        client.get_emoji(457171368358969354)
        await message.add_reaction('Despacito:457171368358969354')
        await message.channel.send("I just reacted with dame tu cosita a.k.a despacito 2 lol")
    if '<@450583639638540288>' in message.content:
        if message.author.id == 382026183040303125:
            await message.channel.send("Shifu owo")
        else:
            await message.channel.send("Hey guys some faggot just pinged me,I wonder who it is :thinking:")


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Help", description="Help Menu lol", color=0x00ff00)
    embed.add_field(name="help", value="help - shows this command", inline=False)
    embed.add_field(name="main_commands", value="Commands for normal plebs", inline=False)
    embed.add_field(name="mod_commands", value="Commands for mods", inline=False)
    embed.add_field(name="admin_commands", value="Commands for admins", inline=False)
    embed.set_footer(text="Developed by Miso™#7681")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('\U00002705')


@client.command(pass_context=True)
async def main_commands(ctx):
    embed = discord.Embed(title="Main_commands", description="Main commands xD", color=0x00ff00)
    embed.add_field(name="8ball", value="Yes/No (this is never wrong)", inline=False)
    embed.add_field(name="dab", value="sends a random dab image/GIF", inline=False)
    embed.add_field(name="info", value="Tells you about harold", inline=False)
    embed.add_field(name="givetips", value="Gives tips for life", inline=False)
    embed.add_field(name="coinflip", value="flips the coin xD", inline=False)
    embed.add_field(name="dick", value="how big is your dick?", inline= False)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('\U00002705')


@client.command(pass_context=True)
async def mod_commands(ctx):
    embed = discord.Embed(title="Mod_commands", description="Commands that mods can use", color=0x00ff00)
    embed.add_field(name="kick", value="kicks people who broke the rules", inline=False)
    embed.add_field(name="ban", value="swings the ban hammer on retards", inline=False)
    embed.add_field(name="strike", value="warns people breaking the rules", inline=False)
    embed.add_field(name="mute", value="mutes people breaking the rules", inline=False)
    embed.add_field(name="unmute", value="unmutes people who repented", inline=False)
    embed.add_field(name="roll", value="rolls someone's ass in roulette", inline=False)
    embed.add_field(name="probe", value="clears messages in the channel(limit is 500)", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('\U00002705')


@client.command(pass_context=True)
async def admin_commands(ctx):
    embed = discord.Embed(title="admin_commands", description="Commands that admins can use", color=0x00ff00)
    embed.add_field(name="send", value="Sends some trash", inline=False)
    embed.add_field(name="die", value="Dies and logsout", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('\U00002705')


@client.command()
async def die(ctx):
    if ctx.author.id == 382026183040303125:
        await ctx.send("dies")
        await client.logout()
    else:
        await ctx.send("You can't kill me lol")


@client.command(pass_context=True)
async def dick(ctx):
    await ctx.send(f'Dick size of {ctx.author} is 8{"=" * random.randint(0, 50)}D')


@client.command(pass_context=True, name='8ball')
async def _ball(ctx):
    await ctx.send(random.choice(["Ye cunt",
                                 "No idiot",
                                 "Dude wtf is wrong with you",
                                 "Lolno go die xd",
                                 "Please try again",
                                 "Maybe..",
                                 "Over my dead body",
                                 "YESSS",
                                 "Yesn't",
                                 "Of course mate",
                                 "Yeah fam"]))


@client.command(pass_context=True)
async def coinflip(ctx):
    await ctx.send(random.choice([ctx.message.author.mention + " flipped the coin and got Heads",
                                  ctx.message.author.mention + " flipped the coin and got Tails"]))


@client.command(pass_context=True)
async def dab(ctx):
    embed = discord.Embed()
    embed.set_image(url=random.choice(["https://i.imgur.com/rRlogPT.jpg",
                                       "https://i.imgur.com/szETMKl.jpg",
                                       "https://i.imgur.com/P9iNP38.jpg",
                                       "https://i.imgur.com/tXfQhrA.jpg",
                                       "https://media.giphy.com/media/1SyVh1hiw4vm7VUyTV/giphy.gif",
                                       "https://gph.is/2t7TmNw",
                                       "https://imgur.com/IVajFdo",
                                       "https://media.giphy.com/media/3h5VTO6F1i2gU/giphy.gif",
                                       "https://media.giphy.com/media/3oEjI7M0cOXG0j4HWU/giphy.gif",
                                       "https://media.giphy.com/media/3oz8xPyx3qgq5jAmMo/giphy.gif",
                                       "https://media.giphy.com/media/26uTt19akcFxRFCy4/giphy.gif", ]))
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def givetips(ctx, member: discord.Member):
    await ctx.send(random.choice(["{}, being gay is the key to life".format(member.mention),
                                  "Hang yourself {} for that is the way of life".format(member.mention),
                                  "MeMs CURES DEPRESSION {}".format(member.mention),
                                  "grow up {} yer dirty swine".format(member.mention), ]))


@client.command(pass_context=True)
async def image(ctx):
    embed = discord.Embed()
    embed.set_image(url="https: // cdn.discordapp.com / attachments / 456449063169294350 / 459935883349458954 / OoF.gif")
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def rules(ctx):
    embed = discord.Embed(title="RULES", description="Follow discord guidelines too xD", color=0xf8470c)
    embed.add_field(name='1', value = "Don't spam", inline=False)
    embed.add_field(name='1', value = "Don't spam", inline=False)
    embed.add_field(name='1', value = "Don't spam", inline=False)
    embed.add_field(name='2', value = "Respect everyone", inline=False)
    embed.add_field(name='3', value = "Don't be a homophobic faggot", inline=False)
    embed.add_field(name='4', value = "No racism lol", inline = False)
    embed.add_field(name='5', value = "You can argue with mods, until they mute or ban you lol", inline=False)
    embed.add_field(name='6', value = "Don't be afraid to turn down dm advertisers but its rude tho", inline=False)
    embed.add_field(name='7', value = "Banned memes and animes are not allowed", inline=False)
    embed.add_field(name='8', value = "Don't post gore shit since they are against discord tos", inline=False)
    embed.add_field(name='9', value = "Please don't use other languages", inline=True)
    embed.set_footer(text = "Powered by Lucian's fat body™")
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def kick(ctx, member: discord.Member, *args):
    """Kick the member off the server lol."""
    if ctx.author.guild_permissions.kick_members:
        reason = ' '.join(args)
        await member.kick()
        await ctx.send(f"{member.mention} has been kicked from {ctx.guild.name}")
        await member.send(f"You have been kicked from {ctx.guild.name} for {reason}")
    else:
        await ctx.send(":no_entry: You are not a mod!")


@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, *args):
    """Bans the member off the server lol."""
    if ctx.author.guild_permissions.ban_members:
        reason = ' '.join(args)
        await ctx.send(f"{member.mention} has been banned from {ctx.guild.name} by {ctx.author.mention}")
        await member.ban(reason=reason)
        await member.send(f"You have been banned from {ctx.guild.name}, {reason}")

    else:
        await ctx.send(":no_entry: You are not a mod!")


@client.command(pass_context=True)
async def work(ctx):
    money = random.randint(100, 150)
    await ctx.send(f"You cashed in {money}:moneybag: ")


@client.command(pass_context=True)
async def strike(ctx, member: discord.Member, *args):
    if ctx.author.guild_permissions.kick_members:
        mesg = ' '.join(args)
        await ctx.message.delete()
        await member.send(f"You have been striked :{mesg}")
        await ctx.send(f"{member.name} has been striked by {ctx.author.mention}")

    else:
        await ctx.send(":no_entry: You are not a mod!")


@client.command(pass_context=True)
async def roll(ctx, member: discord.Member, xp: int):
    if ctx.author.guild_permissions.ban_members:
        random_number = random.randint(1, 6)
        if xp > 2500:
            await ctx.send(f"{ctx.author.mention} rolled {member.name} at {random_number} lol")
            time.sleep(5)
            if random_number in [5, 6]:
                await ctx.send(f"@everyone this is so sad {member.mention} won the doomed weeb role, Can we hit children?")
                role = discord.utils.get(member.guild.roles, name="Doomed weebs")
                await member.add_roles(role)
            else:
                await ctx.send(f"Congrats {member.mention} won the Thigh connoisseur role")
                role = discord.utils.get(member.guild.roles, name="Thigh connoisseur")
                await member.add_roles(role)
        else:
            if random_number is 4:
                await ctx.send(f"{ctx.author.mention} rolled {member.name} at {random_number} lol")
                time.sleep(5)
                await ctx.send(f"Congrats {member.mention} won the Thigh connoisseur role")
                role = discord.utils.get(member.guild.roles, name="Thigh connoisseur")
                await member.add_roles(role)
            else:
                await ctx.send(f"{ctx.author.mention} rolled {member.name} at {random_number} lol")
                role = discord.utils.get(member.guild.roles, name="Thigh connoisseur")
                await member.add_roles(role)
    else:
        await ctx.send("You do not have permissions to roll their ass")


@client.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    """Mute the client on the server."""
    if "Knights" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Doomed weebs")
        await member.add_roles(role)
        await ctx.send(f"Ok the {member.mention} is Muted!")
        overwrite = discord.PermissionOverwrite()
        overwrite.ctx.send = False
        for each in ctx.guild.channels:
            await each.set_permissions(member, overwrite=overwrite)


@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    """Unmute the client on the server."""
    if "Knights" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(member.guild.roles, name="Doomed weebs")
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} repented and is now unmuted")
        overwrite = discord.PermissionOverwrite()
        overwrite.ctx.send = None
        for each in ctx.guild.channels:
            await each.set_permissions(member, overwrite=overwrite)


@client.command(pass_context=True)
async def probe(ctx, num: int, target: discord.Member = None):
    if num > 500 or num < 0:
        await ctx.send("Invalid amount. Maximum is 500.")
        return

    def msgcheck(amsg):
        if target:
            return amsg.author.id == target.id
        return True

    await ctx.channel.purge(limit=num, check=msgcheck)
    await ctx.send(f" :ok_hand::skin-tone-5: Probed **{num}** messages for you lol ", delete_after=10)


@client.command(pass_context=True)
async def send(ctx, *args):
    if ctx.author.guild_permissions.administrator:
        mesg = ' '.join(args)
        await ctx.message.delete()
        await ctx.guild.get_channel(456444044915245058).send(mesg)
    else:
        await ctx.send("You are not an admin lol")


@client.command()
@commands.is_owner()
async def source(ctx, *, text: str):
    """Shows source code of a command."""
    nl2 = '`'
    nl = f"``{nl2}"
    source_thing = inspect.getsource(client.get_command(text).callback)
    await ctx.send(f"{nl}py\n{source_thing}{nl}")


client.run('NDUwNTgzNjM5NjM4NTQwMjg4.DgfOQg.tUBR0w4IKykB4CaIai3AQVPXt7E')
