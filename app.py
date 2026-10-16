import streamlit as st
import pandas as pd

st.set_page_config(page_title="全球宏观经济数据看板", layout="wide")
st.title("🌍 全球宏观经济数据看板")

def safe_format_date(series):
    def _fmt(val):
        s = str(val).strip()
        try:
            if '年' in s and '月' in s: return s
            if '-' in s:
                parts = s.split('-')
                if len(parts) >= 2: return f"{parts[0]}年{int(parts[1])}月份"
            if len(s) == 6 and s.isdigit(): return f"{s[:4]}年{int(s[4:6])}月份"
            if len(s) >= 8 and s[:4].isdigit(): return f"{s[:4]}年{int(s[5:7])}月份"
        except Exception: pass
        return s
    return series.astype(str).apply(_fmt)

@st.cache_data
def load_all_data():
    files = {
        'cpi': 'cpi_data.csv', 'gdp': 'gdp_data.csv', 'ppi': 'ppi_data.csv',
        'm2': 'm2_data.csv', 'lpr': 'lpr_data.csv', 'pmi': 'pmi_data.csv',
        'shrzgm': 'shrzgm_data.csv', 'us_gdp': 'us_gdp_data.csv',
        'us_cpi': 'us_cpi_data.csv', 'us_unemployment': 'us_unemployment_data.csv',
        'us_rate': 'us_rate_data.csv', 'jp_rate': 'jp_rate_data.csv',
        'jp_cpi': 'jp_cpi_data.csv', 'eu_rate': 'eu_rate_data.csv',
        'in_rate': 'in_rate_data.csv',
    }
    data = {}
    for name, path in files.items():
        try:
            df = pd.read_csv(path)
            for col in df.columns:
                if col in ['月份', '日期', 'TRADE_DATE', '时间']:
                    df[col] = safe_format_date(df[col])
            data[name] = df
        except FileNotFoundError:
            data[name] = None
    return data

all_data = load_all_data()

# 中国数据智能画图（只保留指定的 X 和 Y 两列，剔除干扰列）
def cn_chart(df, title, unit, x_candidates, y_candidates, chart_type="line"):
    if df is None or len(df) == 0:
        st.warning(f"{title} 暂无数据"); return
    st.subheader(title)
    st.caption(f"纵坐标单位：{unit}")
    
    col_x = df.columns[0]
    for c in x_candidates:
        if c in df.columns: col_x = c; break
            
    col_y = None
    for c in y_candidates:
        if c in df.columns: col_y = c; break
            
    if col_y is None:
        st.error(f"⚠️ 找不到数值列，请检查 {title} 的原始数据表。"); return
        
    # 核心修复：只取出这两列，彻底解决双坐标轴问题！
    plot_df = df[[col_x, col_y]].copy()
    plot_df[col_y] = pd.to_numeric(plot_df[col_y], errors='coerce').fillna(0)
    plot_df[col_x] = plot_df[col_x].astype(str)
    
    if chart_type == "line":
        st.line_chart(plot_df, x=col_x, y=col_y)
    else:
        st.bar_chart(plot_df, x=col_x, y=col_y)

# 外国数据专属画图
def foreign_chart(df, title, unit):
    if df is None or len(df) == 0:
        st.warning(f"{title} 暂无数据"); return
    st.subheader(title)
    st.caption(f"纵坐标单位：{unit}")
    
    col_x = '日期' if '日期' in df.columns else df.columns[0]
    col_y = '今值' if '今值' in df.columns else df.columns[1]
    
    plot_df = df[[col_x, col_y]].copy()
    plot_df[col_y] = pd.to_numeric(plot_df[col_y], errors='coerce').fillna(0)
    plot_df[col_x] = plot_df[col_x].astype(str)
    
    if len(plot_df) == 1:
        st.metric(label=title, value=plot_df[col_y].iloc[0])
    else:
        st.line_chart(plot_df, x=col_x, y=col_y)

# 创建标签页
tab_cn, tab_us, tab_jp, tab_eu, tab_in = st.tabs(["🇨🇳 中国", "🇺🇸 美国", "🇯🇵 日本", "🇪🇺 欧洲", "🇮🇳 印度"])

with tab_cn:
    st.header("中国宏观经济数据")
    cn_chart(all_data['cpi'], "居民消费价格指数 (CPI)", "指数（上年同月=100）", ['月份', '日期'], ['全国-当月'])
    cn_chart(all_data['gdp'], "国内生产总值 (GDP)", "亿元（绝对值）", ['季度', '日期'], ['国内生产总值-绝对值'], "bar")
    cn_chart(all_data['ppi'], "工业生产者出厂价格指数 (PPI)", "指数（上年同月=100）", ['月份', '日期'], ['当月'])
    cn_chart(all_data['m2'], "货币供应量 (M2)", "亿元", ['月份', '日期'], ['货币和准货币(M2)-数量(亿元)'])
    cn_chart(all_data['lpr'], "贷款市场报价利率 (LPR)", "利率（%）", ['TRADE_DATE', '日期'], ['LPR1Y', '1年期'])
    cn_chart(all_data['pmi'], "采购经理指数 (PMI)", "指数（50为荣枯线）", ['月份', '日期'], ['制造业-指数'])
    cn_chart(all_data['shrzgm'], "社会融资规模 (社融)", "亿元（增量）", ['月份', '日期'], ['社会融资规模增量'])

with tab_us:
    st.header("美国宏观经济数据")
    foreign_chart(all_data['us_gdp'], "美国 GDP 月率", "%")
    foreign_chart(all_data['us_cpi'], "美国 CPI 月率", "%")
    foreign_chart(all_data['us_unemployment'], "美国失业率", "%")
    foreign_chart(all_data['us_rate'], "美国联邦基金利率", "%")

with tab_jp:
    st.header("日本宏观经济数据")
    foreign_chart(all_data['jp_rate'], "日本央行利率", "%")
    foreign_chart(all_data['jp_cpi'], "日本 CPI 年率", "%")

with tab_eu:
    st.header("欧洲宏观经济数据")
    foreign_chart(all_data['eu_rate'], "欧洲央行利率", "%")

with tab_in:
    st.header("印度宏观经济数据")
    foreign_chart(all_data['in_rate'], "印度央行利率", "%")

with st.expander("📂 查看所有原始数据表"):
    for name, df in all_data.items():
        if df is not None:
            st.write(f"**{name}**")
            st.dataframe(df)
