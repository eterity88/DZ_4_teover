import math
import scipy.stats as stats

#Задание 4
#Рост взрослого населения города X имеет нормальное распределение.
#Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
#Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
#а) больше 182 см\n\
#б) больше 190 см\n\
#в) от 166 см до 190 см\n\
#г) от 166 см до 182 см\n\
#д) от 158 см до 190 см\n\
#е) не выше 150 см или не ниже 190 см\n\
#ё) не выше 150 см или не ниже 198 см\n\
#ж) ниже 166 см")

# из условий
M=174
σ=8
D=σ**2

print(f"Вероятность того, рост:\n\
а) больше 182 см: {1-stats.norm.cdf(182, loc=M, scale=D)}\n\
б) больше 190 см: {1-stats.norm.cdf(190, loc=M, scale=D)}\n\
в) от 166 см до 190 см: {stats.norm.cdf(190, loc=M, scale=D)-stats.norm.cdf(166, loc=M, scale=D)}\n\
г) от 166 см до 182 см: {stats.norm.cdf(182, loc=M, scale=D)-stats.norm.cdf(166, loc=M, scale=D)}\n\
д) от 158 см до 190 см: {stats.norm.cdf(190, loc=M, scale=D)-stats.norm.cdf(158, loc=M, scale=D)}\n\
е) не выше 150 см или не ниже 190 см: {stats.norm.cdf(150, loc=M, scale=D)+1-stats.norm.cdf(190, loc=M, scale=D)}\n\
ё) не выше 150 см или не ниже 198 см: {stats.norm.cdf(150, loc=M, scale=D)+1-stats.norm.cdf(198, loc=M, scale=D)}\n\
ж) ниже 166 см: {stats.norm.cdf(166, loc=M, scale=D)}\n\
")