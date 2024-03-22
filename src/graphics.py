import matplotlib.pyplot as plt
from tkinter import messagebox

def generateHistogram(cpuData):
    if cpuData:
        plt.figure(figsize=(8, 6))
        plt.hist(cpuData, bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Porcentagem de utilização da CPU (%)')
        plt.ylabel('Frequência')
        plt.title('Histograma de utilização da CPU')
        plt.grid(True)
        plt.show()
    else:
        messagebox.showwarning("Nenhum arquivo selecionado", "Por favor selecione um arquivo primeiro.")

def generateBoxplot(cpuData):
    if cpuData:
        plt.figure(figsize=(8, 6))
        plt.boxplot(cpuData)
        plt.xlabel('Porcentagem de utilização da CPU (%)')
        plt.title('Boxplot de utilização da CPU')
        plt.grid(True)
        plt.show()
    else:
        messagebox.showwarning("Nenhum arquivo selecionado", "Por favor selecione um arquivo primeiro.")

def generateLineChart(cpuData):
    if cpuData:
        plt.figure(figsize=(8, 6))
        plt.plot(cpuData, marker='o', linestyle='-')
        plt.xlabel('Amostra')
        plt.ylabel('Porcentagem de utilização da CPU (%)')
        plt.title('Tendência de utilização da CPU')
        plt.grid(True)
        plt.show()
    else:
        messagebox.showwarning("Nenhum arquivo selecionado", "Por favor selecione um arquivo primeiro.")
