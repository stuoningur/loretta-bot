import datetime

import aiosqlite
import disnake
from disnake.ext import commands

DB = "userspecs.sqlite3"


class Specs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="specs", aliases=["s"], invoke_without_command=True)
    async def specs_command(self, ctx, *, user=None):
        if user is None:
            user = (ctx.message.author.id,)
        elif "@" in user:
            res = "".join(filter(lambda i: i.isdigit(), user))
            user = (int(res),)
        else:
            matches = [
                member
                for member in ctx.guild.members
                if user.lower() in member.display_name.lower()
            ]
            if len(matches) == 0:
                await ctx.send("Das Servermitglied konnte nicht gefunden werden.")
            elif len(matches) > 1:
                await ctx.send(
                    "Mehrere Servermitglieder gefunden, bitte schränke die Suche ein."
                )
            else:
                user = (matches[0].id,)

        if type(user) is tuple:
            guild_member = ctx.guild.get_member(user[0]).display_name
            async with aiosqlite.connect(DB) as db:
                async with db.execute(
                        """SELECT * FROM user_specs WHERE userid=?""", user
                ) as cursor:
                    result = await cursor.fetchone()
                    if result is not None:
                        embed = disnake.Embed(
                            title=f"PC von: {guild_member}",
                            colour=0xE74C3C,
                            description=result[1],
                        )
                        if result[2] is not None:
                            embed.add_field(
                                name="Zuletzt Aktualisiert:", value=f"{result[2]}"
                            )
                        else:
                            embed.add_field(
                                name="Zuletzt Aktualisiert:",
                                value="Wert konnte nicht gefunden werden.",
                            )
                        embed.set_footer(
                            text=f"Angefordert von {ctx.message.author.display_name}",
                            icon_url=ctx.message.author.avatar.url,
                        )
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send(
                            "Das Servermitglied hat keine Spezifikationen registriert."
                        )

    @specs_command.command(name="search")
    async def specs_search(self, ctx, *, arg: str = None):
        search_result = []
        search_term = (f"%{arg}%",)
        async with aiosqlite.connect(DB) as db:
            async with db.execute(
                    """SELECT userid FROM user_specs WHERE specs LIKE ?""", search_term
            ) as cursor:
                result = await cursor.fetchall()
                for search_id in result:
                    search_result.append(search_id[0])
        if len(search_result) == 0:
            await ctx.send(f"Keine Enträge mit {arg} gefunden.")
        else:
            guild_members = []
            for user in search_result:
                if ctx.guild.get_member(user) is not None:
                    guild_member = ctx.guild.get_member(user).display_name
                    guild_members.append(guild_member)
            embed = disnake.Embed(
                title=f"Suche nach: {arg}",
                colour=0xE74C3C,
                description="\n".join(guild_members),
            )
            embed.add_field(
                name=f"Insgesamt:",
                value=f"{len(guild_members)} Einträge gefunden",
                inline=False,
            )
            embed.set_footer(
                text=f"Angefordert von {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar.url,
            )
            await ctx.send(embed=embed)

    @specs_command.command(name="show")
    async def specs_show(self, ctx, *, user=None):
        await ctx.invoke(self.specs_command, user=user)

    @specs_command.command(name="set")
    async def specs_set(self, ctx, *, arg: str = None):
        today = datetime.datetime.now()
        time = today.strftime("%d.%m.%Y %H:%M:%S")
        user = (ctx.message.author.id,)
        async with aiosqlite.connect(DB) as db:
            async with db.execute(
                    """SELECT userid FROM user_specs WHERE userid = ?""",
                    user,
            ) as cursor:
                result = await cursor.fetchone()
                if result is not None:
                    user = str(ctx.message.author.id)
                    update_specs = (arg, time, user)
                    await db.execute(
                        """UPDATE user_specs SET specs=?, timestamp=? WHERE userid=?""",
                        update_specs,
                    )
                    await db.commit()
                    await ctx.send("Deine Spezifikationen wurden aktualisiert!")
                else:
                    user = ctx.message.author.id
                    insert_specs = (user, arg, time)
                    await db.execute(
                        """INSERT INTO user_specs VALUES (?,?,?)""",
                        insert_specs,
                    )
                    await db.commit()
                    await ctx.send("Deine Spezifikationen sind jetzt registriert!")

    @specs_command.command(name="delete")
    async def specs_delete(self, ctx):
        user = (ctx.message.author.id,)
        async with aiosqlite.connect(DB) as db:
            await db.execute(
                """DELETE FROM user_specs WHERE userid = ?""",
                user,
            )
            await db.commit()
        await ctx.send("Deine Spezifikationen wurden gelöscht!")


def setup(bot):
    bot.add_cog(Specs(bot))
