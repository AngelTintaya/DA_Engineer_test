from packages import utils
import duckdb

print(utils.CALCULATE_USE_PERCENTAGE(2))
print(utils.CALCULATE_USE_PERCENTAGE(2, until=True))
print(utils.CALCULATE_USE_PERCENTAGE_WITH_AT_LEASE_TWO_LOGGINGS(2))
print(utils.CALCULATE_USE_PERCENTAGE_WITH_AT_LEASE_TWO_LOGGINGS_FROM_LOGGED(2))
print(utils.CALCULATE_USE_PERCENTAGE_INACTIVE_USERS(2))

DATABASE_NAME = 'database/UserLogDB.db'
DAYS_NUMBER = 2

conn = duckdb.connect(DATABASE_NAME)

# Creating Transformed Users Table
query = """
DROP TABLE IF EXISTS USERS_TRANSFORMED;

CREATE TABLE USERS_TRANSFORMED AS
SELECT
userid,
created_at,
MONTH(created_at)::INTEGER AS MONTH_CREATED,
YEAR(created_at)::INTEGER AS YEAR_CREATED,
DAY(created_at)::INTEGER AS DAY_CREATED,
HOUR(created_at)::INTEGER AS HOUR_CREATED,
FROM users;
"""
conn.execute(query)

# Creating Transformed Loggin Table
query = """
DROP TABLE IF EXISTS LOGON_EVENTS_TRANSFORMED;

CREATE TABLE LOGON_EVENTS_TRANSFORMED AS
SELECT
userid,
logon_ts,
MONTH(logon_ts)::INTEGER AS MONTH_LOGON,
YEAR(logon_ts)::INTEGER AS YEAR_LOGON,
DAY(logon_ts)::INTEGER AS DAY_LOGON,
HOUR(logon_ts)::INTEGER AS HOUR_LOGON,
FROM logon_events;
"""
conn.execute(query)
