import streamlit as st
import pandas as pd
import backend

st.set_page_config(page_title="Meal Match", page_icon="🍕",layout="wide")

# 💡 Add Custom CSS 
st.markdown(
    """
    <style>
    /* Remove top deploy menu & footer */
    header, footer {visibility: hidden;}

    /* Tables */
    .dataframe {
        background-color: #222;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Main page (right side)
st.title("🍽️ Meal Match - Find Your Perfect Meal!")

# Sidebar
st.sidebar.header("🔍 Choose Preferences")
email = st.sidebar.text_input("Enter your email")

if email:
    if email not in backend.user_db:
        backend.user_db[email] = {"favorite_cuisines": [], "past_orders": []}
        backend.save_user_data()
    
    if st.sidebar.button("Delete User"):
        backend.delete_user(email)
        st.success("User deleted successfully.")

    # Select Cuisines, City, and Budget
    favorite_cuisines = st.sidebar.multiselect("Select Favorite Cuisines", backend.df["Cuisine"].unique(), 
                                               default=backend.user_db[email]["favorite_cuisines"])
    backend.user_db[email]["favorite_cuisines"] = favorite_cuisines
    backend.save_user_data()
    
    city = st.sidebar.selectbox("Select Your City", backend.df["City"].unique())
    budget = st.sidebar.slider("Select Your Budget (€)", 2, 100, 20)

    # Order History
    with st.sidebar.expander("📜 Your Order History"):
        if backend.user_db[email]["past_orders"]:
            for meal_id in backend.user_db[email]["past_orders"]:
                meal_data = backend.df.loc[int(meal_id)]
                st.write(f"✅ {meal_data['Meal Name']} - {meal_data['Restaurant Name']}")
        else:
            st.write("No past orders yet.")

    # Main UI Layout
    col1, col2 = st.columns([3, 1])

    with col1:
        # Trending Meals
        st.subheader("🔥 Trending Meals")
        trending_meals = backend.get_trending_meals(city)
        st.dataframe(trending_meals)
        selected_trending_meals = st.multiselect("Select from trending meals", 
                                                 [f"{meal_id} - {row['Meal Name']}" for meal_id, row in trending_meals.iterrows()])

        # Budget-Based Meals
        st.subheader("💰 Top Budget Meals")
        budget_meals = backend.get_budget_based_meals(city, budget)
        st.dataframe(budget_meals)
        selected_budget_meals = st.multiselect("Select from budget meals", 
                                               [f"{meal_id} - {row['Meal Name']}" for meal_id, row in budget_meals.iterrows()])

        # Recommended Combo
        st.subheader("🍽️ Recommended Combo")
        selected_meals, total_cost = backend.generate_meal_combo(city, budget, favorite_cuisines)
        recommended_meals_df = pd.DataFrame.from_dict(selected_meals, orient='index').reset_index().rename(columns={'index': 'Meal ID'})
        st.dataframe(recommended_meals_df)
        selected_recommended_meals = st.multiselect("Select from recommended combo", 
                                                    [f"{row['Meal ID']} - {row['Meal Name']}" for _, row in recommended_meals_df.iterrows()])

        # Consolidate All Selected Meals (Using Meal ID)
        all_selected_meals = {}
        selected_meal_ids = selected_trending_meals + selected_budget_meals + selected_recommended_meals

        for meal_entry in selected_meal_ids:
            meal_id, _ = meal_entry.split(" - ", 1)  # Extract ID
            meal_id = int(meal_id)  # Convert to int
            meal_data = backend.df.loc[meal_id]  # Fetch correct row using ID
            all_selected_meals[meal_id] = {
                "Meal Name": meal_data["Meal Name"],
                "Price (€)": meal_data["Meal Price (€)"],
                "Restaurant Name": meal_data["Restaurant Name"],
            }

        # Final Order Summary
        st.subheader("📌 Final Order Summary")
        if all_selected_meals:
            final_order_df = pd.DataFrame.from_dict(all_selected_meals, orient='index').reset_index().rename(columns={'index': 'Meal ID'})
            st.dataframe(final_order_df)
            total_expense = final_order_df["Price (€)"].sum()
            st.markdown(f"### 💵 **Total Expense: €{total_expense}**")

        if st.button("✅ Place Order"):
            backend.save_order(email, list(all_selected_meals.keys()))
            st.success("Order placed successfully! Your preferences are updated.")
