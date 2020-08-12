hour = 6

minutes = 52

mins_tot = (8 * 2) + (7 * 3) #total minutes of the 5 laps (37 minutes)

sec_tot = ((15 * 2) + (12 * 3)) // 60 #total seconds of the 5 laps converted to minutes = 1 minute (rounded value)

#print (hour, minutes, mins_tot, sec_tot) #delete "#" from "#print" in order to see the values

arrival = hour + ((minutes + (mins_tot + sec_tot)) / 60) #the result is 7.5 meaning 7:30 am (the mathematical operation doesn't know it's about time in order to show the minutes) 

print ('You will arrive at:', arrival, 'am', '(7:30 am)')