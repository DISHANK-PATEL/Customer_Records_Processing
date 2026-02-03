from processor import process_customers

def print_valid_records(records):
    print("\nVALID RECORDS")
    print("-------------")
    for record in records:
        print(record)

def print_invalid_records(records):
    print("\nINVALID RECORDS (With Reasons)")
    print("------------------------------")
    for item in records:
        print(f"Record: {item['record']}")
        print(f"Reason: {'  , '.join(item['errors'])}")
        print("-" * 40)

def print_failure_distribution(distribution):
    print("\nValidation Failure Distribution")
    print("-------------------------------")
    for reason, count in distribution.items():
        print(f"{reason:25} : {count}")

def filter_by_age_group(records):
    group = input("Enter age group (18-25, 26-40, 41-60, 60+): ")
    filtered = [r for r in records if r["age_group"] == group]

    print(f"\nRecords in age group {group}")
    print("----------------------------")
    for r in filtered:
        print(r)

def filter_by_email_suffix(records):
    suffix = input("Enter email suffix (e.g. gmail.com): ")
    filtered = [r for r in records if r["email_domain"] == suffix]

    print(f"\nRecords with email domain {suffix}")
    print("--------------------------------")
    for r in filtered:
        print(r)

def main():
    result = process_customers()

    if result is None:
        print("Processing failed. Check logs.")
        return

    valid_records = result["valid"]
    invalid_records = result["invalid"]

    print("Processing Summary")
    print("------------------")
    print(f"Total records   : {result['total']}")
    print(f"Valid records   : {len(valid_records)}")
    print(f"Invalid records : {len(invalid_records)}")

    print_failure_distribution(result["failure_distribution"])

    while True:
        print("\nOptions:")
        print("1. Show all valid records")
        print("2. Show all invalid records with reasons")
        print("3. View valid records by age group")
        print("4. View valid records by email suffix")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print_valid_records(valid_records)
        elif choice == "2":
            print_invalid_records(invalid_records)
        elif choice == "3":
            filter_by_age_group(valid_records)
        elif choice == "4":
            filter_by_email_suffix(valid_records)
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

