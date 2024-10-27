# src/__init__.py

# 版本信息
__version__ = '1.0.0'

# 作者信息
__author__ = 'smilemonk'

# 导出主要类，这样其他地方可以直接从包导入
from .main import QXCApp

# 所有可以被外部导入的内容
__all__ = ['QXCApp']

