import CarClass as c

def main():
    car = c.CarClass('Jeep', 'Patriot')

    for i in range(5):
        car.accelerate()
        print('Current speed is: ', car.get_speed())

    for i in range(5):
        car.brake()
        print('Current speed is: ', car.get_speed())
    




main()