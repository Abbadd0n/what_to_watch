import csv

import click

from opinions_app import app, db
from opinions_app.models import Opinion


# CLI-команда для загрузки мнений из CSV-файла.
@app.cli.command('load_opinions')
def load_opinions_command():
    counter = 0

    with open('opinions.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        try:
            for row in reader:
                opinion = Opinion(**row)
                db.session.add(opinion)
                counter += 1

            db.session.commit()

        except Exception:
            db.session.rollback()
            raise

    click.echo(f'Загружено мнений: {counter}')
    