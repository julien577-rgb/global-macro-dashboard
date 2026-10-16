import akshare as ak
import pandas as pd

print("正在从国家统计局抓取 CPI 数据，请稍等几秒钟...")

cpi_data = ak.macro_china_cpi()

print("\n=== 抓取成功！以下是最近 5 个月的 CPI 数据 ===")
print(cpi_data.head())
