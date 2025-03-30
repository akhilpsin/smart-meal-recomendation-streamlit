import pandas as pd
import random

# Function to generate 1000 unique random restaurant names
def generate_restaurant_names():
    """
    Generates a list of 1000 unique restaurant names by combining random adjectives and nouns.
    """
    adjectives = [
        "Tasty", "Delicious", "Savory", "Yummy", "Gourmet", "Heavenly", "Exquisite", "Authentic",
        "Flavorful", "Juicy", "Spicy", "Zesty", "Sizzling", "Crispy", "Succulent", "Fusion", "Divine",
        "Smoky", "Fresh", "Golden", "Rustic", "Cozy", "Exotic", "Elegant", "Royal", "Grand", "Vibrant"
    ]
    nouns = [
        "Bites", "Kitchen", "Diner", "Grill", "House", "Corner", "Heaven", "Oasis", "Palace",
        "Cafe", "Bistro", "Tavern", "Eats", "Table", "Delights", "Cuisine", "Feast", "Flavors",
        "Barbecue", "Burger Spot", "Pizza House", "Resto", "Gastronomy", "Food Spot", "Grove",
        "Cellar", "Den", "Retreat", "Nest", "Hub"
    ]

    # Generate unique restaurant names
    restaurant_names = list(set(f"{random.choice(adjectives)} {random.choice(nouns)}" for _ in range(1000)))

    # Ensure exactly 1000 unique names
    while len(restaurant_names) < 1000:
        restaurant_names.append(f"{random.choice(adjectives)} {random.choice(nouns)}")

    random.shuffle(restaurant_names)  # Shuffle the names for randomness
    return restaurant_names

# Define constants for cities, cuisines, and meals
CITIES = [
    'Berlin', 'Munich', 'Düsseldorf', 'Hamburg', 'Bonn', 'Bochum', 'Heidelberg', 'Bielefeld', 'Braunschweig', 
    'Leipzig', 'Stuttgart', 'Bergisch Gladbach', 'Bremerhaven', 'Bottrop', 'Dortmund', 'Gelsenkirchen', 
    'Nuremberg', 'Chemnitz', 'Mannheim', 'Aachen', 'Dresden', 'Frankfurt am Main', 'Cologne', 'Hanover', 
    'Duisburg', 'Lübeck', 'Magdeburg', 'Augsburg', 'Wuppertal', 'Mainz', 'Regensburg', 'Essen', 'Potsdam', 
    'Göttingen', 'Erlangen', 'Wolfsburg', 'Salzgitter', 'Koblenz', 'Herne', 'Leverkusen', 'Oberhausen', 
    'Halle (Saale)', 'Heilbronn', 'Offenbach', 'Pforzheim', 'Mülheim', 'Reutlingen', 'Siegen', 'Kassel', 
    'Münster', 'Trier'
]

CUISINES = [
    "German", "Italian", "Turkish", "Japanese", "Chinese", "Indian", "Mexican", "French", "Thai", "Mediterranean"
]

