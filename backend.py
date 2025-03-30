import pandas as pd
import json
import os

# Load dataset
DATA_FILE = "data/germany_restaurant_data_3000.csv"
df = pd.read_csv(DATA_FILE, index_col=0)  # Use the first column as index

# User Data File
USER_DATA_FILE = "data/user_preferences.json"

# Load or initialize user database
if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "r") as f:
        user_db = json.load(f)
else:
    user_db = {}

def save_user_data():
    """Save user data to JSON."""
    with open(USER_DATA_FILE, "w") as f:
        json.dump(user_db, f, indent=4)

def get_trending_meals(city):
    """Get top trending meals in the selected city."""
    city_meals = df[df["City"].str.lower() == city.lower()]
    return city_meals.sort_values(by="Meal Rating", ascending=False).head(7)

def get_budget_based_meals(city, budget):
    """Get top 10 budget meals within user’s budget."""
    city_meals = df[df["City"].str.lower() == city.lower()]
    return city_meals[city_meals["Meal Price (€)"] <= budget].sort_values(by=["Restaurant Rating", "Meal Rating"], ascending=False).head(10)

def generate_meal_combo(city, budget, favorite_cuisines):
    """Generate a meal combo based on budget and cuisine preferences."""
    city_meals = df[df["City"].str.lower() == city.lower()]
    preferred_meals = city_meals[city_meals["Cuisine"].isin(favorite_cuisines)]
    sorted_meals = preferred_meals.sort_values(by=["Restaurant Rating", "Meal Rating"], ascending=False)

    selected_meals = {}
    total_cost = 0

    for meal_id, meal in sorted_meals.iterrows():
        if total_cost + meal["Meal Price (€)"] <= budget:
            selected_meals[str(meal_id)] = {
                "Meal Name": meal["Meal Name"],
                "Price (€)": meal["Meal Price (€)"],
                "Restaurant Name": meal["Restaurant Name"],
            }
            total_cost += meal["Meal Price (€)"]

    return selected_meals, total_cost

def save_order(email, meal_ids):
    """Save user order history using meal IDs."""
    if email in user_db:
        user_db[email]["past_orders"].extend(meal_ids)
    else:
        user_db[email] = {"favorite_cuisines": [], "past_orders": meal_ids}
    save_user_data()

def delete_user(email):
    """Delete a user and their preferences."""
    if email in user_db:
        del user_db[email]
        save_user_data()
