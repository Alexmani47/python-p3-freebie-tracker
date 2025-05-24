#!/usr/bin/env python3

# Script goes here!
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Company, Dev, Freebie, Base

engine = create_engine('sqlite:///lib/freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

c1 = Company(name="TechCorp", founding_year=1999)
c2 = Company(name="InnovateX", founding_year=2005)


d1 = Dev(name="Alice")
d2 = Dev(name="Bob")


f1 = c1.give_freebie(d1, "USB Drive", 15)
f2 = c1.give_freebie(d2, "Notebook", 10)
f3 = c2.give_freebie(d1, "Mug", 8)

session.add_all([c1, c2, d1, d2, f1, f2, f3])
session.commit()
print("Seed data added.")
