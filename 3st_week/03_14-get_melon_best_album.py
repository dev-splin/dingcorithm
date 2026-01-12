from collections import deque


def get_melon_best_album(genre_array, play_array):
    dict = {}

    for i in range(len(genre_array)):
        key = genre_array[i]
        if key in dict:
            dict[key][0] += play_array[i]
            dict[key][1].append([i, play_array[i]])
        else:
            arr = []
            arr.append([i, play_array[i]])
            dict[key] = [play_array[i], arr]

    sums = []
    for key in dict.keys():
        sum = dict[key][0]
        sums.append(sum)

    sums.sort(reverse=True)

    result = []
    for sum in sums:
        for key in dict.keys():
            if sum != dict[key][0]:
                continue

            arr = dict[key][1]
            arr.sort(key=lambda x: (x[1], -x[0]))
            count = 0
            while arr:
                if count >= 2:
                    break

                result.append(arr.pop()[0])
                count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))