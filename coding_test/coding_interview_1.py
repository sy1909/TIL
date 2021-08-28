#펠린드롬 -> 앞뒤가 똑같은 단어나 문장 (회문)
# 1 리스트 변환 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 영문자와 숫자가 아닌 기호나 한글이면 걸러라 if
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): #양옆비교 pop 
                return False

        return True

# 2 데크 자료형을 이용 > 1보다 5배 속도 향상
import collections
from typing import Deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque() # strs 를 데크형으로 선언
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

# 3 정규표현식 , 슬라이싱 사용 > 2보다 2배 향상
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s) # a-z0-9 문 제외하고 다 지운다
        return s == s[::-1]  # 슬라이싱
    # 별달리 알고리즘이라고 부를만한 게 없지만
    # 정규식으로 불필요한 문자를 필터링하고 문자열을 조작할 수

    