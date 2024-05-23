def to_dict(data):
  if (type(data) == list):
    return [ to_dict(m) for m in data ]
  else:
    return { c.name: getattr(data, c.name) for c in data.__table__.columns }