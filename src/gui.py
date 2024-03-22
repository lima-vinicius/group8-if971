import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from graphics import generateHistogram, generateBoxplot, generateLineChart
from data_analysis import calculateMean, calculateMedian, calculateStandardDeviation, calculateMode, calculateVariance, calculateCoefficientOfVariation, calculateQuartiles, calculateKurtosis

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Análise de utilização da CPU")
        self.geometry("400x150")
        
        self.fileFrame = FileFrame(self)
        self.fileFrame.pack(fill="both", expand=True)
        
        self.optionsFrame = None
        self.resultsFrame = None

    def resizeWindow(self):
        self.geometry("800x550")
        self.optionsFrame = OptionsFrame(self)
        self.optionsFrame.pack(fill="both", expand=True)
        self.resultsFrame = ResultsFrame(self)
        self.resultsFrame.pack(fill="both", expand=True)

class FileFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.lblDescription = ttk.Label(self, text="Este programa realiza análise de dados de utilização da CPU durante a transcodificação de vídeo.")
        self.lblDescription.pack(pady=20)
        
        self.btnSelectFile = ttk.Button(self, text="Selecione o arquivo", command=self.readCpuData)
        self.btnSelectFile.pack(pady=10)
        
    def readCpuData(self):
        filename = filedialog.askopenfilename(title="Selecione o arquivo de dados", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'r') as file:
                cpuData = [float(line.strip()) for line in file]
            self.master.resizeWindow()
            self.master.optionsFrame.showOptions(cpuData)
            self.master.resultsFrame.displayResults(cpuData)

class OptionsFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.cpuData = None
        
        self.btnHistogram = ttk.Button(self, text="Gerar Histograma", command=self.generateHistogram)
        self.btnHistogram.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        
        self.btnBoxplot = ttk.Button(self, text="Gerar Boxplot", command=self.generateBoxplot)
        self.btnBoxplot.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
        
        self.btnLineChart = ttk.Button(self, text="Gerar Gráfico de Linhas", command=self.generateLineChart)
        self.btnLineChart.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")
        
        self.hideOptions()

    def showOptions(self, cpuData):
        self.cpuData = cpuData
        self.pack(fill="both", expand=True)

    def hideOptions(self):
        self.pack_forget()

    def generateHistogram(self):
        generateHistogram(self.cpuData)

    def generateBoxplot(self):
        generateBoxplot(self.cpuData)

    def generateLineChart(self):
        generateLineChart(self.cpuData)

    def displayResults(self):
        if self.cpuData:
            self.master.resultsFrame.displayResults(self.cpuData)
        else:
            messagebox.showwarning("Nenhum arquivo selecionado", "Por favor selecione um arquivo primeiro.")

class ResultsFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lblResults = tk.Text(self, width=95, height=15, font=("Arial", 14))
        self.lblResults.pack(pady=20)

    def displayResults(self, cpuData):
        mean = calculateMean(cpuData)
        median = calculateMedian(cpuData)
        mode = calculateMode(cpuData)
        standardDeviation = calculateStandardDeviation(cpuData)
        variance = calculateVariance(cpuData)
        coefficientOfVariation = calculateCoefficientOfVariation(cpuData)
        quartiles = calculateQuartiles(cpuData)
        kurtosis = calculateKurtosis(cpuData)

        message = "Resultados da análise estatística:\n"
        message += "-------------------------------------------\n"
        message += f"A média dos dados é: {mean:.2f}\n"
        message += f"A mediana dos dados é: {median:.2f}\n"
        message += f"A moda dos dados é: {mode[0]:.2f}\n"
        message += f"O desvio padrão dos dados é: {standardDeviation:.2f}\n"
        message += f"A variação dos dados é: {variance:.2f}\n"
        message += f"O coeficiente de variação dos dados é: {coefficientOfVariation:.2f}\n"
        message += f"O primeiro quartil dos dados é: {quartiles[0]:.2f}\n"
        message += f"O segundo quartil dos dados é: {quartiles[1]:.2f}\n"
        message += f"O terceiro quartil dos dados é: {quartiles[2]:.2f}\n"
        message += f"O quarto quartil dos dados é: {quartiles[3]:.2f}\n"
        message += f"A curtose dos dados é: {kurtosis:.2f}\n"

        self.lblResults.insert(tk.END, message)

if __name__ == "__main__":
    app = Gui()
    app.mainloop()
