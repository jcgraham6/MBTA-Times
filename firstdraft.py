#Packages to install
from plyer import notification        #Computer notification 
import requests                       #API
from datetime import datetime, date   #Time differences
import json                           #Read json file    
from twilio.rest import Client        #Send txt message 



#First Function

#Create function call
def copley():
    '''
    Takes user input and shows the Green line trains coming into Copley
    '''
    
    response = requests.get('https://api-v3.mbta.com/predictions?filter[stop]=place-coecl')
    
    #Check for error within the call
    response.raise_for_status()

    #Convert JSON into a dictionary for parsing
    y = json.loads(response.content)
    
    #Empty lists for appending
    time = []
    lines = []
    skipped = 0
    
    line = input('Please choose which Green line: \n Green-B \n Green-C \n Green-D \n Green-E \n\n')
    
    checklist_lines = ['GREEN-B','GREEN-C','GREEN-D','GREEN-E']
    checklist_direction = ['WESTBOUND','EASTBOUND']
    
    #Add details to the destination      
        
    if line.upper().strip() in checklist_lines:
            
        print('Line in list')
               
        direction = input('\n Eastbound or Westbound? \n')
        
        if direction.upper().strip() in checklist_direction:
                       
            if direction.upper() == 'WESTBOUND':
                direction = 0
                                
                for x in range(len(y['data'])):
                    
                        
                    #Determine skipped stops
                    if ((y['data'][x]['attributes']['direction_id'] == direction) and
                       (y['data'][x]['relationships']['route']['data']['id'] == line)):
                        
                    #Classify as datetime object
                        military_time = y["data"][x]['attributes']['arrival_time'][-14:-9]
                        dt = datetime.strptime(military_time, "%H:%M")
        
                    #Convert into standard time
                        standard_time = dt.strftime("%I:%M %p")
                        time.append(standard_time)   
            
            
                    #Get current time and convert train arrival
                        now = datetime.now()
                        current_time = now.strftime("%I:%M %p")
                        current_time = datetime.strptime(current_time,'%I:%M %p')
                        standard = datetime.strptime(standard_time,'%I:%M %p')
            
                        diff = standard - current_time
                        diff = diff.total_seconds()/60
                    
                    #Remove any negative times
                        if diff > 0:
                            
                    
                        #Line detail
                            line = str(y['data'][x]['relationships']['route']['data']['id'])
                            lines.append(line)
                            
                            if line == 'Green-B':
                                line += ' to Boston College'
                            elif line == 'Green-C':
                                line += ' to Cleveland Circle'
                            elif line == 'Green-D':
                                line += ' to Riverside'
                            else:
                                line += ' to Heath St'
            
                    #Build desktop notification
                            title = 'Arriving at Copley'
                            message = str(line) + ' is arriving at ' + standard_time + '\nYou have ' + str(diff) + ' minute(s) until arrival'
                            print(message, 'A text will be sent shortly')
                                
                            notification.notify(title= title,
                            message= message,
                            app_icon = None,
                            timeout= 60,
                            toast=False)
                            
                            
                    #Phone notification!
                         #Account SID from twilio.com/console
                            account_sid = 'AC59086b39adf701d1e556124108a45164' 

                        #Auth Token from twilio.com/console
                            auth_token = 'cf1e5f2e7d1825cc5edd82b014014ce8' 
                            client = Client(account_sid, auth_token) 
 
                            message = client.messages.create(  
                                  messaging_service_sid='MG45952c62fb1f56de0f555683ff8f18ce', 
                                  body= message,      
                                  to='+12039647165' 
                                  )  
                            
                        else:
                            continue
                    
            else:
                direction = 1
                for x in range(len(y['data'])):
                    
                        
                    #Determine skipped stops
                    if ((y['data'][x]['attributes']['direction_id'] == direction) and
                       (y['data'][x]['relationships']['route']['data']['id'] == line)):
                        
                    #Classify as datetime object
                        military_time = y["data"][x]['attributes']['arrival_time'][-14:-9]
                        dt = datetime.strptime(military_time, "%H:%M")
        
                    #Convert into standard time
                        standard_time = dt.strftime("%I:%M %p")
                        time.append(standard_time)
                    
                     #Get current time and convert train arrival
                        now = datetime.now()
            
                        current_time = now.strftime("%I:%M %p")
                        current_time = datetime.strptime(current_time,'%I:%M %p')
                        standard = datetime.strptime(standard_time,'%I:%M %p')
            
                        diff = standard - current_time
                        diff = diff.total_seconds()/60
                        
                        if diff >= 0:
    
                            line = str(y['data'][x]['relationships']['route']['data']['id'])
                            lines.append(line)
                            
                            if line == 'Green-B':
                                line += ' from Boston College'
                            elif line == 'Green-C':
                                line += ' from Cleveland Circle'
                            elif line == 'Green-D':
                                line += ' from Riverside'
                            else:
                                line += ' from Heath St'                       
            
                    #Build desktop notification
                            title = 'Arriving at Copley'
                            message = str(line) + ' is arriving at ' + standard_time + '\nYou have ' + str(diff) + ' minute(s) until arrival'
                            print(message, 'A text will be sent shortly')
                                
                            notification.notify(title= title,
                            message= message,
                            app_icon = None,
                            timeout= 60,
                            toast=False)
                            
                    
                    #Phone notification!
                         #Account SID from twilio.com/console
                            account_sid = 'AC59086b39adf701d1e556124108a45164' 

                        #Auth Token from twilio.com/console
                            auth_token = 'cf1e5f2e7d1825cc5edd82b014014ce8' 
                            client = Client(account_sid, auth_token) 
 
                            message = client.messages.create(  
                                  messaging_service_sid='MG45952c62fb1f56de0f555683ff8f18ce', 
                                  body= message,      
                                  to='+12039647165' 
                                  )  
                                                               
        else:
            print('Please match the syntax of the options listed!')
       
    else:
        print('Please match the syntax of the options listed! Remember the "-"!')      
        
        
        
