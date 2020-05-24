"""
Funktionen zum Umwandeln der Daten aus der API in Teile eines Wetterberichts.

Globale Variablen:
- WEATHER_DESCRIPTIONS: Dictionary mit verschiedenen Beschreibungen des Wetters anhand eines Codes.
Funktion: random_weather_descriptions(code): Sucht eine Beschreibung für einen bestimmten Wetter-Code als String aus und
gibt diesen zurück.
- CITY_DESCRIPTIONS: Dictionary mit verschiedenen Beschreibungen einer Stadt.
Funktion: random_city_descriptions(city_name): Sucht eine Beschreibung für eine bestimmte Stadt als String aus und
gibt diesen zurück.
"""
from numpy import random

from visuanalytics.analytics.preprocessing.weather import transform
from visuanalytics.analytics.util import date_time


def rh_data_to_text(rh):
    """Wandelt die von der Weatherbit-API gegebenen Werte rh in Text um.

    Der Ausgabeparameter dient später der flüssigeren Wiedergabe des Textes als Audiodatei.

    :param rh: relative Luftfeuchtigkeit in % (Prozent) (Wert aus der Weatherbit-API)
    :return: String mit z.B. "58 Prozent"

    Example:
        rh = 58
        r = air_data_to_text(rh)
        print(r)
    """
    rh_text = str(rh) + " Prozent"
    return rh_text


def pres_data_to_text(pres):
    """Wandelt die von der Weatherbit-API gegebenen Werte pres in Text um.

    Der Ausgabeparameter dient später der flüssigeren Wiedergabe des Textes als Audiodatei.

    :param pres: Luftdruck in mbar (Wert aus der Weatherbit-API)
    :return: String mit z.B. "0,83 Millibar"

    Example:
        pres = 0.83
        p = air_data_to_text(pres)
        print(pres)
    """
    pres_text = str(pres).replace(".", ",") + " Millibar"
    return pres_text


def pop_data_to_text(pop):
    """Wandelt die von der Weatherbit-API gegebenen Werte pop in Text um.

    Der Ausgabeparameter dient später der flüssigeren Wiedergabe des Textes als Audiodatei.

    :param pop: Niederschlagswahrscheinlichkeit in % (Prozent) (Wert aus der Weatherbit-API)
    :return: String mit z.B. "58 Prozent"

    Example:
        pop = 58
        pop_p = air_data_to_text(pop)
        print(pop_p)
    """
    pop_text = str(pop) + " Prozent"
    return pop_text


def wind_cdir_full_data_to_text(wind_cdir_full):
    """Wandelt die Windrichtung so um, dass sie flüssig vorgelesen werden kann.

    Dieser Eingabeparameter ist ein Wert aus der Weatherbit-API.
    Im Dictionary directions_dictionary sind die englischen Wörter für die Himmelsrichtungen auf zwei verschiedene
    Weisen auf Deutsch übersetzt. Die Übersetzungen dienen später der flüssigeren Wiedergabe des Textes als Audiodatei.

    :param wind_cdir_full: Angabe der Windrichtung Beispiel: west-southwest (Wert aus der Weatherbit-API)
    :return: wind_direction String mit z.B. "West Südwest"

    Example:
        wind_cdir_full = "west-southwest"
        wind_cdir_full = wind_data_to_text(wind_cdir_full)
        print(wind_cdir_full)
    """
    directions_dictionary = {
        "west": {0: "West", 1: "westlich"},
        "southwest": {0: "Südwest", 1: "südwestlich"},
        "northwest": {0: "Nordwest", 1: "nordwestlich"},
        "south": {0: "Süd", 1: "südlich"},
        "east": {0: "Ost", 1: "östlich"},
        "southeast": {0: "Südost", 1: "südöstlich"},
        "northeast": {0: "Nordost", 1: "nordöstlich"},
        "north": {0: "Nord", 1: "nördlich"}
    }
    if (wind_cdir_full.find("-") != -1):
        wind_cdir = wind_cdir_full.split("-")
        wind_1 = wind_cdir[0]
        wind_2 = wind_cdir[1]
        wind_direction_1 = directions_dictionary[wind_1][0]
        wind_direction_2 = directions_dictionary[wind_2][0]
        wind_direction_text = f"{wind_direction_1} {wind_direction_2}"
    else:
        wind_direction_text = f"{directions_dictionary[wind_cdir_full][0]}"
    return wind_direction_text


