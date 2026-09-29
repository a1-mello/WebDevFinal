def everyOtherItemStr(aList):
    for i in range(0,len(aList), 2):
        if type(aList[i]) == str:
            result.append(aList[i])
    return result
print(everyOtherItemStr([3,5,1,4,"aa","ab"]))  # should print ["aa"]
print(everyOtherItemStr(["cat", "dog", 34]))   # should print ["cat"]
print(everyOtherItemStr([1, 5, 2, 6.4]))       # should print []



            
                   
        
    
