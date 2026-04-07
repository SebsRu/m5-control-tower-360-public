# Module 5 — AI Control Tower 360 — Executive Masters Console

**Part of the Supply Chain AI Suite** | By Sebastián Rueda, Supply Chain AI Orchestrator

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://m5-control-tower-360-public-jmieqpoyedjmbpfqqrh99x.streamlit.app)

---

## 🎯 The Problem

By the time executives reach the boardroom, they face a critical blind spot:

- **M1, M2, M3, M4 each delivered insights, but WHERE IS THE UNIFIED VISION?** (Data scattered across 4 tools)
- **How do I synthesize 15+ metrics into ONE strategic decision?** (Executive overwhelm)
- **What is the TRUE financial impact if we do nothing vs. act now?** (Business case quantification)
- **Can I generate a board-ready QBR in minutes, not days?** (Time-to-insight)

Executive teams spend **weeks** pulling data from four modules, building PowerPoint decks, and second-guessing financial impact. **Module 5** answers all four in **one dashboard, one click**.

---

## 💡 The Solution

**Module 5** is an AI-powered executive intelligence console that:

✅ **Consolidates** findings from M1–M4 into a single Strategic Hub
✅ **Visualizes** global resilience metrics (SKU health, category risk, ABC priority)
✅ **Quantifies** dual scenarios: **Act Now** (Savings) vs. **Do Nothing** (Loss)
✅ **Generates** professional QBR reports (PDF + Excel) in one click
✅ **Provides** dynamic AI executive interpretation for every insight
✅ **Enables** C-suite strategic decision-making in real time

---

## 🚀 Live Demo

### **👉 [Launch the App](https://m5-control-tower-360-public-jmieqpoyedjmbpfqqrh99x.streamlit.app)**

Try it now with **demo data** (5 Kellanov SKUs across 5 categories) or **upload consolidated M1–M4 exports**.

### What you'll see:

**🏆 Tab 1 — Strategic Hub**
- Resilience Index gauge (tower health: 0–100)
- AI Master Executive Briefing (Act Now outcome + Strategic alerts)
- Dual-scenario financial impact (Savings vs. Loss)
- Dynamic AI interpretation of consolidated portfolio

**🧩 Tab 2 — Global Heatmap**
- Integrated Module Intelligence table (SKU-level metrics from M1–M4)
- ROI vs. Risk scatter matrix (savings vs. loss by category)
- Category-level concentration analysis
- AI-powered portfolio interpretation (top risk zones, ABC priority opportunities)

**📄 Tab 3 — QBR Package**
- One-click professional report generation
- PDF: Strategic Executive Summary + ROI matrices + Strategic Roadmap
- Excel: Complete SKU-level detail + financial analysis
- Board-ready formatting (no manual editing)

**💰 Tab 4 — Cost of Inaction Analyzer**
- Economic Impact Comparison chart (Act Now vs. Do Nothing)
- Systemic financial drag analysis
- Per-category opportunity loss breakdown
- AI-powered "inaction forecast" interpretation

---

## 📊 Key Metrics

| Metric | What It Means | Source |
|--------|---------------|--------|
| **Resilience Index** | Portfolio health score (0–100) based on M1–M4 weighted maturity | Consolidated |
| **Savings (Act Now)** | Realizable suite-wide ROI if recommendations are implemented immediately | M1–M4 |
| **Loss (Do Nothing)** | Projected financial drag from operational inertia (excess inventory, lost sales, supply delays) | M1–M4 |
| **ABC Classification** | Pareto-based SKU segmentation for priority action | M2 |
| **Unit Price** | Average selling price per SKU | M1–M4 |
| **Global Category Risk** | Concentration of financial exposure by category | M1–M4 |
| **Operational Alpha** | Efficiency gain % from implementing all M1–M4 recommendations | Consolidated |

---

## 🏗 Architecture

```
M1–M4 Outputs (Forecast, Inventory, Replenishment, OTIF)
    ↓
ETL Pipeline (Pandas consolidation)
    ├─ Weighted Resilience Index (maturity scoring)
    ├─ Dual-scenario Financial Model (Act Now vs. Do Nothing)
    ├─ ABC Classification (Pareto aggregation)
    ├─ Category-level Risk Concentration
    └─ AI Executive Interpretation Engine
    ↓
Streamlit Executive Dashboard
    ├─ 4 Strategic Tabs
    ├─ 4 KPI Cards (Savings, Resilience, Loss, Alpha)
    ├─ Plotly Interactive Visualizations (Gauge, Scatter, Bar)
    ├─ AI-powered Dynamic Insights
    └─ Export Functions (PDF + Excel QBR)
    ↓
Outputs
    ├─ PDF → Board / C-Suite / Stakeholder Review
    ├─ Excel → Finance / Operations for implementation tracking
    └─ Dashboard → Real-time executive visibility
```