def wind_spd_data_to_text(wind_spd):
    """Wandelt die Windgeschwindigkeit so um, dass sie flüssig vorgelesen werden können.

    Dieser Eingabeparameter ist ein Wert aus der Weatherbit-API.
    Die Umwandlung in einen Satzteil in einem String dient später der flüssigeren Wiedergabe des Textes als Audiodatei.

    :param wind_spd: Angabe der Windgeschwindigkeit in m/s (Wert aus der Weatherbit-API)
    :return: String mit z.B. "0,83 Metern pro Sekunde"

    Example:
        wind_spd = 0.827464
        wind_spd = wind_data_to_text(wind_spd)
        print(wind_spd)
    """
    wind_spd_text = str(round(wind_spd, 2)).replace(".", ",") + " Metern pro Sekunde"
    return wind_spd_text


WEATHER_DESCRIPTIONS = {
    "200": {0: "kommt es zu Gewittern mit leichtem Regen",
            1: "ist mit Gewitter und leichtem Regen zu rechnen",
            2: "Gewitter & Regen"},
    "201": {0: "kommt es zu Gewittern mit Regen",
            1: "ist mit Gewitter und Regen zu rechnen",
            2: "Gewitter & Regen"},
    "202": {0: "kommt es zu Gewittern mit starkem Regen",
            1: "ist mit Gewitter und starkem Regen zu rechnen",
            2: "Gewitter & Regen"},
    "230": {0: "kommt es zu Gewittern mit leichtem Nieselregen",
            1: "ist mit Gewitter und leichtem Nieselregen zu rechnen",
            2: "Gewitter & Nieselregen"},
    "231": {0: "kommt es zu Gewittern mit Nieselregen",
            1: "ist mit Gewitter und Nieselregen zu rechnen",
            2: "Gewitter & Nieselregen"},
    "232": {0: "kommt es zu Gewittern mit starkem Nieselregen",
            1: "ist mit Gewitter und starkem Nieselregen zu rechnen",
            2: "Gewitter & Nieselregen"},
    "233": {0: "kommt es zu Gewittern mit Hagel",
            1: "ist mit Gewitter und Hagel zu rechnen",
            2: "Gewitter & Hagel"},
    "300": {0: "kommt es zu leichtem Nieselregen",
            1: "ist mit leichtem Nieselregen zu rechnen",
            2: "Nieselregen"},
    "301": {0: "kommt es zu Nieselregen",
            1: "ist mit Nieselregen zu rechnen",
            2: "Gewitter & Regen"},
    "302": {0: "kommt es zu starkem Nieselregen",
            1: "ist mit starkem Nieselregen zu rechnen",
            2: "Nieselregen"},
    "500": {0: "kommt es zu leichtem Regen",
            1: "ist es leicht regnerisch",
            2: "regnerisch"},
    "501": {0: "kommt es zu mäßigem Regen",
            1: "ist es regnerisch",
            2: "regnerisch"},
    "502": {0: "kommt es zu starkem Regen",
            1: "ist es stark regnerisch",
            2: "regnerisch"},
    "511": {0: "kommt es zu Eisregen",
            1: "ist mit Eisregen zu rechnen",
            2: "Eisregen"},
    "520": {0: "kommt es zu leichtem Regenschauer",
            1: "ist mit leichten Regenschauern zu rechnen",
            2: "regnerisch"},
    "521": {0: "kommt es zu Regenschauer",
            1: "ist mit Regenschauern zu rechnen",
            2: "regnerisch"},
    "522": {0: "kommt es zu starkem Regenschauer",
            1: "ist mit starken Regenschauern zu rechnen",
            2: "regnerisch"},
    "600": {0: "kommt es zu leichtem Schneefall",
            1: "ist mit leichtem Schneefall zu rechnen",
            2: "Schnee"},
    "601": {0: "kommt es zu Schnee",
            1: "ist mit Schnee zu rechnen",
            2: "Schnee"},
    "602": {0: "kommt es zu starkem Schneefall",
            1: "ist mit starkem Schneefall zu rechnen",
            2: "Schnee"},
    "610": {0: "kommt es zu einem Mix aus Schnee und Regen",
            1: "ist mit einem Mix aus Schnee und Regen zu rechnen",
            2: "Schnee & Regen"},
    "611": {0: "kommt es zu Schneeregen",
            1: "ist mit Schneeregen zu rechnen",
            2: "Schneeregen"},
    "612": {0: "kommt es zu starkem Schneeregen",
            1: "ist mit starkem Schneeregen zu rechnen",
            2: "Schneeregen"},
    "621": {0: "kommt es zu Schneeschauer",
            1: "ist mit Schneeschauern zu rechnen",
            2: "Schneeschauer"},
    "622": {0: "kommt es zu starkem Schneeschauer",
            1: "ist mit starken Schneeschauern zu rechnen",
            2: "Schneeschauer"},
    "623": {0: "kommt es zu Windböen",
            1: "ist mit Windböen zu rechnen",
            2: "windig"},
    "700": {0: "kommt es zu Nebel",
            1: "ist mit Nebel zu rechnen",
            2: "nebelig"},
    "711": {0: "kommt es zu Nebel",
            1: "ist mit Nebel zu rechnen",
            2: "nebelig"},
    "721": {0: "kommt es zu Dunst",
            1: "ist mit Nebel zu rechnen",
            2: "nebelig"},
    "731": {0: "kommt es zu Staub in der Luft",
            1: "ist mit Staub in der Luft zu rechnen",
            2: "staubig"},
    "741": {0: "kommt es zu Nebel",
            1: "ist mit Nebel zu rechnen",
            2: "nebelig"},
    "751": {0: "kommt es zu Eisnebel",
            1: "ist mit Eisnebel zu rechnen",
            2: "Eisnebel"},
    "800": {0: "ist der Himmel klar",
            1: "wird es heiter mit klarem Himmel",
            2: "heiter"},
    "801": {0: "sind nur wenige Wolken am Himmel",
            1: "ist es leicht bewölkt",
            2: "leicht bewölkt"},
    "802": {0: "sind vereinzelte Wolken am Himmel",
            1: "ist es vereinzelt bewölkt",
            2: "vereinzelt bewölkt"},
    "803": {0: "ist die Wolkendecke durchbrochen",
            1: "kommt es zu einer durchbrochenen Wolkendecke",
            2: "bewölkt"},
    "804": {0: "kommt es zu bedecktem Himmel",
            1: "ist es bewölkt",
            2: "bewölkt"},
    "900": {0: "kommt es zu unbekanntem Niederschlag",
            1: "ist mit unbekanntem Niederschlag zu rechnen",
            2: "unbekannter Niederschlag"}
}


