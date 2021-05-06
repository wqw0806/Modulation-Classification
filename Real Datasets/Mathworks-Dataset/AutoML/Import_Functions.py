import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pimg
import seaborn as sns
import scipy.io
import os
from sklearn.model_selection import train_test_split

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
			DataofScheme[snr] = rx
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
	if Channel == "Rician":
		Path =  "../Data/" + Channel
	Data = ImportData(Path)
    
	Dataset = {}
	Dataset['Classes'] = list(Data.keys())
	OneHotClasses = np.eye(len(Dataset['Classes']))

	Classes = {}
	for i in range(len(Dataset['Classes'])):
		Classes[Dataset['Classes'][i]] = OneHotClasses[i]

	Valid_SNRs = [-15,-10,-5,0,5,10,15,20,25,30]

	if Channel == "Rician":
		X_Train, y_Train = np.empty((0,1,1024,2)), np.empty((0,3))
		X_Valid, y_Valid = {}, {}
		for snr in Valid_SNRs:
			X_Valid[snr] = np.empty((0,1,1024,2))
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
					
	return X_Train, y_Train, X_Valid, y_Valid
	
	

# Splitting Data with all SNRs
def SplitData(X_train, y_train, X_valid, y_valid,test_size):
	X_Valid = {}
	y_Valid = {}
	X_Train,X_Test,y_Train,y_Test = train_test_split(X_train,y_train,test_size=test_size,stratify=y_train)
	X_Valid[30] = X_Test
	y_Valid[30] = y_Test

	for snr in [-15,-10,-5,0,5,10,15,20,25]:
		xtrain,xtest,ytrain,ytest = train_test_split(X_valid[snr],y_valid[snr],test_size=test_size,stratify=y_valid[snr])
        
		X_Train = np.append(X_Train,xtrain,axis=0)
		y_Train = np.append(y_Train,ytrain,axis=0)

		X_Valid[snr] = xtest
		y_Valid[snr] = ytest

	return X_Train,y_Train,X_Valid,y_Valid
