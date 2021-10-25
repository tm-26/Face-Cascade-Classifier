import os
import random
import xml.etree.ElementTree

if __name__ == '__main__':

    # Generate Positive data
    os.chdir("datasets/positiveSamples")
    faces = os.listdir("lfwcropRefactored")
    random.shuffle(faces)
    trainFaces = faces[:10586]  # 80% of data
    testFaces = faces[10586:]  # 20% of data

    print("Generating positiveTrainDataInfo.txt")
    file = open("positiveTrainDataInfo.txt", "w")
    for face in trainFaces:
        file.write("lfwcropRefactored/" + face + " 1 0 0 64 64\n")
    file.close()

    print("Generating positiveTestDataInfo.txt")
    file = open("positiveTestDataInfo.txt", "w")
    for face in testFaces:
        file.write("lfwcropRefactored/" + face + '\n')
    file.close()

    print("Generating negativeTrainDataInfo.txt")
    os.chdir("../negativeSamples/SUN2012Refactored")
    images = []
    for currentScene in os.listdir("Images"):
        for image in os.listdir("Images/" + currentScene):
            notFound = True
            tree = 0
            try:
                tree = xml.etree.ElementTree.parse("Annotations/" + currentScene + '/' + image[:-3] + "xml")
            except xml.etree.ElementTree.ParseError:
                break
            for currentObject in xml.etree.ElementTree.parse(
                    "Annotations/" + currentScene + '/' + image[:-3] + "xml").getroot().findall("object"):
                if set(currentObject[0].text[1:-1].split()) & {"person", "man", "people"}:
                    found = False
                    break
            if notFound:
                images.append("datasets/negativeSamples/SUN2012Refactored/Images/" + currentScene + '/' + image + "\n")

    random.shuffle(images)
    file = open("../negativeTrainDataInfo.txt", "w")
    for image in images[:13440]:  # 80% of data
        file.write(image)
    file = open("../negativeTestDataInfo.txt", "w")
    for image in images[13440:]:  # 20% of data
        file.write(image)
    print("Generating negativeTestDataInfo.txt")
    file.close()