def random_weather_descriptions(code):
    """Nimmt den Code vom Wetter-Icon aus der Weatherbit-API und generiert einen Satzteil als String.

    Innerhalb des Moduls wird der Code vom Wetter-Icon in einen String umgewandelt und im Dictionary
    weather_descriptions nachgeschaut, welcher Satzteil dazugehört. Es sind mehrere Satzteile pro
    Code möglich, daher wird mit der random-Funktion einer der möglichen Satzteile ausgesucht und als
    String ausgegeben. Dieser Satzteil wird ein Teil des späteren Wetterberichts (.txt-Datei), welcher
    dann in eine Audio-Datei umgewandelt wird.

    :param code: Wetter-Icon aus der Weatherbit-API, z.B. 501 als Integer.
    :return text_weather: String. Wird am Ende als Beschreibung zum Wetter als Satzteil in den Wetterbericht eingebaut.

    Example:
        code = 601
        text = random_weather_descriptions(code)
        print("In Berlin " + text + ".")
    """

    icon_code = str(code)
    x = random.choice([0, 1])
    text_weather = str(WEATHER_DESCRIPTIONS[icon_code][x])
    return text_weather


CITY_NAMES = {
    "Berlin": "in Berlin",
    "Bremen": "in Bremen",
    "Dresden": "in Dresden",
    "Düsseldorf": "in Düsseldorf",
    "Frankfurt": "in Frankfurt am Main",
    "Gießen": "in Gießen",
    "Hamburg": "in Hamburg",
    "Hannover": "in Hannover",
    "Kiel": "in Kiel",
    "Konstanz": "in Konstanz am Bodensee",
    "München": "in München",
    "Nürnberg": "in Nürnberg",
    "Saarbrücken": "in Saarbrücken",
    "Schwerin": "in Schwerin",
    "Stuttgart": "in Stuttgart",
    "Leipzig": "in Lepzig",
    "Magdeburg": "in Magdeburg",
    "Mainz": "in Mainz",
    "Regensburg": "in Regensburg"
}


