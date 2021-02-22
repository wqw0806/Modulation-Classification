# Modulation-Classification
Detecting the Modulation Scheme of Received Signal using AutoML Techniques.

## References
- [How to choose a neural network architecture? – A modulation classification example](https://ieeexplore.ieee.org/document/9221167)
- [Modulation Classification with Deep Learning](https://in.mathworks.com/help/deeplearning/ug/modulation-classification-with-deep-learning.html)

## Data-Generation
- Data represents Constellation Received-Signal at the Receiver's End.
- Data is generated using MatLab Communication ToolBox.
- Transmitted Signal is modulated with QPSK, 16-QAM, 64-QAM Modulation Schemes.
- Signal is passed through Rayleigh's Multi-Path Fading Channel and AWGN for various SNR ratios.
- For training, SNR = 30dB.
- For testing, SNR = 5dB, 10dB, 15dB, 20dB, 25dB.

## Visualisations
- Visualising generated Data
