import random
import string
from flask import render_template, request, redirect, url_for
from app import create_app
from app.models import Poster

app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id_poster = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10))
        poster = request.form['poster']
        form_content = request.form['form_content']

        poster = Poster(id_poster=id_poster, author=poster,
                        content=form_content)

        app.db.session.add(poster)
        app.db.session.commit()

        return redirect(url_for('render_post', id_poster=id_poster))

    return render_template('index.html')


@app.route('/p/<id_poster>')
def render_post(id_poster: str):
    if (poster := Poster.query.filter_by(id_poster=id_poster).first()) is not None:
        return render_template('paste.html', poster=poster)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
