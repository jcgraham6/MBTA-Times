# MBTA-Times
Use two separate functions to view the times of incoming Green line trains to Copley Square. 

# First Function
This function will take two user inputs starting with the specific Green line (B,C,D or E). Second, the function will ask for a direction - Eastbound or Westbound.
Combining these two parameters, the function will then return the next train that meets the inputted criteria. This message will additionally come up as a desktop
notification and a SMS text (if a Twilio account is created and details are filled out).

# Second Function
The purpose of the second function is to take  in a time (**must be in military format**) and pull all upcoming trains. If the time is not a string or before the current time, an error will be returned. 

# Using Twilio 
You must create a free account and pull the necessary SIDs from their [website](https://www.twilio.com/docs).
Twilio does offer a free trial for a single cellphone!
