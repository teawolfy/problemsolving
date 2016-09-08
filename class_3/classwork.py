import time
time_sec = time.time()
date = int(time_sec)
days = date // 3600 // 24

midnight = days * 24 * 3600
mid_seconds = time_sec - midnight

hours = mid_seconds // 3600
minutes = (mid_seconds - (hours * 3600)) // 60
seconds = int(mid_seconds - (hours * 3600 + minutes * 60))

current_time = 'Time: %s:%s:%s, %s days since the epoch' % (hours, minutes, seconds, days)

print(current_time)
