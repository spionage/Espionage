import platform
import subprocess
 
# getting the OS
osPlatform = platform.system()
 
if (osPlatform == "Linux"):
   # running the command using subProcess Module and process it into string
   Ubuntu_info = subprocess.check_output('sudo lshw -class disk', shell=True).decode('utf-8')
   # print(Ubuntu_info)
 
   f = open("hardDriveInfo.txt", "w")
   f.write("Hard Drive Info" + '/n' + Ubuntu_info)
   f.close()
  
elif (osPlatform == "Windows"):
   windows_info = subprocess.check_output(['powershell.exe','get-physicaldisk']).decode('utf-8')
   # print(windows_info)
   
   f = open("hardDriveInfo.txt", "w")
   f.write("Hard Drive Info" + windows_info)
   f.close()
 
else :
   print("os not ideal")

