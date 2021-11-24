def checkAlarm(alarmSet, alarmTime):
  """checks if alarm is set and alarm time is reached

  :param alarmSet: true if the alarm is set to go off at specified time
  :type alarmSet: boolean

  :param alarmTime: the time when the alarm buzzer is to sound, e.g. 18:45
  :type alarmTime: string

  :returns: true if alarm is set and current time matches alarm time
  :rtype: boolean

  examples are baes on current time of 7:00
  >>>checkAlarm(True, '7:00')
  True
  >>>checkAlarm(False, '7:00')
  False
  >>>checkAlarm(True, '7:05')
  False
  >>>checkAlarm(False, '7:05')
  False

  STRATEGY: Apply conditional if else statement and logical AND operator

  """

