# Heading1 CS361-TextMicroservice

Communication Contract:

Request Data:
    To request data, ensure the file "test.txt" (changeable if needed) includes only the phrase "run" on line 1. Be sure there are no additional lines. 
    Then call the program. While this program is active, it will search the provided file for the key phrase to begin servicing data.
    The program will search for 20 seconds before exiting.

    Example call:
        python3 microservice.py

Receive Data:
    Once key phrase has been found, microservice will rewrite the provided text file with data



UML Diagram:

![UML class](https://user-images.githubusercontent.com/98556557/218412025-4ce33929-2cfc-44e3-8a90-86ab5efa00c1.png)
