# Excel Agent

這是一個基於 Google ADK 框架開發的 Excel 處理代理，可以幫助使用者處理 Excel 文件。

## 功能特點

- 讀取 Excel 文件名稱
- 讀取 Excel 文件內容
- 讀取工作表名稱
- 支持讀取指定工作表或所有工作表

## 環境要求

- Python 3.13 或更高版本
- 必要的 Python 套件（見 requirements.txt）

## 安裝步驟

1. 克隆專案：
```bash
git clone https://github.com/long0426/ai-agent-poc.git
cd excel-agent
```

2. 創建並激活虛擬環境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安裝依賴：
```bash
pip install -r requirements.txt
```

4. 安裝專案：
```bash
pip install -e .
```

## 環境變量設置

在專案根目錄創建 `.env` 文件，並設置以下環境變量：

```env
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_API_ENDPOINT=your_api_endpoint
```

## 使用方法

1. 將 Excel 文件放在 `excel_agent/data` 目錄下

2. 啟動代理：
```bash
python -m excel_agent
```

3. 與代理互動：
   - 提供 Excel 文件名稱來讀取文件內容
   - 提供工作表名稱來讀取特定工作表
   - 不提供工作表名稱則讀取所有工作表

## 專案結構

```
excel_agent/
├── __init__.py
├── agent.py          # 代理主程序
├── tools.py          # 工具函數
└── data/            # Excel 文件目錄
    └── *.xlsx
```
