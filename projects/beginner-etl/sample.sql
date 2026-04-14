-- Sample schema for beginner ETL project
-- 入門 ETL 專案範例 schema

CREATE TABLE IF NOT EXISTS raw_weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    temperature NUMERIC(5, 2),
    humidity NUMERIC(5, 2),
    description VARCHAR(255),
    recorded_at TIMESTAMP NOT NULL,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Idempotent load: delete and re-insert by date
-- 冪等載入：依日期刪除後重新插入
DELETE FROM raw_weather
WHERE recorded_at::date = CURRENT_DATE;

-- INSERT INTO raw_weather (city, temperature, humidity, description, recorded_at)
-- VALUES (...);
