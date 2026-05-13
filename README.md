# mech-tools
Trial project

## stackup.py
`stackup.py` is a Python script that calculates the worst-case tolerance stack-up for an assembly of 3 parts.

### How it works
The script will prompt the user to input the following for 3 distinct parts:
1. Nominal dimension
2. Positive (+) tolerance
3. Negative (-) tolerance (entered as a positive number, e.g., 0.1 for -0.1)

It then calculates:
- The Total Nominal Length
- The Total Max Assembly Length
- The Total Min Assembly Length

### How to run
Run the script using Python 3:
```bash
python stackup.py
```
