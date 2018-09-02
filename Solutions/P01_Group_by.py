daily_data = trips_data.groupby('start_date_date').start_station_id.count().reset_index()
daily_data = daily_data.rename(columns={'start_station_id':'sum_trips'})
daily_data.head(30)
