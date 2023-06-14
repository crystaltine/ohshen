##Logging library to record performance of the program
import time
import os
import sys
import datetime
import torch

class Log:
    m_GPU = False
    m_CPU = False
    m_GPU_Name = ""
    m_CPU_Name = ""
    m_GPU_Memory = 0
    m_Memory = 0
    m_Date = datetime.datetime.now()
    m_Time = time.time()

    m_logFile_Name = ""
    m_infoFile_Name = ""

    def __init__(self, directory, length: int, width: int):
        #Log hardware
        if torch.cuda.is_available():
            self.m_GPU = True
            self.m_GPU_Name = torch.cuda.get_device_name(0)
            self.m_GPU_Memory = torch.cuda.get_device_properties(0).total_memory
        else:
            self.m_CPU = True
            self.m_Device_Name = os.environ['COMPUTERNAME']
        
        ##Create log file
        self.m_logFile_Name = self.createIterativeFile(directory, "log", ".csv")
        self.m_logFile_Name.write("Time/Iteration, TempCalcIterTime(ns), ColorCalcIterTime(ns), TempCalcIterBest(ns), ColorCalcIterBest(ns), TempCalcIterWorst(ns), ColorCalcIterWorst(ns), TempCalcIterAvg(ns), ColorCalcIterAvg(ns)\n")
        self.m_logFile_Name.close()
        
        ##Create info file
        self.m_infoFile_Name = self.createIterativeFile(directory, "info", ".txt")
        self.m_infoFile_Name.write("Log File: " + str(self.m_logFile_Name) + "\n")
        self.m_infoFile_Name.write("Directory: " + str(directory) + "\n")
        self.m_infoFile_Name.write("Length: " + str(length) + "\n")
        self.m_infoFile_Name.write("Width: " + str(width) + "\n")
        
        for i in range(0, 30):
            self.m_infoFile_Name.write(".")
        self.m_infoFile_Name.write("\n")
        self.m_infoFile_Name.write("Date: " + str(self.m_Date) + "\n")
        self.m_infoFile_Name.write("Time: " + str(self.m_Time) + "\n")

        for i in range(0, 30):
            self.m_infoFile_Name.write(".")
        self.m_infoFile_Name.write("\n")
        self.m_infoFile_Name.write("GPU: " + str(self.m_GPU) + "\n")
        self.m_infoFile_Name.write("CPU: " + str(self.m_CPU) + "\n")
        self.m_infoFile_Name.write("GPU Name: " + str(self.m_GPU_Name) + "\n")
        self.m_infoFile_Name.write("Device Name: " + str(self.m_Device_Name) + "\n")
        self.m_infoFile_Name.write("GPU Memory: " + str(self.m_GPU_Memory) + "\n")
        self.m_infoFile_Name.write("Memory: " + str(self.m_Memory) + "\n")
        self.m_infoFile_Name.close()

        
        return
    
    def createIterativeFile(self, directory, basename, extension):
        file_iterator = 0
        while(os.path.exists(directory + basename + str(file_iterator) + extension)):
            file_iterator += 1
        return open(directory + basename + str(file_iterator) + extension, "w+")


        
        

        


