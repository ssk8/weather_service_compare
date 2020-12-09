import sqlalchemy
import sqlalchemy.orm
from weather_model import ModelBase

__factory = None


def global_init():
    global __factory

    conn_str = 'sqlite:///' + "data/weather.db"

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    ModelBase.metadata.create_all(engine)

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


def create_session():
    global __factory

    if __factory is None:
        global_init()

    return __factory()