def city_name_to_text(city_name):
    """Gibt eine Beschreibung der Stadt aus.

    Um die Texte des Wetterberichts automatisch zu generieren und sie trotzdem nicht immer gleich aussehen, wird
    hier das Dictionary CITY_DESCRIPTIONS verwendet mit verschiedenen Beschreibungen zu einer Stadt. Dies kann ganz normal der Name
    der Stadt sein oder zum Beispiel die Lage der Stadt in Deutschland. Mithilfe der Random-Funktion wird eine
    dieser Beschreibungen ausgewählt und später im Text des Wetterberichts eingefügt.

    :param city_name: Die von der Weatherbit-API ausgegebene Stadt.
    :return text_city: Gibt eine Stadt oder eine Eigenschaft (wie z.B. Himmelsrichtung) der eingegebenen Stadt als
    Text aus.

    Example:
        city_name = "Schwerin"
        x = random_city_descriptions(city_name)
        print(x + " scheint am Donnerstag die Sonne.")
    """
    text_city = str(CITY_NAMES[city_name])
    return text_city


def get_data_today_tomorrow_three(data):
    data_lowest_and_highest_max = {}
    for i in range(5):
        cities_max_temp = transform.get_cities_max_temp(data, i)
        city_highest_max = city_name_to_text(cities_max_temp[0])
        city_lowest_max = city_name_to_text(cities_max_temp[3])
        code_highest_max = random_weather_descriptions(cities_max_temp[2])
        code_lowest_max = random_weather_descriptions(cities_max_temp[5])
        temp_highest_max = str(cities_max_temp[1])
        temp_lowest_max = str(cities_max_temp[4])
        data_lowest_and_highest_max.update(
            {i: {"city_highest_max": city_highest_max, "temp_highest_max": temp_highest_max,
                 "code_highest_max": code_highest_max, "city_lowest_max": city_lowest_max,
                 "temp_lowest_max": temp_lowest_max, "code_lowest_max": code_lowest_max}})
    return data_lowest_and_highest_max


