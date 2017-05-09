class Car(object):
    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0

        if self.name == 'Koenigsegg':
            self.num_of_doors = 2
        elif self.name == 'Porshe':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.car_type == 'saloon':
            return True

    def drive(self, moving_speed):
        if moving_speed == 3:
            self.speed = 1000
        elif moving_speed == 7:
            self.speed = 77
        return self
