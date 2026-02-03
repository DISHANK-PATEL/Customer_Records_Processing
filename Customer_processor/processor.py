from reader import read_csv
from validator import validate_record
from writer import write_clean_data
from logger import setup_logger
from config import INPUT_FILE, CLEAN_DATA_FILE

logger = setup_logger()

def get_age_group(age):
    age = int(age)
    if 18 <= age <= 25:
        return "18-25"
    elif 26 <= age <= 40:
        return "26-40"
    elif 41 <= age <= 60:
        return "41-60"
    else:
        return "60+"

def process_customers():
    try:
        records = read_csv(INPUT_FILE)
    except RuntimeError as error:
        logger.error(error)
        return None

    valid_records = []
    invalid_records = []
    failure_distribution = {}

    for record in records:
        errors = validate_record(record)

        if errors:
            invalid_records.append({
                "record": record,
                "errors": errors
            })

            for error in errors:
                failure_distribution[error] = failure_distribution.get(error, 0) + 1

            logger.error(f"{record} | Errors: {errors}")
        else:
            record["age_group"] = get_age_group(record["age"])
            record["email_domain"] = record["email"].split("@")[-1]
            valid_records.append(record)

    write_clean_data(CLEAN_DATA_FILE, valid_records)

    return {
        "total": len(records),
        "valid": valid_records,
        "invalid": invalid_records,
        "failure_distribution": failure_distribution
    }
