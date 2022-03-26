import datetime
import locale

import aiohttp
import disnake
from disnake.ext import commands
from tabulate import tabulate

locale.setlocale(locale.LC_TIME, "de_DE")

ICONS = {200: "🌩️",
         201: "🌩️",
         202: "🌩️",
         210: "🌩️",
         211: "🌩️",
         212: "🌩️",
         221: "🌩️",
         230: "🌩️",
         231: "🌩️",
         232: "🌩️",
         300: "🌧️",
         301: "🌧️",
         302: "🌧️",
         310: "🌧️",
         311: "🌧️",
         312: "🌧️",
         313: "🌧️",
         314: "🌧️",
         321: "🌧️",
         500: "🌦️",
         501: "🌦️",
         502: "🌦️",
         503: "🌦️",
         504: "🌦️",
         511: "🌦️",
         520: "🌦️",
         521: "🌦️",
         522: "🌦️",
         531: "🌦️",
         600: "🌨️",
         601: "🌨️",
         602: "🌨️",
         611: "🌨️",
         612: "🌨️",
         613: "🌨️",
         615: "🌨️",
         616: "🌨️",
         620: "🌨️",
         621: "🌨️",
         622: "🌨️",
         701: "🌫️",
         711: "🌫️",
         721: "🌫️",
         731: "🌫️",
         741: "🌫️",
         751: "🌫️",
         761: "🌫️",
         762: "🌫️",
         771: "🌫️",
         781: "🌫️",
         800: "☀️",
         801: "⛅",
         802: "⛅",
         803: "⛅",
         804: "⛅",
         }


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = bot.owm_key

    @commands.command(aliases=["w"])
    async def wetter(self, ctx, *, arg):
        forecast = {}
        current_weather = {}
        url_cords = f"http://api.openweathermap.org/geo/1.0/direct?q={arg}&appid={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url_cords) as response:
                data = await response.json()
                if data:
                    lon = data[0]["lon"]
                    lat = data[0]["lat"]
                    if "local_names" in data[0]:
                        if "de" in data[0]["local_names"]:
                            location = f'{data[0]["local_names"]["de"]}, {data[0]["country"]}'
                        else:
                            location = f'{data[0]["local_names"]["feature_name"]}, {data[0]["country"]}'
                    else:
                        location = f'{data[0]["name"]}, {data[0]["country"]}'
                    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&lang=de&units=metric&appid={self.api_key}"
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url) as response:
                            data = await response.json()
                            current_weather["timestamp"] = datetime.datetime.fromtimestamp(
                                data["current"]["dt"]).strftime("%d.%m.%y %H:%M")
                            current_weather["weather_desc"] = data["current"]["weather"][0]["description"]
                            current_weather["temp"] = int(
                                data["current"]["temp"])
                            current_weather["feels_like"] = int(
                                data["current"]["feels_like"])
                            current_weather["icon"] = data["current"]["weather"][0]["icon"]
                            current_weather["humidity"] = data["current"]["humidity"]
                            current_weather["wind_speed"] = int(data["current"]["wind_speed"] * 3.6)
                            current_weather["temp_morning"] = int(data["daily"][0]["temp"]["morn"])
                            current_weather["temp_day"] = int(data["daily"][0]["temp"]["day"])
                            current_weather["temp_eve"] = int(data["daily"][0]["temp"]["eve"])
                            current_weather["temp_night"] = int(data["daily"][0]["temp"]["night"])
                            current_weather["weather"] = data["daily"][0]["weather"][0]["description"]
                            current_weather["pop"] = int(data["daily"][0]["pop"] * 100)
                            for day in range(1, 7):
                                forecast[day] = {}
                                forecast[day]["timestamp"] = datetime.datetime.fromtimestamp(
                                    data["daily"][day]["dt"]).strftime("%a %d.%m.")
                                forecast[day]["weather_desc"] = data["daily"][day]["weather"][0]["description"]
                                forecast[day]["temp_min"] = int(
                                    data["daily"][day]["temp"]["min"])
                                forecast[day]["temp_max"] = int(
                                    data["daily"][day]["temp"]["max"])
                                forecast[day]["pop"] = int(
                                    data["daily"][day]["pop"] * 100)
                                forecast[day]["icon"] = data["daily"][day]["weather"][0]["id"]
                    embed = disnake.Embed(
                        title=f"Wetter für {location}",
                        colour=0xE74C3C,
                        description=f"**Aktuelles Wetter:**\n{current_weather['weather_desc']} bei {current_weather['temp']}°C (Gefühlte {current_weather['temp']}°C) .\nLuftfeuchte: {current_weather['humidity']}%\nWind: {current_weather['wind_speed']}km/h\n\n**Heutige Aussicht:**\n{current_weather['weather']}. Temperatur morgens bei {current_weather['temp_morning']}°C, tagsüber {current_weather['temp_day']}°C. Abends {current_weather['temp_eve']}°C und in der Nacht {current_weather['temp_night']}°C. Die Niederschlagswahrscheinlichkeit liegt bei {current_weather['pop']}%.",
                    )
                    if "alerts" in data:
                        for alert in data["alerts"]:
                            if not alert["tags"]:
                                embed.add_field(
                                    name=f"Wetterwarnung: {alert['event']}",
                                    value=f"{alert['description']}\nGültig {datetime.datetime.fromtimestamp(alert['start']).strftime('%d.%m. %H:%M')} bis {datetime.datetime.fromtimestamp(alert['end']).strftime('%d.%m. %H:%M')}",
                                    inline=False
                                )
                    table = []
                    buffer = []
                    for id, day in forecast.items():
                        if id % 2 == 0:

                            name = f"{day['timestamp']} {ICONS[day['icon']]}"
                            value = f"{day['weather_desc']}\nMin: {day['temp_min']}°C\nMax: {day['temp_max']}°C\nNiederschlag: {day['pop']}%"
                            buffer.append(f"{name}\n{value}")
                            table.append(buffer)
                            table.append(["\u200b"])
                            buffer = []
                        else:
                            name = f"{day['timestamp']} {ICONS[day['icon']]}"
                            value = f"{day['weather_desc']}\nMin: {day['temp_min']}°C\nMax: {day['temp_max']}°C\nNiederschlag: {day['pop']}%"
                            buffer.append(f"{name}\n{value}")

                    embed.add_field(
                        name="\u200b",
                        value=f"```{tabulate(table, tablefmt='plain')}```",
                        inline=False
                    )

                    embed.set_thumbnail(
                        url=f"http://openweathermap.org/img/wn/{current_weather['icon']}@2x.png")
                    embed.set_author(
                        name="Loretta der Wetterfrosch",
                    )
                    embed.set_footer(
                        text=f"Stand: {current_weather['timestamp']}"
                    )
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Der Ort konnte nicht gefunden werden.")


def setup(bot):
    bot.add_cog(Weather(bot))
