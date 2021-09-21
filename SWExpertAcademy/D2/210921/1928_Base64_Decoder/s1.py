import sys
sys.stdin = open('input.txt')
'''
[문제]
1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.
입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.
[제약사항]
문자열의 길이는 항상 4의 배수로 주어진다.
그리고 문자열의 길이는 100000을 넘지 않는다.

[풀이과정]
 1. 24비트 버퍼에 1byte씩 3byte의 문자를 집어넣지만 Encoding과정에서 6비트씩 잘라 읽으므로 4개의 문자가 나온다. input:3, output:4 => input:4, output:3
 2. Encoding된 문자를 4개씩 짝지어서 비트로 바꾼 후 8비트씩 잘라서 decoding 하기
'''
T = int(input())
for tc in range(1,T+1):
    # Base64 Encoding 문자열에 매치되는 숫자 dict
    base64_Encoding = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
                       'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
                       'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,
                       'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,
                       'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,
                       'z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,
                       '9':61,'+':62,'/':63}
    encoding_strs = input()    # Base64 Encoding 된 String
    temp_nums = []
    result = ''

    # 1. Base64 Encoding 된 encodeing_strs를 4단어씩 끊어서 숫자로 변환하는 과정
    # => encoding된 output이 4개이므로 4개씩 끊는것임
    for i in range(0, len(encoding_strs),4):
        # 1-1. 해당 문자를 Base64 Encoding된 문자열에 매칭되는 숫자로 변환하기
        for j in encoding_strs[i:i+4]:
            word_num = str(bin(base64_Encoding.get(j))[2:])     # 1-2. 변환한 숫자를 2진수로 변환
            if len(word_num) < 6:
                word_num = '0'*(6 - len(word_num)) + word_num   # 1-3. 6자리 수를 맞춰주기 위해 길이가 6이하면 앞자리에 '0'채워주기
            temp_nums.append(word_num)                          # temp_nums에 해당 2진수를 담기

    # 2. encoding된 output 4개를 input 3개로 돌리는 과정
    for m in range(0, len(temp_nums), 4):
        temp_numbers = ''.join(temp_nums[m:m+4])        # 2-1. 6bit씩 4묶음의 2진수를 하나의 24bit로 만들기
        for n in range(0, len(temp_numbers), 8):        # 2-2. 24bit를 8bit씩 끊은 후 해당 8bit를 10진수로 변환
            chr_str = int(temp_numbers[n:n+8],2)
            if chr_str > 127 :  # 10진수가 127을 초과하면 128 빼기
                chr_str -= 128
            result += chr(chr_str)                      # 2-3. 아스키코드를 문자열로 변환

    print('#{} {}'.format(tc, result))