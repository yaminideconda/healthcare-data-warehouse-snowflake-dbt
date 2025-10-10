with base as (
    select * from {{ ref('stg_claims') }}
)
select
    provider_id,
    count(distinct claim_id) as total_claims,
    sum(amount) as total_amount,
    round(avg(amount), 2) as avg_claim_amount
from base
group by provider_id
order by total_amount desc
