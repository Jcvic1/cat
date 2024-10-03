import random

cat_breeds = [
    'Siamese',
    'Persian',
    'Maine Coon',
    'British Shorthair',
    'Sphynx',
    'Ragdoll',
    'Scottish Fold',
    'Russian Blue',
    'Oriental Shorthair',
    'Birman',
    'Himalayan',
    'Balinese',
    'Abyssinian',
    'Devon Rex',
    'Cornish Rex',
    'Singapura',
    'Manx',
    'Tonkinese',
    'Burmese',
    'Chartreuse',
    'Egyptian Mau',
    'Korat',
    'Ojos Azules',
    'Peterbald',
    'Pixie-bob',
    'Selkirk Rex',
    'Snowshoe',
    'Turkish Van',
    'Colorpoint Shorthair',
    'Javanese'
]

data_list = []
sql_statements = []

for _ in range(150):
    breed = random.choice(cat_breeds)
    year = str(random.randint(2000, 2023))
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 28))

    attributes = {
        'breed': breed,
        'year': year,
        'month': month,
        'day': day,
        'color': random.choice(['Brown', 'Black', 'White', 'Golden', 'Red', 'Blue']),
        'description': f"Short-nosed, wrinkled face {breed}",
    }

    data_list.append(attributes)


def json_to_sql(data_list):  # type: ignore

    sql_statement = (
        """
CREATE TABLE IF NOT EXISTS cat (
id SERIAL PRIMARY KEY,
breed VARCHAR(50) NOT NULL,
age DATE,
color VARCHAR(20),
description TEXT
);
""")
    sql_statements.append(sql_statement)

    for cat in data_list:
        breed = cat['breed']
        age = f"{cat['year']}-{cat['month']}-{cat['day']}"
        color = cat['color']
        description = cat['description']

        sql_statement = (
            f"""
INSERT INTO cat (breed, age, color, description)
VALUES ('{breed}', '{age}', '{color}', '{description}');
""")  # noqa: ignore=E702,E231

        sql_statements.append(sql_statement)

    return ''.join(sql_statements)


sql_statements = json_to_sql(data_list)


with open('insert_cats.sql', 'w') as sql_file:
    sql_file.write(sql_statements)  # type: ignore

print('SQL statements have been saved to insert_cats.sql')
