from database import engine
from sqlalchemy import inspect, text


def add_laboratory_column():

    inspector = inspect(engine)

    # Get existing columns from laboratories table
    columns = [
        column["name"]
        for column in inspector.get_columns("laboratories")
    ]

    # Check whether supported_standards already exists
    if "supported_standards" not in columns:

        with engine.begin() as connection:

            connection.execute(
                text(
                    "ALTER TABLE laboratories "
                    "ADD COLUMN supported_standards TEXT"
                )
            )

        print(
            "supported_standards column added successfully!"
        )

    else:

        print(
            "supported_standards column already exists!"
        )


if __name__ == "__main__":

    add_laboratory_column()