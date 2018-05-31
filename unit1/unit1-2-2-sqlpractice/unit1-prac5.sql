select
end_station,
avg(duration)
from
trips
group by end_station