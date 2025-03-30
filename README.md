# Meal Match - Find Your Perfect Meal 🍽️

Meal Match is a Streamlit-based web application designed to help users find and order meals based on their preferences in Germany. The app suggests trending meals, budget-friendly options, and curated meal combos that fit the user's taste and budget.

## Screenshot of the Application
<p align="center">
  <img src="https://github.com/akhilpsin/smart-meal-recomendation-streamlit/blob/main/assets/Screenshot_1.png" width="45%" />
  <img src="https://github.com/akhilpsin/smart-meal-recomendation-streamlit/blob/main/assets/Screenshot_2.png" width="45%" />
</p>

## Features

- **User Preferences**: Users can enter their userID and set their favorite cuisines, city, and budget preferences.
- **Trending Meals**: Display top-rated meals in a selected city.
- **Budget-Based Meals**: Suggest meals within a selected budget.
- **Recommended Combo**: Generate meal combos based on the user’s preferences and budget.
- **Order History**: Track past orders and easily reorder.
- **Order System**: Users can select meals, view the total cost, and place an order.

## Requirements

- Python 3.8+
- Streamlit
- Pandas

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

## How to Run the Application

1. Clone the repository:

   ```bash
   git clone "https://github.com/akhilpsin/smart-meal-recomendation-streamlit.git"
   cd meal-match
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser (typically at `http://localhost:8501`).

## Data

The application uses a sample dataset (`germany_restaurant_data_3000.csv`) that contains information about restaurants, meals, prices, and ratings across various cities in Germany. This dataset can be generated using the `Generate_SampleRestaurantData.py` script.

To generate the sample dataset, run:

```bash
python Generate_SampleRestaurantData.py
```

This will create the `germany_restaurant_data_3000.csv` file in the `data` directory.

## File Structure

- `app.py`: The main Streamlit application script.
- `backend.py`: Contains functions for managing user data and interacting with the meal dataset.
- `Generate_SampleRestaurantData.py`: Script to generate the sample restaurant data.
- `requirements.txt`: Lists the required Python packages.

## Contributing

Feel free to fork this repository, create an issue, or submit a pull request with improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
