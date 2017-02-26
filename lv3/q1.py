# coding=utf8

from collections import namedtuple

import time

question = """엑셀은 행과 열을 표시하는 방식이 다릅니다. 1행은 1이라고 표시하지만 1열은 A라고 표시하지요.
그래서 1열 1행은 A1이라고 표시합니다. 이렇게 행과 열을 다르게 표시하면 사용자는 덜 헷갈리겠지만
만드는 사람은 머리를 조금 더 써야합니다.

A-Z 1-26
AA-ZZ 27-702
AAA-ZZZ 703-18278
...

자, 여기서 숫자를 받고 알파벳 문자열을 생성하는 함수를 만드세요.
혹시 0이나 음수값을 받았을땐 빈 문자열을 반환하면 됩니다.
"""
congrats = "레벨3의 첫번째 문제를 푸셨군요. 멋있어요!"

test = namedtuple("test", "i want")

tests = [
	test(i=-1, want=""),
	test(i=0, want=""),
	test(i=1, want="A"),
	test(i=25, want="Y"),
	test(i=26, want="Z"),
	test(i=27, want="AA"),
	test(i=28, want="AB"),
	test(i=701, want="ZY"),
	test(i=702, want="ZZ"),
	test(i=703, want="AAA"),
	test(i=704, want="AAB"),
	test(i=18277, want="ZZY"),
	test(i=18278, want="ZZZ"),
	test(i=18279, want="AAAA"),
	test(i=18280, want="AAAB"),
	test(i=475253, want="ZZZY"),
	test(i=475254, want="ZZZZ"),
]

def answer(func):
	for t in tests:
		got = func(t.i)
		if got != t.want:
			return "답변한 함수에 {0}를 넣었더니 {1}가 나왔습니다.\n원하는 값 {2}".format(t.i, got, t.want)
		print("{0} => {1}".format(t.i, got))
		time.sleep(1)

