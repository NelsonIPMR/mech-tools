import sys

def main():
    print("Worst-Case Tolerance Stack-Up Calculator")
    print("Please enter the nominal dimension, positive (+) tolerance, and negative (-) tolerance for 3 parts.")
    print("Note: Enter the negative tolerance as a positive number (e.g., enter 0.1 for -0.1).")

    max_length = 0.0
    min_length = 0.0
    nominal_length = 0.0

    for i in range(1, 4):
        print(f"\n--- Part {i} ---")
        try:
            nominal = float(input("Nominal dimension: "))
            pos_tol = float(input("Positive (+) tolerance: "))
            neg_tol = float(input("Negative (-) tolerance: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            sys.exit(1)

        nominal_length += nominal
        max_length += nominal + pos_tol
        min_length += nominal - neg_tol

    print("\n=== Worst-Case Stack-Up Results ===")
    print(f"Total Nominal Length:      {nominal_length:.4f}")
    print(f"Total Max Assembly Length: {max_length:.4f}")
    print(f"Total Min Assembly Length: {min_length:.4f}")

if __name__ == "__main__":
    main()
