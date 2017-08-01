import uuid

import time

import logging

from firstaio.db.Field import StringFieldC, BooleanFieldC, FloatFieldC, TextFieldC, IntegerFieldC
from firstaio.db.ModelMetaclass import ModelMetaclassC


class ModelC(dict, metaclass=ModelMetaclassC):
    def __init__(self, **kwargs):
        super(ModelC, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'ModelC' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


class TestModelC(ModelC):
    __table__ = 'test'
    id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(50)')
    admin = BooleanFieldC()
    create_at = FloatFieldC(default=time.time)
    content = TextFieldC()
    count = IntegerFieldC()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test = TestModelC()