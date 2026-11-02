# Dairy Farm Management System

A backend application for managing dairy farm operations, including branches, users, milkmen, milk collection records, milk rates, and payments. The system is designed to simplify daily dairy operations, maintain accurate financial records, and support branch-level management.

## Project Status

🚧 **In Development** — Database models and Alembic migrations are implemented. API development is the next phase.

## Features

### Database and Data Management

- Branch management
- User management with role-based access foundations
- Milkman registration and branch assignment
- Milk rate management with effective dates
- Daily milk collection tracking
- Payment records for milkmen
- Historical rate preservation for accurate earnings
- Database integrity through foreign keys, unique constraints, and check constraints

### Planned Features

- RESTful APIs using FastAPI
- Authentication and authorization using JWT
- Role-based and branch-level access control
- Collection and payment summaries
- Milkman balance calculation
- Request validation and centralized error handling
- Automated testing
- Redis caching
- Docker-based deployment

## Tech Stack

| Technology     | Purpose                                      |
| -------------- | -------------------------------------------- |
| Python         | Backend programming language                 |
| FastAPI        | REST API framework                           |
| PostgreSQL     | Relational database                          |
| SQLAlchemy 2.x | ORM and database interaction                 |
| Alembic        | Database migrations                          |
| Pydantic       | Data validation and settings                 |
| Redis          | Planned caching                              |
| Docker         | Containerization                             |
| uv             | Python dependency and environment management |

## Database Models

| Model            | Description                                        |
| ---------------- | -------------------------------------------------- |
| `Branch`         | Stores branch information                          |
| `User`           | Stores user details, roles, and branch assignments |
| `Milkman`        | Stores milkman details and branch association      |
| `MilkRate`       | Stores milk rates and their effective periods      |
| `MilkCollection` | Records daily milk quantities and applicable rates |
| `Payment`        | Records payments made to milkmen                   |

### Key Business Rules

- Each milkman belongs to a branch.
- Milk collection records preserve the rate used at the time of collection.
- Milk quantities and monetary values use decimal-based database types for precision.
- Historical collection records are not recalculated when milk rates change.
- A milkman's outstanding balance is calculated from total collection earnings minus total payments.
- Database constraints protect against invalid quantities, rates, and payment amounts.

## Project Structure

```text
DairyManagement/
├── app/
│   ├── main.py
│   ├── config/
│   │   └── settings.py
│   └── databases/
│       ├── database.py
│       └── models/
│           ├── __init__.py
│           ├── base.py
│           ├── branch.py
│           ├── user.py
│           ├── milkman.py
│           ├── milk_rate.py
│           ├── milk_collection.py
│           └── payment.py
├── alembic/
│   ├── versions/
│   └── env.py
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

Install the following tools:

- Python 3.11+
- Docker and Docker Compose
- uv

### 1. Clone the repository

```bash
git clone https://github.com/yadavsunnykumar/DairyManagement.git
cd DairyManagement
```

### 2. Configure environment variables

Create a local `.env` file based on the example:

```bash
cp .env.example .env
```

Configure your database connection:

```env
DATABASE_URL=postgresql+psycopg2://dairy_user:dairy_password@localhost:5432/dairy_db
```

Use your own credentials for local development. Never commit your `.env` file or production secrets.

### 3. Install dependencies

```bash
uv sync
```

### 4. Start PostgreSQL

```bash
docker compose up -d
```

Check that the database container is running:

```bash
docker compose ps
```

### 5. Apply database migrations

```bash
uv run alembic upgrade head
```

This creates or upgrades the database schema using the committed Alembic migrations.

### 6. Start the FastAPI application

Once the API entry point is configured:

```bash
uv run uvicorn dairymanagement.app.main:app --reload
```

If your application package or entry point differs, update the command to match your project structure.

The interactive API documentation will be available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Database Migrations

Create a migration after changing SQLAlchemy models:

```bash
uv run alembic revision --autogenerate -m "describe your schema change"
```

Review the generated migration before applying it:

```bash
uv run alembic upgrade head
```

Check the current migration revision:

```bash
uv run alembic current
```

View migration history:

```bash
uv run alembic history
```

**Always commit migration files to version control.** Do not edit an already-applied migration in a shared environment; create a new migration instead.

## Development

Stop the database containers:

```bash
docker compose down
```

Stop containers and remove the local database volume:

```bash
docker compose down -v
```

> **Warning:** `docker compose down -v` deletes the persisted local PostgreSQL data.

## Future Improvements

- Complete CRUD endpoints for all models
- Authentication and authorization
- Branch-level data access
- Daily and monthly reports
- Milkman earnings and payment summaries
- Automated tests with pytest
- Redis caching
- CI/CD pipeline
- Production deployment

## Contributing

1. Create a feature branch.
2. Make your changes.
3. Add or update tests.
4. Generate and review database migrations if the schema changes.
5. Submit a pull request.

## License

This project is currently for learning and development purposes. Add a license before distributing or using it commercially.
