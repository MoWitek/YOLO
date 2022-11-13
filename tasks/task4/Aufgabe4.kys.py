from __future__ import annotations
from datasets import NormalAufgabe4
from typing import List, Tuple, Dict, Any

class Job:
    def __init__(self, starttime, neededtime):
        self.starttime = starttime
        self.neededtime = neededtime

        self.work_done = 0

    def __str__(self):
        return f"JOB[st{self.starttime}][ne{self.neededtime}][wd{self.work_done}]"

    def __repr__(self):
        return self.__str__()

class EmptyJob(Job):
    def __init__(self):
        super().__init__(0, 0)

class DoneJob:
    def __init__(self, job: Job, finish):
        self.job = job
        self.finish = finish

        self.wait = finish - job.starttime

    def __str__(self):
        return f"<[{self.job}] -> fn {self.finish} | qt {self.wait}>\n"

    def __repr__(self):
        return self.__str__()

class EmptyDoneJob(DoneJob):
    def __init__(self):
        super().__init__(EmptyJob(), 0)

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
        done: bool = True
        job: Job = EmptyJob()
        while self.jobs:
            if done:
                self.done_jobs.append(DoneJob(job, self._time))
                job = self.pick_new_job()

            done = self.do_work_on_job(job)

        while not done:
            done = self.do_work_on_job(job)

        self.done_jobs.append(DoneJob(job, self._time))

        return self.done_jobs[1:]

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
        if self._time <= job.starttime:
            time_left_4_job = job.starttime - self._time

            # wait for next day
            if time_left_4_job >= self.daily_work_duration:
                self._time += self.daily_work_duration
                return False
            # if will be able to start working today
            else:
                self._time += time_left_4_job


        # cant finish job in working hours
        work_on_job_left = job.neededtime - job.work_done
        if work_on_job_left >= self.daily_work_duration:

            job.work_done += self.daily_work_duration
            self._time += self.daily_work_duration

            # INSERT wait 24h delay sthst
            self._time += 24 * 60 - self.daily_work_duration
            return False

        # can finish job in working hours
        else:

            job.work_done += work_on_job_left
            self._time += work_on_job_left
            return True  # job done


def get_done_job_results(jobs: List[DoneJob]):
    waits = []
    for j in jobs:
        waits.append(j.finish - j.job.starttime)

    return sum(waits) / len(waits), max(waits)


def main():
    data: List[Tuple[int, ...]] = [tuple([int(y) for y in x.split(" ", 1)]) for x in NormalAufgabe4.txt0.split("\n")]

    data = data[:5]

    jobs: List[Job] = [Job(x, y) for x, y in data]

    j = Verfahren1(jobs)

    m = j.main()

    print(m)
    print()
    print(get_done_job_results(m))


if __name__ == '__main__':
    main()

    # print(Time.in_work_time(539))
    # print(Time.in_work_time(540))
    # print(Time.in_work_time(1019))
    # print(Time.in_work_time(1020))
