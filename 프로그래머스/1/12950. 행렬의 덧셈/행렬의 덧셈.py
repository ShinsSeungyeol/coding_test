def solution(arr1, arr2):
    w, h = len(arr1[0]), len(arr1)
    answer = [[arr1[i][j] + arr2[i][j] for j in range(w)] for i in range(h)]

    return answer