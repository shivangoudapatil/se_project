#using dynamic programming to store all the common substrings and counting them to predict 
def getplag(txt1,txt2):

	#we are creating a table horizontally is bigger string and vertically smaller

    # After unit testing , length can't be equal to zero , return 0 plagarism default


    if(len(txt1)==0 or len(txt2)==0):
        return 0

    if len(txt1)<len(txt2): txt1,txt2 = txt2,txt1


	
    txt1 = txt1.lower();
    txt2 = txt2.lower();
	
    mx = len(txt1)
    mn = len(txt2)
	
	#if the strings were same this will be total number of common substrings
    total = (mn*(mn+1))/2
    cur = mx
    		
	#2d array, (first array is all 0's)
    dp = [[0 for i in range(0,mx)]]
	
	#will count total number of common substrings along with length
    plag = 0
	
    for i in range(0,mn):
        tmp = [0]
        for j in range(0,mx):
            if txt2[i]==txt1[j]: 
                plag = plag + dp[i][j] + 1
                tmp.append(dp[i][j]+1)
            else: 
                tmp.append(0)
        dp.append(tmp)
	
    ans = min(plag/total,1)
	
    return round(ans,2)