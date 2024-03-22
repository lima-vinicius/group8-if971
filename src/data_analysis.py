import numpy as np
import scipy.stats as stats

def calculateMean(data):
    if data:
        return np.mean(data)
    return None

def calculateMedian(data):
    if data:
        return np.median(data)
    return None

def calculateStandardDeviation(data):
    if data:
        return np.std(data)
    return None

def calculateMode(data):
    if data:
        return stats.mode(data)
    return None

def calculateVariance(data):
    if data:
        return np.var(data)
    return None

def calculateCoefficientOfVariation(data):
    if data:
        return stats.variation(data)
    return None

def calculateQuartiles(data):
    if data:
        return np.percentile(data, [25, 50, 75, 100])
    return [None] * 4

def calculateKurtosis(data):
    if data:
        return stats.kurtosis(data)
    return None

