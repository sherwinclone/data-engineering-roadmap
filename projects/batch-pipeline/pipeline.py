"""
Batch Pipeline Example 批次管線範例

A simple Bronze → Silver → Gold pipeline skeleton.
簡單的 Bronze → Silver → Gold 管線骨架。
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def extract(source_path: str) -> list[dict]:
    """Extract: read raw data from source 擷取：從來源讀取原始資料"""
    logger.info(f"Extracting from {source_path}")
    # TODO: implement file reading
    return []


def load_bronze(data: list[dict]) -> int:
    """Load raw data into Bronze layer 將原始資料載入 Bronze 層"""
    logger.info(f"Loading {len(data)} rows into Bronze")
    # TODO: implement Bronze load
    return len(data)


def transform_silver(bronze_data: list[dict]) -> list[dict]:
    """Transform: clean and deduplicate 轉換：清洗與去重"""
    logger.info("Transforming Bronze → Silver")
    # TODO: implement cleaning logic
    return bronze_data


def aggregate_gold(silver_data: list[dict]) -> list[dict]:
    """Aggregate into Gold layer 聚合為 Gold 層"""
    logger.info("Aggregating Silver → Gold")
    # TODO: implement aggregation
    return silver_data


def validate_row_count(step: str, expected_min: int, actual: int) -> None:
    """Validate row count between steps 驗證步驟間的 row count"""
    if actual < expected_min:
        raise ValueError(
            f"Row count check failed at {step}: "
            f"expected >= {expected_min}, got {actual}"
        )
    logger.info(f"Row count check passed at {step}: {actual} rows")


def run():
    """Run the full pipeline 執行完整管線"""
    raw = extract("data/input.csv")
    bronze_count = load_bronze(raw)
    validate_row_count("bronze", expected_min=1, actual=bronze_count)

    silver = transform_silver(raw)
    validate_row_count("silver", expected_min=1, actual=len(silver))

    gold = aggregate_gold(silver)
    validate_row_count("gold", expected_min=1, actual=len(gold))

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run()
