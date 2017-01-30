# coding=utf8

from collections import namedtuple
import sys
import time

question = """여러분은 현재 좀비게임에서 주변 사람이 좀비가 되면 자신도 좀비가 되는 함수를 짜고 있습니다.
전염이 된 상태는 True, 전염이 되지 않은 상태는 False로 표현합니다.
def 전염(왼쪽, 오른쪽) 처럼 작성하고 내 상태를 반환하면 됩니다.
"""
congrats = "좀비게임을 만들 좋은 자질을 가지고 있네요! 다음으로 넘어가세요."

# test는 테스트에 필요한 정보이다.
# orig는 최초상태, first는 첫번째 감염후 상태, second는 두번째 감염후 상태, last는 마지막 상태를 가리킨다.
test = namedtuple("test", "orig first second last")

tests = [
	test(
		orig = [True, False, False, False, False, False, False, False, True, False],
		first = [True, True, False, False, False, False, False, True, True, True],
		second = [True, True, True, False, False, False, True, True, True, True],
		last = [True, True, True, True, True, True, True, True, True, True],
	),
	test(
		orig = [False, False, False, False, True, False, False, False, False, False],
		first = [False, False, False, True, True, True, False, False, False, False],
		second = [False, False, True, True, True, True, True, False, False, False],
		last = [True, True, True, True, True, True, True, True, True, True],
	),
	test(
		orig = [False, False, False, False, False, False, False, False, False, False],
		first = [False, False, False, False, False, False, False, False, False, False],
		second = [False, False, False, False, False, False, False, False, False, False],
		last = [False, False, False, False, False, False, False, False, False, False],
	),
]

def equal(a, b):
	"""받아들인 두 개의 논리값 리스트가 완전히 동등한지 검사한다."""
	if len(a) != len(b):
		return False
	for i in range(len(a)):
		if a[i] is not b[i]:
			return False
	return True

def sprintBoolList(lst):
	"""
	sprintBoolList는 리눅스계열 OS에서 받아들인 논리값 리스트의 항목이 True일 경우
	초록색으로 표기한 문자열을 반환한다.

	http://stackoverflow.com/questions/2616906/how-do-i-output-coloured-text-to-a-linux-terminal 참고.
	"""
	result = []
	for v in lst:
		if v is True:
			if sys.platform in ["linux", "linux2", "darwin"]:
				result.append("\033[32m{0}\033[0m".format(v))
			else:
				result.append(str(v))
		else:
			result.append(str(v))
	return "[" + ", ".join(result) + "]"

def infect(func, before):
	"""infect는 퀴즈를 푸는 사람이 준 함수를 가지고 한번 감염을 진행시키고 그 결과를 반환한다."""
	after = []
	for i, v in enumerate(before):
		prev = False
		if i != 0:
			prev = before[i-1]
		next = False
		if i != len(before)-1:
			next = before[i+1]
		curr = before[i]
		if not curr:
			# 감염되지 않은 사람에 대해서만 이 함수를 실행시킨다.
			# 이렇게 하지 않으면 이미 감염이 된 사람이 감염에서 풀리는 결과를 나을수 있기 때문이다.
			curr = func(prev, next)
		after.append(curr)
	return after

def answer(func):
	"""answer는 퀴즈를 푸는 사람이 준 함수를 가지고 테스트를 진행한다."""
	for i, t in enumerate(tests):
		print("{0}번째 테스트".format(i+1))
		time.sleep(1)
		print("시작할 때 상태: {0}".format(sprintBoolList(t.orig)))
		time.sleep(1)
		j = 0
		before = []
		after = t.orig
		while before != after:
			before = after
			after = infect(func, before)
			print("{0}번째 적용 결과: {1}".format(j+1, sprintBoolList(after)))
			if j == 0 and not equal(after, t.first):
				return "실패!\n답변한 함수를 이용해 한번 전염을 시킨 결과:\n\t{0}\n원하는 값:\n\t{1}".format(sprintBoolList(after), sprintBoolList(t.first))
			if j == 1 and not equal(after, t.second):
				return "실패!\n답변한 함수를 이용해 두번째 전염을 시킨 결과:\n\t{0}\n원하는 값:\n\t{1}".format(sprintBoolList(after), sprintBoolList(t.second))
			# 더이상의 체크는 하지 않고 마지막만 같은지 체크한다.
			j += 1
			time.sleep(1)
		if not equal(after, t.last):
			return "실패!\n답변한 함수를 이용해 전염을 시킨 최종결과:\n\t{0}\n원하는 값:\n\t{1}".format(sprintBoolList(after), sprintBoolList(t.last))
		print("성공!\n")
		time.sleep(1)

