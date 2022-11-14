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


class JobQueue:
    def __init__(self, jobs):
        self.done_jobs: List[DoneJob] = []
        self.jobs: List[Job] = jobs
        self._q: List[Tuple[Tuple[int, int], Job]] = []
        self._t: int = 0

    def get_job(self) -> Job:
        return self.jobs.pop(0)

    def work(self, job: Job, day_time_left: int) -> Tuple[bool, int]:

        # decide if you have to wait
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
        if work_on_job_left < day_time_left:
            job.work_done += work_on_job_left
            self._t += work_on_job_left
            day_time_left -= work_on_job_left

            return True, day_time_left

        else:
            self._t += day_time_left
            job.work_done += day_time_left
            day_time_left -= day_time_left

            return False, day_time_left

    def main(self):
        job: Job = self.get_job()
        day_time_left = 8 * 60
        l: int = len(self.jobs)
        c = 0
        while len(self.done_jobs) != l + 1:
            c += 1
            if c > 10:
                break
            done_job, day_time_left = self.work(job, day_time_left)

            if done_job:
                self.done_jobs.append(DoneJob(job, self._t))

                if self.jobs:
                    job = self.get_job()
                else:

                    break

            if day_time_left < 0:
                raise Exception("Fak")

            if day_time_left <= 0:
                day_time_left = 8 * 60
                self._t += 24 * 60 - day_time_left

        return self.done_jobs


def main():
    data: List[Tuple[int, ...]] = [tuple([int(y) for y in x.split(" ", 1)]) for x in NormalAufgabe4.txt0.split("\n")]

    data = data[:1]

    jobs: List[Job] = [Job(x, y) for x, y in data]

    v1 = JobQueue(jobs).main()

    print(v1)


if __name__ == '__main__':
    main()
