#------------------------TO-DO-LIST-----------------------------------------#

tasks = []


#FOR ADD TASK
def add_task():
    print("\n===== TO-DO LIST =====")
    print("\n----- ADD TASK -----")

    task = input("Enter your task:- ")

    tasks.append(task)

    print("Task added successfully!")


#FOR VIEW TASK
def view_task():
    print("\n===== TO-DO LIST =====")

    if len(tasks) == 0:
        print("No tasks available.")

    else:
        for number, task in enumerate(tasks, 1):
            print(number, ".", task)

#FOR DELETE TASK
def delete_task():
    print("\n----- DELETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_task()

    number = int(input("Enter task number to delete: "))

    if number >= 1 and number <= len(tasks):
        deleted_task = tasks.pop(number - 1)

        print(deleted_task, "deleted successfully!")

    else:
        print("Invalid task number!")

#MENU BAR 
while True:

    print("\n======================")
    print("      TO-DO LIST")
    print("======================")

    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")


#--------------------------------Simple Wether Application--------------------------------------
import requests

api_key ="9ed57c38f46bfe521efde7e62d4de3ed"
base_url = "https://api.openweathermap.org/data/2.5/weather"

while True:

    print("=============================")
    print("|      WEATHER APPLICATION   |")
    print("=============================")

    print("1. Single City Weather")
    print("2. Multiple City Weather")
    print("3. Exit")

    choice = int(input("Enter Your choice:- "))

    weather = {}
    citys = set()

    if choice == 3:

        print("Exiting Weather App......")
        break

    elif choice == 1:

        city = input("Enter city name:- ")

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        print("Fetching weather data....")

        response = requests.get(base_url, params=params)

        if response.status_code == 200:

            data = response.json()

            print("\n====== WEATHER SUMMARY ======")
            print(f"CITY: {city}")
            print("-" * 30)

            print(f"TEMPERATURE: {data['main']['temp']} °C")
            print(f"WEATHER: {data['weather'][0]['description']}")
            print(f"HUMIDITY: {data['main']['humidity']}%")
            print(f"WIND SPEED: {data['wind']['speed']} m/s")

            print("-" * 30)

        else:

            print("Cannot find weather data!")
            continue

    elif choice == 2:

        print("\n====== MULTIPLE CITY WEATHER ======")

        while True:

            try:

                num_citys = int(
                    input("\nHow many cities to check (1-4): ")
                )

                if num_citys < 1 or num_citys > 4:

                    print("Invalid input! Please enter number between 1 to 4.")
                    continue

                break

            except ValueError:

                print("Invalid input! Please enter a valid number.")
                continue

        for num in range(num_citys):

            while True:

                city = input(
                    f"Enter the city name {num + 1}: "
                )

                if not city.strip():

                    print("City name cannot be empty.")
                    continue

                params = {
                    "q": city,
                    "appid": api_key,
                    "units": "metric"
                }

                print("Fetching weather data...")

                response = requests.get(
                    base_url,
                    params=params
                )

                if response.status_code == 200:

                    city = city.strip()

                    citys.add(city)

                    data = response.json()

                    weather[city] = data

                    break

                else:

                    print("Cannot find city!")
                    continue

        citys = sorted(citys)

        print("\n============================ WEATHER SUMMARY ============================")

        print(
            f"{'No.':<5}"
            f"{'City':<15}"
            f"{'Temperature':<15}"
            f"{'Weather':<20}"
            f"{'Humidity':<10}"
            f"{'Wind Speed':<10}"
        )

        print("-" * 75)

        for number, city in enumerate(citys, 1):

            data = weather[city]

            print(
                f"{number:<5}"
                f"{city:<15}"
                f"{str(data['main']['temp']) + ' °C':<15}"
                f"{data['weather'][0]['description']:<20}"
                f"{str(data['main']['humidity']) + '%':<10}"
                f"{str(data['wind']['speed']) + ' m/s':<10}"
            )

        print("-" * 75)

    else:

        print(
            "Invalid choice! Please select a valid option (1-3)."
        )

        continue