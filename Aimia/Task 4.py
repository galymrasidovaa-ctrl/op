class Subject:
    def _init_(self):
        self.observers = []
        self.temperature = None

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self.temperature)

    def set_temperature(self, value):
        self.temperature = value
        print(f"\nТемпература изменилась: {value}")
        self.notify()


class PhoneDisplay:
    def update(self, temp):
        print(f"📱 Телефон: температура {temp}°C")


class WarningSystem:
    def update(self, temp):
        if temp > 30:
            print("⚠ ОПАСНО! ЖАРКО!")
        else:
            print("Температура в норме.")


# DEMO
if __name__ == "_main_":
    sensor = Subject()
    sensor.attach(PhoneDisplay())
    sensor.attach(WarningSystem())

    sensor.set_temperature(22)
    sensor.set_temperature(35)