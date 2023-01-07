Dim WinScriptHost, cmd
Set WinScriptHost = CreateObject("WScript.Shell")

usr = CreateObject("WScript.Network").UserName
'WinScriptHost.CurrentDirectory = "C:\Users\" + usr + "\source" 'python script path
cmd = "c:\Users\" + usr + "\AppData\Local\Microsoft\WindowsApps\python3.10.exe battery-plug.py"
WinScriptHost.Run cmd, 0
Set WinScriptHost = Nothing