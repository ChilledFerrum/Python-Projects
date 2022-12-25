import os
import cv2 as cv


datasetPath = "ExDark/Dataset"
groundtruthPath = "ExDark/Groundtruth"

subFoldersGT = [f for f in os.listdir(groundtruthPath)]
subFoldersData = [f for f in os.listdir(datasetPath)]
CategoryPathsGTruth = []
CategoryPathsData = []
for subFolder in subFoldersGT:
    CategoryPathsGTruth.append(groundtruthPath + "/" + subFolder)
for subFolder in subFoldersData:
    CategoryPathsData.append(datasetPath + "/" + subFolder)

CategoryPathsData.sort()
CategoryPathsGTruth.sort()

ClassColors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 218, 90), (0, 110, 204), (255, 110, 192),
          (192, 201, 255), (0, 255, 255), (255, 125, 111), (255, 255, 255), (129, 180, 128), (0, 48, 122)]

count = 0
for (pathGT, pathData) in zip(CategoryPathsGTruth, CategoryPathsData):
    FilesGTruth = [f for f in os.listdir(pathGT)]
    FilesDataset = [f for f in os.listdir(pathData)]
    FilesGTruth.sort()
    FilesDataset.sort()
    for (fileGT, fileData) in zip(FilesGTruth, FilesDataset):
        FileName = fileGT.replace(".txt", "")

        # if FileName != fileData:
        #     print("Groundtruth: ", pathGT + "/" + FileName, "\t fileDataset: ", pathData + "/" + fileData)
        if FileName != fileData:
            print("Incorrect File Matching!")
            print("Groundtruth: ", FileName, "\tDataset: ", fileData)
        else:
            fGT = open(pathGT + "/" + fileGT)
            fGT.readline()  # Skips first line
            fData = cv.imread(pathData + "/" + fileData)
            HEIGHT, WIDTH, _ = fData.shape
            Lines = fGT.readlines()
            for line in Lines:
                Data = line.split()
                ClassType = Data[0]
                start_point = (int(Data[1]), int(Data[2]))
                if ClassType == "Bicycle":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[0], 2)
                if ClassType == "Boat":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[1], 2)
                if ClassType == "Bottle":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[2], 1)
                if ClassType == "Bus":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[3], 2)
                if ClassType == "Car":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[4], 1)
                if ClassType == "Cat":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[5], 2)
                if ClassType == "Chair":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[6], 2)
                if ClassType == "Cup":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[7], 1)
                if ClassType == "Dog":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[8], 2)
                if ClassType == "Table":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[9], 2)
                if ClassType == "People":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[10], 1)
                if ClassType == "Motorbike":
                    fData = cv.rectangle(fData, start_point, (int(Data[3]) + int(Data[1]), int(Data[4]) + int(Data[2])), ClassColors[11], 2)
                cv.putText(fData,
                           ClassType,
                           tuple(map(sum, zip(start_point, (0, -7)))),
                           cv.FONT_HERSHEY_SIMPLEX,
                           0.5,
                           (255, 255, 255),
                           2)
            cv.imwrite("Groundtruth_Images/" + FileName, fData)