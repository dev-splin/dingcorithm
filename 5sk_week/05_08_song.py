def convertSongsToArr(songs):
    arr = []
    for char in songs:
        if char == '#':
            arr[-1] = arr[-1] + char
        else:
            arr.append(char)

    return arr


def getTotalSongArr(song_arr, play_minute):
    if play_minute == 0:
        return ""

    # 곡 계속 반복(곡 길이가 재생 시간보다 길면 중간에 중단됨)
    total_song_arr = []
    while play_minute >= len(total_song_arr):
        for song in song_arr:
            total_song_arr.append(song)
            if len(total_song_arr) == play_minute:
                return total_song_arr

    return total_song_arr


def solution(m, musicinfos):
    answer = '(None)'
    answer_minute = 0
    # 곡 순회
    for musicinfo in musicinfos:
        start_time, end_time, title, songs = musicinfo.split(',')

        # 시간 분리(시, 분)
        start_hour, start_minute = start_time.split(":")
        end_hour, end_minute = end_time.split(":")

        # 시간 -> 분 단위로 변경하여 재생된 분 구하기
        play_minute = (int(end_hour) - int(start_hour)) * 60 + (int(end_minute) - int(start_minute))

        # 곡 길이와 재생시간 비교하여 전체 재생된 곡 구하기
        song_arr = convertSongsToArr(songs)
        total_song_arr = getTotalSongArr(song_arr, play_minute)

        # m도 음 별로 분리(# 때문)
        m_arr = convertSongsToArr(m)
        # 전체 곡에 들은 음악(m)이 포함되어 있으면 title 반환
        m_length= len(m_arr)
        isMatch = any(total_song_arr[i:i+m_length] == m_arr for i in range(len(total_song_arr) - m_length + 1))
        if isMatch and play_minute > answer_minute:
            answer_minute = play_minute
            answer = title

    # 전체 곡에 들은 음악(m)이 포함되어 있으면 None 반환
    return answer