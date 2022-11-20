from __future__ import annotations
from dataset import NormalAufgabe4
from typing import List, Tuple

debug = False

priority = 10  # if this value goes higher the avg gets lower but the max gets higher


# dataclass
class Job:
    def __init__(self, starttime: int, neededtime: int):
        self.starttime = starttime
        self.neededtime = neededtime

        self.work_done = 0
        self.prio = priority

    # for 3)
    def get_prio(self):
        self.prio += 1
        return self.neededtime / self.prio

    def __str__(self):
        return f"JOB[st{self.starttime}][ne{self.neededtime}][wd{self.work_done}]"

    def __repr__(self):
        return self.__str__()

# dataclass
class DoneJob:
    def __init__(self, job: Job, finish: int):
        self.job = job
        self.finish = finish

        self.wait = finish - job.starttime

    def __str__(self):
        return f"<[{self.job}] -> fn {self.finish} | qt {self.wait}>\n"

    def __repr__(self):
        return self.__str__()


# get avg and max values
def get_done_job_results(jobs: List[DoneJob]):
    waits = []
    for j in jobs:
        waits.append(j.finish - j.job.starttime)

    return sum(waits) // len(waits), max(waits)


class IncompleteInterfaceError(NotImplementedError):
    pass


# kinda like a abstract class where all tree solutions derive
# as the core process is the same
class JobQueue:
    working_times = 9 * 60, 17 * 60  # everything in minutes

    daily_work_duration = working_times[1] - working_times[0]

    def __init__(self, jobs):
        self.done_jobs: List[DoneJob] = []
        self.jobs: List[Job] = jobs
        self._q: List[Tuple[Tuple[int, int], Job]] = []
        self._t: int = 0

    # this has to be overloaded as it is the only difference in the code
    def get_job(self) -> Job:
        raise IncompleteInterfaceError

    # core function which handles if a day goes by or the job finishes with in the day
    def work(self, job: Job, day_time_left: int) -> Tuple[bool, int]:
        """
        :param job: the job to do the work on 
        :param day_time_left: this allows the work time to be in the 9-17 work time
        :return: whether job is finished | how much time is left in the work day
        """

        # decide if you have to wait, bc the task starting time is in the future
        if job.starttime > self._t:
            time_left_4_job = job.starttime - self._t

            # wait longer than today
            if time_left_4_job > day_time_left:
                self._t += day_time_left
                day_time_left -= day_time_left

                return False, day_time_left

            # start working today
            else:
                day_time_left -= time_left_4_job
                self._t += time_left_4_job

        work_on_job_left = job.neededtime - job.work_done
        # finish same day
        if work_on_job_left < day_time_left:
            job.work_done += work_on_job_left
            self._t += work_on_job_left
            day_time_left -= work_on_job_left

            return True, day_time_left

        # takes longer than current day
        else:
            self._t += day_time_left
            job.work_done += day_time_left
            day_time_left -= day_time_left

            return False, day_time_left

    # the main time loop, here the work() function gets called as often as it needs to
    def main(self):
        job: Job = self.get_job()
        day_time_left = self.daily_work_duration
        l: int = len(self.jobs)

        # main loop
        while len(self.done_jobs) != l + 1:  # wait until the whole queue has finished processing

            done_job, day_time_left = self.work(job, day_time_left)

            # process done job
            if done_job:
                self.done_jobs.append(DoneJob(job, self._t))

                # if there are still open jobs, get new
                if self.jobs:
                    job = self.get_job()
                else:
                    break

            # check if day passed, if so add the addition waiting time
            if day_time_left <= 0:
                day_time_left = self.daily_work_duration
                self._t += 24 * 60 - self.daily_work_duration

        return self.done_jobs

# 1)
class Verfahren1(JobQueue):
    def get_job(self) -> Job:
        return self.jobs.pop()

# 2)
class Verfahren2(JobQueue):
    # gets the
    def get_job(self) -> Job:
        time = self._t

        # get all wich you can start working now
        smallest: Job = self.jobs[-1]
        smallest_index: int = len(self.jobs) - 1
        avaliabe = []
        for i, j in enumerate(self.jobs):
            if j.starttime < smallest.starttime:
                smallest = j
                smallest_index = i

            if j.starttime < time:
                avaliabe.append((i, j))

        # if nothing avaliable get the one with shortest waiting time
        if not avaliabe:
            self.jobs.pop(smallest_index)
            return smallest

        # get the one wich hast the shortest processing time
        x, y = avaliabe[-1]
        smallest: Job = y
        smallest_index: int = x
        for i, j in avaliabe:
            if j.neededtime < smallest.neededtime:
                smallest = j
                smallest_index = i

        return self.jobs.pop(smallest_index)

# 3)
# this algo is similar to nr2 but it uses a combination of waiting time and task length
class Verfahren3(JobQueue):
    def get_job(self) -> Job:
        time = self._t

        # get all wich you can start working now
        smallest: Job = self.jobs[-1]
        smallest_index: int = len(self.jobs) - 1
        avaliabe = []
        for i, j in enumerate(self.jobs):
            if j.starttime < smallest.starttime:
                smallest = j
                smallest_index = i

            if j.starttime < time:
                avaliabe.append((i, j))

        # if nothing available get the one with shortest waiting time
        if not avaliabe:
            self.jobs.pop(smallest_index)
            return smallest

        # get the one which hast the lowest waiting to priority ratio
        # the ratio makes the algorithm occasionally pick the longer tasks which nr2 does not
        x, y = avaliabe[-1]
        smallest: Job = y
        smallest_index: int = x
        smallest_priority = smallest.get_prio()
        for i, j in avaliabe:
            pr = j.get_prio()
            if pr < smallest_priority:
                smallest = j
                smallest_index = i
                smallest_priority = pr

        return self.jobs.pop(smallest_index)


# benchmark task to show the algo improvements
def benchmark(meth, show_hrs = False):
    data: str = NormalAufgabe4.txt1
    data: List[Tuple[int, ...]] = [tuple([int(y) for y in x.split(" ", 1)]) for x in data.split("\n")]
    jobs: List[Job] = [Job(x, y) for x, y in data]

    m = meth(jobs)
    x = m.main()

    x = get_done_job_results(x)
    print(f"Name: {meth.__name__}")
    print(f"Avg m: {x[0]: <12} Max m: {x[1]: <12}")
    if show_hrs:
        print(f"Avg h: {str(divmod(x[0], 60)): <12} Max h: {str(divmod(x[1], 60)): <12}")
    print()


def main():
    benchmark(Verfahren1)
    benchmark(Verfahren2)
    benchmark(Verfahren3)

if __name__ == '__main__':
    main()
