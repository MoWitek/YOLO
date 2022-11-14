from __future__ import annotations
from datasets import NormalAufgabe4
from typing import List, Tuple, Dict, Any

debug = False


class Job:
    def __init__(self, starttime, neededtime):
        self.starttime = starttime
        self.neededtime = neededtime

        self.work_done = 0
        self.prio = 1

    def get_prio(self):
        x = self.prio
        self.prio += 1
        return self.neededtime / self.prio

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

def get_done_job_results(jobs: List[DoneJob]):
    waits = []
    for j in jobs:
        waits.append(j.finish - j.job.starttime)

    return sum(waits) // len(waits), max(waits)

class IncompleteInterfaceError(NotImplementedError):
    pass

class JobQueue:
    working_times = 9 * 60, 17 * 60  # everything in minutes

    starting_offset = working_times[0]
    daily_work_duration = working_times[1] - working_times[0]
    def __init__(self, jobs):
        self.done_jobs: List[DoneJob] = []
        self.jobs: List[Job] = jobs
        self._q: List[Tuple[Tuple[int, int], Job]] = []
        self._t: int = 0

    def get_job(self) -> Job:
        raise IncompleteInterfaceError

    def work(self, job: Job, day_time_left: int) -> Tuple[bool, int]:

        # decide if you have to wait
        if job.starttime > self._t:
            time_left_4_job = job.starttime - self._t

            # wait longer than today
            if time_left_4_job > day_time_left:
                print("waiting", day_time_left, self._t) if debug else None
                self._t += day_time_left
                day_time_left -= day_time_left

                return False, day_time_left

            # start working today
            else:
                print("waited but now working", time_left_4_job, self._t) if debug else None
                day_time_left -= time_left_4_job
                self._t += time_left_4_job


        work_on_job_left = job.neededtime - job.work_done
        # same day
        if work_on_job_left < day_time_left:
            job.work_done += work_on_job_left
            print("did work", work_on_job_left, self._t) if debug else None
            self._t += work_on_job_left
            day_time_left -= work_on_job_left

            return True, day_time_left

        # multi day
        else:
            print("did work24", day_time_left, self._t) if debug else None
            self._t += day_time_left
            job.work_done += day_time_left
            day_time_left -= day_time_left

            return False, day_time_left

    def main(self):
        job: Job = self.get_job()
        day_time_left = self.daily_work_duration
        l: int = len(self.jobs)

        while len(self.done_jobs) != l + 1:

            done_job, day_time_left = self.work(job, day_time_left)

            if done_job:
                self.done_jobs.append(DoneJob(job, self._t))

                if self.jobs:
                    job = self.get_job()
                    print("new job", job) if debug else None
                else:

                    break

            if day_time_left < 0:
                raise Exception("Fak")

            if day_time_left <= 0:
                day_time_left = self.daily_work_duration
                self._t += 24 * 60 - self.daily_work_duration

        return self.done_jobs

class Verfahren1(JobQueue):
    def get_job(self) -> Job:
        return self.jobs.pop()

class Verfahren2(JobQueue):
    def get_job(self) -> Job:
        time = self._t

        sm: Job = self.jobs[-1]
        smi: int = len(self.jobs) - 1
        avaliabe = []
        for i, j in enumerate(self.jobs):
            if j.starttime < sm.starttime:
                sm = j
                smi = i

            if j.starttime < time:
                avaliabe.append((i, j))

        if not avaliabe:
            self.jobs.pop(smi)
            return sm

        x, y = avaliabe[-1]
        sm: Job = y
        smi: int = x
        for i, j in avaliabe:
            if j.neededtime < sm.neededtime:
                sm = j
                smi = i

        return self.jobs.pop(smi)

class Verfahren3(JobQueue):
    def get_job(self) -> Job:
        time = self._t

        sm: Job = self.jobs[-1]
        smi: int = len(self.jobs) - 1
        avaliabe = []
        for i, j in enumerate(self.jobs):
            if j.starttime < sm.starttime:
                sm = j
                smi = i

            if j.starttime < time:
                avaliabe.append((i, j))

        if not avaliabe:
            self.jobs.pop(smi)
            return sm

        x, y = avaliabe[-1]
        sm: Job = y
        smi: int = x
        smpr = sm.get_prio()
        for i, j in avaliabe:
            pr = j.get_prio()
            if pr < smpr:
                sm = j
                smi = i
                smpr = pr

        return self.jobs.pop(smi)

def benchmark(meth):
    data: List[Tuple[int, ...]] = [tuple([int(y) for y in x.split(" ", 1)]) for x in NormalAufgabe4.txt1.split("\n")]
    data = data[:]
    jobs: List[Job] = [Job(x, y) for x, y in data]

    m = meth(jobs)
    x = m.main()

    x = get_done_job_results(x)
    print(f"Name: {meth.__name__}")
    print(f"Avg m: {x[0]: <12} Max m: {x[1]: <12}")
    print(f"Avg h: {str(divmod(x[0], 60)): <12} Max h: {str(divmod(x[1], 60)): <12}")
    print()

def main():

    benchmark(Verfahren1)
    benchmark(Verfahren2)
    benchmark(Verfahren3)

if __name__ == '__main__':
    main()
