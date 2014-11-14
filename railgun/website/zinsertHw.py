from sqlalchemy import create_engine, schema, Table
from sqlalchemy.orm import create_session, mapper, relation
from . import webconfig

from datetime import datetime
from babel.dates import timedelta, get_timezone

db = create_engine(webconfig.SQLALCHEMY_DATABASE_URI)
metadata = schema.MetaData(db)
session = create_session()

users = Table('users', metadata, autoload=True)
finalscore = Table('finalscore', metadata, autoload=True)
handins = Table('handins', metadata, autoload=True)
hwtypes = Table('hwtypes', metadata, autoload=True)
hws = Table('hws', metadata, autoload=True)


class User(object):
    pass


class FinalScore(object):
    pass


class Handin(object):
    pass


class HwType(object):

    def __init__(self, type=None, is_hidden=True):
        self.type = type
        self.is_hidden = is_hidden

    def __repr__(self):
        return "<HwType:%s>" % self.type


class Hw(object):

    def __init__(self, uuid=None, type_id=None):
        self.uuid = uuid
        self.type_id = type_id

    def __repr__(self):
        return "<homework:%s>" % self.uuid 

HwtypeMapper = mapper(HwType, hwtypes)
hwsMapper = mapper(Hw, hws, properties={
    'hw_type': relation(HwType, backref='hws')
})

# onehw = Hw()
# oneType = HwType()

# onehw.uuid = '9f286333b778488c9a14d66aaf559f48'
# oneType.is_hidden = True
# onehw.hw_type = oneType
# oneType.basetime = datetime(2015,01,01)

# oneType.type = 'Arithmetic API'
# oneType.hws.append(onehw)

# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()

# onehw.uuid = '69e937823ac04e0fbe8cfefd0bb197ab'
# oneType.is_hidden = True
# onehw.hw_type = oneType
# oneType.basetime = datetime(2015,01,01)

# oneType.type = 'Whitebox Test'
# oneType.hws.append(onehw)

# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()

# onehw.uuid = 'ad19289bde3b496b88ef2421b2f2e153'
# oneType.is_hidden = True
# onehw.hw_type = oneType
# oneType.basetime = datetime(2015,01,01)

# oneType.type = 'Blackbox Test'
# oneType.hws.append(onehw)

# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()

# onehw.uuid = 'b388ad5b25ee44bbac9be46c43851768'
# oneType.is_hidden = True
# onehw.hw_type = oneType
# oneType.basetime = datetime(2015,01,01)

# oneType.type = 'Format Path'
# oneType.hws.append(onehw)

# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()

# onehw.uuid = 'bfff167aaf2a471a9bc4d2cb56c15ede'
# oneType.is_hidden = True
# onehw.hw_type = oneType
# oneType.basetime = datetime(2015,01,01)

# oneType.type = 'Learn xUnit'
# oneType.hws.append(onehw)

# session.add(oneType)
# session.flush()
