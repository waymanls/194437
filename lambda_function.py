import json
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
times = ['morning', 'afternoon', 'evening', 'night', 'day']

def lambda_handler(event, context):
 name = event.get(name, "you")
 city = event.get(city, "world")
 try:
   if (times.index(event.get(time, None))) >-1:
     time = event.get(time)
 except ValueError:
   time = day
 try:
   if (days.index(event.get(day,None))) >-1:
     day = event['day']
 except ValueError:
   day = None
 greetings = "Good {time}, {name} of {city}! .format(time=time, name=name, city=city)
 if day:
   greetings += "Happy {}".format(day)
 return {
   'statusCode': 200,
   'body': json.dumps(greetings)
 }
