# python -m streamlit run Car.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Car World!",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)
df = pd.read_csv("cars_2010_2026.csv")

all_brands = sorted(df["Brand"].unique())
all_fuel_types = sorted(df["Fuel_Type"].unique())
all_conditions = sorted(df["Condition"].unique())
all_countries = sorted(df["Country"].unique())

st.title("🚗 Car Data Analysis Dashboard")
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏠 Home", "📊 Data Analysis", "📈 Visualizations", "🏆 Popular Models", "ℹ️ About"]
)
with tab1:

    total_cars = len(df)
    total_brands = df["Brand"].nunique()
    total_fuels = df["Fuel_Type"].nunique()
    total_countries = df["Country"].nunique()
    total_years = df["Year"].nunique()

    st.markdown("""
    <div style="
        padding:20px;
        border-radius:18px;
        background:linear-gradient(135deg,#0f172a,#172554,#312e81);
        color:white;
        text-align:center;
        box-shadow:0 6px 15px rgba(0,0,0,0.3);
        margin-bottom:20px;
    ">
        <h2>🚗 Car Data Analysis Dashboard</h2>
        <p>Explore Cars From 2010 - 2026</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    card_style = """
    padding:6px;
    border-radius:12px;
    background:linear-gradient(135deg,#1e293b,#334155);
    text-align:center;
    color:white;
    border:1px solid #475569;
    box-shadow:0 3px 8px rgba(0,0,0,0.25);
    border:1px solid #4f46e5; 
    height:105px;
    """

    with col1:
        st.markdown(f"""
        <div style="{card_style}">
            <div style="font-size:22px;">🚘</div>
            <div style="font-size:20px;font-weight:bold;">{total_cars:,}</div>
            <div style="font-size:15px;">Total Cars</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="{card_style}">
            <div style="font-size:22px;">🏭</div>
            <div style="font-size:20px;font-weight:bold;">{total_brands}</div>
            <div style="font-size:15px;">Brands</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="{card_style}">
            <div style="font-size:22px;">⛽</div>
            <div style="font-size:20px;font-weight:bold;">{total_fuels}</div>
            <div style="font-size:15px;">Fuel Types</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style="{card_style}">
            <div style="font-size:22px;">🌍</div>
            <div style="font-size:20px;font-weight:bold;">{total_countries}</div>
            <div style="font-size:15px;">Countries</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div style="{card_style}">
            <div style="font-size:22px;">📅</div>
            <div style="font-size:20px;font-weight:bold;">{total_years}</div>
            <div style="font-size:15px;">Years</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📈 Quick Insights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(f"🏆 Most Popular Brand: {df['Brand'].mode()[0]}")

    with c2:
        st.info(f"⛽ Most Common Fuel: {df['Fuel_Type'].mode()[0]}")

    with c3:
        st.info(f"🌍 Top Country: {df['Country'].mode()[0]}")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fuel_count = df["Fuel_Type"].value_counts()

        fig = px.pie(
            values=fuel_count.values,
            names=fuel_count.index,
            title="Fuel Type Distribution",
            hole=0.4
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        brand_count = df["Brand"].value_counts().head(10)

        fig = px.bar(
            x=brand_count.index,
            y=brand_count.values,
            title="Top 10 Most Listed Brands",
            labels={"x": "Brand", "y": "Count"}
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)
    

    st.markdown("---")

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.success("✅ Explore more insights from the tabs above.")
    
with tab2:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Year Range: 2010-2026")
        year = st.selectbox(
            "Year",
            options=list(range(2010, 2027))
        )

    filtered_df = df[df["Year"] == year]

    with col3:
        rec = filtered_df.shape[0]
        st.write(f"You selected: {year} | Total Records : {rec}")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    card_style = """
    <div style="
    padding:6px;
    border-radius:11px;
    background:linear-gradient(135deg,#0f172a,#1e293b);
    border:1px solid #4f46e5;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.3);
    color:white;
    ">
    <h2 style="margin:0;">{value}</h2>
    <p style="margin:0;font-size:20px;color:#cbd5e1;">{label}</p>
    </div>
    """

    with col1:
        st.markdown(
            card_style.format(value=rec, label="🚘 Cars"),
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            card_style.format(
                value=filtered_df["Brand"].nunique(),
                label="🏭 Brands"
            ),
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            card_style.format(
                value=filtered_df["Fuel_Type"].nunique(),
                label="⛽ Fuel Types"
            ),
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            card_style.format(
                value=filtered_df["Country"].nunique(),
                label="🌍 Countries"
            ),
            unsafe_allow_html=True
        )

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Brands")
        st.dataframe(
            filtered_df["Brand"]
            .value_counts()
            .reset_index()
            .rename(columns={"count": "Count"}),
            use_container_width=True
        )

    with col2:
        st.subheader("Fuel Types")
        st.dataframe(
            filtered_df["Fuel_Type"]
            .value_counts()
            .reset_index()
            .rename(columns={"count": "Count"}),
            use_container_width=True
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Body Type Analysis")
        st.dataframe(
            filtered_df["Body_Type"]
            .value_counts()
            .reset_index()
            .rename(columns={"count": "Count"}),
            use_container_width=True
        )

    with col2:
        st.subheader("Transmission Analysis")
        st.dataframe(
            filtered_df["Transmission"]
            .value_counts()
            .reset_index()
            .rename(columns={"count": "Count"}),
            use_container_width=True
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Price Statistics")
        st.dataframe(
            filtered_df["Price_INR"]
            .describe()
            .to_frame(),
            use_container_width=True
        )

    with col2:
        st.subheader("Engine Statistics")
        st.dataframe(
            filtered_df[["Power_BHP", "Torque_Nm"]]
            .describe(),
            use_container_width=True
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Safety Features")

        st.write("ABS Cars :", filtered_df["ABS"].value_counts().get("Yes", 0))
        st.write("Average Airbags :", round(filtered_df["Airbags"].mean(), 2))
        st.write("Average Safety Rating :", round(filtered_df["Safety_Rating"].mean(), 2))
        
    with col2:
        st.subheader("Other Information")

        mileage = pd.to_numeric(filtered_df["Mileage_kmpl"], errors="coerce")
        st.write("Average Mileage :", round(mileage.mean(), 2))
        st.write("Sunroof Cars :", filtered_df["Sunroof"].value_counts().get("Yes", 0))
        st.write("Touchscreen Cars :", filtered_df["Touchscreen"].value_counts().get("Yes", 0))

    st.markdown("---")

    st.subheader("Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True)

with tab3:
    st.subheader("📈 Beautiful Visualizations")

    filtered_df = df

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            filtered_df,
            x="Price_INR",
            nbins=30,
            title="Price Distribution"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.bar(
            filtered_df.groupby("Brand")["Price_INR"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .reset_index(),
            x="Brand",
            y="Price_INR",
            title="Top 10 Expensive Brands"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        fig = px.scatter(
            filtered_df,
            x="Engine_CC",
            y="Power_BHP",
            color="Fuel_Type",
            title="Engine CC vs Power"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.scatter(
            filtered_df,
            x="Power_BHP",
            y="Price_INR",
            color="Transmission",
            title="Power vs Price"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        yearly_price = filtered_df.groupby("Year")["Price_INR"].mean().reset_index()

        fig = px.line(
            yearly_price,
            x="Year",
            y="Price_INR",
            markers=True,
            title="Average Price by Year"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.box(
            filtered_df,
            x="Fuel_Type",
            y="Mileage_kmpl",
            title="Mileage by Fuel Type"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            filtered_df,
            names="Body_Type",
            title="Body Type Distribution",
            hole=0.4
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.bar(
            filtered_df.groupby("Country")["Price_INR"]
            .mean()
            .sort_values(ascending=False)
            .reset_index(),
            x="Country",
            y="Price_INR",
            title="Average Price by Country"
        )

        fig.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    corr_cols = [
        "Engine_CC",
        "Power_BHP",
        "Torque_Nm",
        "Mileage_kmpl",
        "KM_Driven",
        "Price_INR",
        "Safety_Rating",
        "Airbags",
        "Warranty_Years"
    ]

    corr_df = filtered_df[corr_cols].copy()

    for col in corr_cols:
        corr_df[col] = pd.to_numeric(corr_df[col], errors="coerce")

    corr = corr_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    fig.update_layout(template="plotly_dark", height=700)

    st.plotly_chart(fig, use_container_width=True)
with tab4:
   
    st.markdown("""
    <h1>
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg" width="50" style="vertical-align:middle;">
        BMW
    </h1>
    """, unsafe_allow_html=True)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.image("https://i.ytimg.com/vi/ij6ZRywMwQI/maxresdefault.jpg")
    with col2:
        st.image("https://i.ytimg.com/vi/J_CFVAi40Lk/maxresdefault.jpg")
    with col3:
        st.image("https://i.ytimg.com/vi/GIrFBDFZg2o/maxresdefault.jpg")

    st.markdown("---")
    st.markdown("""
    <h1>
        <img src="https://i.pinimg.com/originals/3b/10/42/3b1042d30785fea245a2086f5cff3641.jpg" width="60" style="vertical-align:middle;">
        Mercedes
    </h1>
    """, unsafe_allow_html=True)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.image("https://i.ytimg.com/vi/hGQC3-f1Xus/maxresdefault.jpg")
    with col2:
        st.image("https://i.ytimg.com/vi/tXmkFiN2Kc8/maxresdefault.jpg")
    with col3:
        st.image("https://i.ytimg.com/vi/8F-rjSFXopA/maxresdefault.jpg")
        
    st.markdown("---")
    st.markdown("""
    <h1>
        <img src="https://www.lambocars.com/wp-content/uploads/2024/08/ritle-image.jpg" width="100" style="vertical-align:middle;">
        Lamborghini
    </h1>
    """, unsafe_allow_html=True)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.image("https://i.ytimg.com/vi/sV1JHW8VKYQ/maxresdefault.jpg")
    with col2:
        st.image("https://i.ytimg.com/vi/wB4puo5M-Lo/maxresdefault.jpg")
    with col3:
        st.image("https://i.ytimg.com/vi/_53B2WKJlEU/maxresdefault.jpg")
        
    st.markdown("---")
    st.markdown("""
    <h1>
        <img src="https://pngimg.com/uploads/ferrari/ferrari_PNG10665.png" width="40" style="vertical-align:middle;">
        ferrari
    </h1>
    """, unsafe_allow_html=True)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.image("https://cryptoslate.com/wp-content/uploads/2024/07/ferrari-bitcoin.jpg")
    with col2:
        st.image("https://i.ytimg.com/vi/y7n3t2sZMjo/maxresdefault.jpg")
    with col3:
        st.image("https://i.ytimg.com/vi/pmV0y0j1lB4/maxresdefault.jpg")
        
    st.markdown("---")

    st.markdown("""
    <h1>
        <img src="https://thumbs.dreamstime.com/b/close-logo-logotype-sign-porsche-black-background-prague-czech-republic-september-close-logo-logotype-sign-porsche-126065580.jpg" width="70" style="vertical-align:middle;">
        Porsche
    </h1>
    """, unsafe_allow_html=True)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.image("https://avatars.mds.yandex.net/get-autoru-vos/5231844/990fe5b671bff9d29ab32d327f97eef6/1200x900")
    with col2:
        st.image("https://i.ytimg.com/vi/fFFjxEsjUjo/maxresdefault.jpg")
    with col3:
        st.image("https://www.supercars.net/blog/wp-content/uploads/2024/10/Porsche-911-Carrera-T-2.jpg")
        
    st.markdown("---")
    st.markdown("""
    <h1>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Tesla_logo.png/1280px-Tesla_logo.png" width="60" style="vertical-align:middle;">
        Tesla
    </h1>
    """, unsafe_allow_html=True)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.image("https://i.ytimg.com/vi/dAlkOlz9LjA/maxresdefault.jpg")
    with col2:
        st.image("https://i.pinimg.com/originals/52/be/7b/52be7b0cf23a7f9a87ebfc32d6984597.jpg")
    with col3:
        st.image("https://i.pinimg.com/originals/c8/ed/9c/c8ed9c55b77be5c089fcbdc8dbda4f59.jpg")
        
with tab5:
    st.markdown("""
    <div style="
        padding:25px;
        border-radius:18px;
        background:linear-gradient(135deg,#0f172a,#172554,#312e81);
        color:white;
        text-align:center;
        box-shadow:0 6px 15px rgba(0,0,0,0.3);
        margin-bottom:20px;
    ">
        <h2>🚗 Project Summary</h2>
        <p>Car Data Analysis Dashboard — 2010 to 2026</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("✨ Features")

    feature_card_style = """
    padding:15px;
    border-radius:12px;
    background:linear-gradient(135deg,#1e293b,#334155);
    text-align:center;
    color:white;
    border:1px solid #4f46e5;
    box-shadow:0 3px 8px rgba(0,0,0,0.25);
    height:90px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    """

    features = [
        ("🏠", "Home Dashboard"),
        ("📊", "Data Analysis"),
        ("📈", "Interactive Visualizations"),
        ("🏆", "Popular Car Gallery"),
    ]

    cols = st.columns(4)
    for col, (icon, label) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div style="{feature_card_style}">
                <div style="font-size:24px;">{icon}</div>
                <div style="font-size:15px;font-weight:bold;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🛠️ Technologies Used")

    tech_cols = st.columns(4)
    techs = [
        ("🐍", "Streamlit"),
        ("🐼", "Pandas"),
        ("🔢", "NumPy"),
        ("📊", "Plotly"),
    ]

    for col, (icon, label) in zip(tech_cols, techs):
        with col:
            st.markdown(f"""
            <div style="{feature_card_style}">
                <div style="font-size:24px;">{icon}</div>
                <div style="font-size:15px;font-weight:bold;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.success("Thanks for exploring the Car Data Analysis Dashboard! 🚗")     


st.markdown("""
<hr style="margin-top:50px;">
<div style="text-align:center; padding:10px;">
<a href="https://github.com/Pareshprajapati-777" target="_blank">
    <img src="https://github.com/Pareshprajapati-777.png"
         width="90"
         style="border-radius:50%; border:2px solid #555; margin-bottom:10px;">
</a>
<p style="font-size:18px; margin:0;"><b>Paresh Prajapati</b></p>
<p style="color:gray; margin:5px 0;">AI • ML • Data Science</p>
<p style="font-size:14px; color:#808080;">© 2026 Pandas Questions Solver</p>
</div>""", unsafe_allow_html=True)
    