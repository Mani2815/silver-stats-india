import streamlit as st
import pandas as pd
import altair as alt
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Silver Price Calculator & Silver Sales Analysis", layout="wide")

price_df = pd.read_csv("historical_silver_price.csv")
sales_df = pd.read_csv("state_wise_silver_purchased_kg.csv")

price_df.columns = price_df.columns.str.strip()
sales_df.columns = sales_df.columns.str.strip()

price_df["Date"] = pd.to_datetime(
    price_df["Year"].astype(str) + "-" + price_df["Month"] + "-01",
    errors="coerce"
)

tab1, tab2 = st.tabs(["Silver Price Calculator", "Silver Sales Dashboard"])

with tab1:
    st.subheader("Silver Price Calculator")

    c1, c2 = st.columns(2)

    with c1:
        weight = st.number_input("Enter Silver Weight", min_value=0.0)
        unit = st.selectbox("Weight Unit", ["Grams", "Kilograms"])
        price_per_gram = st.number_input("Current Price per Gram (INR)", min_value=0.0)

    with c2:
        currency = st.selectbox("Currency", ["INR", "USD"])

    weight_grams = weight * 1000 if unit == "Kilograms" else weight
    total_cost = weight_grams * price_per_gram

    if currency == "USD":
        st.success(f"Total Cost: ${total_cost / 83:.2f}")
    else:
        st.success(f"Total Cost: ₹{total_cost:.2f}")

    price_filter = st.selectbox(
        "Filter Price Range (INR per kg)",
        ["All", "≤ 20000", "20000 - 30000", "≥ 30000"]
    )

    if price_filter == "≤ 20000":
        filtered_price = price_df[price_df["Silver_Price_INR_per_kg"] <= 20000]
    elif price_filter == "20000 - 30000":
        filtered_price = price_df[
            (price_df["Silver_Price_INR_per_kg"] > 20000) &
            (price_df["Silver_Price_INR_per_kg"] < 30000)
        ]
    elif price_filter == "≥ 30000":
        filtered_price = price_df[price_df["Silver_Price_INR_per_kg"] >= 30000]
    else:
        filtered_price = price_df

    price_chart = (
        alt.Chart(filtered_price)
        .mark_line(point=True)
        .encode(
            x="Date:T",
            y="Silver_Price_INR_per_kg:Q",
            tooltip=["Date", "Silver_Price_INR_per_kg"]
        )
        .interactive()
        .properties(height=350)
    )

    st.altair_chart(price_chart, use_container_width=True)

with tab2:
    st.subheader("Silver Sales Dashboard")

    india_map = gpd.read_file("india_state_geo.json")
    india_map.columns = india_map.columns.str.strip()

    state_col = None
    for col in india_map.columns:
        if col.lower() in ["st_nm", "state", "name_1", "name"]:
            state_col = col
            break

    if state_col is None:
        st.error("No state name column found in GeoJSON")
        st.stop()

    india_map[state_col] = india_map[state_col].str.strip()
    sales_df["State"] = sales_df["State"].str.strip()

    sales_df["State"] = sales_df["State"].replace({
        "Delhi": "NCT of Delhi",
        "Jammu & Kashmir": "Jammu and Kashmir"
    })

    merged_df = india_map.merge(
        sales_df,
        left_on=state_col,
        right_on="State",
        how="left"
    )

    fig, ax = plt.subplots(figsize=(10, 12))
    merged_df.plot(
        column="Silver_Purchased_kg",
        cmap="Greys",
        linewidth=0.8,
        edgecolor="black",
        legend=True,
        ax=ax
    )
    ax.set_title("State-wise Silver Purchases in India")
    ax.axis("off")
    st.pyplot(fig)

    top_states = sales_df.sort_values(
        by="Silver_Purchased_kg",
        ascending=False
    ).head(5)

    top_chart = (
        alt.Chart(top_states)
        .mark_bar()
        .encode(
            x="State:N",
            y="Silver_Purchased_kg:Q",
            color="State:N",
            tooltip=["State", "Silver_Purchased_kg"]
        )
        .properties(height=350)
    )

    st.altair_chart(top_chart, use_container_width=True)

    st.dataframe(sales_df, use_container_width=True)
