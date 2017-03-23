# coding: utf-8
import os


class Machine(object):
    """docstring for ClassName"""

    def __init__(self):
        # cpu informatiom
        self.cpu_temp = self.getcputemperature()
        self.cpu_usage = self.getcpuuse()
        # ram information
        # Output is in kb, here I convert it in Mb for readability
        self.ram_stats = self.getraminfo()
        self.ram_total = round(int(self.ram_stats[0]) / 1000, 1)
        self.ram_used = round(int(self.ram_stats[1]) / 1000, 1)
        self.ram_free = round(int(self.ram_stats[2]) / 1000, 1)
        self.fast_data = self.fast_reply()

    def fast_reply(self):

        return [
            {
                'CPU Temperature = ' + self.cpu_temp + '\n',
                'CPU Use =' + self.cpu_usage + '\n',
                'RAM Total = ' + str(self.ram_stats) + ' MB\n'
            }
            # add more ...
        ]

    # Return cpu temperature as a character string
    def getcputemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return(res.replace("temp=", "").replace("'C\n", ""))

    # Return ram information (unit=kb) in a list
    # Index 0: total ram
    # Index 1: used ram
    # Index 2: free ram
    def getraminfo(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i == 2:
                return(line.split()[1:4])

    # Return % of cpu used by user as a character string
    def getcpuuse(self):
        return(str(os.popen("top -n1 | awk '/cpu\(s\):/ {print $2}'").readline().strip()))

    # Return information about disk space as a list (unit included)
    # Index 0: total disk space
    # Index 1: used disk space
    # Index 2: remaining disk space
    # Index 3: percentage of disk used
    def getDiskSpace(self):
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i == 2:
                DISK_stats = (line.split()[1:5])
                return DISK_stats[0], DISK_stats[1], DISK_stats[3]


if __name__ == '__main__':
    mac = Machine()
    print mac.ram_stats
