import InsectClass as I 

def main():
    fly = I.Insect()


    print('ten random flight lengths')

    for value in range(10):
        fly.length_flight()
        print('The value of the flight is', fly.get_flight())
    

main()