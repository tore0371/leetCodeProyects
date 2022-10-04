
def findMedianSortedArrays(nums1, nums2):
    '''
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    '''
    finalArray = []
    for i in nums1:
        finalArray.append(i)
    for j in nums2:
        finalArray.append(j)
    finalArray.sort()

    leng = len(finalArray)
    print("Longitud --> ", leng)
    print (finalArray)
    if leng%2 == 0:
        print("Es par")
        mediumValue1 = leng / 2 - 1
        mediumValue2 = mediumValue1 + 1
        return (float(finalArray[int(mediumValue1)]+ finalArray[int(mediumValue2)]) / 2)
    else:
        print("Es impar")
        mediumValue = float(leng) / 2.0 - 0.5
        print("Valor medio --> ", mediumValue)
        return float(finalArray[int(mediumValue)])


findMedianSortedArrays([1,3], [2])