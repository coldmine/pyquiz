# coding=utf8

from collections import namedtuple
import time

question = """블리자드에 입사한 여러분은 스타크래프트 팀에 배속되었습니다!
공격속도가 다른 두 유닛이 맵 안에서 싸울 때 각 유닛의 다음 공격까지 남은 시간을 받아
먼저 공격하는 유닛의 번호와 남은 시간을 반환하세요.
번호는 첫번째 유닛이 공격하면 0, 두번째 유닛이 공격하면 1을 반환하면 됩니다.

다음공격(유닛1의남은시간, 유닛2의남은시간) => (유닛번호, 남은시간)
"""
congrats = "와 또 해냈군요! 하지만 다음 문제는 쉽지 않을거에요!"

# char는 캐릭터 정보이다.
class char:
	def __init__(self, name, life, power, interval, sound):
		self.name = name
		self.life = life
		self.power = power
		self.interval = interval
		self.cooltime = interval
		self.sound = sound

def zealot():
	"""zealot은 새로운 질럿을 생성한다."""
	return char(name="질럿", life=30, power=5, interval=1.5, sound="차가장")

def zergling():
	"""zergling은 새로운 저글링을 생성한다."""
	return char(name="저글링", life=6, power=1, interval=0.4, sound="톡")

def marine():
	"""marine은 새로운 마린을 생성한다."""
	return char(name="마린", life=15, power=3, interval=0.7, sound="투둥")

# test는 두 캐릭터를 가지고 있다.
test = namedtuple("test", ["chars"])

tests = [
	test(chars=[zealot(), zergling()]),
	test(chars=[zergling(), marine()]),
	test(chars=[marine(), zealot()]),
]

def answer(func):
	"""answer는 받아들인 함수로 테스트를 진행한다."""
	for i, t in enumerate(tests):
		print("{0}번째 테스트".format(i+1))
		ch1, ch2 = t.chars
		print("{0}과 {1}이 싸웁니다!".format(ch1.name, ch2.name))
		while True:
			ans = func(ch1.cooltime, ch2.cooltime)
			try:
				ai, elapse = ans
			except:
				return "실패!\n리턴값은 항상 2개여야 합니다. (다음액션까지남은시간, 공격자번호)"
			if ai not in [0, 1]:
				return "실패!\n공격자 번호는 항상 0 또는 1 이어야 합니다. 결과값: {0}".format(ai)
			ch1.cooltime -= elapse
			ch2.cooltime -= elapse
			if ch1.cooltime != 0 and ch2.cooltime != 0:
				return "실패!\n적어도 둘 중의 하나의 쿨타임이 0이 되어야 합니다. 결과값: ({0}:{1}, {2}:{3})".format(ch1.name, ch1.cooltime, ch2.name, ch2.cooltime)
			if ch1.cooltime < 0 or ch2.cooltime < 0:
				return "실패!\n다른 유닛의 공격 시간이 이미 지났습니다: ({0}:{1}, {2}:{3})".format(ch1.name, ch1.cooltime, ch2.name, ch2.cooltime)
			if t.chars[ai].cooltime != 0:
				return "실패!\n{0}번 캐릭터가 공격할 차례가 아닙니다.".format(ai)
			attacker = t.chars[ai]
			defender = t.chars[1-ai]
			time.sleep(elapse)
			print("{0}: {1}".format(attacker.name, attacker.sound))
			defender.life -= attacker.power
			if defender.life <= 0:
				print("{0}이 죽었습니다!".format(defender.name))
				print("성공\n")
				time.sleep(0.5)
				break
			attacker.cooltime = attacker.interval

