import HeredityPart.Corss as hpc
import HeredityPart.Individual as hpi
import HeredityPart.Modules as hpm
from copy import deepcopy
from random import choice

class Heredity(object):
    def __init__(self, jobs, mach,crossRate = 0.9, abnormalRate = 1.0, times = 10, indiNum = 100):
        """
        init the heredity algorithm
        :param jobs: whole job sequence
        :param mach: the match of job and machine
        :param crossRate: the rate of the cross operation
        :param abnormalRate: the rate of the abnormal operation
        :param times: the iter time
        :param indiNum: individual number
        """
        self.CRate = crossRate
        self.ARate = abnormalRate
        self.times = times
        self.indiNum = indiNum
        self.individuals = []

        self.randomInit(jobs, mach)

    def run(self):
        for i in range(self.times):
            # evaluate
            for id in self.individuals:
                try:
                    id.Evaluate()
                except Exception, e:
                    print 'error_run_23 ' + str(e)

            # cross and abnormal
            self.individuals.sort(cmp=hpm.cmp)
            pos = int(len(self.individuals) * self.CRate)

            if pos == len(self.individuals):
                pos -= 1

            if len(self.individuals) == 0:
                print 'error'

            _cross = hpm.getRange(self.individuals, 0, pos)
            _abnormal = hpm.getRange(self.individuals, pos, len(self.individuals))
            new_cross = []

            for j in range(0, len(_cross), 2):
                try:
                    if j == len(_cross) - 1:
                        a, b = hpc.DoCorss(_cross[j], _cross[j])
                        new_cross.append(a)
                        new_cross.append(b)
                        break
                    a,b = hpc.DoCorss(_cross[j], _cross[j + 1])
                    new_cross.append(a)
                    new_cross.append(b)
                except Exception,e:
                    print 'error_heredity_46 ' + str(e)

            for j in _abnormal:
                j.Abnormal(self.ARate)

            for _ in _abnormal:
                new_cross.append(_)

            self.individuals = new_cross

    def randomInit(self, job, match):
        for i in range(self.indiNum):
            _job = deepcopy(job)
            ranJob = []

            for __ in range(len(job)):
                ___ = choice(_job)
                ranJob.append(___)
                _job.remove(___)

            _ = hpi.Individual(job = deepcopy(ranJob), mach=deepcopy(match))
            self.individuals.append(_)

    def output(self):
        self.individuals.sort(cmp=hpm.cmp)
        self.individuals[0].display()

    def getBest(self):
        return self.individuals[0]
