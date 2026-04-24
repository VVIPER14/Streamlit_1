import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="E-Commerce Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# GLOBAL STYLING
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px;
}

#MainMenu, footer, header { visibility: hidden; }

/* HERO */
.hero-wrap {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    border-radius: 20px;
    padding: 2.5rem 2.8rem;
    margin-bottom: 1.8rem;
    position: relative;
    overflow: hidden;
}
.hero-wrap::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(255,120,50,0.25) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-wrap::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 40px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(100,200,255,0.2) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 0.3rem 0;
    line-height: 1.2;
}
.hero-sub {
    font-size: 0.95rem;
    color: rgba(255,255,255,0.65);
    margin: 0;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    margin-bottom: 0.8rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* METRIC CARDS */
.metric-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.8rem;
}
.metric-card {
    flex: 1;
    border-radius: 16px;
    padding: 1.3rem 1.4rem;
    position: relative;
    overflow: hidden;
}
.metric-card.c1 { background: linear-gradient(135deg, #FF6B6B, #FF8E53); }
.metric-card.c2 { background: linear-gradient(135deg, #4ECDC4, #2ECC71); }
.metric-card.c3 { background: linear-gradient(135deg, #667eea, #764ba2); }
.metric-card.c4 { background: linear-gradient(135deg, #f7971e, #FFD200); }
.metric-card .m-icon { font-size: 1.6rem; margin-bottom: 0.5rem; display: block; }
.metric-card .m-label {
    font-size: 0.73rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.08em;
    color: rgba(255,255,255,0.82); margin-bottom: 0.25rem;
}
.metric-card .m-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.9rem; font-weight: 700; color: #ffffff; line-height: 1;
}
.metric-card .m-sub { font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.25rem; }

/* SECTION CARD */
.section-card {
    background: #ffffff;
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.06);
    border: 1px solid #f0f0f0;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem; font-weight: 700; color: #1a1a2e; margin: 0 0 0.2rem 0;
}
.section-q { font-size: 0.82rem; color: #8888a0; margin: 0; font-style: italic; }

/* INSIGHT */
.insight-block {
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-top: 1.2rem;
}
.insight-block.blue { background: linear-gradient(135deg, #e8f4fd, #dbeeff); border-left: 4px solid #3b82f6; }
.insight-block.purple { background: linear-gradient(135deg, #f3e8ff, #ede9fe); border-left: 4px solid #8b5cf6; }
.insight-block.orange { background: linear-gradient(135deg, #fff7ed, #ffedd5); border-left: 4px solid #f97316; }
.insight-block.green { background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-left: 4px solid #22c55e; }
.insight-block h4 {
    font-size: 0.82rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.07em;
    color: #374151; margin: 0 0 0.6rem 0;
}
.insight-block ul { margin: 0; padding-left: 1.2rem; }
.insight-block ul li { font-size: 0.88rem; color: #374151; margin-bottom: 0.35rem; line-height: 1.5; }

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    background: #f4f4f8;
    border-radius: 12px;
    padding: 4px;
    gap: 2px;
    margin-bottom: 1.5rem;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 9px;
    font-weight: 600;
    font-size: 0.88rem;
    padding: 0.55rem 1.2rem;
    color: #666;
}
.stTabs [aria-selected="true"] {
    background: #ffffff !important;
    color: #1a1a2e !important;
    box-shadow: 0 1px 6px rgba(0,0,0,0.1);
}

/* CONCLUSION */
.concl-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.concl-item {
    border-radius: 14px;
    padding: 1.3rem;
    text-align: center;
}
.concl-item.a { background: linear-gradient(135deg, #ffecd2, #fcb69f); }
.concl-item.b { background: linear-gradient(135deg, #a1c4fd, #c2e9fb); }
.concl-item.c { background: linear-gradient(135deg, #d4fc79, #96e6a1); }
.concl-item .ci-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem; font-weight: 700; color: rgba(0,0,0,0.35);
}
.concl-item .ci-title { font-weight: 700; font-size: 0.9rem; color: #1a1a2e; margin: 0.4rem 0 0.5rem 0; }
.concl-item .ci-text { font-size: 0.82rem; color: #374151; line-height: 1.5; }

/* RECO */
.reco-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.reco-card {
    background: #fff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.2rem 1.3rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
}
.reco-icon { font-size: 1.6rem; flex-shrink: 0; margin-top: 0.1rem; }
.reco-title { font-weight: 700; font-size: 0.9rem; color: #1a1a2e; margin-bottom: 0.35rem; }
.reco-text { font-size: 0.82rem; color: #6b7280; line-height: 1.5; margin: 0; }

/* DIVIDER */
.colored-divider {
    height: 3px;
    background: linear-gradient(90deg, #FF6B6B, #FFD200, #4ECDC4, #667eea);
    border-radius: 999px;
    margin: 0.2rem 0 1.5rem 0;
    border: none;
}
</style>
""", unsafe_allow_html=True)


# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    orders = pd.read_csv(os.path.join(base_path, "orders_clean.csv"))
    payments = pd.read_csv(os.path.join(base_path, "orders_payments_clean(Merge).csv"))
    return orders, payments

orders, payments = load_data()
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])


# =========================
# COMPUTE DATA
# =========================
total_orders = orders['order_id'].nunique()
total_customers = orders['customer_id'].nunique()
total_revenue = payments['payment_value'].sum()
avg_order_value = payments.groupby('order_id')['payment_value'].sum().mean()

monthly = (
    orders
    .groupby(orders['order_purchase_timestamp'].dt.to_period("M"))
    .agg(jumlah_transaksi=('order_id', 'count'))
    .reset_index()
)
monthly['order_month'] = monthly['order_purchase_timestamp'].astype(str)

df_rfm = orders.merge(payments[['order_id', 'payment_value']], on='order_id')
reference_date = df_rfm['order_purchase_timestamp'].max()
rfm = df_rfm.groupby('customer_id').agg(
    Recency=('order_purchase_timestamp', lambda x: (reference_date - x.max()).days),
    Frequency=('order_id', 'count'),
    Monetary=('payment_value', 'sum')
).reset_index()
rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1], duplicates='drop')
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4], duplicates='drop')
rfm['M_score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 4, labels=[1, 2, 3, 4], duplicates='drop')
rfm['RFM_score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)

def segment(row):
    if row['RFM_score'] == '444':
        return 'Best Customer'
    elif int(row['R_score']) == 4:
        return 'Recent Customer'
    elif int(row['F_score']) == 4:
        return 'Loyal Customer'
    else:
        return 'Others'

rfm['Segment'] = rfm.apply(segment, axis=1)
seg_count = rfm['Segment'].value_counts().reset_index()
seg_count.columns = ['Segment', 'Jumlah']
rfm_summary = rfm.groupby('Segment').agg(
    Avg_Recency=('Recency', 'mean'),
    Avg_Frequency=('Frequency', 'mean'),
    Avg_Monetary=('Monetary', 'mean'),
    Count=('customer_id', 'count')
).reset_index().round(2)

payment_df = orders.merge(payments, on='order_id')
pay_count = payment_df['payment_type'].value_counts().reset_index()
pay_count.columns = ['payment_type', 'total_transactions']
pay_avg = payment_df.groupby('payment_type')['payment_value'].mean().reset_index()
pay_avg.columns = ['payment_type', 'avg_transaction_value']
payment_summary = pay_count.merge(pay_avg, on='payment_type').round(2)


# =========================
# HERO
# =========================
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">📊 Proyek Analisis Data</div>
    <div class="hero-title">E-Commerce Analytics Dashboard</div>
    <p class="hero-sub">Suroso Aditya Wibowo &nbsp;·&nbsp; CDCC184D6Y1024 &nbsp;·&nbsp; Data transaksi September 2016 – Agustus 2018</p>
</div>
""", unsafe_allow_html=True)

# =========================
# METRICS
# =========================
st.markdown(f"""
<div class="metric-row">
    <div class="metric-card c1">
        <span class="m-icon">📦</span>
        <div class="m-label">Total Transaksi</div>
        <div class="m-value">{total_orders:,}</div>
        <div class="m-sub">order unik tercatat</div>
    </div>
    <div class="metric-card c2">
        <span class="m-icon">👥</span>
        <div class="m-label">Total Pelanggan</div>
        <div class="m-value">{total_customers:,}</div>
        <div class="m-sub">customer unik</div>
    </div>
    <div class="metric-card c3">
        <span class="m-icon">💰</span>
        <div class="m-label">Total Revenue</div>
        <div class="m-value">R$ {total_revenue/1e6:.1f}M</div>
        <div class="m-sub">dari seluruh transaksi</div>
    </div>
    <div class="metric-card c4">
        <span class="m-icon">🧾</span>
        <div class="m-label">Rata-rata Nilai Order</div>
        <div class="m-value">R$ {avg_order_value:.0f}</div>
        <div class="m-sub">per transaksi</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)


# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📈  Tren Transaksi",
    "👥  Segmentasi RFM",
    "💳  Metode Pembayaran",
    "📋  Kesimpulan"
])

# ------- TAB 1 -------
with tab1:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Tren Jumlah Transaksi Bulanan</div>
        <div class="section-q">Bagaimana tren jumlah transaksi bulanan pada platform e-commerce selama periode September 2016 hingga Februari 2017?</div>
    </div>
    """, unsafe_allow_html=True)

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=monthly['order_month'],
        y=monthly['jumlah_transaksi'],
        mode='lines+markers',
        line=dict(color='#667eea', width=3, shape='spline', smoothing=0.6),
        marker=dict(size=8, color='#764ba2', line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor='rgba(102,126,234,0.12)',
        hovertemplate='<b>%{x}</b><br>Transaksi: <b>%{y:,}</b><extra></extra>'
    ))
    fig1.update_layout(
        height=370, margin=dict(l=10, r=10, t=15, b=10),
        plot_bgcolor='white', paper_bgcolor='white',
        xaxis=dict(showgrid=False, tickangle=-45, tickfont=dict(size=11),
                   title=dict(text='Bulan', font=dict(size=12, color='#6b7280')), linecolor='#e5e7eb'),
        yaxis=dict(showgrid=True, gridcolor='#f3f4f6', tickfont=dict(size=11),
                   title=dict(text='Jumlah Transaksi', font=dict(size=12, color='#6b7280'))),
        hovermode='x unified'
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("""
    <div class="insight-block blue">
        <h4>💡 Insight Pertanyaan 1</h4>
        <ul>
            <li>Jumlah transaksi bulanan menunjukkan <strong>tren peningkatan yang konsisten</strong> sepanjang periode September 2016 hingga Agustus 2018.</li>
            <li>Pada September–Desember 2016, transaksi masih sangat rendah (1–270/bulan), mencerminkan platform yang baru berkembang dan belum memiliki basis pengguna besar.</li>
            <li>Terjadi lonjakan signifikan mulai <strong>Januari 2017 (748 transaksi)</strong> dan terus meningkat drastis hingga <strong>November 2017 mencapai puncak 7.288 transaksi</strong>.</li>
            <li>Meski sempat turun di Desember 2017, tren kembali stabil di kisaran <strong>6.000–7.000 transaksi per bulan</strong> sepanjang 2018.</li>
            <li>Pertumbuhan ini mengindikasikan perkembangan platform yang sehat dan peningkatan kepercayaan serta aktivitas pengguna secara berkelanjutan.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 Lihat Data Bulanan"):
        st.dataframe(monthly[['order_month', 'jumlah_transaksi']].rename(
            columns={'order_month': 'Bulan', 'jumlah_transaksi': 'Jumlah Transaksi'}
        ), use_container_width=True, hide_index=True)

# ------- TAB 2 -------
with tab2:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Segmentasi Pelanggan Berdasarkan RFM</div>
        <div class="section-q">Bagaimana segmentasi pelanggan berdasarkan nilai Recency, Frequency, dan Monetary (RFM) untuk mengidentifikasi pelanggan bernilai tinggi?</div>
    </div>
    """, unsafe_allow_html=True)

    seg_colors = {
        'Best Customer': '#f59e0b',
        'Loyal Customer': '#34d399',
        'Recent Customer': '#60a5fa',
        'Others': '#a78bfa'
    }
    order_seg = ['Best Customer', 'Loyal Customer', 'Recent Customer', 'Others']
    seg_plot = seg_count[seg_count['Segment'].isin(order_seg)].copy()
    seg_plot['Segment'] = pd.Categorical(seg_plot['Segment'], categories=order_seg, ordered=True)
    seg_plot = seg_plot.sort_values('Segment')

    col_l, col_r = st.columns([3, 2])
    with col_l:
        fig2a = go.Figure(go.Bar(
            x=seg_plot['Segment'],
            y=seg_plot['Jumlah'],
            marker_color=[seg_colors[s] for s in seg_plot['Segment']],
            text=seg_plot['Jumlah'].apply(lambda x: f'{x:,}'),
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Jumlah: <b>%{y:,}</b> pelanggan<extra></extra>'
        ))
        fig2a.update_layout(
            title=dict(text='Distribusi Segmen Pelanggan', font=dict(size=13, color='#1a1a2e')),
            height=340, margin=dict(l=5, r=5, t=40, b=10),
            plot_bgcolor='white', paper_bgcolor='white',
            xaxis=dict(showgrid=False, linecolor='#e5e7eb'),
            yaxis=dict(showgrid=True, gridcolor='#f3f4f6'), showlegend=False
        )
        st.plotly_chart(fig2a, use_container_width=True)

    with col_r:
        fig2b = go.Figure(go.Pie(
            labels=seg_count['Segment'],
            values=seg_count['Jumlah'],
            hole=0.5,
            marker_colors=[seg_colors.get(s, '#ccc') for s in seg_count['Segment']],
            textinfo='percent',
            hovertemplate='<b>%{label}</b><br>%{value:,} pelanggan (%{percent})<extra></extra>'
        ))
        fig2b.update_layout(
            title=dict(text='Proporsi Segmen', font=dict(size=13, color='#1a1a2e')),
            height=340, margin=dict(l=5, r=5, t=40, b=10),
            paper_bgcolor='white',
            legend=dict(font=dict(size=11), orientation='v', x=0, y=0.5)
        )
        st.plotly_chart(fig2b, use_container_width=True)

    st.markdown("#### 📊 Rata-rata Nilai RFM per Segmen")
    st.dataframe(rfm_summary.rename(columns={
        'Segment': 'Segmen', 'Avg_Recency': 'Avg Recency (hari)',
        'Avg_Frequency': 'Avg Frequency', 'Avg_Monetary': 'Avg Monetary (R$)', 'Count': 'Jumlah Pelanggan'
    }), use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="insight-block purple">
        <h4>💡 Insight Pertanyaan 2</h4>
        <ul>
            <li><strong>Others (54.081 pelanggan / 56%)</strong>: Segmen terbesar. Mayoritas pelanggan belum menunjukkan loyalitas maupun frekuensi transaksi yang tinggi, dengan rata-rata Monetary hanya R$ 158,31.</li>
            <li><strong>Recent Customer (22.623 pelanggan / 23%)</strong>: Pelanggan yang baru bertransaksi dalam waktu dekat (rata-rata Recency 57 hari). Berpotensi besar dikonversi menjadi pelanggan loyal melalui strategi re-engagement yang tepat.</li>
            <li><strong>Loyal Customer (18.215 pelanggan / 19%)</strong>: Pelanggan dengan frekuensi transaksi tinggi, namun Recency-nya sudah cukup lama (301 hari). Perlu program reaktivasi untuk membawa mereka kembali aktif.</li>
            <li><strong>Best Customer (1.541 pelanggan / 1,6%)</strong>: Segmen paling bernilai (RFM = 444) dengan rata-rata Monetary tertinggi <strong>R$ 405,64</strong> dan Recency terpendek (58 hari). Kontribusinya terhadap revenue sangat signifikan.</li>
            <li>Bisnis memiliki peluang besar untuk meningkatkan jumlah Best Customer melalui program loyalitas, upselling, dan personalisasi layanan bagi segmen Others dan Recent Customer.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 Lihat Data RFM Lengkap"):
        st.dataframe(rfm[['customer_id', 'Recency', 'Frequency', 'Monetary', 'RFM_score', 'Segment']],
                     use_container_width=True, hide_index=True)

# ------- TAB 3 -------
with tab3:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Analisis Metode Pembayaran</div>
        <div class="section-q">Metode pembayaran apa yang paling sering digunakan dan bagaimana rata-rata nilai transaksi untuk setiap metode pembayaran?</div>
    </div>
    """, unsafe_allow_html=True)

    pay_colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#6C63FF']
    col_l, col_r = st.columns(2)

    with col_l:
        fig3a = go.Figure(go.Bar(
            x=payment_summary['payment_type'],
            y=payment_summary['total_transactions'],
            marker_color=pay_colors,
            text=payment_summary['total_transactions'].apply(lambda x: f'{x:,}'),
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Transaksi: <b>%{y:,}</b><extra></extra>'
        ))
        fig3a.update_layout(
            title=dict(text='Jumlah Transaksi per Metode Pembayaran', font=dict(size=13, color='#1a1a2e')),
            height=360, margin=dict(l=5, r=5, t=45, b=10),
            plot_bgcolor='white', paper_bgcolor='white',
            xaxis=dict(showgrid=False, linecolor='#e5e7eb'),
            yaxis=dict(showgrid=True, gridcolor='#f3f4f6',
                       title=dict(text='Jumlah Transaksi', font=dict(size=11, color='#6b7280'))),
            showlegend=False
        )
        st.plotly_chart(fig3a, use_container_width=True)

    with col_r:
        fig3b = go.Figure(go.Bar(
            x=payment_summary['payment_type'],
            y=payment_summary['avg_transaction_value'],
            marker_color=pay_colors,
            text=payment_summary['avg_transaction_value'].apply(lambda x: f'R$ {x:.2f}'),
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Rata-rata: <b>R$ %{y:.2f}</b><extra></extra>'
        ))
        fig3b.update_layout(
            title=dict(text='Rata-rata Nilai Transaksi per Metode Pembayaran', font=dict(size=13, color='#1a1a2e')),
            height=360, margin=dict(l=5, r=5, t=45, b=10),
            plot_bgcolor='white', paper_bgcolor='white',
            xaxis=dict(showgrid=False, linecolor='#e5e7eb'),
            yaxis=dict(showgrid=True, gridcolor='#f3f4f6',
                       title=dict(text='Rata-rata Nilai (R$)', font=dict(size=11, color='#6b7280'))),
            showlegend=False
        )
        st.plotly_chart(fig3b, use_container_width=True)

    st.markdown("""
    <div class="insight-block orange">
        <h4>💡 Insight Pertanyaan 3</h4>
        <ul>
            <li><strong>Credit Card (74.584 transaksi)</strong>: Metode pembayaran paling dominan, jauh melampaui metode lain. Rata-rata nilai transaksinya juga tertinggi yaitu <strong>R$ 162,24</strong>, menunjukkan kartu kredit digunakan untuk pembelian bernilai besar.</li>
            <li><strong>Boleto (19.177 transaksi)</strong>: Posisi kedua dengan rata-rata nilai transaksi R$ 144,34. Metode pembayaran alternatif yang cukup populer namun jauh di bawah credit card.</li>
            <li><strong>Voucher (5.493 transaksi)</strong>: Rata-rata nilai transaksi paling rendah (<strong>R$ 62,45</strong>), mengindikasikan voucher umumnya digunakan untuk transaksi bernilai kecil atau dalam konteks promo dan diskon.</li>
            <li><strong>Debit Card (1.485 transaksi)</strong>: Paling sedikit digunakan, namun rata-rata nilai transaksinya cukup tinggi di R$ 140,11, hampir setara dengan boleto.</li>
            <li>Dominasi credit card menunjukkan pentingnya mengoptimalkan pengalaman pembayaran via kartu kredit, serta peluang untuk mendorong penggunaan metode lain melalui insentif yang tepat.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 Lihat Data Pembayaran"):
        st.dataframe(payment_summary.rename(columns={
            'payment_type': 'Metode Pembayaran',
            'total_transactions': 'Total Transaksi',
            'avg_transaction_value': 'Rata-rata Nilai (R$)'
        }), use_container_width=True, hide_index=True)

# ------- TAB 4 -------
with tab4:
    st.markdown("### 🔍 Kesimpulan")
    st.markdown("""
    <div class="concl-grid">
        <div class="concl-item a">
            <div class="ci-num">01</div>
            <div class="ci-title">Tren Transaksi Positif</div>
            <div class="ci-text">Dari 1 order (Sep 2016) tumbuh hingga puncak 7.288 order di November 2017, kemudian stabil 6.000–7.000/bulan sepanjang 2018. Pertumbuhan konsisten mencerminkan platform yang berkembang sehat.</div>
        </div>
        <div class="concl-item b">
            <div class="ci-num">02</div>
            <div class="ci-title">Mayoritas Belum Loyal</div>
            <div class="ci-text">56% pelanggan masuk segmen Others. Best Customer hanya 1,6% namun memiliki Monetary rata-rata R$ 405 — tertinggi dari semua segmen. Potensi besar ada di 23% Recent Customer untuk dijadikan loyal.</div>
        </div>
        <div class="concl-item c">
            <div class="ci-num">03</div>
            <div class="ci-title">Credit Card Mendominasi</div>
            <div class="ci-text">Credit card menguasai 74.584 transaksi (73,5%) dengan rata-rata nilai R$ 162,24 tertinggi. Voucher paling rendah di R$ 62,45. Credit card adalah pilar utama pendapatan platform.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💡 Rekomendasi")
    st.markdown("""
    <div class="reco-grid">
        <div class="reco-card">
            <div class="reco-icon">🎯</div>
            <div>
                <div class="reco-title">Program Retensi & Loyalitas</div>
                <p class="reco-text">Kembangkan program loyalty untuk mengkonversi 22.623 Recent Customer menjadi Loyal Customer, misalnya melalui poin reward, notifikasi personalisasi, dan promo eksklusif setelah transaksi pertama.</p>
            </div>
        </div>
        <div class="reco-card">
            <div class="reco-icon">👑</div>
            <div>
                <div class="reco-title">Pertahankan Best Customer</div>
                <p class="reco-text">Berikan program eksklusif seperti early access produk baru, layanan prioritas, atau cashback premium untuk mempertahankan 1.541 Best Customer dengan Monetary rata-rata R$ 405,64.</p>
            </div>
        </div>
        <div class="reco-card">
            <div class="reco-icon">💳</div>
            <div>
                <div class="reco-title">Optimasi Credit Card</div>
                <p class="reco-text">Perkuat kerja sama dengan penyedia kartu kredit, tawarkan cicilan 0% atau cashback untuk transaksi di atas nominal tertentu guna meningkatkan rata-rata nilai transaksi yang sudah tinggi di R$ 162,24.</p>
            </div>
        </div>
        <div class="reco-card">
            <div class="reco-icon">🔄</div>
            <div>
                <div class="reco-title">Diversifikasi Metode Bayar</div>
                <p class="reco-text">Dorong penggunaan debit card dan boleto melalui promo khusus agar ketergantungan tidak hanya pada credit card, sekaligus membuka akses bagi pelanggan yang tidak memiliki kartu kredit.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-block green" style="margin-top:1.2rem;">
        <h4>📌 Catatan Analisis</h4>
        <ul>
            <li>Dataset mencakup periode <strong>September 2016 – Agustus 2018</strong> dengan total <strong>96.461 transaksi</strong> dan revenue <strong>R$ 15,4 juta</strong>.</li>
            <li>Outlier pada kolom payment_value dan price tidak dihapus karena mencerminkan variasi transaksi yang valid dalam konteks e-commerce.</li>
            <li>Segmentasi RFM menggunakan metode <strong>quartile scoring (1–4)</strong> dengan reference date pada tanggal transaksi terakhir dalam dataset.</li>
            <li>Dashboard ini berjalan secara lokal menggunakan Streamlit dan data dari file CSV yang telah dibersihkan pada tahap Data Wrangling.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)