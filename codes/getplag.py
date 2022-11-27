def getplag(txt1,txt2):

	if len(txt1)<len(txt2): txt1,txt2 = txt2,txt1
	
	txt1 = txt1.lower();
	txt2 = txt2.lower();
	
	mx = len(txt1)
	mn = len(txt2)
	total = (mn*(mn+1))/2
	cur = mx
    		
	dp = [[0 for i in range(0,mx)]]
	
	plag = 0
	
	for i in range(0,mn):
		tmp = [0]
		for j in range(0,mx):
			if txt2[i]==txt1[j]: 
			    plag = plag + dp[i][j] + 1
			    tmp.append(dp[i][j]+1)
			else: tmp.append(0)
		dp.append(tmp)
	
	ans = min(plag/total,1)
	
	return round(ans,2)
