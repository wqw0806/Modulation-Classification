# Modulation-Classification
Detecting the Modulation Scheme of Received Signal using AutoML Techniques.

## AutoML
- AutoML Procedure is used for Traning and Testing of Generated Data. AutoKeras are used for performing AutoML for deep learning models.

## References
- [How to choose a neural network architecture? – A modulation classification example](https://ieeexplore.ieee.org/document/9221167)
- [Modulation Classification with Deep Learning](https://in.mathworks.com/help/deeplearning/ug/modulation-classification-with-deep-learning.html)

## Synthetic Datasets

### Data-Generation
- Data represents Constellation Received-Signal at the Receiver's End.
- Data is generated using Basic MatLab Commands.
- Transmitted Signal is modulated with QPSK, 16-QAM, 64-QAM Modulation Schemes.
- Signal is passed through Rayleigh's Multi-Path Fading Channel and AWGN for various SNR ratios.
- For training, SNR = 30dB.
- For testing, SNR = 5dB, 10dB, 15dB, 20dB, 25dB.
- For Rayleigh Multi-Path Fading, ChannelLengths = [2,3] are considered. Channel Model is changed for each and every SNR Ratio.

### Visualisations
- Visualising generated Data.

### Training and Testing
- Training and Testing on Synthetic Datasets is complete and their Results and Models are saved in Syntheic Datasets folder.

## Real Datasets

### Data-Generation
- Data is generated from the code in [Modulation Classification with Deep Learning](https://in.mathworks.com/help/deeplearning/ug/modulation-classification-with-deep-learning.html).
- Data is generated for 1000 Frames and for SNR Ratios = [5,10,15,20,25,30]dB. Note that Channel in thiscase is **Rician**.
- For training, SNR = 30dB.
- For testing, SNR = 5dB, 10dB, 15dB, 20dB, 25dB.

### Training and Testing
- Training and Testing on Dataset is going on. Intermediate Results and Models are saved in Real Datasets folder.


## Tasks
### Synthetic Datasets
- Evaluating AWGN Data with Image Classifier of AutoKeras.
- Adding [-15,-10,-5,0]db SNRs to Rayleigh Data and then Evaluating Results with Image Classifier of AutoKeras.
- Adding [-15,-10,-5,0]db SNRs to Rayleigh Data and then Evaluating Results using CNN  from the Research Paper.
- Adding [-15,-10,-5,0]db SNRs to Rayleigh Data and then Evaluating Results using RNN  from the Research Paper.

### Real Dataset
- Larger Training time for Mathworks Dataset
- AutoML over RadioML Data.

---

**Note:**
This Project is still under Development.