#Second Function
def all_stops(time):  
    
    '''
    Takes in military time as string and shows all Eastbound and Westbound Green line 
    trains through Copley until inputted time
    '''
    
    print(isinstance(time,str))

    
    #Check for string
    if isinstance(time,str) != 'False':   
        
    #Create variable for current time
        now = datetime.now()
        now = now.strftime("%H:%M")   
        
    #Make sure time is beyond or equal to current time   
        if now<=time:

    #Call API
            response = requests.get('https://api-v3.mbta.com/predictions?filter[stop]=place-coecl')
            print('Response received')
    
    #Check for error within the call
            response.raise_for_status()
            print('No error')
    
    #Convert JSON into a dictionary for parsing
            y = json.loads(response.content)
            print('Json loaded into variable y \n')
    
    #Empty lists for appending
            arrivals = []
            lines = []
            skipped = 0
       
            for x in range(len(y['data'])):
      
    #Determine skipped stops
                if ((y['data'][x]['attributes']['schedule_relationship'] != 'SKIPPED') and
                    (y['data'][x]['attributes']['direction_id'] == 0) and 
                    (y["data"][x]['attributes']['arrival_time'][-14:-9])<time): #Set for Westbound
        
        
    #Classify as datetime object
                    military_time = y["data"][x]['attributes']['arrival_time'][-14:-9]
                    dt = datetime.strptime(military_time, "%H:%M")
        
    #Convert into standard time
                    standard_time = dt.strftime("%I:%M %p")
                    arrivals.append(standard_time)
        
    #Add variable to store line
                    line = y['data'][x]['relationships']['route']['data']['id']
                    lines.append(line)
      
    #Add details to the destination
                    if line == 'Green-B':
                        line += ' to Boston College'
                    elif line == 'Green-C':
                        line += ' to Cleveland Circle'
                    elif line == 'Green-D':
                        line += ' to Riverside'
                    else:
                        line += ' to Heath St'
            
                        print(lines[x], 'arrives at', arrivals[x], 'going Westbound')
        
            
        #Determine skipped stops
                elif ((y['data'][x]['attributes']['schedule_relationship'] != 'SKIPPED') and
                    (y['data'][x]['attributes']['direction_id'] == 1) and 
                    (y["data"][x]['attributes']['arrival_time'][-14:-9])<time): #Set for Eastbound
        
        #Store line data
                    line = y['data'][x]['relationships']['route']['data']['id']
        
        #Classify as datetime object
                    military_time = y["data"][x]['attributes']['arrival_time'][-14:-9]
                    dt = datetime.strptime(military_time, "%H:%M")
        
        #Convert into standard time
                    standard_time = dt.strftime("%I:%M %p")
                    arrivals.append(standard_time)
                
        #Add details to the destination
                    if line == 'Green-B':
                        line += ' to Boston College'
                    elif line == 'Green-C':
                        line += ' to Cleveland Circle'
                    elif line == 'Green-D':
                        line += ' to Riverside'
                    else:
                        line += ' to Heath St'
        
        #Add variable to store line
                    lines.append(line)
                    skipped += 1
                
                    print(lines[x], 'arrives at', arrivals[x], 'going Eastbound')

                else:
                    time = datetime.strptime(time, "%H:%M")
                    time = time.strftime("%I:%M %p")
                    print('No more trains before ', time)
                    break
        else:
            print('Please pick a time equal to or later than the current time')
    else:
        print('Please use military time (ex. 18:55 for 6:55pm) and input as a string')
