#리스트의 길이가 홀수이므로 중앙값은 2로 나눈 몫이다.
def solution(array):
    array = sorted(array)
    l = len(array)//2
    answer = array[l]
    return answer