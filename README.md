# Literary Compass

A Flask-based **book recommendation web app** that helps users discover books similar to a title they already like. The project also shows a curated **Top 50 Books** section and includes a simple **Contact** page for user feedback.

## Features

- Recommend books based on a selected book title
- Display a Top 50 books list with ratings and vote counts
- Show book cover images and author names
- Handle invalid or empty user input gracefully
- Simple contact page with EmailJS integration
- Clean multi-page UI built with HTML, CSS, and Bootstrap

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap
- **Libraries:** NumPy, Pandas
- **Deployment:** Gunicorn, Procfile support
- **Data/Model Storage:** Pickle (`.pkl`) files

## Project Structure

```bash
Literary-Compass/
│── app.py
│── requirements.txt
│── Procfile
│── popular.pkl
│── pt.pkl
│── books.pkl
│── similarity_scores.pkl
│── Datasets/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│── templates/
│   ├── index.html
│   ├── recommend.html
│   └── contact.html
```

## How It Works

The application loads preprocessed data from pickle files:

- `popular.pkl` stores the popular books data used on the home page
- `pt.pkl` stores the pivot table used for recommendation lookup
- `books.pkl` stores book metadata
- `similarity_scores.pkl` stores similarity values between books

When a user enters a book name, the app:

1. Checks whether the title exists in the pivot table
2. Finds the matching index
3. Uses similarity scores to identify similar books
4. Returns the top recommendations with author names and cover images

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd literary-compass-main
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask app

```bash
python app.py
```

Then open your browser and visit:

```bash
http://127.0.0.1:5000/
```

## Pages in the Application

### Home Page
- Displays the Top 50 books
- Shows title, author, votes, rating, and cover image

### Recommend Page
- Accepts a book title from the user
- Returns 5 similar book recommendations
- Shows an error message if the field is empty or the book is not found

### Contact Page
- Lets users send a message through a contact form
- Uses EmailJS on the client side

## Requirements

The project uses the following main packages:

- Flask
- NumPy
- Pandas
- Gunicorn
- python-dotenv

Install them with:

```bash
pip install -r requirements.txt
```

## Deployment

This project includes a `Procfile`:

```bash
web: gunicorn app:app
```

This makes it suitable for deployment on platforms that support Gunicorn-based Python apps.

## Notes

- The recommendation system depends on the presence of the `.pkl` files in the project root
- The contact page uses EmailJS credentials directly in the frontend; for a public repository, it is better to review and secure such configuration
- Large dataset and pickle files make the repository heavy, so GitHub LFS or external storage may be useful if the repo grows further

## Future Improvements

- Add search suggestions/autocomplete for book titles
- Improve handling for case-insensitive title matching
- Add genre, publication year, and ratings filters
- Store contact form submissions on the backend
- Deploy with a production-ready configuration
- Add screenshots and live demo link to the README

## Use Cases

This project is useful for:

- Book recommendation systems
- Mini machine learning deployment projects
- Flask-based data-driven web applications
- Portfolio projects for recommender systems

## License

This project is available for educational and personal use. You can add a specific open-source license if needed.

## Author

**Aayush Mehta**
