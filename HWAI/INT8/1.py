import sys
import math



def round(x):
    x_curly = x - math.floor(x)
    if x_curly < 1/2:
        return math.floor(x)
    if x_curly > 1/2:
        return math.floor(x) + 1
    return 2 * math.floor((x + 1) / 2) 

def clamp(n, min_, max_):
    if n < min_:
        return min_
    if n > max_:
        return max_
    return n

def quant(v, scale, min_):
    if type(v[0]) == list:
        row = len(v)
        col = len(v[0]) 
        return [ 
                [clamp(round((v[r][c] - min_) / scale) - 128, -128, 127) for c in range(col)]
                for r in range(row)
            ]
    else:
        col = len(v)
        return [ 
                clamp(round((v[c] - min_) / scale) - 128, -128, 127) 
                for c in range(col)
            ]
    
def dequant(v, scale, min_):
    if type(v[0]) == list:
        row = len(v)
        col = len(v[0]) 
        return [ 
                [(v[r][c] + 128) * scale + min_ for c in range(col)]
                for r in range(row)
            ]
    else:
        col = len(v)
        return [ 
                (v[c] + 128) * scale + min_
                for c in range(col)
            ]
    


# s = [[1,2,3], 
#      [4,5,6], 
#      [7,8,9]]
# st = transpose(s)
# print(st)

# s1 = [[1,2,3,4], 
#       [5,6,7,8]]
# s1t = transpose(s1)
# print(s1t)
def transpose(x):
    m = len(x)
    n = len(x[0])
    xt = [[0] * m for _ in range(n)]
    for row in range(m):
        for col in range(n):
            xt[col][row] = x[row][col]
    return xt

def matmul(x, w):
    result = [0.0] * len(w[0])
    for col in range(len(w[0])):
        for row in range(len(x)):
            result[col] += x[row] * w[row][col]
    return result
            




def main():
    data = sys.stdin.readline
    n = int(data())
    x = list(map(float, data().split()))
    m, n1 = list(map(int, data().split()))
    w = list(list(map(float, data().split())) for _ in range(m))
    # print(n)
    # print(x)
    # print(m, n1)
    # print(w)
    ################-------quant&dequant-------##########################
    min_x = min(x)
    max_x = max(x)
    min_w = min(min(v for v in row) for row in w)
    max_w = max(max(v for v in row) for row in w)
    if min_x == max_x:
        scale_x = 0
        x_quant = [-128] * n
        x_dequant = [min_x] * n
    else:
        scale_x = (max_x - min_x) / 255
        x_quant = quant(x, scale_x, min_x)
        x_dequant = dequant(x_quant, scale_x, min_x)
    if min_w == max_w:
        scale_w = 0
        w_quant = [[-128] * n1 for _ in range(m)]
        w_dequant = [[min_w] * n1 for _ in range(m)]
    else:
        scale_w = (max_w - min_w) / 255
        w_quant = quant(w, scale_w, min_w)
        w_dequant =  dequant(w_quant, scale_w, min_w)

    #############################################################

    
    quant_result = map(int, matmul(x_quant, transpose(w_quant)))

    Y_float = matmul(x, transpose(w))
    Y_dequant = matmul(x_dequant, transpose(w_dequant))
    mse = sum((Y_dequant[i] - Y_float[i]) ** 2 for i in range(m)) / m

    print(*quant_result)
    print(int(math.floor(mse * 100000 + 0.5)))

    
    


if __name__ == "__main__":
    main()