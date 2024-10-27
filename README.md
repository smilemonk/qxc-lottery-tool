# 七星彩数据更新工具

一个简单的工具，用于自动获取和更新七星彩历史开奖数据。

## 功能特点

- 自动获取最新开奖数据
- 支持增量更新（只更新缺失的数据）
- 数据以 Excel 格式保存
- 跨平台支持（Windows/macOS）
- 自动保存到用户文档目录
- 友好的图形界面

## 下载和安装

### 方法一：直接下载可执行文件（推荐）

1. 访问 [Releases](https://github.com/smilemonk/qxc-lottery-tool/releases) 页面
2. 下载对应系统的可执行文件：
   - Windows: `七星彩数据更新工具.exe`
   - macOS: `七星彩数据更新工具.app`
3. 双击运行即可

### 方法二：从源码运行

1. 克隆仓库：
   ```bash
   git clone https://github.com/smilemonk/qxc-lottery-tool.git
   cd qxc-lottery-tool
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行程序：
   ```bash
   python src/main.py
   ```

## 使用说明

1. 首次运行：
   - Windows：程序会在"文档"文件夹中创建"七星彩数据"目录
   - macOS：程序会在"Documents"文件夹中创建"七星彩数据"目录

2. 基本操作：
   - 点击"更新数据"按钮获取最新数据
   - 通过菜单栏的"文件"可以打开数据文件或文件夹
   - 数据自动以 Excel 格式保存

3. 数据文件位置：
   - Windows：`文档/七星彩数据/qxc_history_data_full.xlsx`
   - macOS：`Documents/七星彩数据/qxc_history_data_full.xlsx`

## 开发说明

### Windows 打包
bash
安装打包工具
pip install cx_Freeze
打包
python setup_win.py build

### macOS 打包
bash
安装打包工具
pip install py2app
打包
python setup_mac.py py2app

## 注意事项

- 需要联网使用
- 首次运行会下载所有历史数据
- 后续运行只会更新新增数据
- 数据来源：体彩官网

## 问题反馈

如有问题或建议，请提交 [Issue](https://github.com/smilemonk/qxc-lottery-tool/issues)

## 许可证

[MIT License](LICENSE)

## 作者

[@smilemonk](https://github.com/smilemonk)

## 更新日志

### v1.0.0 (2024-02-24)
- 首次发布
- 支持自动获取和更新七星彩数据
- 支持 Windows 和 macOS 系统
