# "If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?
#  What is your average speed in miles per hour?"

km_to_m  = 10 / 1.61

tot_min = 42 / km_to_m #for a rounded number put // instead of /

tot_sec = 42 / km_to_m #for a rounded number put // instead of /

tot_time = (42 * 60 + 42) / 60

avg_spd_m_h = km_to_m * 60 / tot_time #for a rounded number put // instead of /

print('Your time per mile is:', tot_min, 'minutes', tot_sec, 'seconds')

print('Your average speed in miles per hour is:', avg_spd_m_h)
