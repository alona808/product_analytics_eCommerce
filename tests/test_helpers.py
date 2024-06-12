import sys
import os
import pandas as pd
import pandas as pd
# Set path
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the path to the root directory
import tools.helpers as hp


import tools.helpers as hp

def test_create_calendar_table():
    start_date = '2022-01-01'
    end_date = '2022-01-31'
    df = hp.create_calendar_table(start_date, end_date)
    
    assert isinstance(df, pd.DataFrame)
    assert 'date' in df.columns
    assert 'date_weekday' in df.columns
    assert 'day_of_week' in df.columns
    assert 'is_weekend' in df.columns
    assert 'abbreviated_weekday' in df.columns
    assert 'month_start' in df.columns
    assert 'month_num' in df.columns
    assert 'month_year' in df.columns
    assert 'quarter_number' in df.columns
    assert 'quarter_text' in df.columns
    assert 'year_start' in df.columns
    assert 'year' in df.columns
    assert df['date'].min() == pd.to_datetime(start_date)
    assert df['date'].max() == pd.to_datetime(end_date)
