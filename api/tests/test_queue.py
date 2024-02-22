from queue import Queue, Empty
from time import sleep
from threading import Thread


queueManager = Queue()

def do_task (task):
    print("doing task ",task["id"])
    print("task done ",task["id"])
    if task["test"] == "long":
        sleep(10)
        queueManager.task_done()
    else :
        sleep(2)
        queueManager.task_done()

def process_loop():
    while True:
        try:
            command = queueManager.get_nowait()
            do_task(command)
            
        except Empty :
            pass

#process_loop()
t1 = Thread(target=process_loop, daemon = True)
t1.start()


def test_queue_list ():
    queueManager.put_nowait({"id" : 5, "test" : "short"})
    assert queueManager.qsize() == 1

def test_queue_list_effectuation ():
    queueManager.put_nowait({"id" : 5, "test" : "short"})
    queueManager.put_nowait({"id" : 10, "test" : "short"})
    queueManager.put_nowait({"id" : 7, "test":"long"})
    sleep(6)
    assert queueManager.unfinished_tasks == 1

def test_queue_get_job ():
    queueManager.put_nowait({"id" : 7, "test":"long"})
    queueManager.put_nowait({"id" : 9, "test":"long"})
    found_item = [ item["id"] for item in queueManager.queue if item["id"] == 7 ]
    assert found_item[0] == 7

def test_queue_remove_job ():
    queueManager.put_nowait({"id" : 7, "test":"long"})
    queueManager.put_nowait({"id" : 9, "test":"long"})
    found_item = [ item["id"] for item in queueManager.queue if item["id"] == 7 ]
    queueManager.remove()
    assert found_item[0] == 7