import itertools


zip_courses = zip(main_courses, price_main_courses)
zip_desserts = zip(desserts, price_desserts)
zip_drinks = zip(drinks, price_drinks)

for course, dessert, drink in itertools.product(zip_courses, zip_desserts, zip_drinks):
    costs = course[1] + dessert[1] + drink[1]
    if costs <= 30:
        print(f"{course[0]} {dessert[0]} {drink[0]} {costs}")