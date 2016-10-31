from copy import deepcopy

class Machine(object):
    def __init__(self, mN = 'machine'):
        self.currentTime = 0.
        self.name = mN

    def DoJob(self, job):
        if self.currentTime < job.releaseTime:
            self.currentTime = job.releaseTime
        self.currentTime += job.workTime
        return self.currentTime

    def ReSet(self):
        'init the machine, used for repeat'
        self.currentTime = 0.



class Job(object):
    def __init__(self, jN = 'job', rT=0.0, wT=0.0, fT=0.0):
        'job name, release time, working time, finish time'
        self.name = jN
        self.releaseTime = rT
        self.workTime = wT
        self.finishTime = fT

def cmp(a, b):
    # print a,b
    try:
        if a.delayTime < b.delayTime:
            return -1
        return 1
    except Exception,e:
        print 'error_cmp ' + str(a) + 'hhhh' + str(b)

def getRange(sets, start, end, step = 1):
    ans = []
    for i in range(start, end, step):
        try:
            ans.append(deepcopy(sets[i]))
        except Exception,e:
            print 'error_getRange ' + start + ' ' + end
    return ans