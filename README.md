# CS:361 - Software Engineering I 

## Microservice For David Zager by Preston Hang - 2/13/2023

### Communication Contract:
This microservice implements a "text file" based communication pipeline

#### Request Data:
To request data, ensure a local file "test.txt" (changeable if needed) includes only the phrase "run" on line 1.
Be sure there are no additional lines. 
    
Then call the program. While this program is active, it will search the provided file for the key phrase to begin servicing data.
The program will search for 20 seconds before exiting.

Example call:
        python3 microservice.py

#### Receive Data:
Once key phrase has been found, microservice will rewrite the provided text file with new data
Data provided includes:
Between 1-20 lines of randomly generated Latin text



### UML Diagram:
   This diagram showcases how data is requested and received.
        1. User provides text file with key phase.
        2. Microservice checks text file for key phrase. 
        3. If key phrase "run" is found, insert new text into file
        4. Else, continue searching for key phrase until timer expires
        5. When timer expires, microservice shuts down
        
#### Read from top to bottom. 
![UML class](https://user-images.githubusercontent.com/98556557/218412025-4ce33929-2cfc-44e3-8a90-86ab5efa00c1.png)
