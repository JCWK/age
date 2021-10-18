driving = input("你有開過車嗎？ ")
if driving != "有" and driving != "沒有":
	print("只能輸入 有/沒有")
	raise SystemExit

age = input("你多少歳呀？ ")
age = float(age)
if driving == "有":
	if age >= 18:
		print("你應該考到車牌了，對吧！")
	else:
		print("你是否開大膽車了！")
elif driving == "沒有":
	if age >= 18:
		print("你快去考車牌啦")
	else:
		print("那麼記得一到18歳就去考啊")