# -*- coding: utf-8 -*-

# Copyright (C) 2023 jbleyel, Mr.Servo
#
# OAWeather is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dogtag is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OAWeather.  If not, see <http://www.gnu.org/licenses/>.

# Some parts are taken from msnweathercomponent plugin for compatibility reasons.
from os.path import join, exists, isfile
from traceback import print_exc

from Components.Converter.Converter import Converter
from Components.config import config
from Components.Element import cached

# --------------------------- Logfile -------------------------------

from datetime import datetime
from shutil import copyfile
from os import remove
from os.path import isfile
########################### log file loeschen ##################################
from Plugins.Extensions.OAWeather.plugin import logstatusin
myfile="/tmp/OAWeatherConverter.log"

## If file exists, delete it ##
if isfile(myfile):
    remove(myfile)
############################## File copieren ############################################


###########################  log file anlegen ##################################
# kitte888 logfile anlegen die eingabe in logstatus

logstatus = "on"
#logstatus = logstatusin

# ________________________________________________________________________________

def write_log(msg):
    if logstatus == ('on'):
        with open(myfile, "a") as log:

            log.write(datetime.now().strftime("%Y/%d/%m, %H:%M:%S.%f") + ": " + msg + "\n")

            return
    return

# ****************************  test ON/OFF Logfile ************************************************


def logout(data):
    if logstatus == ('on'):
        write_log(data)
        return
    return


# ----------------------------- so muss das commando aussehen , um in den file zu schreiben  ------------------------------
logout(data="start")
#def logstatusin():
    # Funktion implementieren
#logout(data=str(logstatusin)

