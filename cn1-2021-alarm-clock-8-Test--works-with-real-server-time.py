import datetime
import time

def checkAlarm(alarmSet, alarmTime):
  """checks if alarm is set and alarm time is reached

  :param alarmSet: true if the alarm is set to go off at specified time
  :type alarmSet: boolean

  :param alarmTime: the time when the alarm buzzer is to sound, e.g. 18:45
  :type alarmTime: string

  :returns: true if alarm is set and current time matches alarm time
  :rtype: boolean

  >>>checkAlarm(True, '7:00') # example based on current time of 7:00
  True
  >>>checkAlarm(False, '7:00') # example based on current time of 7:00
  False
  >>>checkAlarm(True, '7:05') # example based on current time of 7:00
  False
  >>>checkAlarm(False, '7:05') # example based on current time of 7:00
  False

  STRATEGY: Apply conditional if else statement and logical AND operator

  """
  x = datetime.datetime.now()
  currentTime = x.strftime("%H:%M")
  if alarmSet==True and alarmTime==currentTime:
    return True
  else:
    return False




# below example will check every 5 seconds for 16:10 alarm time
didAlarmGoOff = False
while didAlarmGoOff == False:
  if checkAlarm(True, '16:10') == True:
    print("Alarm Buzzer is sounding")
    didAlarmGoOff = True
  else:
    print("Alarm Buzzer is NOT sounding")
  time.sleep(5)





