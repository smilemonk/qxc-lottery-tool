import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pandas", "requests", "openpyxl"],
    "excludes": ["matplotlib"],
    "include_files": [("resources/tc_favicon.ico", "resources/tc_favicon.ico")]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="七星彩数据更新工具",
    version="1.0.0",
    description="七星彩历史数据更新工具",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "src/main.py",
            base=base,
            icon="resources/tc_favicon.ico",
            target_name="七星彩数据更新工具.exe"
        )
    ]
)
