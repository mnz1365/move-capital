# Move Capital Letters to the Front. Create a function that moves all capital letters to the front of a word.
import copy


def moveCapitals(tt):
        
    myText = tt
    result = ""
    word = ""
    myCapital = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    myLower = list("abcdefghijklmnopqrstuvwxyz")
    capitalPosition = []
    lowerCasePosition = []
    tempWord = None
    editWord = None
    secondword = ""
    myNewText = ""


    myTextList = myText.split()


    for x in range(len(myTextList)):
        capitalPosition = list()
        lowerCasePosition = list()
        tempWord = None
        tempWord = myTextList[x]
        tempWord = list(tempWord)
        for y in range(len(tempWord)):
            for z in range(len(myCapital)):
                if tempWord[y] == myCapital[z]:
                    capitalPosition.append(y)
        if len(capitalPosition) > 0:
            
            for y in range(len(tempWord)):
                for z in range(len(myLower)):
                    if len(lowerCasePosition) == len(capitalPosition):
                        break
                    if tempWord[y] == myLower[z]:
                        lowerCasePosition.append(y)
                    
            
            
            editWord = copy.deepcopy(tempWord)
            # editWord = list(editWord)
            
            
            
            for y in range(len(capitalPosition)):
                if capitalPosition[y] > lowerCasePosition[y]:  
                    editWord[capitalPosition[y]] = copy.deepcopy(tempWord[lowerCasePosition[y]])
                    editWord[y] = copy.deepcopy(tempWord[capitalPosition[y]])
                
            
            for y in range(len(editWord)):
                secondword = secondword + editWord[y]
            
            myTextList[x] = secondword
            secondword = ""
            
    for y in range(len(myTextList)):
        if y < len(myTextList):
            myNewText = myNewText + myTextList[y] + " "
        else:
            myNewText = myNewText + myTextList[y]
    
    return myNewText         


print(moveCapitals("thIS Is tHe tEtXs"))