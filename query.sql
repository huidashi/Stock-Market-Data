select *
from (
  select name, ts,high, max(high) over (partition by name) as max_high
  from sta9760s2021stream01) t
 where high = max_high