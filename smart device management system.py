# Parent Class
class SmartDevice:
    def __init__(self, device_id, name):
        self.__device_id = device_id
        self.__power_status = False
        self.name = name

    # Getter for device ID
    @property
    def device_id(self):
        return self.__device_id

    # Setter for device ID with validation
    @device_id.setter
    def device_id(self, value):
        if value != "":
            self.__device_id = value
        else:
            print("Device ID cannot be empty!")

    # Getter for power status
    @property
    def power_status(self):
        return self.__power_status

    # Setter for power status
    @power_status.setter
    def power_status(self, status):
        self.__power_status = status

    def turn_on(self):
        self.power_status = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.power_status = False
        print(f"{self.name} is now OFF.")

    def display_info(self):
        print("\nDevice Information")
        print("-------------------")
        print("Name:", self.name)
        print("Device ID:", self.device_id)
        print("Power Status:", "ON" if self.power_status else "OFF")


# Child Class 1
class SecurityCamera(SmartDevice):

    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.recording_status = False

    def start_recording(self):
        self.recording_status = True
        print(f"{self.name} started recording.")

    def stop_recording(self):
        self.recording_status = False
        print(f"{self.name} stopped recording.")

    def display_info(self):
        super().display_info()
        print("Recording:", "ON" if self.recording_status else "OFF")


# Child Class 2
class SmartLight(SmartDevice):

    def __init__(self, device_id, name, brightness=50):
        super().__init__(device_id, name)

        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            self.brightness = 50

    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10
            print("Brightness increased.")
        else:
            print("Brightness already at maximum.")

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 10
            print("Brightness decreased.")
        else:
            print("Brightness already at minimum.")

    def display_info(self):
        super().display_info()
        print("Brightness:", self.brightness)


# Child Class 3
class TemperatureSensor(SmartDevice):

    def __init__(self, device_id, name, temperature):
        super().__init__(device_id, name)
        self.temperature = temperature

    def read_temperature(self):
        print(
            f"{self.name} temperature reading: {self.temperature}°C"
        )

    def display_info(self):
        super().display_info()
        print("Temperature:", self.temperature, "°C")


# Creating objects
temperature_sensor = TemperatureSensor(
    "TS001",
    "Living Room Temperature Sensor",
    26
)

smart_light = SmartLight(
    "SL001",
    "Bedroom Smart Light",
    70
)

security_camera = SecurityCamera(
    "SC001",
    "Front Door Security Camera"
)


devices = [
    temperature_sensor,
    smart_light,
    security_camera
]


# Menu System
def menu():

    while True:

        print("\n===== Smart Device Management System =====")
        print("1. Display Device Information")
        print("2. Turn Device On")
        print("3. Turn Device Off")
        print("4. Read Temperature")
        print("5. Adjust Brightness")
        print("6. Start Recording")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            for device in devices:
                device.display_info()

        elif choice == "2":

            for device in devices:
                device.turn_on()

        elif choice == "3":

            for device in devices:
                device.turn_off()

        elif choice == "4":

            temperature_sensor.read_temperature()

        elif choice == "5":

            print("1. Increase Brightness")
            print("2. Decrease Brightness")

            option = input("Choose option: ")

            if option == "1":
                smart_light.increase_brightness()

            elif option == "2":
                smart_light.decrease_brightness()

            else:
                print("Invalid choice.")

        elif choice == "6":

            security_camera.start_recording()

        elif choice == "7":

            print("Exiting system...")
            break

        else:

            print("Invalid menu option.")


# Run program
menu()