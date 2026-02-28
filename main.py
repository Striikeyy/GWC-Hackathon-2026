from person import Person
from group import Group

persons = []
groups = []

def setup_data():
    persons.append(Person("Jacob", "algebra2", 90638, "2026-3-01", "2027-12-31"))
    persons.append(Person("Tony", "geometry", 90638, "2026-4-01", "2027-12-31"))

    groups.append(Group("tonygeometry", "geometry", 5, "2026-4-15", 90638))
    groups.append(Group("jacobalgebra2", "algebra2", 5, "2026-3-15", 90638))