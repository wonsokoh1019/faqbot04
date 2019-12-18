#!/bin/bash python3
# -*- coding: UTF-8 -*-
"""
resource.py Defining the resource address used for a project.
"""

from conf.config import LOCAL_ADDRESS
from faq_bot.constant import ABSDIR_OF_PARENT

# RICH_MENUS
RICH_MENUS = {
    'en': {
        "name": "faq_bot_rich_menu_en",
        "path": ABSDIR_OF_PARENT + "/image/en/Rich_Menu.png"
    },
    'ko': {
        "name": "faq_bot_rich_menu_en",
        "path": ABSDIR_OF_PARENT + "/image/kr/Rich_Menu.png"
    },
    'ja': {
        "name": "faq_bot_rich_menu_en",
        "path": ABSDIR_OF_PARENT + "/image/jp/Rich_Menu.png"
    }

}

BOARDS = {
    'leave': {
        "title": "leave boards for faq",
        "description": "leave boards for faq",
    },

    'welfare': {
        "title": "welfare boards for faq",
        "description": "welfare boards for faq",
    },

    'security': {
        "title": "security boards for faq",
        "description": "security boards for faq",
    }

}

# API ADDRESS
CAROUSEL = {
    "leave": [
        LOCAL_ADDRESS + "static/carousel/Carousel_01.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_02.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_03.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_04.png"
    ],
    "welfare": [
        LOCAL_ADDRESS + "static/carousel/Carousel_05.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_06.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_07.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_08.png"
    ],
    "security": [
        LOCAL_ADDRESS + "static/carousel/Carousel_09.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_10.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_11.png",
        LOCAL_ADDRESS + "static/carousel/Carousel_12.png"
    ]
}

POST_BACK_URLS = {
    "leave": [
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/"
    ],
    "welfare": [
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/"
    ],
    "security": [
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/",
        "https://community.worksmobile.com/jp/"
    ]
}