---

## 📥 Input Format

Upload a consolidated CSV or Excel file with outputs from M1–M4:

| Column | Type | Example | Source |
|--------|------|---------|--------|
| `SKU` | String | "SKU-1120" | M1–M4 |
| `Product_Name` | String | "Switch-V3 Console" | M1–M4 |
| `Category` | String | "Electronics" | M2 |
| `ABC_Classification` | String | "A" | M2 |
| `Unit_Price` | Float | 299.0 | M1–M4 |
| `Savings_ActNow_$` | Float | 45000 | M1–M4 |
| `Loss_DoNothing_$` | Float | 148585 | M1–M4 |
| `Resilience_Index` | Integer | 94 | Consolidated |

**If no file is uploaded**, the app runs with **5 synthetic Kellanov SKUs** (demo dataset) with realistic pharma/CPG financial scenarios.

---

## 💻 Tech Stack

- **Frontend:** Streamlit (Python web framework)
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly (interactive gauge, scatter, bar charts)
- **Reporting:** FPDF (PDF generation)
- **Styling:** Custom CSS (Premium Light theme, Inter typography)
- **Deployment:** Streamlit Community Cloud

---

## 🔄 Part of the Supply Chain AI Suite

| Module | Tool | Status | Link |
|--------|------|--------|------|
| **M1** | Demand Planning — AI Forecast Comparator | ✅ Live | [Demo](https://m1-demand-forecast-public.streamlit.app) |
| **M2** | Inventory Diagnosis & Coverage Analyzer | ✅ Live | [Demo](https://m2-inventory-diagnosis-public.streamlit.app) |
| **M3** | Replenishment Coach — Safety Stock Calculator | 🔄 In Dev | — |
| **M4** | Procurement — OTIF Risk Tracker | 🔄 In Dev | — |
| **M5** | **Control Tower 360 — Executive Dashboard** | ✅ **THIS** | **[Live](https://m5-control-tower-360-public-jmieqpoyedjmbpfqqrh99x.streamlit.app)** |

Module flow: **M1 → M2 → M3 → M4 → M5 (Consolidated Executive Dashboard)**

---

## 👤 About

**Sebastián Rueda** — Supply Chain AI Orchestrator

- 7+ years in **Pharma** (Novartis Colombia) and **CPG** (Kellanov)
- Pioneered **Kinaxis Maestro** implementation in Colombia
- Expert in: Demand Planning, Inventory Optimization, Supply Chain Analytics, Executive Strategy

**Connect:**
- [LinkedIn](https://www.linkedin.com/in/sebastiaan-rueda)
- [GitHub](https://github.com/SebsRu)

---

## 📜 License

Code available under **NDA** for commercial use. Contact for licensing.

---

## 🎓 Learn More

**Want to understand the math?**

**Resilience Index (Consolidated Score)**
- Weighted average of maturity scores from M1–M4
- Formula: `(M1_Health + M2_Health + M3_Health + M4_Health) / 4`
- Range: 0–100 (higher = more resilient)
- Interpretation: Reflects overall supply chain optimization across all four modules

**Savings (Act Now)**
- Sum of all financial recovery opportunities identified in M1–M4
- Formula: `SUM(Inventory Optimization + Demand Planning Benefits + OTIF Improvements + Replenishment Efficiency)`
- Impact: Realizable within 60–90 days of implementation
- ABC Class A items prioritized for highest ROI

**Loss (Do Nothing)**
- Projected financial drag from operational inertia
- Formula: `SUM(Excess Inventory Cost + Lost Sales Revenue + Supply Chain Delays + Inefficiency Penalties)`
- Period: Annual forward-looking estimate
- Interpretation: Compounding cost of delayed decision-making

**Cost of Inaction Multiplier**
- Formula: `Loss_DoNothing_$ / Savings_ActNow_$`
- Example: If multiplier = 2.8x, then every $1 not saved = $2.80 in additional loss
- Strategic insight: Acts as a business case justification for swift implementation

**ABC Classification (Pareto Principle)**
- Class A: Top 20% of value (80% of management attention)
- Class B: Next 30% of value
- Class C: Remaining 50% of value (20% of attention)
- Application: Prioritize Act Now investments in Class A items first

---

**Ready to make strategic supply chain decisions with confidence?** 👉 [Launch the App](https://m5-control-tower-360-public-jmieqpoyedjmbpfqqrh99x.streamlit.app)
