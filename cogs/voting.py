import aiosqlite
import disnake
from disnake.ext import commands

DB = "userspecs.sqlite3"


class Voting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ignore_next_removed_reaction = {}

    @commands.command(aliases=["poll", "wahl"])
    @commands.has_permissions(manage_messages=True)
    async def vote(self, ctx: commands, title, *options: str) -> None:
        if len(title) > 256:
            await ctx.send("Der Titel kann nicht länger als 256 Zeichen sein")
        elif len(options) < 2:
            await ctx.send("Bitte gebe mindestens 2 Auswahlmöglichkeiten an.")
        elif len(options) > 20:
            await ctx.send("Maximal 20 Auswahlmölgichkeiten sind möglich.")

        else:
            codepoint_start = 127462
            options = {
                chr(i): f"{chr(i)} - {v}"
                for i, v in enumerate(options, start=codepoint_start)
            }
            embed = disnake.Embed(title=title, description="\n".join(options.values()))
            message = await ctx.send(embed=embed)
            for reaction in options:
                await message.add_reaction(reaction)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        user_id = data.user_id
        emoji = data.emoji
        channel = self.bot.get_channel(data.channel_id)
        message = await channel.fetch_message(data.message_id)
        server = channel.guild
        user = server.get_member(user_id)

        if user_id == self.bot.user.id:
            return
        elif message.author.id == self.bot.user.id:
            search = (
                user_id,
                data.message_id,
            )

            async with aiosqlite.connect(DB) as db:
                async with db.execute(
                        """SELECT user_id FROM voting WHERE user_id = ? AND message_id=?""",
                        search,
                ) as cursor:
                    result = await cursor.fetchone()

                    if result is None:
                        insert = (
                            data.message_id,
                            user_id,
                            str(emoji),
                        )
                        await db.execute(
                            """INSERT INTO voting VALUES (?,?,?)""", insert
                        )
                        await db.commit()

                    else:
                        await message.remove_reaction(emoji, user)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        user_id = data.user_id
        emoji = data.emoji
        search = (
            user_id,
            data.message_id,
            str(emoji),
        )
        async with aiosqlite.connect(DB) as db:
            async with db.execute(
                    """SELECT user_id FROM voting WHERE user_id = ? AND message_id=? AND emoji = ?""",
                    search,
            ) as cursor:
                result = await cursor.fetchone()

                if result is None:
                    pass
                else:
                    await db.execute(
                        """DELETE FROM voting WHERE user_id = ? AND message_id=? AND emoji = ?""",
                        search,
                    )
                    await db.commit()


def setup(bot):
    bot.add_cog(Voting(bot))
