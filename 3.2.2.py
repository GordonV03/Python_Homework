import pandas as pd
from datetime import datetime


def to_fixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def sort_dict(dict_to_sort):
    sorted_tuples = sorted(dict_to_sort.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_tuples}
    sorted_dict = list(sorted_dict.items())[:10]
    return dict(sorted_dict)


pd.set_option('expand_frame_repr', False)

file = 'vacancies_by_year.csv'
vacancy = 'Веб-программист'
df = pd.read_csv(file)
df['published_at'] = df['published_at'].apply(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S%z').year)
years = df['published_at'].unique()

df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
cities = df['area_name'].unique()

salary_by_years = {year: [] for year in years}
vacancies_by_years = {year: 0 for year in years}
vac_salary_by_years = {year: [] for year in years}
vac_counts_by_years = {year: 0 for year in years}
cities_salary = {city: [] for city in cities}
cities_fraction = {city: 0 for city in cities}

for year in years:
    salary_by_years[year] = int(df[df['published_at'] == year]['salary'].mean())
    vacancies_by_years[year] = len(df[df['published_at'] == year])
    vac_salary_by_years[year] = int(df[(df['published_at'] == year) & (df['name'] == vacancy)]['salary'].mean())
    vac_counts_by_years[year] = len(df[(df['published_at'] == year) & (df['name'] == vacancy)])

for city in cities:
    cities_salary[city] = int(df[df['area_name'] == city]['salary'].mean())
    cities_fraction[city] = to_fixed(len(df[df['area_name'] == city])/(len(df.axes[0])), 4)

sorted_cities_salary = sort_dict(cities_salary)
sorted_cities_fraction = sort_dict(cities_fraction)

print('Динамика уровня зарплат по годам:', salary_by_years)
print('Динамика количества вакансий по годам:', vacancies_by_years)
print('Динамика уровня зарплат по годам для выбранной профессии:', vac_salary_by_years)
print('Динамика количества вакансий по годам для выбранной профессии:', vac_counts_by_years)
print('Уровень зарплат по городам (в порядке убывания):', sorted_cities_salary)
print('Доля вакансий по городам (в порядке убывания):', sorted_cities_fraction)