from datetime import datetime

def benchmark(input_func):
	def output_func(*args):
		start_time = datetime.now()
		ret = input_func(*args)
		print(f'{input_func.__name__}: {datetime.now() - start_time}')
		return ret
	return output_func