import os
import random
import time

class Car:
    def __init__(self, name, top_speed, acceleration, drivetrain):
        self.name = name
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.drivetrain = drivetrain
        self.speed = 0

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

    def brake(self):
        self.speed -= self.acceleration
        if self.speed < 0:
            self.speed = 0

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')  

def main():
    car1 = Car("Volkswagen Passat", 135, 10, "Front-Wheel Drive")
    car2 = Car("Dacia Logan", 110, 8, "Front-Wheel Drive")
    car3 = Car("Daweoo Matiz", 90, 5, "Front-Wheel Drive")
    car4 = Car("Skoda Octavia", 135, 10, "Front-Wheel Drive")
    car5 = Car("BMW 330D", 141, 11, "Rear-Wheel Drive")

    cars = [car1, car2, car3, car4, car5]

    print("Welcome to the Car Racing Game!")
    print("Choose your car:")

    for i, car in enumerate(cars, 1):
        print(f"{i}. {car.name} (Top Speed: {car.top_speed} mph, 0-60 mph Acceleration: {car.acceleration} seconds, Drivetrain: {car.drivetrain})")

    choice = int(input("Enter the number of the car you want to race: ")) - 1

    if 0 <= choice < len(cars):
        player_car = cars[choice]
        print(f"You've chosen the {player_car.name} for the race!")

        race_distance = 400

        computer_cars = [Car("Computer Car 1", random.randint(120, 200), random.randint(6, 12), random.choice(["Front-Wheel Drive", "Rear-Wheel Drive", "All-Wheel Drive"])),
                         Car("Computer Car 2", random.randint(120, 200), random.randint(6, 12), random.choice(["Front-Wheel Drive", "Rear-Wheel Drive", "All-Wheel Drive"]))]

        print("Computer-controlled cars:")
        for car in computer_cars:
            print(f"{car.name} (Top Speed: {car.top_speed} mph, 0-60 mph Acceleration: {car.acceleration} seconds, Drivetrain: {car.drivetrain})")

        print("The race begins!")

        while player_car.speed < player_car.top_speed and any(computer_car.speed < computer_car.top_speed for computer_car in computer_cars):
            player_car.accelerate()
            for computer_car in computer_cars:
                if computer_car.speed < computer_car.top_speed:
                    computer_car.accelerate()

            clear_screen() 
            print(f"{player_car.name} is currently going {player_car.speed} mph.")
            for computer_car in computer_cars:
                print(f"{computer_car.name} is currently going {computer_car.speed} mph.")
            time.sleep(1)

        print("The race is over!")

        player_time = race_distance / player_car.speed
        computer_times = [race_distance / computer_car.speed for computer_car in computer_cars]

        if all(player_time < computer_time for computer_time in computer_times):
            print(f"Congratulations! {player_car.name} has won the race!")
        else:
            print("Computer-controlled cars have won the race.")

    else:
        print("Invalid car choice. Please choose a valid car.")
main()
input()

