import os
import time
import sys
import subprocess
import imp
import unicornhat

def run(job):
    started = False
    command = 'python {0}'.format(job)
    process = None
    while True:
        if not started:
            process = (subprocess.Popen(command.split(), stdout=subprocess.PIPE))
            print("created unicorn {0}".format(job))
            started = True
        else:
            runtime_seconds=10
            t_end = time.time() + runtime_seconds
            while time.time() < t_end:
                pass
            process.terminate()
            unicornhat.off()
            return


def unicorn_up():
    blacklist_examples=["/simple.py", "/detect.py", "/test_rotation.py", "/toggle.py", "/show_png.py"]
    path = '/home/pi/Pimoroni/unicornhat/examples'
    files = []
    print("gathering files")
    for root, directory, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))    
    
    for f in files:
        print("{0} LOADED".format(f))
    while True:
        for job in files:
            if any(blacklist_examples) in job:
                continue
            run(job)


if __name__ == "__main__":
    try:
        unicorn_up()
    finally:
        unicornhat.off()
