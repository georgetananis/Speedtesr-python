# go to cmd and write pip install speedtest-cli
import speedtest
s = speedtest.Speedtest()
d = s.download()
u = s.upload()
print("Running SpeedTest")
print(d/1000000)
print(u/1000000)