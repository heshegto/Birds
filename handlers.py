import json
from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass

from android.widget import Toast
from com.chaquo.python import Python

from datetime import datetime


# ------- Обработчики экрана Меню -------
def menu_on_start(hashMap, _files=None, _data=None):
    return hashMap


def menu_on_input(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "menu":
        if hashMap.get("menu") == "Список":
            hashMap.put("ShowScreen", "Список птиц")
        elif hashMap.get("menu") == "Создание":
            hashMap.put("ShowScreen", "Создание новой птицы")
    elif hashMap.get("listener") == 'ON_BACK_PRESSED':
        hashMap.put("FinishProcess", "")
    return hashMap


# ------- Обработчкики экрана Создание новой птицы -------
def create_on_start(hashMap, _files=None, _data=None):
    if not hashMap.containsKey("saved_bird"):
        hashMap.put("saved_bird", "")
    return hashMap


def create_on_input(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_nosql")

    if hashMap.get("listener") == "save_bird":
        if hashMap.containsKey("name_bird") and hashMap.containsKey("color_bird"):

            name, color = hashMap.get("name_bird"), hashMap.get("color_bird")
            j = {
                "name": name,
                "color": color
            }
            if hashMap.containsKey("foto"):
                j["foto"] = hashMap.get("foto")
            jkeys = ncl.getallkeys()
            keys = json.loads(jkeys)
            id = 0
            if len(keys) > 0:
                id = max([int(x) for x in keys]) + 1

            ncl.put(str(id), json.dumps(j, ensure_ascii=False), True)

            hashMap.put("saved_bird", str(id) + ' ' + name + ' ' + color)
            hashMap.put("toast", "successfully saved")

    if hashMap.get("listener") == 'ON_BACK_PRESSED':
        hashMap.put("ShowScreen", "Меню")
    if hashMap.get("listener") == 'del_all':
        ncl.destroy()
        list_of_views = noClass("list_of_views")
        count = noClass("count_views")
        list_of_views.destroy()
        count.destroy()
        hashMap.put("speak", "Attention! All data has been destroyed!")
    return hashMap


# ------- Обработчики экрана Карточка птицы -------
def card_on_start(hashMap, files=None, data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_nosql")
    bird = json.loads(ncl.get(hashMap.get("selected_card_key")))

    hashMap.put("bird_name", bird['name'])
    hashMap.put("bird_color", bird['color'])
    if 'foto' in bird.keys():
        hashMap.put("image", bird['foto'])
    else:
        hashMap.put("image", "None")

    return hashMap


def card_on_input(hashMap, files=None, data=None):
    if hashMap.get("listener") == 'ON_BACK_PRESSED':
        hashMap.put("ShowScreen", "Список птиц")
    if hashMap.get("listener") == 'btn_saw':
        id = hashMap.get('selected_card_key')
        hashMap.put("selected_card_id", id)
        hashMap.put("ShowScreen", "Птицы, которых я видел, добавить")
    return hashMap


# ------- Обработчики экрана Список птиц -------
def list_on_start(hashMap, _files=None, _data=None):
    j = {
        "customcards": {
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "match_parent",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "Elements": [
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "match_parent",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "Picture",
                                        "show_by_condition": "",
                                        "Value": "@picture",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": "",
                                        "TextSize": "16",
                                        "TextColor": "#DB7093",
                                        "TextBold": True,
                                        "TextItalic": False,
                                        "BackgroundColor": "",
                                        "width": "match_parent",
                                        "height": "wrap_content",
                                        "weight": 2
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@idBird",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": "",
                                        "TextSize": "-1",
                                        "TextColor": "#6F9393",
                                        "TextBold": False,
                                        "TextItalic": True,
                                        "BackgroundColor": "",
                                        "width": "wrap_content",
                                        "height": "wrap_content",
                                        "weight": 0
                                    }
                                ]
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "Название птички:",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "TextColor": "#6F93FF",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@name",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "Цвет птички:",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "TextColor": "#6F93FF",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@color",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                ]
                            },
                        ]
                    },
                ]
            }
        }
    }

    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_nosql")

    keys = json.loads(ncl.getallkeys())

    j["customcards"]["cardsdata"] = []

    for i in keys:
        bird = json.loads(ncl.get(i))

        c = {
            "key": i,
            "idBird": "id: " + i,
            "name": bird['name'],
            "color": bird['color'],
        }
        if 'foto' in bird.keys():
            c["picture"] = bird['foto']

        j["customcards"]["cardsdata"].append(c)

    hashMap.put("cards", json.dumps(j, ensure_ascii=False).encode('utf8').decode())
    return hashMap


