# 초당 최대 처리량 계산(임의 시간 + 1초간 처리하는 요청 최대 개수)
# 응답 완료 시간 S: 오름차순 정렬
# 처리 시간 T: 0.001 ~ 3.000

# 맨 처음 시작 시간과 마지막 응답 시간 사이에서 0.001 초 마다 1초 구간에 얼마만큼 속해 있는 지를 찾아야 함
# 00:00:00 ~ 23:59:59.999 = 1000(1초) * 60(1분) * 60(1시간) * 24(24시간) = 86,400,000
# 24시간 범위 동안 1초 마다 범위에 속해있는지 lines를 검사해야함(최대 2000개)
# 전부 순회하는 방법은 Timeout 가능성

# 각 응답 완료로 시작 시간을 구할 때마다 0.001초 단위로 나누어진 공간에 해당 line 번호를 넣는 방식으로 해결할 수 있지 않을까?
# 그리고 계산은 앞 뒤로 한 칸씩 늘리면서 하는 거지 -> 이거다
# 00:00:00.000 부터 돌면서 시작 시간에 들어오면 포함, 응답 시간에 나가면 제외로 진행해보자.


# 시작 시간으로 정렬된 stack 1개, 응답 시간으로 정렬된 stack 1개를 사용
# 시작 시간 min heap으로 매번 0.001초 움직일 때마다 시작 시간이 포함되면 count를 늘리고,
# 응답 시간 min heap으로 매번 0.001초 움직일 때마다 응답시간을 넘어서면 count를 뺀다.

# 위는 아니었고...
# 결국 처리량 계산은 로그가 시작해야 이루어질 수 있다.
# 각 로그들을 순회하면서 각 로그들의 시작 시간부터 1초, 끝나는 시간 부터 1초를 계산해서 다른 로그들이 포함되는지의 여부를 확인한다.
def plusTime(time):
    h, m, s = time

    s = s + 1
    if s >= 60:
        s %= 60
        m += 1

    if m >= 60:
        m = 0
        h += 1

    if h >= 24:
        return False

    return [h, m, s]


def splitTime(time):
    h, m, s = time.split(":")

    return [int(h), int(m), float(s)]

def solution(lines):
    answer = 0

    log_times = []
    # 시작 시간, 응답 시간 시간 log 구성
    for line in lines:
        date, response, run_time = line.split(" ")
        res_h, res_m, res_s = splitTime(response)

        run_time = float(run_time.replace("s", ""))
        # 9/15로 고정
        date = 15
        # 응답 시간에서 실행 시간을 뺌
        start_date, start_h, start_m, start_s = 15, res_h, res_m, res_s
        start_s = start_s - run_time

        # 초 계산
        if start_s < 0:
            start_m -= 1
            start_s = 1 + start_s

        # 분 계산
        if start_m < 0:
            start_h -= 1
            start_m = 59

        # 시간 계산
        if start_h < 0:
            start_h = 23
            start_date = 14

        log_times.append([(start_date, start_h, start_m, start_s), (date, res_h, res_m, res_s)])

    for log_time in log_times:
        start, end = log_time




    return answer

print("정답 = 1 / 현재 풀이 값 = ", solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print("정답 = 2 / 현재 풀이 값 = ", solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print("정답 = 7 / 현재 풀이 값 = ", solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))