MEAL_NAMES = {
    "German": [
        "Bratwurst", "Schnitzel", "Currywurst", "Pretzel & Beer", "Kartoffelsalat", 
        "Rinderroulade", "Leberkäse", "Käsespätzle", "Maultaschen", "Weißwurst", 
        "Eisbein mit Sauerkraut", "Spätzle", "Haxe (Pork Knuckle)", "Labskaus", 
        "Zwiebelkuchen", "Brezel mit Obatzda", "Matjes Brötchen"
    ],
    "Italian": [
        "Pasta Carbonara", "Margherita Pizza", "Lasagna", "Risotto", "Tiramisu", 
        "Penne Arrabbiata", "Fettuccine Alfredo", "Minestrone Soup", "Bruschetta", "Gnocchi",
        "Caprese Salad", "Calzone", "Ossobuco", "Parmigiana", "Bolognese Pasta", 
        "Tagliatelle al Tartufo", "Arancini"
    ],
    "Turkish": [
        "Döner Kebab", "Lahmacun Wrap", "Pide", "Köfte", "Baklava", 
        "Adana Kebab", "Iskender Kebab", "Manti", "Simit", "Meze Platter",
        "Menemen", "Etli Ekmek", "Cacik", "Hamsili Pilav", "Şiş Kebab", 
        "Karniyarik", "Kumpir"
    ],
    "Japanese": [
        "Sushi Combo", "Ramen Bowl", "Teriyaki Chicken", "Tempura", "Udon Noodles", 
        "Okonomiyaki", "Takoyaki", "Tonkatsu", "Onigiri", "Soba Noodles",
        "Miso Soup", "Yakitori", "Gyoza", "Unagi Don", "Chirashi Sushi", 
        "Natto with Rice", "Shabu Shabu"
    ],
    "Chinese": [
        "Sweet & Sour Chicken", "Kung Pao Chicken", "Dim Sum", "Fried Rice", "Spring Rolls", 
        "Hot and Sour Soup", "Mapo Tofu", "Peking Duck", "Chow Mein", "Char Siu Pork",
        "Sesame Chicken", "Wonton Soup", "Sichuan Hot Pot", "Steamed Fish with Ginger", "Bok Choy Stir Fry", 
        "Lotus Root Salad", "Century Egg Congee"
    ],
    "Indian": [
        "Chicken Tikka Masala", "Butter Chicken", "Paneer Butter Masala", "Biryani", "Samosa", 
        "Rogan Josh", "Palak Paneer", "Chole Bhature", "Dosa", "Idli Sambar",
        "Pav Bhaji", "Dal Makhani", "Aloo Paratha", "Pani Puri", "Gulab Jamun", 
        "Tandoori Chicken", "Ras Malai"
    ],
    "Mexican": [
        "Tacos", "Burrito", "Quesadilla", "Nachos", "Churros", 
        "Tamales", "Enchiladas", "Fajitas", "Pozole", "Ceviche",
        "Tostadas", "Elote", "Sopes", "Chiles Rellenos", "Guacamole & Chips", 
        "Mole Poblano", "Horchata"
    ],
    "French": [
        "Croissant", "Ratatouille", "Beef Bourguignon", "French Onion Soup", "Crème Brûlée", 
        "Coq au Vin", "Escargots", "Quiche Lorraine", "Soufflé", "Duck Confit",
        "Baguette with Cheese", "Tarte Tatin", "Bouillabaisse", "Moules Marinières", "Cassoulet", 
        "Profiteroles", "Macarons"
    ],
    "Thai": [
        "Pad Thai", "Green Curry", "Tom Yum Soup", "Mango Sticky Rice", "Thai Fried Rice", 
        "Massaman Curry", "Som Tum (Papaya Salad)", "Khao Pad Sapparod (Pineapple Fried Rice)", "Satay Skewers", "Larb Gai",
        "Tom Kha Gai", "Panang Curry", "Pad Kra Pao", "Khao Soi", "Pla Rad Prik (Fried Fish with Chili Sauce)", 
        "Tod Mun Pla (Fish Cakes)", "Kanom Krok (Coconut Pancakes)"
    ],
    "Mediterranean": [
        "Falafel", "Hummus & Pita", "Greek Salad", "Moussaka", "Shawarma", 
        "Baba Ganoush", "Tzatziki", "Dolma", "Spanakopita", "Tabbouleh",
        "Paella", "Briam", "Manakeesh", "Grilled Halloumi", "Kibbeh", 
        "Saganaki", "Shakshuka"
    ]
}

def generate_sample_data(num_samples=3000):
    """
    Generates a sample dataset of restaurants, meals, and ratings.
    """
    restaurant_names = generate_restaurant_names()
    data = []

    for _ in range(num_samples):
        city = random.choice(CITIES)
        cuisine = random.choice(CUISINES)
        restaurant = f"{random.choice(restaurant_names)} {city}"
        meal = random.choice(MEAL_NAMES[cuisine])
        price = round(random.uniform(1.0, 80.0), 2)  # Random price between 8 and 25 EUR
        restaurant_rating = round(random.uniform(1.0, 5.0), 1)  # Restaurant rating between 4.0 and 5.0
        meal_rating = round(random.uniform(1.0, 5.0), 1)  # Meal rating between 4.0 and 5.0

        data.append([restaurant, city, cuisine, meal, price, restaurant_rating, meal_rating])

    return pd.DataFrame(data, columns=[
        "Restaurant Name", "City", "Cuisine", "Meal Name", "Meal Price (€)", "Restaurant Rating", "Meal Rating"
    ])

def save_dataset_to_csv(df, filename="data\germany_restaurant_data_3000.csv"):
    """
    Saves the given DataFrame to a CSV file.
    """
    df.to_csv(filename)
    print(f"Dataset generated and saved as '{filename}'")

# Main execution
if __name__ == "__main__":
    df = generate_sample_data()
    save_dataset_to_csv(df)