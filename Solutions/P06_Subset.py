null_rows = trips_data.loc[trips_data.isnull().any(axis=1)]
null_rows['end_station_name'].unique()