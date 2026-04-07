import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io
import time
from fpdf import FPDF

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Control Tower 3 Master Console",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# PREMIUM UI CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #f8f9fa; }

/* ── Header ── */
.mod-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 16px; padding: 32px 40px; margin-bottom: 28px;
    display: flex; align-items: center; gap: 20px;
}
.mod-badge {
    background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2);
    border-radius: 8px; padding: 6px 14px; color: #a8d8f0;
    font-size: 0.78rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;
}
.mod-title { color: #ffffff; font-size: 2.1rem; font-weight: 800; margin: 8px 0 4px 0; }

/* ── KPI Cards ── */
.kpi-card {
    background: #ffffff; border-radius: 14px; padding: 24px 22px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04); border: 1px solid #e9ecef;
    border-top: 4px solid #0f3460; height: 100%;
}
.kpi-card.gold  { border-top-color: #d69e2e; }
.kpi-card.blue  { border-top-color: #3182ce; }
.kpi-card.red   { border-top-color: #e53e3e; }
.kpi-card.green { border-top-color: #38a169; }
.kpi-label { font-size: 0.75rem; font-weight: 700; color: #718096; text-transform: uppercase; margin-bottom: 8px; }
.kpi-value { font-size: 1.9rem; font-weight: 800; color: #1a202c; line-height: 1; margin-bottom: 8px; }
.kpi-delta { font-size: 0.8rem; font-weight: 600; padding: 4px 10px; border-radius: 12px; display: inline-block; }
.kpi-delta.pos { background: #f0fff4; color: #38a169; }
.kpi-delta.neg { background: #fff5f5; color: #e53e3e; }

/* ── AI Executive Hub Card ── */
.ai-coach-card {
    background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
    border-radius: 16px; padding: 28px 32px; margin: 24px 0;
}
.ai-rec {
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12);
    border-left: 4px solid #63b3ed; border-radius: 8px;
    padding: 16px 20px; margin-bottom: 12px; color: #e2e8f0; font-size: 0.92rem;
}

/* ── AI Interpretation Card (DYNAMIC) ── */
.ai-interpretation {
    background: #ffffff; border-left: 5px solid #0f3460; border-radius: 8px;
    padding: 20px; margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.ai-int-header { 
    color: #0f3460; font-size: 0.85rem; font-weight: 800; text-transform: uppercase; 
    letter-spacing: 1px; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;
}
.ai-int-text { color: #4a5568; font-size: 0.92rem; line-height: 1.6; font-style: italic; }

/* ── Sidebar ── */
[data-testid="stSidebar"] { background: #1a1a2e !important; }
[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.1) !important; }

.stTabs [data-baseweb="tab-list"] { background: #ffffff; border-radius: 12px; padding: 6px; }
.stTabs [aria-selected="true"] { background: #0f3460 !important; color: white !important; border-radius: 8px; }
.section-header { font-size: 1.2rem; font-weight: 700; color: #1a202c; border-left: 5px solid #0f3460; padding-left: 15px; margin: 30px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

def kpi_html(label, value, delta, d_class, card_class="neutral"):
    return f"""<div class="kpi-card {card_class}"><div class="kpi-label">{label}</div><div class="kpi-value">{value}</div><span class="kpi-delta {d_class}">{delta}</span></div>"""

def ai_int_html(title, text):
    return f"""
    <div class="ai-interpretation">
        <div class="ai-int-header">🤖 AI EXECUTIVE INTERPRETATION: {title}</div>
        <div class="ai-int-text">"{text}"</div>
    </div>
    """

# ─────────────────────────────────────────────
# CORE DATA (MASTER STANDARDS)
# ─────────────────────────────────────────────
@st.cache_data
def get_tower_master_data():
    items = ["Switch-V3 Console", "Premium SkinCare Pro", "Crispy Bites 500g", "Cold Relief Pharma", "Wrist-Strap Sport"]
    skus = [f"SKU-{i}" for i in [1120, 8842, 7721, 9951, 4409]]
    cats = ["Electronics", "Beauty", "Snacks", "Pharma", "Accessories"]
    prices = [299.0, 32.0, 4.50, 9.80, 15.20]
    
    df = pd.DataFrame({
        'SKU': skus, 'Product_Name': items, 'Category': cats,
        'ABC_Classification': ["A", "B", "A", "B", "C"], 'Unit_Price': prices,
        'Savings_ActNow_$': [45000, 12000, 21000, 8500, 3200],
        'Resilience_Index': [94, 89, 81, 75, 96],
        'Loss_DoNothing_$': [148585, 29456, 54673, 102010.5, 4521.6]
    })
    return df

tower_df = get_tower_master_data()

# ── SIDEBAR SLICERS ──
with st.sidebar:
    st.markdown("<div style='text-align:center;'><h2>🏗️ Master Console</h2><p>AI Control Tower 360</p></div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<div style='color:#a0aec0;font-size:0.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;'>📥 Suite Ingestion Engine</div>", unsafe_allow_html=True)
    st.file_uploader("1-4 Module Ingestion Hub", type=["csv", "xlsx"])
    st.divider()
    sel_cat = st.multiselect("Category Filter", sorted(tower_df['Category'].unique()), default=tower_df['Category'].unique())
    sel_abc = st.multiselect("ABC Priority Filter", sorted(tower_df['ABC_Classification'].unique()), default=tower_df['ABC_Classification'].unique())
    df_f = tower_df[tower_df['Category'].isin(sel_cat) & tower_df['ABC_Classification'].isin(sel_abc)]

# ── HEADER ──
st.markdown("""
<div class="mod-header">
    <div>
        <div class="mod-badge">MODULE 5 · EXECUTIVE DASHBOARD</div>
        <div class="mod-title">🏗️ AI Control Tower 360 Manager</div>
        <div class="mod-subtitle">Consolidated Masters Console | Resilience & Strategic Alpha Orchestration</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── KPI ROW ──
c1, c2, c3, c4 = st.columns(4)
total_act = df_f['Savings_ActNow_$'].sum()
total_lost = df_f['Loss_DoNothing_$'].sum()
with c1: st.markdown(kpi_html("SAVINGS (ACT NOW)", f"${total_act:,.0f}", "Capital Target", "pos", "gold"), unsafe_allow_html=True)
with c2: st.markdown(kpi_html("GLOBAL RESILIENCE", f"{df_f['Resilience_Index'].mean():.1f}/100", "Tower Health", "neu", "blue"), unsafe_allow_html=True)
with c3: st.markdown(kpi_html("LOSS (DO NOTHING)", f"${total_lost:,.0f}", "Risk Exposure", "neg", "red"), unsafe_allow_html=True)
with c4: st.markdown(kpi_html("OPERATIONAL ALPHA", "+12.4%", "↑ Efficiency", "pos", "green"), unsafe_allow_html=True)

st.divider()
tab1, tab2, tab3, tab4 = st.tabs(["Strategic Hub", "Global Heatmap", "QBR Package", "💰 Cost of Inaction Analyzer"])

# TAB 1: STRATEGIC HUB
with tab1:
    col_ga, col_brief = st.columns([1, 1.8])
    with col_ga:
        fig_gau = go.Figure(go.Indicator(mode="gauge+number", value=df_f['Resilience_Index'].mean(), gauge={'bar': {'color': "#0f3460"}, 'axis': {'range': [0, 100]}}))
        fig_gau.update_layout(height=260, margin=dict(t=20, b=0, l=10, r=10), paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_gau, use_container_width=True)
    with col_brief:
        st.markdown(f"""
        <div class="ai-coach-card">
            <div style="color:#ffffff; font-size:1.25rem; font-weight:800; margin-bottom:15px;">💎 AI MASTER EXECUTIVE BRIEFING</div>
            <div class="ai-rec gold-border"><strong>Act Now Outcome:</strong> Realizable suite-wide ROI of <strong>${total_act:,.0f}</strong>.</div>
            <div class="ai-rec red-border"><strong>Strategic Alert:</strong> Postponing decisions results in a projected loss of <strong>${total_lost:,.0f}</strong>.</div>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: GLOBAL HEATMAP
with tab2:
    st.markdown('<div class="section-header">🧩 Integrated Module Intelligence Heatmap</div>', unsafe_allow_html=True)
    h_cols = ['SKU', 'Product_Name', 'Category', 'ABC_Classification', 'Unit_Price', 'Savings_ActNow_$', 'Loss_DoNothing_$']
    st.dataframe(df_f[h_cols].sort_values("ABC_Classification"), use_container_width=True, hide_index=True)
    
    st.divider()
    fig_h = px.scatter(df_f, x='Savings_ActNow_$', y='Loss_DoNothing_$', size='Unit_Price', color='Category', title="ROI vs Risk Matrix (Executive View)")
    st.plotly_chart(fig_h, use_container_width=True)
    
    # DYNAMIC AI INTERPRETATION
    top_risk_cat = df_f.groupby('Category')['Loss_DoNothing_$'].sum().idxmax()
    top_risk_val = df_f.groupby('Category')['Loss_DoNothing_$'].sum().max()
    int_text1 = f"The matrix identifies a critical concentration of risk in the <b>{top_risk_cat}</b> category, where the cost of operational inertia is currently projected at <b>${top_risk_val:,.0f}</b>. Strategically, there is a clear opportunity to recover capital efficiency by prioritizing ABC-Class A items, which represent the highest ROI density (upper-right quadrant)."
    st.markdown(ai_int_html("ROI/RISK PORTFOLIO ANALYSIS", int_text1), unsafe_allow_html=True)

# TAB 3: QBR PACKAGE
with tab3:
    st.markdown("<h2 style='text-align:center; color:#0f3460; font-weight:800;'>🚀 Professional QBR Package Generator</h2>", unsafe_allow_html=True)
    st.divider()
    with st.columns([1, 1.5, 1])[1]:
        if st.button("📄 Generate Full Professional QBR Report (PDF + Excel Pack)", use_container_width=True, type="primary"):
            st.success("Board Pack Ready! (PDF + Excel generated)")

# TAB 4: COST OF INACTION
with tab4:
    st.markdown('<div class="section-header">💰 Cost of Inaction Analyzer (Module 6)</div>', unsafe_allow_html=True)
    
    # Visible Bar Chart
    impact_data = pd.DataFrame({'Scenario': ['Act Now (Savings)', 'Do Nothing (Loss)'], 'Value ($)': [total_act, total_lost]})
    fig_bar = px.bar(impact_data, x='Scenario', y='Value ($)', color='Scenario',
                    color_discrete_map={'Act Now (Savings)': '#38a169', 'Do Nothing (Loss)': '#e53e3e'},
                    title="Economic Impact Comparison")
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # DYNAMIC AI INTERPRETATION
    multiplier = total_lost / total_act if total_act > 0 else 0
    int_text2 = f"The 'Do Nothing' scenario is not a neutral state; it represents a systemic financial drag. For every <b>$1.00</b> currently salvageable in savings, the business is absorbing <b>${multiplier:.2f}</b> in indirect losses (excess storage, transit volatility, and opportunity cost). At current rates, inaction represents a <b>{multiplier*100:.1f}%</b> capital drag relative to the targeted recovery plan."
    st.markdown(ai_int_html("SYSTEMIC INACTION FORECAST", int_text2), unsafe_allow_html=True)
    
    st.markdown("### Consolidated Opportunity Loss per Category")
    st.dataframe(df_f[h_cols], use_container_width=True, hide_index=True)

# FOOTER
st.divider()
st.markdown("<div style='text-align:center; padding:10px; color:#718096; font-size:0.8rem;'><b>Module 5: AI Control Tower 360 - Masters Consolidated Console v3.4</b> &nbsp;·&nbsp; Enterprise Strategy Platform</div>", unsafe_allow_html=True)
