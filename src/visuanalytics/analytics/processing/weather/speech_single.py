"""
Hier werden die Audiodateien für eine 5 Tage-Wettervorhersage für eine bestimmte Stadt generiert.

Die Methode get_all_audios_single_city(pipeline_id, data, date, city_name) wenden die Methoden
_generate_first_day_audio(pipeline_id, data_for_text, date, city_name)
_generate_second_day_audio(pipeline_id, data_for_text, date, city_name)
_generate_three_days_audio(pipeline_id, data_for_text, date, city_name)
an, um für jeden Tag eine Audiodatei zu erhalten. Der Rückgabewert der eben genannten Methoden
ist immer eine Audiodatei. Die dritte Methode wird drei Mal angewandt.
"""
from visuanalytics.analytics.processing.util import mp3 as fp


def get_all_audios_single_city(pipeline_id, data, date, city_name):
    """
    Generierung der Audiodateien für eine 5-Tage-Wettervorhersage für eine bestimmte Stadt.


    :param pipeline_id: Ordnername der Audiodatei
    :type pipeline_id: str
    :param data: Dictionary mit relevanten Wetterdaten, die in preprocessing.weather.speech.merge_data
    erstellt wurden
    :type data: dict
    :param date: String mit Wochentag
    :type date: str
    :param city_name: String mit Stadtname
    :type city_name: str
    :return: Gibt für jede generierte Audiodatei einen Pfad an, wo diese zu finden ist.
    :rtype: str
    """
    return [_generate_first_day_audio(pipeline_id, data[0], date[0], city_name),
            _generate_second_day_audio(pipeline_id, data[1], date[1], city_name),
            _generate_three_days_audio(pipeline_id, data[2], date[2], city_name),
            _generate_three_days_audio(pipeline_id, data[3], date[3], city_name),
            _generate_three_days_audio(pipeline_id, data[4], date[4], city_name)]


def _generate_first_day_audio(pipeline_id, data, date, city_name):
    """Generierung von Text und Audiodatei für den heutigen Wetterbericht einer bestimmten Stadt.

    :param pipeline_id: Ordnername der Audiodatei
    :type pipeline_id: str
    :param data: Dictionary mit relevanten Wetterdaten, die in preprocessing.weather.speech.merge_data
    erstellt wurden
    :type data: dict
    :param date: String mit Wochentag
    :type date: str
    :param city_name: String mit Stadtname
    :type city_name: str
    :return: Gibt für die generierte Audiodatei einen Pfad an, wo diese zu finden ist.
    :rtype: str
    """
    text = (
        f"Am heutigen {date} {data['code']}. Die Höchstwerte erreichen in {city_name} {data['max_temp']}. "
        f"Die Tiefstwerte liegen bei {data['min_temp']}. "
        f"Die gefühlten Temperaturen liegen zwischen {data['app_min_temp']} und {data['app_max_temp']}. "
        f"Die Regenwahrscheinlichkeit liegt am {date} bei {data['pop']} und die relative Luftfeuchtigkeit bei {data['rh']}. "
        f"Der Wind kommt heute aus Richtung {data['wind_cdir_full']} und erreicht Geschwindigkeiten von {data['wind_spd']}. "
        f"Die Sonne geht heute um {data['sunset_ts']} unter und geht morgen um {data['sunrise_ts']} wieder auf. "
    )
    file_path = fp.text_to_mp3(pipeline_id, text)
    return file_path


def _generate_second_day_audio(pipeline_id, data, date, city_name):
    """Generierung von Text und Audiodatei für den morgigen Wetterbericht einer bestimmten Stadt.

    :param pipeline_id: Ordnername der Audiodatei
    :type pipeline_id: str
    :param data: Dictionary mit relevanten Wetterdaten, die in preprocessing.weather.speech.merge_data
    erstellt wurden
    :type data: dict
    :param date: String mit Wochentag
    :type date: str
    :param city_name: String mit Stadtname
    :type city_name: str
    :return: Gibt für die generierte Audiodatei einen Pfad an, wo diese zu finden ist.
    :rtype: str
    """
    text = (
        f"Am morgigen {date} {data['code']}. Die Höchstwerte erreichen in {city_name} {data['max_temp']}. "
        f"Die Tiefstwerte liegen bei {data['min_temp']}. "
        f"Die gefühlten Temperaturen liegen zwischen {data['app_min_temp']} und {data['app_max_temp']}. "
        f"Die Regenwahrscheinlichkeit liegt am {date} bei {data['pop']} und die relative Luftfeuchtigkeit bei {data['rh']}. "
        f"Der Wind kommt morgen aus Richtung {data['wind_cdir_full']} und erreicht Geschwindigkeiten von {data['wind_spd']}. "
    )
    file_path = fp.text_to_mp3(pipeline_id, text)
    return file_path


def _generate_three_days_audio(pipeline_id, data, date, city_name):
    """Generierung von Text und Audiodatei für ein 3-Tage-Wetterbericht (ab übermorgen) einer bestimmten Stadt.

    :param pipeline_id: Ordnername der Audiodatei
    :type pipeline_id: str
    :param data: Dictionary mit relevanten Wetterdaten, die in preprocessing.weather.speech.merge_data
    erstellt wurden
    :type data: dict
    :param date: String mit Wochentag
    :type date: str
    :param city_name: String mit Stadtname
    :type city_name: str
    :return: Gibt für die generierte Audiodatei einen Pfad an, wo diese zu finden ist.
    :rtype: str
    """
    text = (
        f"Am {date} {data['code']} bei Temperaturen von {data['min_temp']} bis {data['max_temp']}. "
        f"Die Regenwahrscheinlichkeit liegt am {date} bei {data['pop']}. Der Wind erreicht Geschwindigkeiten von {data['wind_spd']}. "
    )
    file_path = fp.text_to_mp3(pipeline_id, text)
    return file_path
