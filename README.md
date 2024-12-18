
# RecipeApp

RecipeApp is a Django-based API project designed for Strathmore University students to learn how to work with APIs and Python. The app provides endpoints to fetch recipes based on user queries such as ingredients, meal types, or specific recipe names.

---

## Features

- **Django API:** A fully functional Django REST API to handle recipe searches and display recipe details.
- **Search Functionality:** Users can search for recipes by ingredients or meal types.
- **Recipe Details:** API endpoints provide recipe names, ingredients, and preparation instructions.
- **Simple and Interactive API:** Easy-to-use endpoints that return recipes in a JSON format.

---

## Prerequisites

Before running the app, ensure you have the following installed:

- **Python 3.8+** on your system.
- **Pip** to install dependencies.
- **Django 4.x** (or compatible version) to run the API.

---

## Installation

Follow these steps to set up RecipeApp locally:

1. **Clone the Repository:**

   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/RecipeApp.git
   cd RecipeApp
   ```

2. **Create a Virtual Environment (Recommended):**

   It's best to create a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - For **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - For **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   Install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the App

To run RecipeApp locally:

1. Make sure your virtual environment is activated.
2. Navigate to the project directory and run the following commands to set up the database:
   ```bash
   python manage.py migrate
   ```

3. After the migrations are complete, start the Django development server:
   ```bash
   python manage.py runserver
   ```

4. The API will be accessible at:
   ```
   http://127.0.0.1:8000/
   ```

   You can now start making API requests to fetch recipes.

---

## API Endpoints

Here are the available API endpoints in RecipeApp:

1. **GET /api/recipes/** - Fetch a list of recipes based on search parameters (e.g., ingredients, meal type).
   
   Example request:
   ```
   GET /api/recipes/?search=pasta
   ```

   Example response:
   ```json
   {
     "recipes": [
       {
         "name": "Pasta with Tomato Sauce",
         "ingredients": ["Tomatoes", "Garlic", "Olive oil"],
         "instructions": "Cook pasta and prepare sauce."
       },
       {
         "name": "Spaghetti Bolognese",
         "ingredients": ["Ground beef", "Onion", "Garlic"],
         "instructions": "Cook ground beef, prepare sauce, serve with pasta."
       }
     ]
   }
   ```

2. **GET /api/recipes/{id}/** - Fetch details of a specific recipe by ID.

---

## Project Structure

The project directory has the following structure:

```
RecipeApp/
│
├── api/                        # Main API logic and views
│   ├── migrations/             # Database migrations
│   ├── models.py               # Defines the recipe model
│   ├── serializers.py          # Serializes the recipe data
│   ├── views.py                # Handles API requests and logic
│   └── urls.py                 # API routes
│
├── RecipeApp/                  # Django project settings
│   ├── settings.py             # Django settings file
│   ├── urls.py                 # Main URL routing file
│   └── wsgi.py                 # WSGI configuration
│
├── requirements.txt            # Dependencies for the project
├── manage.py                   # Django management script
├── README.md                   # Documentation for the project
└── .env                        # (Optional) Environment variables (e.g., secret keys, API tokens)
```

- **api/**: Contains the logic for handling recipe-related API requests, including views, models, and serializers.
- **RecipeApp/**: Contains the Django project settings and configuration.
- **requirements.txt**: A list of dependencies needed to run the project (e.g., `django`, `djangorestframework`).
- **manage.py**: Django’s command-line utility to interact with the project (e.g., running the server, migrations).

---

## Example API Request

### Search for Recipes:

Make a request to search for recipes by ingredients or meal types:
```
GET /api/recipes/?search=chicken
```

Response:
```json
{
  "recipes": [
    {
      "name": "Chicken Alfredo",
      "ingredients": ["Chicken", "Cream", "Garlic", "Parmesan"],
      "instructions": "Cook chicken, prepare alfredo sauce, mix with pasta."
    }
  ]
}
```

### Fetch a Specific Recipe by ID:

To get detailed information about a specific recipe:
```
GET /api/recipes/1/
```

Response:
```json
{
  "name": "Chicken Alfredo",
  "ingredients": ["Chicken", "Cream", "Garlic", "Parmesan"],
  "instructions": "Cook chicken, prepare alfredo sauce, mix with pasta."
}
```

---

## Contributing

If you would like to contribute to RecipeApp, feel free to fork the repository and submit a pull request. You can help by:
- Adding new features, like saving favorite recipes.
- Improving the API documentation.
- Fixing bugs or enhancing the backend logic.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

This version reflects the Django API setup for RecipeApp, with proper endpoint usage and instructions. Let me know if you need any additional updates!