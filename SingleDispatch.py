import HeredityPart.Individual as hpi
import HeredityPart.Corss as hpc
import HeredityPart.Modules as hpm
import HeredityPart.Heredity as hph
import datetime

j1 = hpm.Job(jN='J1', rT=0, wT=15, fT= 21)
j2 = hpm.Job(jN='J2', rT=0, wT=19, fT= 25)
j3 = hpm.Job(jN='J3', rT=0, wT=26, fT= 30)
j4 = hpm.Job(jN='J4', rT=0, wT=9, fT= 13)
j5 = hpm.Job(jN='J5', rT=15, wT=10, fT= 40)
j6 = hpm.Job(jN='J6', rT=15, wT=14, fT= 55)
j7 = hpm.Job(jN='J7', rT=24, wT=12, fT= 65)
j8 = hpm.Job(jN='J8', rT=34, wT=6, fT= 75)

m1 = hpm.Machine(mN='M1')

jobs = [j1, j2, j3, j4, j5, j6, j7, j8]
match = {j1.name:m1, j2.name:m1, j3.name:m1, j4.name:m1, j5.name:m1, j6.name:m1, j7.name:m1, j8.name:m1}
counter = 0
best = None
if __name__ == '__main__':
    while(True):
        heredity = hph.Heredity(jobs, match, times=10, indiNum=100)
        heredity.run()
        _ = heredity.getBest()
        if best == None or best.delayTime > _.delayTime:
            best = _
            with open('./sequence.txt', 'a+') as f:
                f.write('\n---------- %d ----------\n' % (counter))
                str_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n'
                f.write(str_date)
                f.write(best.toString())
            counter += 1

