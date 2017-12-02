import time
import statistics
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec ".format(time.time() - self._startTime))

with Profiler() as p:
    array = open('10m.txt').read().split('\n')
    array.pop()
    floats = [float(x) for x in array]
    print("max = %s\nmin = %s\nmediana = %s\naverage = %s"
          % (max(floats), min(floats), statistics.median(floats), statistics.mean(floats)) )
   





