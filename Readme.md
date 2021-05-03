# Modulation-Classification
Detecting the Modulation Scheme of Received Signal using AutoML Techniques.

## AutoML
- AutoML Procedure is used for Traning and Testing of Generated Data. AutoKeras are used for performing AutoML for Deep Learning Models.

## References
- [How to choose a neural network architecture? – A modulation classification example](https://ieeexplore.ieee.org/document/9221167)
- [Modulation Classification with Deep Learning](https://in.mathworks.com/help/deeplearning/ug/modulation-classification-with-deep-learning.html)

## Synthetic Datasets

### Data-Generation
- Data represents Constellation Received-Signal at the Receiver's End.
- Data is generated using Basic MatLab Commands.
- Modulation Schemes: QPSK, 16-QAM, 64-QAM.
- Signal is passed through Rayleigh's Multi-Path Fading Channel and AWGN for various SNR ratios.
- For Training, SNR = 30dB.
- For Testing, SNR = -15db, -10dB, -5dB, 0dB, 5dB, 10dB, 15dB, 20dB, 25dB.
- For Rayleigh Multi-Path Fading, ChannelLengths = [2,3] are considered. Channel Model is changed for each and every SNR Ratio.

### Visualisations
- Visualising generated Data.

## Architectures
- AutoML StructuredClassifier, AutoML ImageClassifer for AWGN Data.
- AutoML ImageClassifier, AutoML Customised RNN, CNN form Reseach Paper.

### Training and Testing
- Training and Testing on Synthetic Datasets is complete and their Results and Models are saved in Syntheic Datasets folder.

## Real Datasets

### Data-Generation
- Data is generated from the code in [Modulation Classification with Deep Learning](https://in.mathworks.com/help/deeplearning/ug/modulation-classification-with-deep-learning.html).
- Modulation Schemes: QPSK, 16-QAM, 64-QAM.
- Note that Channel in this case is Rician.
- Data is generated for 2200 Frames and for SNR Ratios = [-15,-10,-5,0,5,10,15,20,25,30]dB.
- 2000 Frames of Data for each SNR of each Modulation Scheme is used for Training the Model and 200 Frames of Data for each SNR of each Modulation Scheme is used for Testing the Model.

## Architectures
- AutoML Customised CNN, AutoML Customised RNN, AutoML Customised CLDNN, CNN from Mathworks Example.

### Training and Testing
- Training and Testing on Dataset is going on. Intermediate Results and Models are saved in Real Datasets folder.


## Tasks
### Real Dataset
- AutoML over RadioML Data.

---

**Note:**
This Project is still under Development.