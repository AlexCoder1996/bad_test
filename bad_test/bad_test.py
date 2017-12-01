import time
 
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec ".format(time.time() - self._startTime))

with Profiler() as p:
    file = open('10m.txt')
    text = file.read()
    array = text.split('\n')
    array.pop()
    #print(array)
    result = []
    for i in array:
        if i[0] == '-':
            result.append(0 - float(i[1:]))
        elif i:
            result.append(float(i))
    #print(result)        
    array_max = max(result)
    array_min = min(result)
    print("min = %s ,\
          max = %s" % (array_min, array_max))







