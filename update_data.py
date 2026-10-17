import akshare as ak
import pandas as pd
from datetime import datetime

print(f"[{datetime.now()}] 开始更新宏观数据...")

# 定义一个容错函数，避免某个接口崩掉导致整个脚本终止
def safe_fetch(name, func, filename):
    try:
        df = func()
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"✅ {name} 数据更新成功！")
    except Exception as e:
        print(f"❌ {name} 抓取失败：{e}")

# ===== 🇨🇳 中国数据 =====
safe_fetch("中国 CPI", ak.macro_china_cpi, 'cpi_data.csv')
safe_fetch("中国 GDP", ak.macro_china_gdp, 'gdp_data.csv')
safe_fetch("中国 PPI", ak.macro_china_ppi, 'ppi_data.csv')
safe_fetch("中国 M2", ak.macro_china_money_supply, 'm2_data.csv')
safe_fetch("中国 LPR", ak.macro_china_lpr, 'lpr_data.csv')
safe_fetch("中国 PMI", ak.macro_china_pmi, 'pmi_data.csv')
safe_fetch("中国 社融", ak.macro_china_shrzgm, 'shrzgm_data.csv')

# ===== 🇺🇸 美国数据 =====
safe_fetch("美国 GDP", ak.macro_usa_gdp_monthly, 'us_gdp_data.csv')
safe_fetch("美国 CPI", ak.macro_usa_cpi_monthly, 'us_cpi_data.csv')
safe_fetch("美国 失业率", ak.macro_usa_unemployment_rate, 'us_unemployment_data.csv')
safe_fetch("美国 联邦基金利率", ak.macro_bank_usa_interest_rate, 'us_rate_data.csv')
safe_fetch("美国 非农就业", ak.macro_usa_non_farm, 'us_non_farm.csv')
safe_fetch("美国 ADP就业", ak.macro_usa_adp_employment, 'us_adp.csv')
safe_fetch("美国 核心CPI", ak.macro_usa_core_cpi_monthly, 'us_core_cpi.csv')
safe_fetch("美国 核心PCE", ak.macro_usa_core_pce_price, 'us_core_pce.csv')
safe_fetch("美国 消费者信心", ak.macro_usa_cb_consumer_confidence, 'us_consumer_confidence.csv')
safe_fetch("美国 耐用品订单", ak.macro_usa_durable_goods_orders, 'us_durable_goods.csv')
safe_fetch("美国 成屋销售", ak.macro_usa_exist_home_sales, 'us_exist_home_sales.csv')
safe_fetch("美国 营建许可", ak.macro_usa_building_permits, 'us_building_permits.csv')

# ===== 🇯🇵 日本数据 =====
safe_fetch("日本 央行利率", ak.macro_japan_bank_rate, 'jp_rate_data.csv')
safe_fetch("日本 CPI年率", ak.macro_japan_cpi_yearly, 'jp_cpi_data.csv')
safe_fetch("日本 核心CPI", ak.macro_japan_core_cpi_yearly, 'jp_core_cpi.csv')
safe_fetch("日本 失业率", ak.macro_japan_unemployment_rate, 'jp_unemployment.csv')

# ===== 🇪🇺 欧洲数据 =====
safe_fetch("欧洲 央行利率", ak.macro_bank_euro_interest_rate, 'eu_rate_data.csv')
safe_fetch("欧元区 GDP", ak.macro_euro_gdp_yoy, 'eu_gdp.csv')
safe_fetch("欧元区 CPI", ak.macro_euro_cpi_mom, 'eu_cpi_mom.csv')
safe_fetch("欧元区 PPI", ak.macro_euro_ppi_mom, 'eu_ppi_mom.csv')
safe_fetch("欧元区 零售销售", ak.macro_euro_retail_sales_mom, 'eu_retail_sales.csv')
safe_fetch("欧元区 贸易帐", ak.macro_euro_trade_balance, 'eu_trade_balance.csv')

# ===== 🇮🇳 印度数据 =====
safe_fetch("印度 央行利率", ak.macro_bank_india_interest_rate, 'in_rate_data.csv')

print("\n全部数据抓取完毕！")
