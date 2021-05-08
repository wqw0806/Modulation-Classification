import numpy as np
import pickle

# One-Hot Encoding of Vectors
def toOneHot(t):
	t1 = np.zeros([len(t), max(t)+1])
	t1[np.arange(len(t)), t] = 1
	return t1
	
# Train and Validation Datasets
"""
Training:
Model is trained on all SNR Ratios

Validation:
Model is evaluated on all SNR Ratios
"""
def ImportDatasets(Path,test_size=0.1):
	# Extracting Data
	with open(Path,'rb') as f:
		Data = pickle.load(f,encoding='latin')
	SNRs, ModulationSchemes = map(lambda j: sorted(list(set(map(lambda x: x[j], Data.keys())))), [1,0])
    
	X = []
	Labels = []
	for modType in ModulationSchemes:
		for snr in SNRs:
			X.append(Data[(modType,snr)])
			Labels += [(modType,snr)] * (Data[(modType,snr)].shape[0])
	X = np.vstack(X)
	
	N = X.shape[0]
	N_Train = int((1-test_size)*N)
	
	Train_Index = np.random.choice(range(0,N), size=N_Train, replace=False)
	Test_Index = list(set(range(0,N)) - set(Train_Index))
	
	X_Train = X[Train_Index]
	X_Test = X[Test_Index]
	
	y_Train = toOneHot(list(map(lambda x: ModulationSchemes.index(Labels[x][0]), Train_Index)))
	y_Test = toOneHot(list(map(lambda x: ModulationSchemes.index(Labels[x][0]), Test_Index)))
	
	return X_Train, y_Train, X_Test, y_Test
