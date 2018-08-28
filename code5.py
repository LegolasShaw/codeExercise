class Solution:
	def Fibonacci(self, n):
		i = 0
		while (i>=0) and (i <= n):
			if i == 0:
				prepreNum = 0
				preNum = 0
				reslut = 0
			if i == 1:
				reslut = 1
				prepreNum = 0
				preNum = 0
			if i == 2:
				reslut = 1
				prepreNum = 1
				preNum = 1

			if i >= 3:
				reslut = prepreNum + preNum
				prepreNum = preNum
				preNum = reslut

			i += 1
		return  reslut


xx = Solution()
print(xx.Fibonacci(3))