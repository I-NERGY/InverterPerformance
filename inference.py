import numpy as np
from numpy import nan

from numpy import split
from numpy import array
from pandas import read_csv

from tensorflow.keras.models import load_model

def genWindow(df):
    dlen = len(df)
	# split data into 7-day week from prior 14 days
    if (dlen > 1) or dlen % 14 == 0:
        df = array(split(df, len(df)//7))
        return df
    else:
        print("supply dataframe with length divisible by 14")

def usage():
	print("\n Usage: organise columns as of csv : PR, G_M0, T, T_WR1, T_WR2, T_WR3, T_WR4, E_N")
	print("Where PR = PERFORMANCE RATIO; G_M0 = Irradiance, T1  ambiant temp, T_WR1 - T_WR4 = internal inverter temps; E_N = nominal energy")

def test(tDf):
	test = genWindow(tDf)
	print("test input shape: ", test.shape)
	test = test.reshape(( int(test.shape[0] * test.shape[1] / int(N_STEPS * LEN)), N_STEPS, 1, LEN, 8))
	print("model input shape: ", test.shape)

	model = load_model(MODEL_PATH)

	output = model.predict(test)
	print("\n performance ratio forcast: ", output.flatten().tolist())

if __name__ == '__main__':
	TEST_PATH = "./test.csv"
	MODEL_PATH = "./models/model"

	# sub sequence and days to use with CONVLSTM
	N_STEPS, LEN = 2, 7
	# The total days to use as input from the subsequence and days
	n_input = N_STEPS * LEN

	testDf = read_csv(TEST_PATH)
	cols = testDf.columns.tolist()
	assert len(cols) == 8, "Invalid Input" # CSV should have 8 columns
	# assert (len(testDf) % 14 == 0), "Invalid Input" # supply dataframe with length divisible by 14
	assert (len(testDf) == 14), "Invalid Input" # supply data with 14-days of data

	COLS_CHECK = ["PR", "G_M0", "T", "T_WR1", "T_WR2", "T_WR3", "T_WR4", "E_N"]
	check = [i in j for i, j in zip(COLS_CHECK, cols)]
	rigthColsArrangement = np.all(check)
	print("rigthColsArrangement", rigthColsArrangement)
	assert(rigthColsArrangement), usage()

	testDf.replace('?', nan, inplace=True)
	testDf = testDf.astype('float32')
	
	test(testDf)

