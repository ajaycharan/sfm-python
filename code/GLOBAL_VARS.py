# ____________________________________________________________________________
#
# 						ALL GLOBALLY DEFINED VARIABLES
#						______________________________
#
#			All code written by Shreyas Skandan. Data taken from CIS580
# 		course at the University of Pennsylvania, taught by Dr. Jianbo Shi.
# ____________________________________________________________________________

MAIN_SFM_DIR = 'C:/Users/Shreyas Skandan/Desktop/StructureFromMotion/'

# Main folder to store all data
DATA_DIR = MAIN_SFM_DIR + 'data/'
# Main code repository
CODE_DIR = MAIN_SFM_DIR + 'code/'
# Text file containing camera parameters
CALIBRATION_FILE = DATA_DIR + 'calibration.txt'
# Folder containing matched features across image frames
FEATURES_DIR = DATA_DIR + 'correspondences/'
# Folder containing the NUMPY file for image match matrices
NUMPY_MATCH_MATRIX_DIR = DATA_DIR + 'correspondences/matchmatrices/'
# Folder containing image frames (2D)
INPUT_IMAGE_DIR = DATA_DIR + 'imgs/'
# Folder to store all visualisation output
OUTPUT_IMAGE_DIR = DATA_DIR + 'output/'
# Folder to store any additional documentation
ADDITIONAL_DOCUMENTATION_DIR = DATA_DIR + 'docs/'
# Number of colour channels in image
CLR_CHANNELS_COUNT = 3


