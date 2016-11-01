import random
from copy import deepcopy

class Individual(object):
    def __init__(self, job, mach):
        """
        init the class
        :param job: list, the job need to be finished
        :param mach: dict, the match of job and machine
        """
        self.sequence = deepcopy(job)
        self.matchMachine = deepcopy(mach)

        self.delayTime = 0.

    def Evaluate(self):
        self.delayTime = 0.
        for j in self.sequence:
            try:
                m = self.matchMachine[j.name]
            except Exception,e:
                print 'error_evaluate_22 ' + str(j)
            m.DoJob(j)
            self.delayTime += max(0., m.currentTime - j.finishTime)

        for key in self.matchMachine:
            self.matchMachine[key].ReSet()

    def Abnormal(self, rate):
        if random.random() <= rate:
            jobs = deepcopy(self.sequence)
            jobNumber = len(jobs)
            for i in range(jobNumber):
                _ = random.choice(jobs)
                self.sequence[i] = deepcopy(_)
                jobs.remove(_)

    def display(self):
        for j in self.sequence:
            print j.name + ' ' + self.matchMachine[j.name].name
        print self.delayTime

    def toString(self):
        _ = ''
        for j in self.sequence:
            _ += j.name + ' ' + self.matchMachine[j.name].name + '\n'
        _ += str(self.delayTime)
        return _