import pandas as pd
from datetime import datetime

# pd.set_option('expand_frame_repr', None)
# pd.set_option('display.max_column', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.float_format', '{:.4f}'.format)

file = 'vacancies_by_year.csv'


class SortByYears:

    @staticmethod
    def sorter(df):
        years = df['years'].unique()
        for year in years:
            data = df[df['years'] == year]
            data[['name', 'salary_from', 'salary_to', 'salary_currency',
                  'area_name', 'published_at']].to_csv(f'csv_files\part_{year}.csv', index=False)

    @staticmethod
    def data_prepare(filename):
        df = pd.read_csv(filename)
        df['years'] = df['published_at'].apply(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S%z').year)
        return df


df = SortByYears.data_prepare(file)
SortByYears.sorter(df)

print(df.head(10))