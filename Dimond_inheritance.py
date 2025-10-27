class vehicals:
    def features(self):
        print("All vehicals have wheels and can move")

class LandVehicals(vehicals):
    def features(self):
        print("Land vehicals: can drive on road")
        super().features()

class ElectricVehicals(vehicals):
    def features(self):
        print("Electric vehicals: can run on electicity")
        super().features()

class Electriccar(LandVehicals,ElectricVehicals):
    def features(self):
        print("Electric car: is the combination of landVehicals and ElectricVehicals")
        super().features()

ele=Electriccar()
ele.features()