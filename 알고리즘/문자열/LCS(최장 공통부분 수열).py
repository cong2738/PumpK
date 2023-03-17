import sys
readline = sys.stdin.readline
class LCS:
    def __init__(self) -> None:
        self.A, self.B = readline().rstrip(), readline().rstrip()

    #문자열의 뭉탱이들을 반환
    def LCS(self)->list[list[str]]:
        #memorize
        LCS = [[str() for _ in range(len(self.B)+1)] for _ in range(len(self.A)+1)]

        for i in range(len(self.A)):
            for j in range(len(self.B)):
                if self.A[i] == self.B[j]: LCS[i+1][j+1] = LCS[i][j] + self.A[i]
                else: LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j], key=lambda x:len(x))

        return LCS

    # 길이만 반환
    def LCS_length(self)->list[list[int]]:
        #memorize
        LCS = [[0 for _ in range(len(self.B)+1)] for _ in range(len(self.A)+1)]

        for i in range(len(self.A)):
            for j in range(len(self.B)):
                if self.A[i] == self.B[j]: LCS[i+1][j+1] = LCS[i][j] + 1
                else: LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])

        return LCS

#예시일뿐이니 하나만써라.
C = LCS()
print(C.LCS()[-1][-1])
print(C.LCS_length()[-1][-1])