import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

def func1():
	for i in range(0,500):
		print("hello1")
def func2():
	for i in range(0,50000):
		print("hello2")
def func3():
	for i in range(0,500000):
		print("hello3")


func1()
func1()
func1()
func2()
func1()
func3()
func1()

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())