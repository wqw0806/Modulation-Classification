import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pimg
import seaborn as sns
import scipy.io
import os

# Importing Data for all SNR Ratio's
def ImportData(Path):
	ModulationSchemes = os.listdir(Path)

	Dataset = {}
	for scheme in ModulationSchemes:
		DataPath = Path + "/" + scheme
		files = os.listdir(DataPath)
		DataofScheme = {}
		for f in files:
			Data = scipy.io.loadmat(DataPath + "/" + f)
			snr = Data['snr'][0][0]
			rx = Data['rx']
			InPhase, QuadPhase = rx.real, rx.imag
			DataofScheme[snr] = np.append(InPhase, QuadPhase, axis=1)
		Dataset[scheme] = DataofScheme

	return Dataset


# Train and Validation Datasets
"""
Training:
Received Signal with SNR Ratio  30 dB is used for Training for both Channels and all Modulation Schemes.

Validation:
AutoML is validated on Received Signals with SNR Ratio's (in dB)  [−15,−10,−5,0,5,10,15,20,25]
"""
def ImportDatasets(Channel,L=None):
    if Channel == "AWGN":
        Path =  "../Data/" + Channel
    elif Channel == "Rayleigh":
        Path = "../Data/" + Channel + "/" + str(L)
    Data = ImportData(Path)
    
    Dataset = {}
    Dataset['Classes'] = list(Data.keys())
    OneHotClasses = np.eye(len(Dataset['Classes']))

    Classes = {}
    for i in range(len(Dataset['Classes'])):
        Classes[Dataset['Classes'][i]] = OneHotClasses[i]

    Valid_SNRs = [-15,-10,-5,0,5,10,15,20,25,30]

    if Channel == "AWGN":
        X_Train, y_Train = np.empty((0,2)), np.empty((0,3))
        X_Valid, y_Valid = {}, {}

        for snr in Valid_SNRs:
            X_Valid[snr] = np.empty((0,2))
            y_Valid[snr] = np.empty((0,3))


        for c in Classes.keys():
            ModData = Data[c]
            SNRs = ModData.keys()
            for snr in SNRs:
                if snr == 30:
                    X = ModData[snr]
                    y = np.repeat(np.expand_dims(Classes[c],axis=0), X.shape[0], axis=0)
                    X_Train = np.append(X_Train,X,axis=0)
                    y_Train = np.append(y_Train,y,axis=0)
                    
                    X_Valid[snr] = X_Train
                    y_Valid[snr] = y_Train
                else:
                    X = ModData[snr]
                    y = np.repeat(np.expand_dims(Classes[c],axis=0), X.shape[0], axis=0)
                    X_Valid[snr] = np.append(X_Valid[snr], X, axis=0)
                    y_Valid[snr] = np.append(y_Valid[snr], y, axis=0)

    elif Channel == "Rayleigh":
        X_Train, y_Train = np.empty((0,100,2)), np.empty((0,3))
        X_Valid, y_Valid = {}, {}
        for snr in Valid_SNRs:
            X_Valid[snr] = np.empty((0,100,2))
            y_Valid[snr] = np.empty((0,3))

        for c in Classes.keys():
            ModData = Data[c]
            SNRs = ModData.keys()
            for snr in SNRs:
                if snr == 30:
                    X = ModData[snr]
                    X = X.reshape(-1,100,2)
                    y = np.repeat(np.expand_dims(Classes[c],axis=0), X.shape[0], axis=0)
                    X_Train = np.append(X_Train,X,axis=0)
                    y_Train = np.append(y_Train,y,axis=0)
                    
                    X_Valid[snr] = X_Train
                    y_Valid[snr] = y_Train
                else:
                    X = ModData[snr]
                    X = X.reshape(-1,100,2)
                    y = np.repeat(np.expand_dims(Classes[c],axis=0), X.shape[0], axis=0)
                    X_Valid[snr] = np.append(X_Valid[snr], X, axis=0)
                    y_Valid[snr] = np.append(y_Valid[snr], y, axis=0)

    return X_Train, y_Train, X_Valid, y_Valid
