
import discord
from discord.ext import commands

from dlgo import agent
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import *

with open('token.txt') as f:
    token = f.readline()[:-1]

board_size = 13
human = gotypes.Player.black
client = commands.Bot(command_prefix='')
game = goboard.GameState.new_game(board_size)
bot = agent.RandomBot()

@client.event
async def on_ready():
    print('Logged in as', client.user.name)

@client.command()
async def show(context):
    await context.send(print_board(game.board))

@client.command()
async def play(context, *args):
    global game

    if game.next_player is human:

        # human's turn
        point = point_from_coords(''.join(args).upper())
        move = goboard.Move.play(point)
        await context.send(print_move(game.next_player, move))
        game = game.apply_move(move)
        await context.send(print_board(game.board))

        while game.next_player is not human:

            # bot's turn(s)
            move = bot.select_move(game)
            await context.send(print_move(game.next_player, move))
            game = game.apply_move(move)
            await context.send(print_board(game.board))

    else:
        await context.send('It is not your turn yet...')

client.run(token)
