def power_ranger(n, a, b):
    numRange = range(a, b)
    roots = []
    output = "#   "
    for num in numRange:
        root = num ** (1.0/n)
        if not root%1: roots.append([int(root), num])
    if roots:
        if n == 2:output += str(len(roots)) + " squares (n^2) lie between " + str(a) + " " + str(b) + ","
        elif n == 3: output += str(len(roots)) + " cubes (n^3) lie between " + str(a) + " " + str(b) + ","
        else: output += str(len(roots)) + " value raised to the " + str(n) + " power lies between " + str(a) + " " + str(b) + ","
        for x in roots:
            output +=  " " + str(x[1]) + "(" + str(x[0]) + "^" + str(n) + "), "
    else: output = "No values found"
    return output


if __name__ == "__main__":
    inFile = open('power_input.txt', 'r')
    nums = inFile.readlines()
    inFile.close()
    outFile = open('LazyGirlChallengeOutput.txt', 'w')
    for num in nums:
        input = num.split(',')
        print(power_ranger(int(input[0]), int(input[1]), int(input[2])), file=outFile)
    outFile.close();
