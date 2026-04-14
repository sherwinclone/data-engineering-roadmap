# Python

Python is the primary programming language for data engineering. Most tools in the ecosystem have Python APIs or SDKs.

Python 是數據工程的主要程式語言，生態系中大多數工具都有 Python API 或 SDK。

## What to Learn 學習內容

### Fundamentals 基礎
- Data types 資料型別: str, int, float, bool, list, dict, set, tuple
- Control flow 控制流程: if/else, for, while
- Functions and arguments 函式與參數
- File I/O 檔案操作: reading and writing CSV, JSON, Parquet 讀寫 CSV、JSON、Parquet
- Error handling 錯誤處理: try/except
- Modules and packages 模組與套件

### Data Engineering Essentials 數據工程必備
- **Virtual environments 虛擬環境**: venv, pip
- **Generators and iterators 生成器與迭代器**: process large files without loading everything into memory 處理大檔案不需全部載入記憶體
- **Context managers 上下文管理器**: `with` statement for resource management 用 `with` 語法管理資源
- **Logging 日誌**: use the `logging` module, not `print()` 使用 `logging` 模組，不要用 `print()`
- **CLI tools 命令列工具**: argparse or click
- **Type hints 型別提示**: improve readability and catch bugs early 提高可讀性並提早發現錯誤

### Key Libraries 重要套件

| Library 套件 | Purpose 用途 |
|---------|---------|
| pandas | Data manipulation 資料操作 (small-medium data 中小資料量) |
| requests | HTTP calls to APIs 呼叫 API |
| sqlalchemy | Database connections and ORM 資料庫連線與 ORM |
| psycopg2 / pymysql | Database drivers 資料庫驅動 |
| boto3 / google-cloud-* | Cloud SDK 雲端 SDK |
| pyspark | Spark Python API |
| pytest | Testing 測試 |

### Code Quality 程式碼品質
- Follow PEP 8 遵循 PEP 8
- Use snake_case for variables and functions 變數與函式使用 snake_case
- Write docstrings for public functions 公開函式寫 docstring
- Use linters 使用 linter: ruff, flake8
- Use formatters 使用 formatter: black, ruff format

## Patterns for Data Engineering 數據工程常用模式

### Processing Large Files 處理大檔案
```python
def process_large_csv(filepath):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield transform(row)
```

### Database Connection Pattern 資料庫連線模式
```python
from contextlib import contextmanager

@contextmanager
def get_connection(conn_string):
    conn = create_connection(conn_string)
    try:
        yield conn
    finally:
        conn.close()
```

### Retry Pattern 重試模式
```python
import time

def fetch_with_retry(url, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            return requests.get(url)
        except requests.RequestException:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay * (2 ** attempt))
```

## Practice 練習

- Write a script that reads a CSV, transforms it, and loads it into a database
  寫一個腳本讀取 CSV、轉換後載入資料庫
- Build a CLI tool that fetches data from a public API
  建一個 CLI 工具從公開 API 取資料
- Write unit tests for your transformation functions
  為轉換函式寫單元測試

## Key Takeaway 重點

> You don't need to be a Python expert. Focus on I/O, data manipulation, and writing clean, testable code.
>
> 你不需要成為 Python 專家。專注在 I/O、資料操作、寫出乾淨可測試的程式碼。
