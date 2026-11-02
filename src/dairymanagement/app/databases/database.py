from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from dairymanagement.app.config.settings import settings
from dairymanagement.app.databases.models.base import Base
from dairymanagement.app.databases.models.branch import Branch

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
    
)






