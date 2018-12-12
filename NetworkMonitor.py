import subprocess
from datetime import datetime

def check_ping():
  hostname = '8.8.8.8'
  p = subprocess.Popen(["ping.exe",hostname,'-n','1'], stdout = subprocess.PIPE)
  com = p.communicate()[0]
  
  #Retorna 'received' e 'average time'
  if int(com.split(',')[1].split('=')[1]) == 1:
    return com.split(',')[1].split('=')[1], com.split(',')[5].split('=')[1].split('m')[0]
  else:
    return com.split(',')[1].split('=')[1], 0

if __name__ == '__main__':
  filename = "output.csv"
  file = open(filename,"a")
  previous = datetime.now()
  previousMinute = previous.minute - 1
  netWorking = 0
  netFailed = 0
  averageTime = 0
  while(True):
    now = datetime.now()
    ping = check_ping()
    print ping
    if now.minute == previous.minute:
      if int(ping[0]) == 0:
        netFailed += 1
      else:
        netWorking += 1
      averageTime += int(ping[1])
    else:
      print "Escrito!"
      if netWorking>0:
        averageTime = averageTime/netWorking
      print "Tempo medio: " + str(averageTime)
      print "Bons: " + str(netWorking)
      print "Ruins: " + str(netFailed)
      file.write(str(previous.month) + "," + str(previous.day) + "," + str(previous.hour) + "," + str(previous.minute) + "," + str(averageTime) + "," + str(netWorking) + "," + str(netFailed) + "\n" )
      previous = now
      netWorking = 0
      netFailed = 0
      averageTime = 0
  file.close()
