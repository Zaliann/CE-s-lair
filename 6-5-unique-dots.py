import time


current_time = time.time()
print(time.strftime("%d.%m.%Y %H:%M", time.localtime()))
print(current_time)
f = open("input.txt", 'r')
r, x, y = [int(x) for x in f.read().split()]
if r == 1:
    f.write(str(1 + 4) + '\n')
else:
    f.write(str((r + 1) * (r + 1) + 4) + '\n')
f.write(str(time.time() - current_time))
f.close()


