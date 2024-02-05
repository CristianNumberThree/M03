class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def display_info(self):
        print(f"Vehicle type: {self.vehicle}")


class Automobile(Vehicle):
    def __init__(self, vehicle, year, make, model, doors, roof):
        super().__init__(vehicle)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def get_info(self):
        super().display_info()
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def main():
    vehicle = input("What is the vehicle type? ")
    year = input("Enter the year: ")
    make = input("What is the make? ")
    model = input("What is the model? ")
    doors = input("Two door or Four door? ")
    roof = input("Does it have a sunroof or solid roof? ")

    output_vehicle = Automobile(vehicle, year, make, model, doors, roof)
    output_vehicle.get_info()


if __name__ == "__main__":
    main()