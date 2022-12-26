from datetime import datetime
import os.path

def benchmark(logging):
    if not type(logging) == bool:
        raise TypeError('Аргумент должен иметь тип boolean')
    def benchmark_without_logs(input_func):
        def func(*args):
            start_time = datetime.now()
            ret = input_func(*args)
            print(f'{input_func.__name__}: {datetime.now() - start_time}')
            return ret
        return func
    def benchmark_with_logs(input_func):
        def func(*args):
            start_time = datetime.now()
            ret = input_func(*args)
            if not os.path.exists('PyBench'):
                os.mkdir('PyBench')
            with open('PyBench/benchmark.pybench', 'a') as file:
                file.write(f'{input_func.__name__}: {datetime.now() - start_time}\n')
            return ret
        return func
    if not logging:
        return benchmark_without_logs
    else:
        return benchmark_with_logs