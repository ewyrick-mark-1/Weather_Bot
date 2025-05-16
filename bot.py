import discord
import respond_current_data
import respond_gpt
import scheduler
import tracemalloc #tracemalloc is a troubleshooting tool
import json
import asyncio
from discord import app_commands
from discord.ext import commands
from discord.ext import commands

tracemalloc.start()


async def send_weather(channel):
    
    try:
        #print("1")
        response = respond_current_data.handle_response()
       # print("2")
        print(channel)
        await channel.send(response) 
        
        #print("3")
        
          
    except Exception as e:
        print(e)
        #print("bbbb")

async def send_weather_gpt(channel):
    
    try:
        #print("1")
        response = respond_gpt.handle_response()
       # print("2")
        print(channel)
        await channel.send(response) 
        
        #print("3")
        
          
    except Exception as e:
        print(e)
        #print("bbbb")

def run_discord_bot():
     TOKEN = 'MTE5MTUxMzg4NzQzOTMyMzE4Ng.GckpDt.W75DuF4iyFvEuRcYxEQPYKcryuZ6ieoZ9NO_Hc'
     client = commands.Bot(command_prefix="!", intents = discord.Intents.default() | discord.Intents(messages=True, message_content=True))
     
     
     @client.event
     async def on_ready():
          print(f'{client.user} is now running')
          scheduler.startsch(client.get_channel(1192297103905542164))# put channel you want the auto post to be in. (the string of numbers is the channel ID)
          #print("made it this far")

          try:
              synced = await client.tree.sync()
              print(f"Synced {len(synced)} command(s)")
          except Exception as e:
              print(e)

     @client.tree.command(name="weather_current")
     async def weather_current(interaction: discord.Interaction):
         
         await interaction.response.defer(ephemeral=True)  # defer
         await send_weather(interaction.channel)
         await interaction.followup.send("Action completed successfully!", ephemeral=True)
    
     @client.tree.command(name="weather_gpt")
     async def weather_gpt(interaction: discord.Interaction):
         
         await interaction.response.defer(ephemeral=True)  # defer
         await send_weather_gpt(interaction.channel)
         await interaction.followup.send("Action completed successfully!", ephemeral=True)    

     @client.tree.command(name="set_weather_channel")
     @app_commands.describe(channel_input = "which channel would you like recurring updates")
     async def set_weather_channel(interaction: discord.Interaction, channel_input : discord.TextChannel):
         
         await interaction.response.defer(ephemeral=True)
         await interaction.channel.send(f"{channel_input}")
         await interaction.followup.send("Action completed successfully!", ephemeral=True)


     @client.event
     async def on_message(message):
         if message.author == client.user:#makes sure it is a user and not the bot (stops endless loops)
             return
         
         
         username = str(message.author)
         user_message = str(message.content)
         channel = str(message.channel)

         print(f"{username} said: '{user_message}' ({channel})")#prints who said what where for debugging


         if message.content.startswith('!weather'):
            await send_weather(message.channel)

     client.run(TOKEN)

