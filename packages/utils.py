import duckdb

DATABASE_NAME = 'database/UserLogDB.db'
DAYS_NUMBER = 2

conn = duckdb.connect(DATABASE_NAME)

def CALCULATE_USE_PERCENTAGE(days: int = DAYS_NUMBER, until: bool = False):
    comparator = '<=' if until else '='

    query = f"""
    WITH USER_LOGGED_DAYS AS (
    SELECT
    u.userid,
    MAX(CASE WHEN date_diff('day', u.created_at, le.logon_ts) {comparator} {days}  THEN 1 ELSE 0
        END
        ) AS FLG_LOGGED_DAYS
    FROM users u
    LEFT JOIN logon_events le ON u.userid = le.userid
    GROUP BY u.userid
    )
    SELECT 100*SUM(FLG_LOGGED_DAYS)/COUNT(*) AS PERCENTAGE FROM USER_LOGGED_DAYS;
    """
    df_users = conn.execute(query).df()

    return df_users['PERCENTAGE'][0]

def CALCULATE_USE_PERCENTAGE_WITH_AT_LEASE_TWO_LOGGINGS(days: int = DAYS_NUMBER, until: bool = False):
    comparator = '<=' if until else '='

    query = f"""
    WITH USER_LOGGED_DAYS AS (
    SELECT
    u.userid,
    SUM(CASE WHEN date_diff('day', u.created_at, le.logon_ts) {comparator} {days}  THEN 1 ELSE 0
        END
        ) AS LOGGED_DAYS
    FROM users u
    LEFT JOIN logon_events le ON u.userid = le.userid
    GROUP BY u.userid
    )
    SELECT 100*SUM(CASE WHEN LOGGED_DAYS >= 2 THEN 1 ELSE 0 END)/COUNT(*) AS PERCENTAGE FROM USER_LOGGED_DAYS;
    """
    df_users = conn.execute(query).df()

    return df_users['PERCENTAGE'][0]

def CALCULATE_USE_PERCENTAGE_WITH_AT_LEASE_TWO_LOGGINGS_FROM_LOGGED(days: int = DAYS_NUMBER, until: bool = False):
    comparator = '<=' if until else '='

    query = f"""
    WITH USER_LOGGED_DAYS AS (
    SELECT
    u.userid,
    SUM(CASE WHEN date_diff('day', u.created_at, le.logon_ts) {comparator} {days}  THEN 1 ELSE 0
        END
        ) AS LOGGED_DAYS
    FROM users u
    LEFT JOIN logon_events le ON u.userid = le.userid
    GROUP BY u.userid
    )
    SELECT 100*SUM(CASE WHEN LOGGED_DAYS >= 2 THEN 1 ELSE 0 END)/SUM(CASE WHEN LOGGED_DAYS > 0 THEN 1 ELSE 0 END) AS PERCENTAGE FROM USER_LOGGED_DAYS;
    """
    df_users = conn.execute(query).df()

    return df_users['PERCENTAGE'][0]

def CALCULATE_USE_PERCENTAGE_INACTIVE_USERS(days: int = DAYS_NUMBER, until: bool = False):
    comparator = '<=' if until else '='

    query = f"""
    WITH USER_LOGGED_DAYS AS (
    SELECT
    u.userid,
    SUM(CASE WHEN date_diff('day', u.created_at, le.logon_ts) {comparator} {days}  THEN 1 ELSE 0
        END
        ) AS LOGGED_DAYS
    FROM users u
    LEFT JOIN logon_events le ON u.userid = le.userid
    GROUP BY u.userid
    )
    SELECT 100*SUM(CASE WHEN LOGGED_DAYS = 0 THEN 1 ELSE 0 END)/COUNT(*) AS PERCENTAGE FROM USER_LOGGED_DAYS;
    """
    df_users = conn.execute(query).df()

    return df_users['PERCENTAGE'][0]
