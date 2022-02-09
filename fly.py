import InsectClass as I 

def main():
    fly = I.Insect()


    print('ten random flight lengths')

    for flights in range(10):
        fly.flight()
        print('The value of the flight is', fly.get_flight())
    

main()