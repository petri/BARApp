"""
To regenerate app:
    python setup.py py2app
"""

from setuptools import setup

APP = ['app.py']
APP_NAME = "giosg BAR"
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'giosg_ball_1024.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "giosg BAR",
        'CFBundleIdentifier': "com.giosg.macos.bar",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': "Copyright © 2020, giosg.com, All Rights Reserved"
    }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
