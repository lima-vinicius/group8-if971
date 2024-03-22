from tkinter import filedialog, messagebox
import file_handling

class FileFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.lblDescription = ttk.Label(self, text="Este programa realiza análise de dados de utilização da CPU durante a transcodificação de vídeo.")
        self.lblDescription.pack(pady=20)
        
        self.btnSelectFile = ttk.Button(self, text="Selecione o arquivo", command=self.readCpuData)
        self.btnSelectFile.pack(pady=10)
        
    def readCpuData(self):
        cpuData = file_handling.readCpuData()
        if cpuData:
            self.master.optionsFrame.showOptions(cpuData)
