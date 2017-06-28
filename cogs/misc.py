import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import time
import random
import asyncio

class Misc():


    def __init__(self, bot):
        self.bot = bot
        self.ball = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
                     'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
                     'Reply hazy try again',
                     'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                     'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
                     'Very doubtful']
        self.selfroles = ['Subscriber','Hype']

    async def send_cmd_help(self,ctx):
        if ctx.invoked_subcommand:
            pages = self.bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await self.bot.send_message(ctx.message.channel, page)
        else:
            pages = self.bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await self.bot.send_message(ctx.message.channel, page)

    @commands.command(pass_context=True)
    async def embedsay(self,ctx, *, message: str = None):
        '''Embed something as the bot.'''
        color = ("#%06x" % random.randint(8, 0xFFFFFF))
        color = int(color[1:],16)
        color = discord.Color(value=color)
        if message:
            msg = ctx.message
            emb = discord.Embed(color=color,description=message)
            await self.bot.delete_message(msg)
            await self.bot.say(embed=emb)
        else:
            await self.bot.say('Usage: `.embedsay [message]`')


    @commands.command()
    async def say(self,*, message: str):
        '''Say something as the bot.'''
        if '@everyone' in message:
            await self.bot.say('Not so fast cheeky boi xdd')
        elif '@here' in message:
            await self.bot.say('Ayy lmao, it doesnt work.')
        else:       
            await self.bot.say(message)

            
    @commands.command()
    async def add(self,*args):
        '''Add multiple numbers.'''
        ans = 0
        try:
            for i in args:
                ans += int(i)
            await self.bot.say(ans)
        except:
            await self.bot.say('Enter numbers only.')
            

    @commands.command(pass_context=True,description='Response time is in ms.')
    async def ping(self,ctx):
        '''Check response time.'''
        msgtime = ctx.message.timestamp.now()
        await (await self.bot.ws.ping())
        now = datetime.datetime.now()
        ping = now - msgtime
        pong = discord.Embed(title='Pong! Response Time:', description=str(ping.microseconds / 1000.0) + ' ms',
                             color=0x00ffff)
        pong.set_thumbnail(url='https://i.imgur.com/PWw08sX.png')
        await self.bot.send_message(ctx.message.channel, embed=pong)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


    @commands.command(pass_context=True)
    async def virus(self,ctx,user: discord.Member=None,*,hack=None):
        """Inject a virus into someones system."""
        nome = ctx.message.author
        if not hack:
            hack = 'discord'
        else:
            hack = hack.replace(' ','_')
        channel = ctx.message.channel
        x = await self.bot.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
        await asyncio.sleep(1.5)
        x = await self.bot.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
        await asyncio.sleep(0.3)
        x = await self.bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
        await asyncio.sleep(1.2)
        x = await self.bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
        await asyncio.sleep(1)
        x = await self.bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
        await asyncio.sleep(1.5)
        x = await self.bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
        await asyncio.sleep(1)
        x = await self.bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
        await asyncio.sleep(1)
        x = await self.bot.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
        await asyncio.sleep(2)
        x = await self.bot.edit_message(x,'``Injecting virus.   |``')
        await asyncio.sleep(0.5)
        x = await self.bot.edit_message(x,'``Injecting virus..  /``')
        await asyncio.sleep(0.5)
        x = await self.bot.edit_message(x,'``Injecting virus... -``')
        await asyncio.sleep(0.5)
        x = await self.bot.edit_message(x,'``Injecting virus....\``')
        await self.bot.delete_message(x)
        await self.bot.delete_message(ctx.message)
        
        if user:
            await self.bot.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
            await self.bot.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
        else:
            await self.bot.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(user.name))
            await self.bot.send_message(nome,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
     
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


    @commands.group(name='self',pass_context=True,description='Selfrole commands for set roles')
    async def self_(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.send_cmd_help(ctx)

    @self_.command(pass_context=True)
    async def list(self,ctx):
        """Current list of allowable selfroles."""
        await self.bot.say('Current list of self roles: {}'.format(', '.join(self.selfroles)))
            
    @self_.command(pass_context=True)
    async def role(self,ctx,role):
        """Give yourself a role."""
        user = ctx.message.author
        server = ctx.message.server
        channel = ctx.message.channel
        frole = role.lower().strip()
        roles_ = [i.lower() for i in self.selfroles]
        sroles = {}
        for i in server.roles:
            x = i.name.lower()
            for role in roles_:
                if x == role:
                    sroles[x] = i
        for r in sroles:
            if r.startswith(frole):
                frole = sroles[r]
                break
        if frole is not None:            
            if frole not in user.roles:
                await self.bot.add_roles(user,frole)
                await self.bot.say('You now have the **{}** role.'.format(frole.name))
            else:
                await self.bot.remove_roles(user,frole)
                await self.bot.say('Removed the **{}** role.'.format(frole.name)) 
        else:
            await self.bot.say('I cant find that role.')

    @commands.command(pass_context=True, aliases=['8ball'])
    async def ball8(self, ctx, *, msg: str):
        """Let the 8ball decide your fate."""
        answer = random.randint(0, 19)
        
        if answer < 10:
            color = 0x008000
        elif 10 <= answer < 15:
            color = 0xFFD700
        else:
            color = 0xFF0000
        em = discord.Embed(color=color)
        em.add_field(name='\u2753 Question', value=msg)
        em.add_field(name='\ud83c\udfb1 8ball', value=self.ball[answer], inline=False)
        await self.bot.send_message(ctx.message.channel, content=None, embed=em)
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        '''Returns the OAUTH invite linke'''
        await self.bot.say('https://discordapp.com/oauth2/authorize?client_id=326703531220271104&scope=bot&permissions=8')

    
def setup(bot):
    bot.add_cog(Misc(bot))
