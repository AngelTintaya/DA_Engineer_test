# %%
import duckdb

# %%
DATABASE_NAME = 'database/UserLogDB.db'
conn = duckdb.connect(DATABASE_NAME)

#%%
query = """
SELECT
u.userid,
MAX(CASE
        WHEN date_diff('day', u.created_at, le.logon_ts) = 2  THEN 1 ELSE 0
    END
   ) AS FLG_LOGGED_SECOND_DAY
FROM users u
LEFT JOIN logon_events le ON u.userid = le.userid
GROUP BY u.userid
"""
df_users = conn.execute(query).df()

# %%
query = """
WITH USER_LOGGED_DAYS AS (
  SELECT
  u.userid,
  MAX(CASE
        WHEN date_diff('day', u.created_at, le.logon_ts) = 2  THEN 1 ELSE 0
        END
    ) AS FLG_LOGGED_SECOND_DAY
  FROM users u
  LEFT JOIN logon_events le ON u.userid = le.userid
  GROUP BY u.userid
)
SELECT 100*SUM(FLG_LOGGED_SECOND_DAY)/COUNT(1) AS PERCENTAGE FROM USER_LOGGED_DAYS;
"""
df_users = conn.execute(query).df()
df_users

# %%
