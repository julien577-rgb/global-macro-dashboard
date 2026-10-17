import akshare as ak
import pandas as pd
import time
import os

# 确保有一个存放数据的文件夹
os.makedirs('stock_data', exist_ok=True)

def fetch_and_save(stock_code):
    print(f"开始抓取 {stock_code} 的数据...")
    
    # 1. 抓取 PE 历史数据
    try:
        print(f"抓取 {stock_code} 历史 PE...")
        pe_df = ak.stock_a_indicator_lg(symbol=stock_code)
        pe_df.to_csv(f'stock_data/{stock_code}_pe.csv', index=False, encoding='utf-8-sig')
        print(f"✅ {stock_code} PE 数据保存成功")
        time.sleep(2) # 休眠 2 秒防限流
    except Exception as e:
        print(f"❌ PE 抓取失败：{e}")

    # 2. 抓取资产负债表
    try:
        print(f"抓取 {stock_code} 资产负债表...")
        symbol = f"SH{stock_code}" if stock_code.startswith("6") else f"SZ{stock_code}"
        bal_df = ak.stock_balance_sheet_by_report_em(symbol=symbol)
        bal_df.to_csv(f'stock_data/{stock_code}_balance.csv', index=False, encoding='utf-8-sig')
        print(f"✅ {stock_code} 资产负债表保存成功")
        time.sleep(2)
    except Exception as e:
        print(f"❌ 财报抓取失败：{e}")

    # 3. 抓取基础信息（行业、主营）
    try:
        print(f"抓取 {stock_code} 基础信息...")
        info_df = ak.stock_individual_info_em(symbol=stock_code)
        info_df.to_csv(f'stock_data/{stock_code}_info.csv', index=False, encoding='utf-8-sig')
        print(f"✅ {stock_code} 基础信息保存成功")
    except Exception as e:
        print(f"❌ 基础信息抓取失败：{e}")

if __name__ == "__main__":
    # 你可以把你关注的股票代码写在这里，每周跑一次
    my_stocks = ["600519", "000001", "300750"]
    for code in my_stocks:
        fetch_and_save(code)
    print("全部数据抓取完毕！")
