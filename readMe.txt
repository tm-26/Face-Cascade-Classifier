In the model folder one can find the trained model, along with its params file.
In order to continue training the model, the OpenCV folder needs to be downloaded from here:
https://sourceforge.net/projects/opencvlibrary/files/

The following command will resume training for an extra 3 steps:
openCV\build\x64\vc15\bin\opencv_traincascade.exe -data model -vec datasets\positiveSamples\positiveTrainDataInfo.vec -bg datasets\negativeSamples\negativeTrainDataInfo.txt -w 24 -h 24 -numPos 10000 -numNeg 10000 -numStages 12 -minHitRate 0.999 -maxFalseRate 0.4


cascade.xml is a copy of the final model.


Artifact1.py tests cascade.xml on the testing data found in the dataset folder.
To run Artifact1.py ensure that python is installed with the opencv-python library. (https://pypi.org/project/opencv-python/)
