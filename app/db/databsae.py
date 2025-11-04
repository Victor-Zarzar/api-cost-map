import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar
from src.config.settings import settings

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

url = settings.DATABASE_URL

engine = create_engine(url, echo=False, pool_pre_ping=True)


def get_session():
    return Session(engine)
