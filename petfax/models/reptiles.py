from .db import db
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column

class Reptile(db.Model):
    id = mapped_column(Integer, primary_key = True)
    common_name = mapped_column(String)
    scientific_name = mapped_column(String)
    conservation_status = mapped_column(String)
    native_habitat = mapped_column(String)
    fun_fact = mapped_column(String)


