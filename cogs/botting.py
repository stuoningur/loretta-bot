import aiohttp
import disnake
from disnake.ext import tasks, commands

urls = {
    "NVIDIA RTX 3080 Ti": "as",
    "NVIDIA RTX 3070 Ti": "das",
    "NVIDIA RTX 3060 Ti": "xcv",
    "NVIDIA RTX 3090": "asd",
    "NVIDIA RTX 3070": "sdf",
    "NVIDIA RTX 3080": "sdf",
}


class Botting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.botting.start()

    @tasks.loop(seconds=15.0)
    async def botting(self):
        channel = self.bot.get_channel(int(self.bot.stock_channel))
        skus = {
            "NVGFT060T_DE": "NVIDIA GeForce RTX 3060 Ti",
            "NVGFT070T_DE": "NVIDIA GeForce RTX 3070 Ti",
            "NVGFT070_DE": "NVIDIA GeForce RTX 3070",
            "NVGFT080T_DE": "NVIDIA GeForce RTX 3080 Ti",
            "NVGFT080_DE": "NVIDIA GeForce RTX 3080",
            "NVGFT090_DE": "NVIDIA GeForce RTX 3090",
        }

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Connection": "keep-alive",
        }
        timeout = aiohttp.ClientTimeout(total=10)

        async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
            async with session.get(self.bot.nvidia_url) as resp:
                if resp.status == 200:
                    json_content = await resp.json()
                    for sku in json_content["listMap"]:
                        if sku["fe_sku"] in skus:
                            if sku["is_active"] == "true":
                                name = skus[sku["fe_sku"]]
                                price = sku["price"]
                                product_url = sku["product_url"]

                                embed = disnake.Embed(
                                    title=name,
                                    colour=0xE74C3C,
                                    url=product_url,
                                    description=f"Status: **Aktiv**\nPreis: {price}€\n{product_url}",
                                )
                                await channel.send(embed=embed)
                else:
                    await channel.send("Nvidia hat Loretta gebannt")
                    print(resp.status)

    @botting.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Botting(bot))
