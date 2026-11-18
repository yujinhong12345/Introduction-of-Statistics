# 통계학입문 과제 1 — 정규분포 (Python 학생용)
# 이름: 홍유진  학번: 2026101260
# 목표: 정규분포의 표준화, 확률, 분위수, 확률밀도 그래프를 계산함
# 실행 전: pip install numpy scipy matplotlib

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# [상황] 시험 점수 X는 평균 70점, 표준편차 10점의 정규분포를 따름
# X ~ N(70, 10^2)

# 문제 1. 평균(mu)과 표준편차(sigma)를 변수에 저장할 것
mu = 70      # TODO: 평균 70 입력
sigma = 10    # TODO: 표준편차 10 입력

# 문제 2. 85점의 Z-score를 계산할 것
# Z = (관측값 - 평균) / 표준편차
score = 85
z_score = (score-mu)/sigma  # TODO: 계산식 입력

# 문제 3. 80점 이상 받을 확률 P(X >= 80)을 구할 것
# stats.norm.cdf(x, loc=평균, scale=표준편차)는 P(X <= x)를 반환함
# stats.norm.sf(...)는 P(X > x)를 반환함 (연속형에서 >=도 동일)
p_above_80 = stats.norm.sf(80, loc=mu, scale=sigma)  # TODO: stats.norm.sf(...) 사용

# 문제 4. 60~80점 사이 확률 P(60 <= X <= 80)을 구할 것
# 힌트: P(X <= 80) - P(X <= 60)
p_60_to_80 = (stats.norm.cdf(80, loc=mu, scale=sigma) - stats.norm.cdf(60, loc=mu, scale=sigma))  # TODO

# 문제 5. 상위 5%에 해당하는 점수(95백분위수)를 구할 것
# stats.norm.ppf(확률, loc=평균, scale=표준편차)는 해당 분위수를 반환함
cutoff_top_5 = stats.norm.ppf(0.95, loc=mu, scale=sigma)  # TODO: 0.95 분위수

# 계산 결과 출력: 빈칸을 채우면 다음 코드로 확인할 수 있음
print('2. Z-score:', z_score)
print('3. P(X >= 80):', p_above_80)
print('4. P(60 <= X <= 80):', p_60_to_80)
print('5. 상위 5% 기준점:', cutoff_top_5)
# 계산 결과: 2. Z-score: 1.5
# 계산 결과: 3. P(X >= 80): 0.15865525393145707 (약 0.1587)
# 계산 결과: 4. P(60 <= X <= 80): 0.6826894921370859 (약 0.6827)
# 계산 결과: 5. 상위 5% 기준점: 86.44853626951472 (약 86.4485)

# 문제 6. 정규분포의 확률밀도함수 그래프를 그릴 것
# np.linspace(40, 100, 400)는 40~100 구간에서 400개 점을 생성함
# stats.norm.pdf(x, loc=..., scale=...)는 각 x에서 확률밀도를 계산함
# TODO를 채워 그래프를 완성할 것
# 주의: 확률밀도(세로축)는 특정 점에서의 확률 그 자체가 아님
if mu is not None and sigma is not None:
    x = np.linspace(40, 100, 400)
    y = stats.norm.pdf(x, loc=mu, scale=sigma)  # TODO: stats.norm.pdf(...) 사용
    if y is not None:
        plt.plot(x, y, label='Normal density')
        plt.axvline(mu, linestyle='--', label='Mean = 70')
        plt.title('Exam scores: Normal distribution')
        plt.xlabel('Score')
        plt.ylabel('Density')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.show()

# [서술] 위 결과가 뜻하는 바를 2~3문장으로 작성할 것
# 답: 시험 점수는 평균 70점, 표준편차 10점인 정규분포를 따르며, 85점의 Z-score는 1.5로 평균보다 표준편차 1.5배 높은 점수이다. 전체 학생 중 약 15.87%가 80점 이상을 받을 것으로 예상되며, 약 68.27%는 60점 이상 80점 이하에 해당한다. 또한 상위 5%에 해당하는 점수는 약 86.45점이다.
