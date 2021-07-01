import os

def get_cli_input() -> str:
    """Get CLI input for the name of the car"""
    car_name = input("Enter the name of the car: ")
    return car_name

def get_cli_input_year() -> str:
    """Get CLI input for the year of the car"""
    car_year = input("Enter the year of the car: ")
    return car_year

def get_car_info_api(car_name: str, car_year: str) -> str:
    """Return the car info as gotten by an API"""
    return f"The {car_name} was manufactured in {car_year}"

car_year = get_cli_input_year()
car_name = get_cli_input()
print(get_car_info_api(car_name, car_year))

def commit_to_github(path: str):
    """Commit the given path to git and github"""
    os.system("git add " + path)
    os.system("git commit -m \"Update " + path + "\"")
    os.system("git push")

# ask if the user wants to commit
commit = input("Do you want to commit to github? (y/n) ")
if commit == "y":
    commit_to_github("getcarinfo.py")
else:
    print("Not commiting to github")
