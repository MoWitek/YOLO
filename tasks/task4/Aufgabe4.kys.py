from __future__ import annotations
from datasets import NormalAufgabe4
from typing import List, Tuple, Dict, Any

class Job:
    def __init__(self, starttime, neededtime):
        self.starttime = starttime
        self.neededtime = neededtime

        self.work_done = 0

    def __str__(self):
        return f"{self.starttime} -> {self.neededtime}"

    def __repr__(self):
        return self.__str__()


class DoneJob:
    def __init__(self, job: Job, finish):
        self.job = job
        self.finish = finish

    def __str__(self):
        return f"[{self.job}] -> {self.finish}"

    def __repr__(self):
        return self.__str__()

class Time:
    @classmethod
    def in_work_time(cls, time):
        h, m = divmod(time, 60)
        d, h2 = divmod(h, 24)
        return h2 * 60 in range(*JobThing.working_times)


"""
    def main(self):
        for j in self.jobs:
            
            print(self._time, j)
            self.do_job(j)
            
    def do_job(self, job: Job):
        if job.starttime > self._time:
            self._time = job.starttime
        self._time += job.neededtime

    def on_job_done(self):
        pass"""
class ForgorInterfaceError(NotImplementedError):
    pass

class JobThing:  # treat this as a abstract
    working_times = 9 * 60, 17 * 60  # everything in minutes
    daily_work_duration = working_times[1] - working_times[0]

    def __init__(self, jobs: List[Job]):
        self._time: int = 0
        self.jobs: List[Job] = jobs
        self.done_jobs: List[DoneJob] = []

    def main(self) -> List[DoneJob]:
        done: bool
        job = self.pick_new_job()
        while self.jobs:
            done = self.do_work_on_job(job)

            if done:
                self.done_jobs.append(DoneJob(job, self._time))
                job = self.pick_new_job()

        return self.done_jobs

    def pick_new_job(self) -> Job:
        raise ForgorInterfaceError

    def do_work_on_job(self, job: Job) -> bool:
        raise ForgorInterfaceError

class Verfahren1(JobThing):

    def pick_new_job(self):
        # always take first job
        return self.jobs.pop(0)

    def do_work_on_job(self, job: Job) -> bool:
        # wait until you can do the job
        if self._time < job.starttime:
            time_left_4_job = job.starttime - self._time
            if time_left_4_job > self.daily_work_duration:
                self._time += self.daily_work_duration
            else:
                self._time += time_left_4_job
            return False

        # cant finish job in working hours
        work_on_job_left = job.neededtime - job.work_done
        if work_on_job_left > self.daily_work_duration:

            job.work_done += self.daily_work_duration
            self._time += self.daily_work_duration

            # INSERT wait 24h delay sthst
            return False

        # can finish job in working hours
        else:

            job.work_done += work_on_job_left
            self._time += work_on_job_left
            return True

def get_done_job_results(jobs: List[DoneJob]):
    maks = 0
    total_wait = 0
    total_waits = 0

    for j in jobs:
        wait = j.finish - j.job.starttime
        total_waits += 1
        total_wait += wait

        if wait > maks:
            maks = wait

    return total_wait / total_waits, maks

def main():
    data: List[Tuple[int, ...]] = [tuple([int(y) for y in x.split(" ")]) for x in NormalAufgabe4.txt0.split("\n")]

    jobs: List[Job] = [Job(x, y) for x, y in data]

    j = Verfahren1(jobs)

    m = j.main()

    print(m)
    print(get_done_job_results(m))


# :TODO:
# detect when day passes

if __name__ == '__main__':
    main()

    # print(Time.in_work_time(539))
    # print(Time.in_work_time(540))
    # print(Time.in_work_time(1019))
    # print(Time.in_work_time(1020))