class OAWeather(Converter, object):
    logout(data="class")
    CURRENT = 0
    DAY1 = 1
    DAY2 = 2
    DAY3 = 3
    DAY4 = 4
    DAY5 = 5
    DAYS = {
        "current": CURRENT,
        "day1": DAY1,
        "day2": DAY2,
        "day3": DAY3,
        "day4": DAY4,
        "day5": DAY5
    }
    logout(data="class 1")

    def __init__(self, type):
        logout(data="init")
        self.enabledebug = config.plugins.OAWeather.debug.value
        Converter.__init__(self, type)
        self.debug("__init__ type:%s" % type)
        self.index = None
        self.mode = None
        self.path = None
        self.logo = None
        self.extension = "png"
        value = type.split(",")
        self.mode = value[0]
        if len(value) > 1:
            logout(data="init 1")
            self.index = self.getIndex(value[1].strip())
            if len(value) > 2 and self.mode in ("weathericon", "yahoocode"):
                logout(data="init 2")
                self.path = value[2].strip()
                if len(value) > 3:
                    logout(data="init 3")
                    self.extension = value[3].strip()
        logout(data="init 4")
        self.debug("__init__ DONE self.mode:%s self.index:%s self.path:%s" % (self.mode, self.index, self.path))
        if config.plugins.OAWeather.debug.value:
            logout(data="init 5")
            self.getText = self.getTextDebug

    def getIndex(self, key):
        logout(data="getIndex")
        self.debug("getIndex key:%s" % (key))
        return self.DAYS.get(key, None)

    @cached
    def getTextDebug(self):
        logout(data="gettextdebug")
        self.debug("getText mode:%s index:%s" % (self.mode, self.index))
        text = self.getText()
        self.debug("getText mode:%s index:%s value:%s" % (self.mode, self.index, text))
        return text

    @cached
    def getText(self):
        logout(data="gettext mode")
        logout(data=str(self.mode))
        if self.mode:
            logout(data="gettext 1 index")
            logout(data=str(self.index))
            try:
                if self.index is not None:
                    logout(data="gettext 2 abfragen commando")

                    if self.mode == "temperature_high":
                        logout(data="temperature_high")
                        logout(data="Value of 'day' before calling getKeyforDay: %s" % self.index)
                        # return self.source.getMaxTemp(self.index)
                        date3_result = str(self.source.getMaxTemp(self.index))
                        logout(data="date3_result: %s" % date3_result)
                        return date3_result


                    elif self.mode == "temperature_low":
                        logout(data="temperature_low")
                        logout(data="Value of 'day' before calling getKeyforDay: %s" % self.index)
                        # return self.source.getMinTemp(self.index)
                        date4_result = str(self.source.getMinTemp(self.index))
                        logout(data="date4_result: %s" % date4_result)
                        return date4_result

                    elif self.mode == "temperature_high_low":
                        logout(data="temperature_high_low")
                        logout(data="Value of 'day' before calling getKeyforDay: %s" % self.index)
                        # return self.source.getMaxMinTemp(self.index)
                        date5_result = str(self.source.getMaxMinTemp(self.index))
                        logout(data="date5_result: %s" % date5_result)

                        return date5_result

                    elif self.mode == "temperature_text":
                        #return self.source.getKeyforDay("text", self.index, "")
                        logout(data="Value of 'day' before calling getKeyforDay: %s" % self.index)
                        temp_result = str(self.source.getKeyforDay("text", self.index, ""))
                        logout(data="temp_result: %s" % temp_result)
                        logout(data=str(temp_result))
                        logout(data=str(self.index))
                        #temp_result = "Leichter Regenfall"
                        return str(temp_result)

                    elif self.mode in ("weathericon", "yahoocode"):
                        return self.source.getYahooCode(self.index)
                    elif self.mode == "meteocode":
                        return self.source.getMeteoCode(self.index)
                    elif self.mode == "weekday":
                        return self.source.getKeyforDay("day", self.index)

                    elif self.mode == "weekshortday":
                        logout(data="if weekshortday")
                        return self.source.getKeyforDay("shortDay", self.index)

                    elif self.mode == "date":
                        logout(data="if date")
                        #return self.source.getDate(self.index)
                        date_result = str(self.source.getDate(self.index))
                        logout(data="date_result: %s" % date_result)
                        return date_result

                    elif self.mode == "precipitation":
                        return self.source.getPrecipitation(self.index)

                    elif self.mode == "precipitationfull":
                        logout(data="precipitationfull")
                        #return self.source.getPrecipitation(self.index, True)
                        date1_result = str(self.source.getPrecipitation(self.index, True))
                        logout(data="date1_result: %s" % date1_result)
                        return date1_result
                    else:
                        logout(data="precipitationfull1")           # hier kommt das cmd rein , daySummary0
                        #return self.source.getKeyforDay(self.mode, self.index, "")
                        date2_result = str(self.source.getKeyforDay(self.mode, self.index, ""))
                        logout(data="date2_result: %s" % date2_result)
                        return date2_result

                if self.mode == "weathersource":
                    return self.source.getVal("source")
                elif self.mode == "city":
                    return self.source.getVal("name")
                elif self.mode == "observationPoint":
                    return self.source.getCurrentVal("observationPoint")

                elif self.mode == "observationtime":
                    logout(data="observationtime")
                    observationtime = str(self.source.getObservationTime())
                    logout(data=str(observationtime))
                    return observationtime

                elif self.mode == "sunrise":
                    logout(data="sunrise")
                    sunrise_value = self.source.getSunrise()
                    logout(data="sunrise_value received from source: %s" % sunrise_value)
                    return str(sunrise_value)

                elif self.mode == "sunset":
                    logout(data="sunset")
                    sunset_value = self.source.getSunset()
                    logout(data="sunset_value received from source: %s" % sunset_value)
                    return str(sunset_value)

                elif self.mode == "isnight":
                    return self.source.getIsNight()

                elif self.mode == "temperature_current":
                    return str(self.source.getTemperature())

                elif self.mode == "feelslike":
                    return self.source.getFeeltemp()

                elif self.mode == "feelslikefull":
                    return str(self.source.getFeeltemp(True))

                elif self.mode == "humidity":
                    return self.source.getHumidity()

                elif self.mode == "humidityfull":
                    return self.source.getHumidity(True)

                elif self.mode == "raintext":
                    logout(data="raintext")
                    raintext = str(self.source.getCurrentVal("raintext", ""))
                    logout(data=str(raintext))
                    return raintext

                #elif self.mode == "winddisplay":
                #    logout(data="winddisplay")
                #    return "%s %s" % (self.source.getWindSpeed(), self.source.getWindDirName())

                elif self.mode == "winddisplay":
                    logout(data="winddisplay")
                    wind_speed = str(self.source.getWindSpeed())
                    logout(data=str(wind_speed))
                    logout(data="winddisplay 1")
                    wind_dir_name = str(self.source.getWindDirName())
                    logout(data="winddisplay 2")
                    logout(data=str(wind_dir_name))
                    logout(data="wind_speed received from source: %s" % wind_speed)
                    logout(data="winddisplay 3")
                    logout(data="wind_dir_name received from source: %s" % wind_dir_name)
                    logout(data="winddisplay 4")
                    return "%s %s" % (str(wind_speed), str(wind_dir_name))  # Hier werden die Werte als Strings zurückgegeben

                elif self.mode == "windspeed":
                    return self.source.getWindSpeed()
                elif self.mode == "winddir":
                    return self.source.getWindDir()
                elif self.mode == "winddirsign":
                    return self.source.getCurrentVal("windDirSign")
                elif self.mode == "winddirarrow":
                    return self.source.getCurrentVal("windDirSign").split(" ")[0]
                elif self.mode == "winddirname":
                    return self.source.getWindDirName()
                elif self.mode == "winddirshort":
                    return self.source.getWindDirShort()
                else:
                    return self.source.getVal(self.mode)

            except Exception as err:
                logout(data="err")
                print("[OAWeather] Converter Error:%s" % str(err))
                print_exc()
            logout(data="gettext 3")
        logout(data="gettext 4")
        return ""

    logout(data="class 3")
    logout(data="gettext 5")

    text = property(getText)
    logout(data="text")
    logout(data=str(text))

    @cached
    def getBoolean(self):
        logout(data="getboolean")
        if self.mode == "raintext":
            return self.source.getCurrentVal("raintext", "") != ""
        elif self.mode in ("daySummary0", "nightSummary0"):
            return self.source.getKeyforDay(self.mode, self.index, "") != ""
        else:
            return False

    boolean = property(getBoolean)

    @cached
    def getIconFilename(self):
        logout(data="geticon")
        if self.mode == "logo":
            try:
                path = join(self.source.pluginpath, "Images", "%s_weather_logo.png" % self.source.logo)
                if isfile(path):
                    return path
            except Exception:
                return ""

        if self.index in (self.CURRENT, self.DAY1, self.DAY2, self.DAY3, self.DAY4, self.DAY5):
            path = self.source.iconpath
            if path and exists(path):
                code = self.source.getYahooCode(self.index)
                if code:
                    path = join(path, "%s.%s" % (code, self.extension))
                    if isfile(path):
                        return path
            self.debug("getIconFilename not found mode:%s index:%s self.path:%s path:%s" % (
            self.mode, self.index, self.path, path))
        return ""

    def debug(self, text):
        logout(data="debug")
        if self.enabledebug:
            print("[OAWeather] Converter DEBUG %s" % text)

    logout(data="class 4")
    logout(data="iconfilename")
    iconfilename = property(getIconFilename)
    logout(data="class 5")
    logout(data=str(iconfilename))
    logout(data="iconfilename out")