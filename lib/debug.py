#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Freebie, Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    import ipdb; ipdb.set_trace()

    dev = session.query(Dev).first()
    print("Dev:", dev)
    print("Dev's Freebies:", dev.freebies)
    print("Dev's Freebies Companies:", dev.companies)

    company = session.query(Company).first()
    print("Company:", company)
    print("Company's Freebies:", company.freebies)
    print("Company's Freebies Devs:", company.devs)

    alice = session.query(Dev).filter_by(name="Alice").first()
print(alice.companies)
print(alice.received_one("USB Drive"))
print(alice.received_one("Notebook"))

freebie = session.query(Freebie).filter_by(item_name="Mug").first()
print(freebie.print_details())


bob = session.query(Dev).filter_by(name="Bob").first()
alice.give_away(bob, freebie)
session.commit()
print(freebie.print_details()) 