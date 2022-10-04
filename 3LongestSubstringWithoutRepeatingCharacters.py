# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max = 0
    strAux = ""
    for i in range(len(s)):
        for j in s:    
            if j not in strAux:
                strAux = strAux + j  
            else:
                if len(strAux) > max:
                    max = len(strAux)
                strAux = ""
                s = s[1 : : ]
                break
        if max > len(s): break
    if len(strAux) > max:
        max = len(strAux)
    return(max)
        
    

lengthOfLongestSubstring("ohomm")
        
        
        