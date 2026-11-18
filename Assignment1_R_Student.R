# 통계학입문 과제 1 — 정규분포 (R 학생용)
# 이름: 홍유진  학번: 2026101260
# 목표: 정규분포의 표준화, 확률, 분위수, 확률밀도 그래프를 계산함
# 별도의 패키지 설치 없이 base R만 사용함

# [상황] 시험 점수 X는 평균 70점, 표준편차 10점의 정규분포를 따름
# X ~ N(70, 10^2)

# 문제 1. 평균과 표준편차를 저장할 것
mu <- 70       # TODO: 70으로 수정
sigma <- 10    # TODO: 10으로 수정

# 문제 2. 85점의 Z-score를 계산할 것
score <- 85
z_score <- (score - mu) / sigma  # TODO: (score - mu) / sigma

# 문제 3. P(X >= 80)을 계산할 것
# pnorm(x, mean=..., sd=...)는 P(X <= x)를 반환함
# lower.tail=FALSE를 지정하면 오른쪽 꼬리확률을 반환함
p_above_80 <- pnorm(80, mean=mu, sd=sigma, lower.tail=FALSE)  # TODO: pnorm(..., lower.tail=FALSE)

# 문제 4. P(60 <= X <= 80)을 계산할 것
p_60_to_80 <- pnorm(80, mean=mu, sd=sigma) - pnorm(60, mean=mu, sd=sigma)   # TODO: 두 누적확률의 차이

# 문제 5. 상위 5% 경계 점수(95백분위수)를 구할 것
# qnorm(확률, mean=..., sd=...)는 분위수를 반환함
cutoff_top_5 <- qnorm(0.95, mean=mu, sd=sigma)  # TODO

cat('2. Z-score:', z_score, '\n')
cat('3. P(X >= 80):', p_above_80, '\n')
cat('4. P(60 <= X <= 80):', p_60_to_80, '\n')
cat('5. 상위 5% 기준점:', cutoff_top_5, '\n')
# 계산 결과: 2. Z-score: 1.5
# 계산 결과: 3. P(X >= 80): 0.1586553 (약 0.1587)
# 계산 결과: 4. P(60 <= X <= 80): 0.6826895 (약 0.6827)
# 계산 결과: 5. 상위 5% 기준점: 86.44854 (약 86.4485)

# 문제 6. 정규분포 확률밀도 그래프를 작성할 것
# seq(40, 100, length.out=400)는 일정 간격으로 400개 점을 생성함
# dnorm(x, mean=..., sd=...)는 확률밀도를 반환함
if (!is.na(mu) && !is.na(sigma)) {
  x <- seq(40, 100, length.out=400)
  y <- dnorm(x, mean=mu, sd=sigma)  # TODO: dnorm(...) 사용
  if (!all(is.na(y))) {
    plot(x, y, type='l', lwd=2, main='Exam scores: Normal distribution',
         xlab='Score', ylab='Density')
    abline(v=mu, lty=2)
    legend('topright', legend=c('Normal density', 'Mean = 70'),
           lty=c(1, 2), bty='n')
  }
}

# [서술] 결과를 2~3문장으로 해석할 것
# 답: 시험 점수는 평균 70점, 표준편차 10점인 정규분포를 따르며, 85점의 Z-score는 1.5로 평균보다 표준편차 1.5배 높은 점수이다. 전체 학생 중 약 15.87%가 80점 이상을 받을 것으로 예상되며, 약 68.27%는 60점 이상 80점 이하에 해당한다. 또한 상위 5%에 해당하는 점수는 약 86.45점이다.
