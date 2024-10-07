from .base import Base

class Ceo(Base, table=True):
    __tablename__ = "apple_ceos"

    name: str
    slug: str
    first_year_active: int