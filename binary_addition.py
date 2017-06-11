def binary_addition(str1, str2):
    bin1 = list(str1)
    bin2 = list(str2)

    bin1.reverse()
    bin2.reverse()

    maxlen = max(len(bin1), len(bin2))
    minlen = min(len(bin1), len(bin2))

    if len(bin1) == maxlen:
        bin_long = bin1
        bin_short = bin2
    else:
        bin_long = bin2
        bin_short = bin1

    bin_long = map(lambda x : int(x),bin_long )
    bin_short = map(lambda x : int(x),bin_short)

    residual = 0
    output_arr = []
    for i in range(maxlen):
        if i < minlen:
            partII = bin_short[i]
        else:
            partII = 0
        if bin_long[i] + partII + residual == 2:
            output_arr.append('0')
            residual = 1
        else:
            output_arr.append('1')
            residual = 0
    output_arr.append(str(residual))

    output_bin = ''
    for i in range(len(output_arr)):
        output_bin = output_arr[i] + output_bin
    return output_bin

if __name__ == "__main__":
    str1 = "10111"
    str2 = "1001"
    print binary_addition(str1, str2)