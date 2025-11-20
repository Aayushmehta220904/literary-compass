from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity_scores.pkl', 'rb'))


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_rating'].values)
    )


# ------------------------------
# RECOMMEND UI PAGE (GET)
# ------------------------------
@app.route('/recommend')
def recommend_ui():
    return render_template(
        'recommend.html',
        recommendations=[],
        images=[],
        authors=[],
        error=None
    )


# ------------------------------
# RECOMMEND BOOKS (POST + GET SAFE)
# ------------------------------
@app.route('/recommend_books', methods=['GET', 'POST'])
def recommend_books():

    # If user visits direct URL → Show empty UI instead of 404
    if request.method == "GET":
        return render_template(
            'recommend.html',
            recommendations=[],
            images=[],
            authors=[],
            error=None
        )

    user_input = request.form.get("user_input").strip()

    if user_input == "":
        return render_template(
            'recommend.html',
            recommendations=[],
            images=[],
            authors=[],
            error="Please enter a book name."
        )

    if user_input not in pt.index:
        return render_template(
            'recommend.html',
            recommendations=[],
            images=[],
            authors=[],
            error="Book not found."
        )

    index = np.where(pt.index == user_input)[0][0]

    similar_items = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []
    images = []
    authors = []

    for item in similar_items:
        title = pt.index[item[0]]
        temp_df = books[books['Book-Title'] == title].drop_duplicates('Book-Title')

        recommendations.append(title)
        authors.append(temp_df['Book-Author'].values[0])
        images.append(temp_df['Image-URL-M'].values[0])

    return render_template(
        'recommend.html',
        recommendations=recommendations,
        images=images,
        authors=authors,
        error=None
    )


# ------------------------------
# CONTACT PAGE
# ------------------------------
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
