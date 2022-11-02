# logs = ["digi1 8 1 5 1","let1 art can", "digi2 3 6", "let2 own kit dig", "let3 art zero"]
# 로그를 재정렬하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자이다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력대로 한다.
def log_sep (logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
                digits.append(log)
        else:
                letters.append(log)
    letters.sort(key= lambda x: (x.split()[1], x.split()[0]))
    return letters+digits

logs = ["digi1 8 1 5 1","let1 art can", "digi2 3 6", "let2 own kit dig", "let3 art zero"]
result = log_sep(logs)
print(result)