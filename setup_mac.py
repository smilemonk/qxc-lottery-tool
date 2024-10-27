from setuptools import setup

APP = ['src/main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['pandas', 'requests', 'openpyxl'],
    'includes': ['tkinter'],
    'excludes': ['matplotlib'],
    'strip': False,
    'semi_standalone': True,
    'site_packages': False,
    'iconfile': 'resources/icon.icns',
    'plist': {
        'CFBundleName': "七星彩数据更新工具",
        'CFBundleDisplayName': "七星彩数据更新工具",
        'CFBundleGetInfoString': "七星彩历史数据更新工具",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'LSMinimumSystemVersion': '10.13.0',
        'NSHighResolutionCapable': True,
    }
}

setup(
    name="七星彩数据更新工具",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
