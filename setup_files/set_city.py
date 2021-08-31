import os

print("\nWelcome to Weather Service Defaults")
print("In order to use Kurooto Weather Service")
city = input("Enter your city:\n")

city_store_loc = os.path.normpath(os.path.join((os.path.dirname(os.path.abspath(__file__))), "user\\user_info"))
city_store_loc = city_store_loc.replace("\\setup_files", "")

city_store = open(city_store_loc + "\city.KRT", 'w')
city_store.write(city)
city_store.close()

print("Done, read the docs for next steps")