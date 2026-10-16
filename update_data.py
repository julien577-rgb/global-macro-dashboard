import akshare as ak
from datetime import datetime

print(f"[{datetime.now()}] 开始自动更新宏观数据...")

# ===== 中国数据 =====
cpi_data = ak.macro_china_cpi()
cpi_data.to_csv('cpi_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 CPI 数据更新成功！")

gdp_data = ak.macro_china_gdp()
gdp_data.to_csv('gdp_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 GDP 数据更新成功！")

ppi_data = ak.macro_china_ppi()
ppi_data.to_csv('ppi_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 PPI 数据更新成功！")

m2_data = ak.macro_china_money_supply()
m2_data.to_csv('m2_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 M2 数据更新成功！")

lpr_data = ak.macro_china_lpr()
lpr_data.to_csv('lpr_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 LPR 数据更新成功！")

pmi_data = ak.macro_china_pmi()
pmi_data.to_csv('pmi_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 PMI 数据更新成功！")

shrzgm_data = ak.macro_china_shrzgm()
shrzgm_data.to_csv('shrzgm_data.csv', index=False, encoding='utf-8-sig')
print("✅ 中国 社融数据更新成功！")

# ===== 美国数据 =====
us_gdp_data = ak.macro_usa_gdp_monthly()
us_gdp_data.to_csv('us_gdp_data.csv', index=False, encoding='utf-8-sig')
print("✅ 美国 GDP 数据更新成功！")

us_cpi_data = ak.macro_usa_cpi_monthly()
us_cpi_data.to_csv('us_cpi_data.csv', index=False, encoding='utf-8-sig')
print("✅ 美国 CPI 数据更新成功！")

us_unemployment_data = ak.macro_usa_unemployment_rate()
us_unemployment_data.to_csv('us_unemployment_data.csv', index=False, encoding='utf-8-sig')
print("✅ 美国 失业率数据更新成功！")

us_rate_data = ak.macro_bank_usa_interest_rate()
us_rate_data.to_csv('us_rate_data.csv', index=False, encoding='utf-8-sig')
print("✅ 美国 联邦基金利率数据更新成功！")

# ===== 日本数据 =====
jp_rate_data = ak.macro_japan_bank_rate()
jp_rate_data.to_csv('jp_rate_data.csv', index=False, encoding='utf-8-sig')
print("✅ 日本 央行利率数据更新成功！")

jp_cpi_data = ak.macro_japan_cpi_yearly()
jp_cpi_data.to_csv('jp_cpi_data.csv', index=False, encoding='utf-8-sig')
print("✅ 日本 CPI 数据更新成功！")

# ===== 欧洲数据 =====
eu_rate_data = ak.macro_bank_euro_interest_rate()
eu_rate_data.to_csv('eu_rate_data.csv', index=False, encoding='utf-8-sig')
print("✅ 欧洲 央行利率数据更新成功！")

# ===== 印度数据 =====
in_rate_data = ak.macro_bank_india_interest_rate()
in_rate_data.to_csv('in_rate_data.csv', index=False, encoding='utf-8-sig')
print("✅ 印度 央行利率数据更新成功！")
