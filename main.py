from so import get_jobs as get_so_jobs
import indeed
from save import save_to_file

#stack_overflow
jobs = get_so_jobs()
save_to_file(jobs)

