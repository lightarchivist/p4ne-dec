from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
import time

# a task has task: Task as the first parameter
def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"\nFrom inside the task {task.host.name} says hello world!\n"
    )


def say(task: Task, text: str) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says {text}"
    )

# the config_file is optional but you would have to throw in
# the runner and inventory parameters instead, add dry_run=True to simulate changes
# my_nornir = InitNornir(config_file = "config.yaml")
my_nornir = InitNornir(config_file="./inventory/rtrs-cisco-simple/config.yaml")
# result is a dictionary like object
result = my_nornir.run(task=hello_world)
print('\nHere is the result of task 1 - hello world:')
print_result(result)

result = my_nornir.run(
    #  this name can be seen in the screen output
    name="Saying goodbye in a very friendly manner",
    # task to run
    task=say,
    # argument
    text="buhbye!"
)
print('\nHere is the result of task 2 - say:')
print_result(result)
