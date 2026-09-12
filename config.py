#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8685753606:AAE3cS4-TAsS_eIjVM50NM0qnq4vhTAtrtc")
    API_ID = int(os.environ.get("API_ID", "34435812"))
    API_HASH = os.environ.get("API_HASH", "ec83fcc94203532d52146a458cc9a274")
    AUTH_USERS = os.environ.get("AUTH_USERS", "8211049757")
  
