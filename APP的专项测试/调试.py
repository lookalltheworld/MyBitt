import os

#cmd='adb shell am start -W -n com.vodqareactnative/.MainActivity'
#result=os.popen(cmd)
#res = result.readlines()
#print (res)
#for line in res:  # 循环输出list的每一项
#
#    if 'ThisTime' in line:
#        startTime = line.split(':')[1]
#        print(startTime)
#        break
#
#print (type(res))
#cmd = 'adb shell am force-stop com.vodqareactnative'
#os.popen(cmd)
result = os.popen("adb shell dumpsys battery")
print(result)
for line in result:
    print(line)
