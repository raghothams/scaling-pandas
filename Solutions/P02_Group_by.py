daily_data_dow = trips_data.groupby(['start_date_date','start_dow']).start_station_id.count().reset_index()

daily_data_dow = daily_data_dow.rename(columns={'start_station_id':'sum_trips'})

daily_data_dow.groupby('start_dow').sum_trips.agg(['mean','median']).reset_index()