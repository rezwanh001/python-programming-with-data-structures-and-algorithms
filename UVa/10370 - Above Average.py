
def Main():
	T = int(input())
	for _ in range(T):
		arr = list(map(int, input().split()))
		n = arr[0]
		del arr[0]
		sm = sum(arr)
		avg = sm/n
		# print(sm, n)
		cnt = 0
		# print(arr)
		for i in range(0,len(arr)):
			if arr[i] > avg:
				cnt += 1

		res = (cnt/n)*100
		# print(round(res, 3) , "%")
		print('%.3f' %res, end='%\n')

if __name__ == '__main__':
    Main()