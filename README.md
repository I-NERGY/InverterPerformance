# Forecasting the Performance of Inverter Systems

We provide a docker container to easily build and run the machine learning model for weekly inverter performance based on prior bi-weekly readings. The model utilizes an 8-column csv file with similar column names of (PR, G_M0, T, T_WR1, T_WR2, T_WR3, T_WR4, E_N), such that PR = PERFORMANCE RATIO; G_M0 = Irradiance, T1  ambiant temp, T_WR1 - T_WR4 = internal inverter temps; E_N = nominal energy". As can be found in the sample (dummy) test.csv. To build the Docker container we provide the following files: 
-	Dockerfile
-	inference.py
-	requirements.txt

The inference file accepts a csv file with 14 observations, with the performance value in the first column, while the rest follow order: PR, G_M0, T, T_WR1, T_WR2, T_WR3, T_WR4, E_N respectively. The machine learning model follows the encoder-decoder paradigm, achieved by the CONVLSTM and LSTM layers. 


The scripts were implemented in tensorflow.


To run:
-   docker build -t [DOCKER_TAG_NAME] .
