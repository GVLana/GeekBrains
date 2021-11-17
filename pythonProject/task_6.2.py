
class Road:
    _length = None
    _width = None

    def __init__(self, length=int(input("Enter the length in meters: ")), width=int(input("Enter the width in meters: "))):
        self._length = length
        self._width = width

    def asphalt_calculations(self):
        weight = 25
        thickness = 5
        asphalt = round(self._length * self._width * weight * thickness / 1000)
        print(f'You will need {asphalt} tons for paving.')


road_to_pave = Road()
road_to_pave.asphalt_calculations()
