# coding=utf8

import lv1

def ans(a, b):
	pass
	# 여기에 답변 코드를 작성하세요.

def main():
	q = lv1.quiz()
	print(q.question)
	err = q.answer(ans)
	if err:
		print(err)
		return
	print("성공!")

main()