def merge_data(data):
    """ Zusammenführen der deutschlandweiten Wetterdaten für 5 Tage zu einem Dictionary mit Satzteilen.

    :param data: Dictionary mit ausgewählten Daten aus der Weatherbit-API (erstellt in der Methode
    preprocess_weather_data in preprocessing/weather/transform.py)
    :return: Dictionary aus relevanten Daten für einen deutschlandweiten Wetterbericht
    """
    data_for_text = {}
    weekdays_for_dict = transform.get_weekday(data)
    common_code = transform.get_common_code_per_day(data)
    data_lowest_and_highest_max = get_data_today_tomorrow_three(data)
    data_for_text.update({"today": {"weekday": weekdays_for_dict["today"],
                                    "common_code": common_code[0],
                                    "city_highest_max": data_lowest_and_highest_max[0]["city_highest_max"],
                                    "temp_highest_max": data_lowest_and_highest_max[0]["temp_highest_max"],
                                    "code_highest_max": data_lowest_and_highest_max[0]["code_highest_max"],
                                    "city_lowest_max": data_lowest_and_highest_max[0]["city_lowest_max"],
                                    "temp_lowest_max": data_lowest_and_highest_max[0]["temp_lowest_max"],
                                    "code_lowest_max": data_lowest_and_highest_max[0]["code_lowest_max"]}})
    data_for_text.update({"tomorrow": {"weekday": weekdays_for_dict["tomorrow"],
                                       "common_code": common_code[1],
                                       "city_highest_max": data_lowest_and_highest_max[1]["city_highest_max"],
                                       "temp_highest_max": data_lowest_and_highest_max[1]["temp_highest_max"],
                                       "code_highest_max": data_lowest_and_highest_max[1]["code_highest_max"],
                                       "city_lowest_max": data_lowest_and_highest_max[1]["city_lowest_max"],
                                       "temp_lowest_max": data_lowest_and_highest_max[1]["temp_lowest_max"],
                                       "code_lowest_max": data_lowest_and_highest_max[1]["code_lowest_max"]}})
    data_for_text.update({"next_1": {"weekday": weekdays_for_dict["next_1"],
                                     "common_code": common_code[2],
                                     "city_highest_max": data_lowest_and_highest_max[2]["city_highest_max"],
                                     "temp_highest_max": data_lowest_and_highest_max[2]["temp_highest_max"],
                                     "code_highest_max": data_lowest_and_highest_max[2]["code_highest_max"],
                                     "city_lowest_max": data_lowest_and_highest_max[2]["city_lowest_max"],
                                     "temp_lowest_max": data_lowest_and_highest_max[2]["temp_lowest_max"],
                                     "code_lowest_max": data_lowest_and_highest_max[2]["code_lowest_max"]}})
    data_for_text.update({"next_2": {"weekday": weekdays_for_dict["next_2"],
                                     "common_code": common_code[3],
                                     "city_highest_max": data_lowest_and_highest_max[3]["city_highest_max"],
                                     "temp_highest_max": data_lowest_and_highest_max[3]["temp_highest_max"],
                                     "code_highest_max": data_lowest_and_highest_max[3]["code_highest_max"],
                                     "city_lowest_max": data_lowest_and_highest_max[3]["city_lowest_max"],
                                     "temp_lowest_max": data_lowest_and_highest_max[3]["temp_lowest_max"],
                                     "code_lowest_max": data_lowest_and_highest_max[3]["code_lowest_max"]}})
    data_for_text.update({"next_3": {"weekday": weekdays_for_dict["next_3"],
                                     "common_code": common_code[4],
                                     "city_highest_max": data_lowest_and_highest_max[4]["city_highest_max"],
                                     "temp_highest_max": data_lowest_and_highest_max[4]["temp_highest_max"],
                                     "code_highest_max": data_lowest_and_highest_max[4]["code_highest_max"],
                                     "city_lowest_max": data_lowest_and_highest_max[4]["city_lowest_max"],
                                     "temp_lowest_max": data_lowest_and_highest_max[4]["temp_lowest_max"],
                                     "code_lowest_max": data_lowest_and_highest_max[4]["code_lowest_max"]}})
    return data_for_text


def merge_data_single(data, city_name):
    """ Zusammenführen der einzelnen Wetterdaten einer Stadt (5 Tage) zu einem Dictionary mit Satzteilen.

    :param data: Dictionary mit ausgewählten Daten aus der Weatherbit-API (erstellt in der Methode
    preprocess_weather_data in preprocessing/weather/transform.py)
    :return: Dictionary aus relevanten Daten für den Wetterbericht einer bestimmten Stadt
    """

    data_list = []
    for day in range(0, 5):
        date_sunset, time_sunset, time_text_sunset = date_time.time_change_format(data[city_name][day]['sunset_ts'])
        date_sunrise, time_sunrise, time_text_sunrise = date_time.time_change_format(data[city_name][day]['sunrise_ts'])
        data_for_text = {"max_temp": f"{str(round(data[city_name][day]['max_temp']))} Grad",
                         "min_temp": f"{str(round(data[city_name][day]['min_temp']))} Grad",
                         "app_max_temp": f"{str(round(data[city_name][day]['app_max_temp']))} Grad",
                         "app_min_temp": f"{str(round(data[city_name][day]['app_min_temp']))} Grad",
                         "wind_cdir_full": wind_cdir_full_data_to_text(data[city_name][day]['wind_cdir_full']),
                         "wind_spd": wind_spd_data_to_text(data[city_name][day]['wind_spd']),
                         "code": random_weather_descriptions(data[city_name][day]['code']),
                         "sunset_ts": time_text_sunset,
                         "sunrise_ts": time_text_sunrise,
                         "rh": rh_data_to_text(data[city_name][day]['rh']),
                         "pop": pop_data_to_text(data[city_name][day]['pop'])}
        data_list.append(data_for_text)
    return data_list
