import json


from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()

class Version(db.Model):
    __tablename__ = 'version'
    id = Column(Integer, primary_key=True)
    component = Column(String())
    version = Column(String())
    environment = Column(String())
    health = Column(String())

    def __repr__(self):
        return '<Version %r>' % self.id + self.component + self.version + self.environment + self.health

def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):

        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)
                if data is not None:
                    fields[field] = data
            except TypeError:
                pass
        return fields