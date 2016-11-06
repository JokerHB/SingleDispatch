from copy import deepcopy
import HeredityPart.Modules as hpm

def DoCorss(individualA, individualB, rate = 0.8):
    # seqA = deepcopy(individualA.sequence)
    # seqB = deepcopy(individualB.sequence)
    rate = rate
    pos = int(len(individualA.sequence) * rate)
    jobs = deepcopy(individualA.sequence)

    if pos == len(individualA.sequence):
        pos -= 1

    subA = hpm.getRange(individualA.sequence, 0, pos)
    _subA = hpm.getRange(individualA.sequence, pos, len(individualA.sequence))
    subB = hpm.getRange(individualB.sequence, 0, pos)
    _subB = hpm.getRange(individualB.sequence, pos, len(individualB.sequence))

    return (Check(individualA ,subA, _subB, deepcopy(jobs)), Check(individualB, subB, _subA, deepcopy(jobs)))

def Check(indi ,subA, _subA, jobs):
   """
   check and rebuild the sequence
   :param subA: first part of the sequence
   :param _subA: second part of the sequence
   :param jobs: whole jobs set
   :return: correct job sequence
   """
   ans = []
   for j in subA:
       if j in jobs:
           jobs.remove(j)
           ans.append(j)
   for j in _subA:
       if j in jobs:
           jobs.remove(j)
           ans.append(j)
   for _ in jobs:
       ans.append(_)
   indi.sequence = ans

   return indi