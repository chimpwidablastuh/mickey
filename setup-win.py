from setuptools import setup
import py2exe

APP = ['app/app.py']
DATA_FILES = []
OPTIONS = {
    'packages': ['rumps', 'Quartz'],
}

setup(
    windows=[{'script': APP[0]}],
    options={'py2exe': OPTIONS},
    zipfile=None,
)