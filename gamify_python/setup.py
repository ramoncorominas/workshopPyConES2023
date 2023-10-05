# $ pip install py2exe
import os
from glob import glob
from setuptools import setup

# required import so py2exe can monkey patch distutils
import py2exe


setup(
	name="Gamify",
	console=["gamify.py"],
	options={"py2exe": {
		"bundle_files": 2,  # main .exe & modules in library.zip
		"excludes": ["tkinter"],
		"includes": ["ui"],
		"packages": ["audioplayer"],
	}},
	data_files=[ # tuples of the form: (where_to_copy, list_of_files)
		("waves", glob("waves/*.wav")),
		("games", ['games/guess_game.py']),
	],
)
