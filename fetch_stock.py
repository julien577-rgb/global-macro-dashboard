import akshare as ak
import pandas as pd
import time

def fetch_stock_data(stock_code):
    print(f"正在获取 {stock_code} 的数据...")
    
    # 1. 获取基本信息
    try:
        info = ak.stock_individual_info_em(symbol=stock_code)
        info.to_csv(f"{stock_code}_info.csv", index=False, encoding='utf-8-sig')
        print("✅ 基本信息获取成功！")
    except Exception as e:
        print(f"❌ 基本信息获取失败: {e}")

    # 2. 获取历史行情（加3次重试）
    for attempt in range(3):
        try:
            # 自动适配上海或深圳的股票代码前缀
symbol_prefix = f"sh{stock_code}" if stock_code.startswith("6") else f"sz{stock_code}"
hist = ak.stock_zh_a_daily(symbol=symbol_prefix, start_date="20200101", adjust="qfq")
            hist.to_csv(f"{stock_code}_hist.csv", index=False, encoding='utf-8-sig')
            print("✅ 历史行情获取成功！")
            break
        except Exception as e:
            print(f"⚠️ 第 {attempt+1} 次尝试失败，1秒后重试...")
            time.sleep(1)
    else:
        print("❌ 历史行情获取彻底失败，请检查网络。")

    # 3. 获取财务指标（加3次重试）
    for attempt in range(3):
        try:
            fin = ak.stock_financial_analysis_indicator(symbol=stock_code, start_year="2020")
            fin.to_csv(f"{stock_code}_fin.csv", index=False, encoding='utf-8-sig')
            print("✅ 财务指标获取成功！")
            break
        except Exception as e:
            print(f"⚠️ 第 {attempt+1} 次尝试失败，1秒后重试...")
            time.sleep(1)
    else:
        print("❌ 财务指标获取彻底失败。")

    # 4. 获取估值数据（加3次重试）
    for attempt in range(3):
        try:
            pe = ak.stock_a_indicator_lg(symbol=stock_code)
            pe.to_csv(f"{stock_code}_pe.csv", index=False, encoding='utf-8-sig')
            print("✅ 估值数据获取成功！")
            break
        except Exception as e:
            print(f"⚠️ 第 {attempt+1} 次尝试失败，1秒后重试...")
            time.sleep(1)
    else:
        print("❌ 估值数据获取彻底失败。")

if __name__ == "__main__":
    fetch_stock_data("600519")
