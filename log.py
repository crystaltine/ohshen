##Logging library to record performance of the program
import time
import os
import sys
import datetime
import torch
from timing import Timer

#Creates a file name string for the log file   
class IterativeFile:
    m_FileName = ""
    def __init__(self, directory, basename, extension):
        #check if the directory exists, if not, create it
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_iterator = 0
        while(os.path.exists(directory + basename + str(file_iterator) + extension)):
            file_iterator += 1
        self.m_FileName = directory + basename + str(file_iterator) + extension
        
    def getFileName(self):
        return self.m_FileName

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

    def __init__(self, directory, length: int, width: int, gif_hex: str):
        #Log hardware
        if torch.cuda.is_available():
            self.m_GPU = True
            self.m_GPU_Name = torch.cuda.get_device_name(0)
            self.m_GPU_Memory = torch.cuda.get_device_properties(0).total_memory
        else:
            self.m_CPU = True
            self.m_Device_Name = os.environ['COMPUTERNAME']
        
        ##Create log file
        LogFS = IterativeFile(directory, "log", ".csv")

        self.m_logFile_Name = open(LogFS.getFileName(), "w+")
        self.m_logFile_Name.write("Time/Iteration, TempCalcIterTime(us), ColorCalcIterTime(us), TempCalcIterBest(us), ColorCalcIterBest(us), TempCalcIterWorst(us), ColorCalcIterWorst(us), TempCalcIterAvg(us), ColorCalcIterAvg(us)\n")
        self.m_logFile_Name.close()
        
        ##Create info file
        InfoFS = IterativeFile(directory, "info", ".txt")

        self.m_infoFile_Name = open(InfoFS.getFileName(), "w+")
        self.m_infoFile_Name.write("Log File: " + str(self.m_logFile_Name) + "\n")
        
        self.m_infoFile_Name.write("Gif File: " + str(gif_hex) + "\n")
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

        self.m_logFile_Name = open(self.m_logFile_Name.name, "a+") #Reopen log file in append mode. Ready for logging

        return


    def log(self, AvgTimer, ColorTimer, iteration):
        #Open log file
        #Write to log file
        
        self.m_logFile_Name.write(str(iteration) + ",")
        self.m_logFile_Name.write(str(AvgTimer.m_Time) + ",")
        self.m_logFile_Name.write(str(ColorTimer.m_Time) + ",")
        self.m_logFile_Name.write(str(AvgTimer.m_BestTime) + ",")
        self.m_logFile_Name.write(str(ColorTimer.m_BestTime) + ",")
        self.m_logFile_Name.write(str(AvgTimer.m_WorstTime) + ",")
        self.m_logFile_Name.write(str(ColorTimer.m_WorstTime) + ",")
        self.m_logFile_Name.write(str(AvgTimer.m_AverageTime) + ",")
        self.m_logFile_Name.write(str(ColorTimer.m_AverageTime) + "\n")
        

        #NEW: write to log file without converting to a string








        
        

        


