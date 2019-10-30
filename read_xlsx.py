# -*- coding: utf-8 -*-
""" Работа с файлом Служебные записки """

import django
from django.conf import settings
import os
from on.readxlsx.read_order import paste_to_db

import logging
logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "memo.settings")
django.setup()

file_path = settings.ORDER_FILE


# if __name__ == "__main__":
paste_to_db(file_path)
