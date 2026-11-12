from flask import render_template

from opinions_app import app, db


# Обработчик внутренней ошибки сервера 500.
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()

    return render_template('500.html'), 500


# Обработчик ошибки 404 — страница не найдена.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
