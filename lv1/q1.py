# coding=utf8

from collections import namedtuple

question = "두 수를 더한 수를 반환하는 함수를 작성하세요."
congrats = "게임을 이해하셨군요! 두번째 문제로 넘어가세요."

test = namedtuple("test", "a b want")

tests = [
	test(a=1, b=2, want=3),
	test(a=-1, b=1, want=0),
	test(a=-2, b=-2, want=-4),
]

def answer(func):
	for t in tests:
		got = func(t.a, t.b)
		if got != t.want:
			return "답변한 함수에 ({0}, {1})를 넣었더니 {2}가 나왔습니다.\n원하는 값 {3}".format(t.a, t.b, got, t.want)

