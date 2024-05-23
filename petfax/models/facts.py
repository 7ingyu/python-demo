from .db import db
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column

class Fact(db.Model):
    id = mapped_column(Integer, primary_key = True)
    submitter = mapped_column(String(250))
    fact = mapped_column(String)


