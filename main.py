import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime



import time
timestamp = time.strftime('%H:%M:%S')
print('Current time:',timestamp)
hour = int(time.strftime('%H'))
if hour>=4 and hour<12:
  print('Good Morning')
elif hour>=12 and hour<16:
  print('Good Afternoon')
elif hour>16 and hour<20:
  print('Good Evening')
else:
  print('Good Night')