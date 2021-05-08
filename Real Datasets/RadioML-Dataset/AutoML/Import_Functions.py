import numpy as np
import pickle

# Importing Data for all SNR Ratio's
def ImportData(Path):
    # Extracting Data
    with open(Path,'rb') as f:
        Data = pickle.load(f,encoding='latin')
    SNRs, ModulationSchemes = map(lambda j: sorted(list(set(map(lambda x: x[j], Data.keys())))), [1,0])
    
    Dataset = {}
    for modType in ModulationSchemes:
        Dataset[modType] = {}
        for snr in SNRs:
            data = Data[(modType,snr)]
            Dataset[modType][snr] = data 
    return Dataset


# Train and Validation Datasets
"""
Training:
Model is trained on all SNR Ratios

Validation:
Model is evaluated on all SNR Ratios
"""
def ImportDatasets(Path,test_size=0.1):
    Dataset = ImportData(Path)
    ModulationSchemes = list(Dataset.keys())
    OneHotClasses = np.eye(len(ModulationSchemes))
    
    Classes = {}
    for i in range(len(ModulationSchemes)):
        Classes[ModulationSchemes[i]] = OneHotClasses[i]

    SNRs = list(Dataset[ModulationSchemes[0]].keys())

    X_Train, y_Train = [],[]
    X_Valid, y_Valid = {},{}

    for snr in SNRs:
        X_Valid[snr] = []
        y_Valid[snr] = []
        for modType in ModulationSchemes:
            Data = Dataset[modType][snr]
            
            N = Data.shape[0]
            N_Train = int((1-test_size)*N)
            Train_Index = np.random.choice(range(0,N), size=N_Train, replace=False)
            Test_Index = list(set(range(0,N)) - set(Train_Index))

            train = Data[Train_Index]
            valid = Data[Train_Index]

            X_Train.append(train)
            X_Valid[snr].append(valid)

            y_Train.append(np.repeat(np.expand_dims(Classes[modType],axis=0),train.shape[0],axis=0))
            y_Valid[snr].append(np.repeat(np.expand_dims(Classes[modType],axis=0),valid.shape[0],axis=0))

        X_Valid[snr] = np.array(X_Valid[snr]).reshape(-1,2,128)
        y_Valid[snr] = np.array(y_Valid[snr]).reshape(-1,len(ModulationSchemes))
    
    X_Train = np.array(X_Train).reshape(-1,2,128)
    y_Train = np.array(y_Train).reshape(-1,len(ModulationSchemes))

    return X_Train, y_Train, X_Valid, y_Valid
