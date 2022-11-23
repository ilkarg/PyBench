from datetime import datetime

class PyBench:
    def run_benchmark(self, func):
        start_time = datetime.now()
        func()
        print(datetime.now() - start_time)