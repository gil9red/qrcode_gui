# -*- coding: utf-8 -*-

# A very simple setup script to create a single executable
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable

includes = []
excludes = []
packages = []

target = Executable(
    script='main.py',
    targetName="qrcode_gui.exe",
    compress=True,
    # icon=None,
)

setup(
    name='qrcode_gui',
    version='0.1',
    author="Ilya Petrash",
    description='qrcode_gui',

    options={
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "packages": packages,
            "build_exe": "bin",
        }
    },

    executables=[target]
)
