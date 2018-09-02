daily_data_hour = trips_data.groupby(['start_date_date','start_dow','start_hour']).start_station_id.count().reset_index()

daily_data_hour = daily_data_hour.rename(columns={'start_station_id':'sum_trips'})

daily_data_hour.groupby(['start_dow','start_hour']).sum_trips.agg(['mean','median']).reset_index()