import pandas as pd

data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

################################################################

print("[ Project 2-1-1 ]")

for year in range(2015, 2019):
    year_data = data[data['year'] == year]
    print(f"\n--------- {year}년 ---------")

    for category in ['H', 'avg', 'HR', 'OBP']:
        top10 = year_data.nlargest(10, category)
        print(f"Category {category}:")
        for _, row in top10.iterrows():
            # 부동소수점 오류가 발생하여 소수점 넷째 자리에서 반올림
            value = round(row[category], 4)
            print(f"{row['batter_name']:10}\t{value}")

################################################################

print("\n[ Project 2-1-2 ]")

data_2018 = data[data['year'] == 2018]

positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
for pos in positions:
    best = data_2018[data_2018['cp'] == pos].nlargest(1, 'war').reset_index(drop=True)
    print(f"\n{pos} 승리 기여도 1등:")
    for _, row in best.iterrows():
        print(f"{row['batter_name']:10}\t{row['war']:.3f}")
        
################################################################

print("\n[ Project 2-1-3 ]")

target = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']

cor_matrix = data[target].corr()

cor_salary = cor_matrix['salary'].drop('salary')

highest_stat = cor_salary.idxmax()
highest_value = cor_salary.max()

print(f"연봉과 가장 높은 상관관계를 가지는 지표:\n{highest_stat} (상관관계: {highest_value:.3f})")