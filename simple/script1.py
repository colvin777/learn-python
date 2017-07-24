import sys

print(str(5/3))
import time

start = time.time(
				)
print(sys.platform)
print(2 ** 8)
x = 'Spam!'
print(x * 8)
hao = 'wei'
print(hao)
def test():
	print('only test')
end = time.time()

print('this is %d' % float((end-start)/60))
print('this is {0}'.format(str(int((end-start)/60))))