from tkinter import Frame
import psutil, variables
from ctypes import *
from ctypes.wintypes import BOOL
import win32con  # from pywin32

global canReadAddres
canReadAddress = Frame        # slight mod to the code just to add this. 


def get_pid(process_name):
    for process in psutil.process_iter():
        if process_name in process.name():
            return process.pid
    return None


class ProcessInterface(object):
    def __init__(self):
        self.h_process = None
        self.pid = None

    def isGameOpen(self, name):
        pid = get_pid(name)
        if pid is None:
            return False
        else:
            return True

    def open(self, name):
        pid = get_pid(name)
        if pid is None:
            raise RuntimeError(f'Could not find a process name containing "{name}"')
        self.pid = pid
        self._get_handle(self.pid)

    def close(self, code=0):
        windll.kernel32.TerminateProcess(self.h_process, code)
        windll.kernel32.CloseHandle(self.h_process)

    def _get_handle(self, pid):
        self.h_process = windll.kernel32.OpenProcess(
            win32con.PROCESS_VM_READ | win32con.PROCESS_VM_WRITE | win32con.PROCESS_ALL_ACCESS | win32con.DEBUG_PROCESS,
            False, pid)
        if self.h_process:
            pass
            print("Success: Got Handle - PID:", self.pid)
        else:
            print("Failed: Get Handle - Error code: ", windll.kernel32.GetLastError())
            windll.kernel32.SetLastError(10000)

    def read_memory(self, address, buffer_size=4):
        global canReadAddress
        buf = create_string_buffer(buffer_size)
        bytes_read = c_ulong(0)
        if windll.kernel32.ReadProcessMemory(self.h_process, address, buf, buffer_size, byref(bytes_read)):
            canReadAddress = True
            variables.lookForGame = False  # check gameReconnect() in DarkSoulsDeathCount.py
            return buf
        else:
            canReadAddress = False
            variables.lookForGame = True
            print("Failed: Read Memory - Error Code: ", windll.kernel32.GetLastError()) 
            windll.kernel32.CloseHandle(self.h_process)
            windll.kernel32.SetLastError(10000)

    def write_memory(self, address, data, length=4):
        count = c_ulong(0)

        c_int(0)
        if not windll.kernel32.WriteProcessMemory(self.h_process, address, byref(data), length, byref(count)):
            print("Failed: Write Memory - Error Code: ", FormatError(windll.kernel32.GetLastError()))
            windll.kernel32.SetLastError(10000)
        else:
            return False

    def read_memorycheck(self, address, buffer_size=4):
        buf = create_string_buffer(buffer_size)
        bytes_read = c_ulong(0)
        if windll.kernel32.ReadProcessMemory(self.h_process, address, buf, buffer_size, byref(bytes_read)):
            return True
        else:
            print("Failed: Read Memory - Error Code: ", windll.kernel32.GetLastError())
            windll.kernel32.CloseHandle(self.h_process)
            windll.kernel32.SetLastError(10000)
            return False
