import InsectClass as I 

def main():
    fly = I.Insect(2,4) #these are the arguements for w and l 


    print('ten random flight lengths')

    for value in range(10):
        fly.length_flight()
        print('The value of the flight is', fly.get_flight())
    

main()