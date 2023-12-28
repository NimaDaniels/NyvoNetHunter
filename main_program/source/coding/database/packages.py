"""
# The package and/or library imports required for the project
---
"""


try:
    from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
    from exceptions.direct_run_error import DirectRunError
    from abc import ABC, abstractmethod, abstractproperty
    from PyQt5.QtWidgets import QApplication, QDialog
    from requests.exceptions import ConnectionError
    from tldextract import extract as extract_url
    from PyQt5.QtCore import QPropertyAnimation
    from requests.exceptions import SSLError
    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtCore import QByteArray
    from PyQt5.QtCore import pyqtSignal
    from os import system as cmd_input
    from dataclasses import dataclass
    from ipaddress import ip_address
    from PyQt5.QtCore import QThread
    from PyQt5.QtCore import QObject
    from typing import Literal, Dict
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtGui import QIcon
    from PyQt5.QtTest import QTest
    from platform import platform
    from PyQt5 import QtWidgets
    from json import loads
    from time import sleep
    import requests
    import inspect
    import socket
    import sys
    import os


except:
    raise ModuleNotFoundError(
        "Please activate the project main virtual environment in order to access the source code direct execute permission."
    )


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise PermissionError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
