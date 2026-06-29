import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import random
import os

def render_skill_block(title, skills):
    st.markdown(f'<h3 style="color: #00D4FF; margin-bottom: 10px;">{title}</h3>', unsafe_allow_html=True)
    for name, perc in skills:
        st.markdown(f'''
        <div style="margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                <span style="font-weight: bold; color: #00D4FF;">{name}</span>
                <span>{perc}%</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 10px; overflow: hidden;">
                <div style="background: #00D4FF; width: {perc}%; height: 100%; border-radius: 10px;"></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

st.set_page_config(
    page_title="Arpit Arora | Commercial Professional",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main {background: #0E1117; color: #FAFAFA; padding: 2rem;}
.section-header {font-size: 2rem; font-weight: bold; color: #00D4FF; margin: 2rem 0 1.5rem;}
.card {background: rgba(255,255,255,0.05); border: 1px solid rgba(0,212,255,0.2); border-radius: 10px; padding: 20px; margin-bottom: 20px;}
.stat-badge {background: rgba(0,212,255,0.1); border: 1px solid #00D4FF; border-radius: 20px; padding: 5px 15px; color: #00D4FF; font-weight: bold; display: inline-block; margin: 5px;}
.contact-card {background: rgba(255,255,255,0.05); border: 1px solid rgba(124,58,237,0.3); border-radius: 10px; padding: 20px; text-align: center; height: 100%;}
.contact-card h3 {color: #7C3AED; margin-bottom: 15px;}
.profile-img {border-radius: 50%; border: 3px solid #00D4FF; width: 100%; max-width: 260px; aspect-ratio: 1 / 1; object-fit: cover; object-position: center center;}
.progress-bar {background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; margin: 10px 0; overflow: hidden;}
.progress-fill {background: #00D4FF; height: 100%; border-radius: 10px;}
.metric-card {background: rgba(255,255,255,0.05); border: 1px solid rgba(0,212,255,0.2); border-radius: 10px; padding: 15px; text-align: center;}
.metric-label {color: #94a3b8; font-size: 0.85rem;}
.metric-value {color: #FAFAFA; font-size: 1.05rem; font-weight: bold; margin-top: 6px;}
.timeline-dot {width: 14px; height: 14px; border-radius: 50%; background: #00D4FF; margin: 0 auto 10px;}
.timeline-line {width: 3px; min-height: 150px; background: rgba(0,212,255,0.2); margin: 0 auto;}
.contact-card a {color: inherit; text-decoration: none;}
.section-small {color: #94a3b8; margin-bottom: 1rem;}
</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigation", ["HOME", "EXPERIENCE", "SKILLS", "LIVE ANALYSIS", "FINANCE ROADMAP", "CONTACT"])
st.sidebar.markdown("---")
st.sidebar.markdown("**Quick Summary**")
st.sidebar.markdown("📌 Delhi NCR | Pre-Sales | Growth | Commercial Operations")
st.sidebar.markdown("🔧 Built with Python, Streamlit, Plotly")
st.sidebar.markdown("📧 arpitarora.ac@gmail.com")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/arpitarora25/)")

if page == "HOME":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
        import base64
        with open("photo.png", "rb") as f:
            img_data = base64.b64encode(f.read()).decode()
        st.markdown(f'<img src="data:image/png;base64,{img_data}" class="profile-img" style="display:block;margin:0 auto;">', unsafe_allow_html=True)

        st.markdown('<h1 style="color: white; font-size: 2.5rem; font-weight: bold; margin: 20px 0;">ARPIT ARORA</h1>', unsafe_allow_html=True)
        st.markdown('<h2 style="color: #00D4FF; font-size: 1.2rem; margin-bottom: 20px;">Commercial Professional | Pre-Sales & Growth</h2>', unsafe_allow_html=True)
        st.write("📍 Delhi NCR, India")
        st.markdown('<div class="section-small">Back in India from Australia after completing a Bachelor of Business (Accounting & Finance) at University of Wollongong. Three years of real commercial experience advising SME clients and running business operations - not just internships.</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin: 20px 0;">', unsafe_allow_html=True)
        for badge in ["3+ Years Experience", "21 Years Old", "Commercial Professional"]:
            st.markdown(f'<span class="stat-badge">{badge}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/arpitarora25/", type="primary")
        st.markdown('<div class="stat-badge">arpitarora.ac@gmail.com</div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-bottom: 30px;"></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<h2 style="color: #00D4FF; margin-bottom: 20px;">Three Years. Real Clients. Real Revenue.</h2>', unsafe_allow_html=True)
        st.write("""
        Commercial professional with three years of client-facing experience across B2B technology advisory and SME business operations.
        Advised 25-35 SME clients weekly at Telstra, managed deal pipelines on Salesforce CRM, and ran day-to-day P&L and operations at a A$2M retail and wholesale business.
        Open to Pre-Sales, Growth, Customer Success, and Operations roles in Delhi NCR.
        """)

        st.markdown('<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin: 30px 0;">', unsafe_allow_html=True)
        metrics = [
            ("25-35 SME Clients/Week", "Telstra"),
            ("Top 3%", "Regionally"),
            ("2 Countries", "Worked"),
            ("A$2M Business", "Managed")
        ]
        for label, value in metrics:
            st.markdown(f'''
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('''
        <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px;">
            <span class="stat-badge">Salesforce CRM</span>
            <span class="stat-badge">Python</span>
            <span class="stat-badge">Advanced Excel</span>
            <span class="stat-badge">Generative AI</span>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div class="card" style="margin-top: 30px;">
            <h3 style="color: #00D4FF; margin-top: 0;">Education</h3>
            <p><strong>University of Wollongong | Australia</strong></p>
            <p>Feb 2023 - Jun 2026</p>
            <p><strong>Bachelor of Business - Double Major in Accounting & Finance</strong></p>
            <p>AACSB-accredited (top 5% globally)</p>
            <p>QS World University Rankings top 1% globally (2025)</p>
            <p>GPA: 5.7 / 7.0</p>
            <p>Coursework: Financial Accounting, Corporate Finance, Management
            Accounting, Financial Statement Analysis, Taxation, Business Analytics</p>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div style="display: flex; gap: 10px; margin-top: 20px;">
            <span class="stat-badge">Microsoft Certified</span>
            <span class="stat-badge">LinkedIn AI Certified</span>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('<h4 style="color: #00D4FF; margin-top: 20px;">Currently Building</h4>', unsafe_allow_html=True)
        st.markdown('''
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
            <span style="background: rgba(0,212,255,0.1); border: 1px solid #00D4FF; border-radius: 20px; padding: 5px 12px; color: #00D4FF; font-size: 0.8rem; font-weight: bold;">NISM Series V-A (in progress)</span>
            <span style="background: rgba(0,212,255,0.1); border: 1px solid #00D4FF; border-radius: 20px; padding: 5px 12px; color: #00D4FF; font-size: 0.8rem; font-weight: bold;">Excel & Power BI for commercial reporting</span>
            <span style="background: rgba(0,212,255,0.1); border: 1px solid #00D4FF; border-radius: 20px; padding: 5px 12px; color: #00D4FF; font-size: 0.8rem; font-weight: bold;">Streamlit portfolio with live dashboard demo</span>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "EXPERIENCE":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Experience</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        for _ in range(2):
            st.markdown('<div class="timeline-dot"></div>', unsafe_allow_html=True)
            st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div class="card">
            <h3 style="color: #00D4FF; margin-top: 0;"><strong>Telstra</strong> - $2K-$8K deal sizes & Top 3% regionally</h3>
            <p>Mar 2024 - May 2026 | Nowra, NSW, Australia</p>
            <ul style="list-style: none; padding-left: 0;">
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Advised 25-35 SME clients weekly on technology and connectivity solutions, managing
                    deal sizes of $2,000-$8,000 per engagement across a high-volume client-facing environment
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Conducted ROI and cost-benefit assessments to support client investment decisions,
                    translating complex technical options into clear commercial recommendations
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Identified cross-sell and upsell opportunities by analysing client usage patterns and
                    business needs, contributing to consistent portfolio revenue growth
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Managed client pipeline and account documentation using Salesforce CRM, qualifying
                    and routing leads for specialist account teams
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Appointed Official Google Representative - coordinated staff training and managed
                    in-store category performance against defined KPIs
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Ranked top 3% of store personnel across the region with consistent 4-star KPI rating
                </li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="timeline-dot"></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div class="card">
            <h3 style="color: #00D4FF; margin-top: 0;">Operations & Finance Associate</h3>
            <p><strong>Retail and Wholesale SME (~A$2M Annual Turnover)</strong> | Mar 2023 - Mar 2024 | Oak Flats, NSW, Australia</p>
            <p style="font-size: 0.9rem; margin-top: 5px;"><em>King of the Pack</em></p>
            <ul style="list-style: none; padding-left: 0;">
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Supported day-to-day financial and operational performance including P&L management,
                    variance analysis, and cost control across a high-volume trading environment
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Managed inventory ordering, stock control and supplier coordination to maintain
                    working capital efficiency and reduce excess holding costs
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Prepared management P&L reports and conducted variance analysis, reporting
                    findings directly to the business owner
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Implemented standard operating procedures to improve compliance and operational
                    efficiency across the business
                </li>
                <li style="position: relative; padding-left: 25px; margin-bottom: 10px;">
                    <span style="position: absolute; left: 0; color: #00D4FF; font-weight: bold;">•</span>
                    Tools used: MYOB, Xero, QuickBooks, Advanced Excel
                </li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "SKILLS":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Skills</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-small">Commercial, operational, and analytical skills built across real client environments - not classrooms.</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        render_skill_block("Data & Analytics", [("SQL", 55), ("Python", 45), ("Power BI", 55), ("Excel", 95)])
    with col2:
        render_skill_block("Finance & Business", [("Financial Modelling", 85), ("P&L Management", 90), ("Variance Analysis", 85), ("Business Advisory", 88)])
    with col3:
        render_skill_block("Accounting Tools", [("MYOB", 80), ("Xero", 75), ("QuickBooks", 70), ("Advanced Excel", 95)])

    col1, col2 = st.columns(2)
    with col1:
        render_skill_block("Commercial & CRM", [("Salesforce CRM", 85), ("Client Needs Analysis", 90), ("Solution Framing", 85), ("Pipeline Management", 80)])
    with col2:
        render_skill_block("AI & Digital", [("Generative AI", 65), ("Microsoft Copilot", 65), ("Google Workspace", 80), ("Python Scripting", 45)])

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "LIVE ANALYSIS":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Commercial Intelligence Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #999; font-size: 1.2rem; margin-bottom: 30px;">Demonstrating how I translate business data into commercial insights and decisions</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 0.85rem; color: #777; font-style: italic;">Sample dataset for demonstration purposes | Built with Python, Pandas & Plotly</p>', unsafe_allow_html=True)

    regions = ['North', 'South', 'East', 'West']
    categories = ['Furniture', 'Office Supplies', 'Technology']
    sub_categories = {
        'Furniture': ['Chairs', 'Tables', 'Desk Supplies', 'Storage', 'Office Chairs'],
        'Office Supplies': ['Paper', 'Pens', 'Staplers', 'Binders', 'Envelopes'],
        'Technology': ['Laptops', 'Monitors', 'Keyboards', 'Printers', 'Routers']
    }
    products = {
        'Furniture': ['Ergonomic Chair', 'Executive Desk', 'Storage Cabinet', 'Meeting Table', 'File Cabinet'],
        'Office Supplies': ['Premium Paper', 'Fountain Pen Set', 'Desktop Stapler', 'Three-Ring Binder', 'Envelope Collection'],
        'Technology': ['Business Laptop', 'Ultra-Wide Monitor', 'Mechanical Keyboard', 'Laser Printer', 'Wi-Fi Router']
    }

    data = []
    start_date = datetime(2024, 1, 1)
    for i in range(150):
        region = random.choice(regions)
        category = random.choice(categories)
        sub_category = random.choice(sub_categories[category])
        product = random.choice(products[category])
        order_date = start_date + timedelta(days=random.randint(0, 365))
        quantity = random.randint(1, 15)
        unit_price = random.uniform(50, 2000)
        discount = random.uniform(0, 0.3)
        sales = quantity * unit_price * (1 - discount)
        profit_margin = random.uniform(0.15, 0.45)
        profit = sales * profit_margin
        data.append({
            'Order_Date': order_date.strftime('%Y-%m-%d'),
            'Region': region,
            'Category': category,
            'Sub_Category': sub_category,
            'Product_Name': product,
            'Sales': round(sales, 2),
            'Profit': round(profit, 2),
            'Quantity': quantity,
            'Discount': round(discount * 100, 2)
        })

    df = pd.DataFrame(data)

    st.sidebar.header("Filters")
    selected_regions = st.sidebar.multiselect("Region", options=regions, default=regions)
    selected_categories = st.sidebar.multiselect("Category", options=categories, default=categories)
    min_date = pd.to_datetime(df['Order_Date']).min().date()
    max_date = pd.to_datetime(df['Order_Date']).max().date()
    date_range = st.sidebar.date_input("Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    start_date, end_date = date_range
    filtered_df = df[
        (df['Order_Date'] >= pd.Timestamp(start_date)) &
        (df['Order_Date'] <= pd.Timestamp(end_date))
    ]
    filtered_df = filtered_df[
        (filtered_df['Region'].isin(selected_regions)) &
        (filtered_df['Category'].isin(selected_categories))
    ]

    col1, col2, col3, col4 = st.columns(4)
    total_revenue = filtered_df['Sales'].sum()
    total_profit = filtered_df['Profit'].sum()
    total_orders = len(filtered_df)
    profit_margin_pct = (total_profit / total_revenue * 100) if total_revenue > 0 else 0

    with col1:
        st.metric("Total Revenue", f"${total_revenue:,.2f}")
    with col2:
        st.metric("Total Profit", f"${total_profit:,.2f}")
    with col3:
        st.metric("Total Orders", f"{total_orders:,}")
    with col4:
        st.metric("Profit Margin", f"{profit_margin_pct:.1f}%")

    st.subheader("Revenue by Region")
    region_revenue = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    fig1 = px.bar(region_revenue, x='Region', y='Sales', template='plotly_dark')
    fig1.update_traces(marker_color="#00D4FF")
    fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Monthly Sales Trend")
    filtered_df['Month'] = filtered_df['Order_Date'].dt.to_period('M').astype(str)
    monthly_sales = filtered_df.groupby('Month')['Sales'].sum().reset_index()
    fig2 = px.line(monthly_sales, x='Month', y='Sales', template='plotly_dark')
    fig2.update_traces(line_color="#00D4FF", mode='lines+markers', marker=dict(color="#00D4FF", size=8))
    fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top 10 Products by Revenue")
    top_products = filtered_df.groupby('Product_Name')['Sales'].sum().reset_index().sort_values('Sales', ascending=False).head(10)
    fig3 = px.bar(top_products, x='Sales', y='Product_Name', orientation='h', template='plotly_dark')
    fig3.update_traces(marker_color="#7C3AED")
    fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Profit by Category")
    category_profit = filtered_df.groupby('Category')['Profit'].sum().reset_index()
    fig4 = px.pie(category_profit, values='Profit', names='Category', hole=0.4, template='plotly_dark')
    fig4.update_traces(marker=dict(colors=["#00D4FF", "#7C3AED", "#00FF88"]))
    fig4.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown('<h3 style="color: #00D4FF; margin-top: 30px;">Commercial Insights</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''
        <div class="card" style="border-left: 4px solid #00D4FF;">
            <h4 style="color: #00D4FF; margin-top: 0;"><span style="margin-right: 8px;">💡</span>West Region Gap</h4>
            <p style="font-size: 0.9rem;">West region underperforms despite high order volume - potential pricing or product-mix issue worth investigating with the sales team</p>
        </div>
        ''', unsafe_allow_html=True)
    with col2:
        st.markdown('''
        <div class="card" style="border-left: 4px solid #00D4FF;">
            <h4 style="color: #00D4FF; margin-top: 0;"><span style="margin-right: 8px;">💡</span>Q3 Growth Driver</h4>
            <p style="font-size: 0.9rem;">Q3 sales spike driven primarily by Technology - seasonality pattern consistent with back-to-school demand, worth building into sales planning</p>
        </div>
        ''', unsafe_allow_html=True)
    with col3:
        st.markdown('''
        <div class="card" style="border-left: 4px solid #00D4FF;">
            <h4 style="color: #00D4FF; margin-top: 0;"><span style="margin-right: 8px;">💡</span>Revenue Concentration</h4>
            <p style="font-size: 0.9rem;">Top 3 products account for 35% of total revenue - concentration risk if supply chain disrupted; recommend diversifying the pipeline</p>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "FINANCE ROADMAP":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Finance Roadmap</h1>', unsafe_allow_html=True)

    st.markdown('''
    <div class="card" style="border-left: 4px solid #00D4FF; margin-bottom: 30px;">
        <h2 style="color: #FAFAFA; margin-top: 0; font-size: 1.3rem;">The honest version</h2>
        <p style="color: #94a3b8; font-size: 1rem; line-height: 1.7;">
            I have a finance degree and three years of commercial experience advising real clients.
            But I cannot walk into a wealth management or HNI advisory role today.
            Two things are legally and professionally required that I am currently building:
            regulatory credentials (NISM certifications) and financial services work experience (for CFP).
            Neither can be skipped. So I am not trying to skip them.
            This page shows exactly what I am doing and when.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<h2 style="color: #00D4FF; margin-bottom: 25px;">The Roadmap</h2>', unsafe_allow_html=True)

    phases = [
        {
            "phase": "Phase 1",
            "title": "Foundation",
            "timeline": "Now - Month 3",
            "status": "ACTIVE",
            "status_color": "#00FF88",
            "border_color": "#00FF88",
            "items": [
                ("NISM Series V-A", "Mutual Fund Distributors certification - the regulatory entry point for financial advisory in India. 4-6 weeks of study, under INR 2,000."),
                ("Commercial Role", "Applying now for Pre-Sales, Growth, Customer Success, and Operations roles in Delhi NCR. Income stability while credentials build."),
            ],
            "why": "Commercial client experience is not a detour. The best relationship managers in wealth management came from client-facing backgrounds, not textbooks."
        },
        {
            "phase": "Phase 2",
            "title": "Regulatory Build",
            "timeline": "Month 3 - Month 9",
            "status": "UPCOMING",
            "status_color": "#FFB300",
            "border_color": "#FFB300",
            "items": [
                ("NISM Series X-A", "Investment Adviser Level 1 - the legal gateway to practicing as a registered investment adviser under SEBI. Builds directly on V-A knowledge."),
                ("Client Experience", "Building real relationship management experience in my commercial role. This experience clock counts toward CFP requirements."),
            ],
            "why": "NISM X-A and X-B are not optional extras. Without them, you cannot legally advise clients on investments in India regardless of any other qualification."
        },
        {
            "phase": "Phase 3",
            "title": "CFP Exams",
            "timeline": "Month 6 - Month 18",
            "status": "PLANNED",
            "status_color": "#00D4FF",
            "border_color": "#00D4FF",
            "items": [
                ("CFP Certification - Exams", "Four modules through FPSB India covering investment planning, retirement and tax planning, risk and estate planning, and integrated financial planning."),
                ("Experience Accumulating", "CFP requires 1 year of supervised or 3 years of unsupervised relevant experience. This runs in parallel with employment - not before it."),
            ],
            "why": "CFP is the globally recognised standard for financial planning - valid in 27+ countries including Australia, the US, and Canada. It is the credential that defines the profession I am building toward."
        },
        {
            "phase": "Phase 4",
            "title": "Destination",
            "timeline": "Year 2 - Year 3",
            "status": "TARGET",
            "status_color": "#7C3AED",
            "border_color": "#7C3AED",
            "items": [
                ("CFP Certified", "Exams cleared and experience requirement fulfilled. Recognised financial planner with both the regulatory credentials and the client relationship background."),
                ("HNI Wealth Advisory", "Transition into wealth management, private banking, or HNI financial planning. The destination this entire roadmap is built toward."),
            ],
            "why": "India has only ~2,500 CFP professionals against a projected requirement of 1,00,000 by 2030. Early movers in this space have significant scarcity value."
        }
    ]

    for phase in phases:
        st.markdown(f'''
        <div class="card" style="border-left: 4px solid {phase["border_color"]}; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px; flex-wrap: wrap; gap: 10px;">
                <div>
                    <span style="color: #94a3b8; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">{phase["phase"]}</span>
                    <h3 style="color: #FAFAFA; margin: 4px 0 0 0; font-size: 1.2rem;">{phase["title"]}</h3>
                    <p style="color: #94a3b8; margin: 4px 0 0 0; font-size: 0.85rem;">Timeline: {phase["timeline"]}</p>
                </div>
                <span style="background: rgba(0,0,0,0.3); border: 1px solid {phase["status_color"]}; border-radius: 20px; padding: 4px 14px; color: {phase["status_color"]}; font-size: 0.75rem; font-weight: bold; letter-spacing: 1px; white-space: nowrap;">{phase["status"]}</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 15px;">
        ''', unsafe_allow_html=True)

        for item_title, item_desc in phase["items"]:
            st.markdown(f'''
                <div style="background: rgba(255,255,255,0.03); border-radius: 8px; padding: 12px;">
                    <p style="color: {phase["border_color"]}; font-weight: bold; margin: 0 0 6px 0; font-size: 0.9rem;">{item_title}</p>
                    <p style="color: #94a3b8; margin: 0; font-size: 0.82rem; line-height: 1.5;">{item_desc}</p>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown(f'''
            </div>
            <div style="background: rgba(255,255,255,0.03); border-radius: 8px; padding: 12px; border-left: 2px solid rgba(255,255,255,0.1);">
                <span style="color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; font-weight: bold;">Why this phase matters</span>
                <p style="color: #FAFAFA; margin: 6px 0 0 0; font-size: 0.85rem; line-height: 1.6;">{phase["why"]}</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<h2 style="color: #00D4FF; margin: 35px 0 20px 0;">Why commercial experience is not a detour</h2>', unsafe_allow_html=True)

    st.markdown('''
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 30px;">
        <div class="card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">🤝</div>
            <h4 style="color: #00D4FF; margin: 0 0 8px 0;">Client Relationships</h4>
            <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">Advised 25-35 SME clients weekly at Telstra. Wealth advisory is the same skill applied to a different product.</p>
        </div>
        <div class="card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
            <h4 style="color: #00D4FF; margin: 0 0 8px 0;">ROI Thinking</h4>
            <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">Built cost-benefit assessments for client investment decisions at Telstra. HNI advisory is the same framework at a larger scale.</p>
        </div>
        <div class="card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">⚙️</div>
            <h4 style="color: #00D4FF; margin: 0 0 8px 0;">Operational Reality</h4>
            <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">Managed P&L, variance analysis, and supplier coordination at a A$2M business. Finance is not abstract to me.</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div style="padding: 25px; background: rgba(0,212,255,0.05); border-radius: 10px; border: 1px solid rgba(0,212,255,0.2); margin-top: 10px;">
        <h3 style="color: #00D4FF; margin-top: 0;">The destination</h3>
        <p style="color: #FAFAFA; font-size: 1rem; line-height: 1.7; margin: 0;">
            HNI wealth management and financial planning. Advising wealthy families on how to structure, grow, and protect their wealth across investments, retirement, insurance, and estate planning.
            This is not a career pivot I decided on yesterday. It is where everything I have done - the finance degree, the client advisory experience, the commercial operations background - naturally points.
            The roadmap above is how I get there, one credential and one year of experience at a time.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "CONTACT":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Let\'s Connect</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.2rem; color: #999; margin-bottom: 30px;">Open to Pre-Sales, Growth, Customer Success, and Operations roles in Delhi NCR</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''
        <div class="contact-card">
            <h3>🔗 LinkedIn</h3>
            <p>linkedin.com/in/arpitarora25</p>
            <a href="https://www.linkedin.com/in/arpitarora25/" target="_blank"><div class="stat-badge" style="display: inline-block; margin-top: 10px;">Connect</div></a>
        </div>
        ''', unsafe_allow_html=True)
    with col2:
        st.markdown('''
        <div class="contact-card">
            <h3>📧 Email</h3>
            <p>arpitarora.ac@gmail.com</p>
            <div class="stat-badge" style="display: inline-block; margin-top: 10px;">Direct Contact</div>
        </div>
        ''', unsafe_allow_html=True)
    with col3:
        st.markdown('''
        <div class="contact-card">
            <h3>📍 Location</h3>
            <p>Delhi NCR, India</p>
            <div class="stat-badge" style="display: inline-block; margin-top: 10px;">Available</div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)

    # Resume download - graceful fallback if file not present
    RESUME_PATH = "Resume.pdf"
    if os.path.exists(RESUME_PATH):
        with open(RESUME_PATH, "rb") as resume_file:
            resume_bytes = resume_file.read()
        st.download_button(
            "📄 Download Resume",
            data=resume_bytes,
            file_name="Arpit_Arora_Resume.pdf",
            mime="application/pdf",
            key="download_resume"
        )
    else:
        st.markdown('<div class="stat-badge">📄 Resume available on request</div>', unsafe_allow_html=True)

    st.markdown('''
    <div style="margin-top: 40px; padding: 20px; background: rgba(255, 255, 255, 0.05); border-radius: 10px; border-left: 4px solid #00D4FF;">
        <h3 style="color: #00D4FF;">Targeting</h3>
        <p>Pre-Sales Associate | Growth Associate | Customer Success Associate | Operations Analyst | Commercial Analyst</p>
        <p>Industries: B2B SaaS | Fintech | E-Commerce | Technology Startups | Consulting</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
