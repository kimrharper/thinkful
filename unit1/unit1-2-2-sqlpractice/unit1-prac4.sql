select
start_station, 
count(start_station) station_count
from
trips
group by
start_station