import time

SECONDS_PER_DAY = 24 * 60 * 60


def doFunc():
    print "do Function..."


def doFirst():
    from datetime import datetime, timedelta
    curTime = datetime.now()
    desTime = curTime.replace(hour=10, minute=0, second=0, microsecond=0)
    delta = curTime - desTime
    skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    print "Must sleep %d h" % (int(skipSeconds) / (60 * 60))
    sleep(skipSeconds)
    doFunc()
if __name__ == '__main__':
    doFirst()
