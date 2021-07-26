Hello sir, this is my program for the given assignment.

Functions :
get_data() -  to create the 20 odd numbers , 
              get last 8 and reverse the order, 
              and join in with "luxPMsoft" string according the the requirement,
              return json packet of the output

insert_data(encoded_string) - takes in the json variable ,
                              converts in StringIO and load into json, 
                              these values will be used for the value part of the command execution and together with the insert command , 
                              the program will get executed and the variables will be saved into database and replies with "incertation success" message,
                              If no parameter feeded or false parameter feeded, it will display "Internal en error occured" message.
                              
                              
Api routing in postman:
1. ("GET" REQUEST) You can run and open it in browser to see get_data executed
2. ("PUT" REQUEST) You can copy the output from above and paste thisbehind the absolute path in this format ("/<output>) and alternatively, 
  u can use the following link :
  http://127.0.0.1:5000/["l", 39, "u", 37, "x", 35, "P", 33, "M", 31, "s", 29, "o", 27, "f", 25, "t"]
