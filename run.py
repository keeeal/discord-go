
import discord
from discord.ext import commands

def main():
    with open('token.txt') as f:
        token = f.readline()[:-1]

    bot = commands.Bot(command_prefix='!')

    @bot.command()
    async def play(context):
        await context.send("Let's play go!")

    bot.run(token)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    main(**vars(parser.parse_args()))