def list_on_input(hashMap, _files=None, _data=None):
    if hashMap.get('selected_card_key'):
        hashMap.put("ShowScreen", "Карточка птицы")
    if hashMap.get("listener") == 'ON_BACK_PRESSED':
        hashMap.put("ShowScreen", "Меню")
    if hashMap.get("listener") == "create_new":
        hashMap.put("ShowScreen", "Создание новой птицы")
    return hashMap


# ------- Обработчики экрана Птицы, которых я видел -------
def i_saw_on_start(hashMap, files=None, data=None):
    j = {
        "customcards": {
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "match_parent",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "Elements": [
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "match_parent",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "Picture",
                                        "show_by_condition": "",
                                        "Value": "@picture",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": "",
                                        "TextSize": "16",
                                        "TextColor": "#DB7093",
                                        "TextBold": True,
                                        "TextItalic": False,
                                        "BackgroundColor": "",
                                        "width": "match_parent",
                                        "height": "wrap_content",
                                        "weight": 2
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@idBird",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": "",
                                        "TextSize": "-1",
                                        "TextColor": "#6F9393",
                                        "TextBold": False,
                                        "TextItalic": True,
                                        "BackgroundColor": "",
                                        "width": "wrap_content",
                                        "height": "wrap_content",
                                        "weight": 0
                                    }
                                ]
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "Дата и время:",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "TextColor": "#6F93FF",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@dateAndTime",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "Название птички:",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "TextColor": "#6F93FF",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@name",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "LinearLayout",
                                        "orientation": "horizontal",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "1",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "show_by_condition": "",
                                                "Value": "Просмотры: ",
                                                "NoRefresh": False,
                                                "document_type": "",
                                                "mask": "",
                                                "TextColor": "#6F93FF",
                                                "Variable": ""
                                            },
                                            {
                                                "type": "TextView",
                                                "show_by_condition": "",
                                                "Value": "@views",
                                                "NoRefresh": False,
                                                "document_type": "",
                                                "mask": "",
                                                "Variable": "",
                                                "TextSize": "16",
                                                "TextColor": "#DB7093",
                                                "TextBold": True,
                                                "TextItalic": False,
                                                "BackgroundColor": "",
                                                "width": "match_parent",
                                                "height": "wrap_content",
                                                "weight": 2
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }

    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    list_of_views = noClass("list_of_views")

    keys = list_of_views.getallkeys()
    jkeys = json.loads(keys)

    j["customcards"]["cardsdata"] = []

    for i in jkeys[::-1]:
        bird = json.loads(list_of_views.get(i))
        c = {
            "key": i,
            "idBird": "id: " + bird['idBird'],
            "dateAndTime": bird['datetime'],
            "name": bird['name'],
            'views': bird['views']
        }
        if 'foto' in bird.keys():
            c["picture"] = bird['foto']
        j["customcards"]["cardsdata"].append(c)

    hashMap.put("seen_birds", json.dumps(j, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def add_to_i_saw_on_input(hashMap, files=None, data=None):
    if hashMap.get("listener") == "add_to_i_saw":

        id = hashMap.get("selected_card_id")

        noClass = jclass("ru.travelfood.simple_ui.NoSQL")

        ncl = noClass("test_nosql")
        str_bird = ncl.get(id)
        bird = json.loads(str_bird)

        count = noClass("count_views")

        list_of_views = noClass("list_of_views")

        j = {
            "idBird": id,
            "datetime": str(datetime.now()),
            "name": bird['name'],
        }
        if 'foto' in bird.keys():
            j["foto"] = bird["foto"]

        keys = count.getallkeys()
        jkeys = json.loads(keys)
        if id in jkeys:
            count.put(id, str(int(count.get(id)) + 1), True)
        else:
            count.put(id, '1', True)

        j["views"] = count.get(id)

        keys = list_of_views.getallkeys()
        jkeys = json.loads(keys)
        pk = 0
        if len(jkeys) > 0:
            pk = max([int(x) for x in jkeys]) + 1

        list_of_views.put(str(pk), json.dumps(j, ensure_ascii=False), True)
        hashMap.put('toast', "Птица " + json.loads(list_of_views.get(str(pk)))['name'] + " увидена")

        hashMap.put("RefreshScreen", "Птицы, которых я видел")

    if hashMap.get("listener") == 'ON_BACK_PRESSED':
        hashMap.put("ShowScreen", "Меню")
    return hashMap


def i_saw_on_input(hashMap, files=None, data=None):
    if hashMap.get("listener") == 'ON_BACK_PRESSED':
        hashMap.put("FinishProcess", "")
    return hashMap
