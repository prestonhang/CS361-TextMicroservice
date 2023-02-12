import time
import lorem
import random

def main():
    filename = "test.txt"                       #declare file you wish to insert latin text
    count = 0                                   #initialize timer for deactivation
    print("Microservice Initiated")
    while(True):
        time.sleep(2)
        file = open(filename, "r")              #open file
        if(file.read() == "run"):               #if phrase "run" is found in file, begin service
            print("---------------------------------------------------------")
            print("Phrase detected")
            insert = open(filename, "w")        #open file with write
            value = random.randrange(1, 20)     #create random number between 1-20
            value = int(value)
            for num in range(0, value):         #create a line of latin text up to random value
                text = lorem.sentence()         #generate latin text
                insert.write(text)              #insert into file
                insert.write("\n")              #newline
            print("Sucessfully wrote Latin paragraph to file")
            print("---------------------------------------------------------")
            insert.close()
            count = 0                           #reset timer
        else:                                   #if phase "run" was not found, initiate timeout countdown
            if(count == 10):                    #if reached 10, exit microservice
                print("No activity detected. Exiting Microservice")
                file.close()
                break
            else:
                print("Listening for key phrase... Time until deactivation: ", 10-count)    #display time until deactivation
                count += 1                                                                  #increment timer
        file.close()

main()