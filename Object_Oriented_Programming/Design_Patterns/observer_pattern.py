"""
Implement the Observer Pattern by creating a weather monitoring system. Your task is to:

Create a WeatherStation class that extends the Subject class
Add a private attribute to track the current temperature
Implement set_temperature(temperature) to update the temperature and notify observers
Implement get_temperature() to return the current temperature
Create a WeatherDisplay class that extends the Observer class
Each display should have a name
When notified of a temperature change, it should display a message
The message format for temperature updates should be exactly:

Display [name]: Current temperature is [temperature]C
"""
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


class WeatherStation(Subject):
    def __init__(self, temperature=0.0):
        super().__init__()
        self._temperature = temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify(self._temperature)

    def get_temperature(self):
        return self._temperature


class WeatherDisplay(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"Display {self.name}: Current temperature is {temperature}C")


# Example usage
if __name__ == "__main__":
    # Create a weather station
    weather_station = WeatherStation()

    # Create displays
    phone_display = WeatherDisplay("Phone")
    tablet_display = WeatherDisplay("Tablet")

    # Attach displays to the weather station
    weather_station.attach(phone_display)
    weather_station.attach(tablet_display)

    # Set temperature and notify displays
    weather_station.set_temperature(25.5)
    
    # Detach one display and update temperature again
    weather_station.detach(phone_display)
    weather_station.set_temperature(30.0)
