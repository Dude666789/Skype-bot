import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
last_member = None
duration = timedelta(minutes=1)
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
target_channel_id = 123456789012345678  # Replace with your target channel ID
target_vc_channel_id = 123456789012345678  # Replace with your target voice channel ID
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u00AD', '\u00A0', '\u0435']
def contains_invisible_characters(text):
    return any(char in invisible_chars for char in text)
#target_channel_id = 1418879042622455831
@tasks.loop(hours=24)
async def send_daily_message():
    channel = client.get_channel(target_channel_id)
    if channel:
        await channel.send("<:Skype:1418880953958404156>")
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    send_daily_message.start()





@client.event
async def on_message(message):
    global last_member
    
    if message.author == client.user:
        return
    last_member = message.author
    await client.process_commands(message)
    if "skype" in message.content.lower() or "skyp​e" in message.content.lower() or "skypе" in message.content.lower() or "skypе" in message.content.lower() or "skypｅ" in message.content.lower() or "skypｅ" in message.content.lower():
        await message.channel.send('Did someone say skype(<:Skype:1418880953958404156>)?( ͡° ͜ʖ ͡°)')
        audio_source = discord.FFmpegPCMAudio('discord_bot/assets/skype_ringtone.mp3')
        voice_channel = message.author.voice.channel if message.author.voice else None
        if voice_channel:
            voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
            if voice_client and voice_client.is_connected():
                if voice_client.channel != voice_channel:
                    await voice_client.move_to(voice_channel)
            else:
                voice_client = await voice_channel.connect()
                
            if not voice_client.is_playing():
                voice_client.play(audio_source)
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()
    if "discord.py" in message.content.lower():
        await message.channel.send('Did someone say discord.py?( ͡° ͜ʖ ͡°)(for reference, im coded in that)')
    if "ok" in message.content.lower() or "o k" in message.content.lower() or "o.k" in message.content.lower() or "o.k." in message.content.lower():
        await message.channel.send('O K <:Skype:1418880953958404156>')
    if "silver the hedgehog" in message.content.lower():
        await message.channel.send('Did someone say silver the hedgehog?( ͡° ͜ʖ ͡°)')
    if "y e s" in message.content.lower() or "y e s." in message.content.lower() or "y.e.s" in message.content.lower() or "y.e.s." in message.content.lower():
        await message.channel.send('https://tenor.com/view/principal-skinner-yes-seymour-skinner-the-simpsons-enthusiastic-yes-gif-15806751')
        await message.channel.send('Y E S <:Skype:1418880953958404156>')
    if contains_invisible_characters(message.content.lower()):
        await message.channel.send('Did someone say zero with space? That‡s not allowed bucko( ͡° ͜ʖ ͡°)')
        await last_member.timeout(duration, reason="Said the forbidden zero with space")
    if "skyping" in message.content.lower():
        await message.channel.send('I am skyping(<:Skype:1418880953958404156>) it so good?( ͡° ͜ʖ ͡°)')
    if "gamble please" in message.content.lower():
        await message.channel.send('Do you want to gamble your life away?( ͡° ͜ʖ ͡°)')
        def check(m):
            return m.author == message.author and m.channel == message.channel
        reply = await client.wait_for('message', check=check)
        if reply.content.lower() == 'yes':
            await message.channel.send('https://tenor.com/view/%D1%81%D1%82%D0%B8%D0%B2%D1%82%D0%B0%D0%BD%D1%86%D1%83%D0%B5%D1%82-%D1%81%D1%82%D0%B8%D0%B2-steve-steve-dancing-minecraft-gif-19716692')
            msg = await message.channel.send('You win, you lose, you gamble your life away!( ͡° ͜ʖ ͡°)(I was gonna add my gamble script, say if you want that)')
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
    if "scarlet fire" in message.content.lower():
        await message.channel.send('Did someone say scarlet fire?( ͡° ͜ʖ ͡°)')
        audio_source = discord.FFmpegPCMAudio('discord_bot/assets/scarlet_fire.mp3')
        voice_channel = message.author.voice.channel if message.author.voice else None
        if voice_channel:
            voice_client = discord.utils.get(client.voice_clients, guild=message.guild)
            if voice_client and voice_client.is_connected():
                if voice_client.channel != voice_channel:
                    await voice_client.move_to(voice_channel)
            else:
                voice_client = await voice_channel.connect()
                
            if not voice_client.is_playing():
                voice_client.play(audio_source)
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()
    if "crazy" and "hamburger" in message.content.lower():
        await message.channel.send('Did someone say Crazy Hamburger?( ͡° ͜ʖ ͡°)')
        await message.channel.send(file = discord.File('discord_bot/assets/crazy-hamburger.jpg'))
            
            
@client.event
async def on_member_join(member):
    channel = client.get_channel(1418861930382102550)
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}! Everyone say Skype to them! <:Skype:1418880953958404156>')
@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(target_vc_channel_id)
    if before.channel is None and after.channel is not None:
        voice_channel = after.channel
        voice_client = discord.utils.get(client.voice_clients, guild=member.guild)
        if voice_client and voice_client.is_connected():
            if voice_client.channel != voice_channel:
                await voice_client.move_to(voice_channel)
        else:
            voice_client = await voice_channel.connect()
                
        audio_source = discord.FFmpegPCMAudio('discord_bot/assets/skype_ringtone.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()
        if channel:
            await channel.send(f'{member.mention} has joined a voice channel! Say Skype to them! <:Skype:1418880953958404156>')
client.run()# Insert your bot token here
