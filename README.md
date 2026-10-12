# Password Strength Analyzer

A lightweight Python-based password strength analysis utility designed to evaluate password complexity, identify common weaknesses, and provide recommendations for improving password security. The application examines password length, character composition, commonly used passwords, repeated characters, and predictable sequences to generate a numerical strength score.

This project demonstrates fundamental cybersecurity concepts, including password complexity evaluation, pattern detection, input validation, and rule-based security assessment.

## Features

- Password strength evaluation using a 100-point scoring system
- Password length verification against minimum and recommended thresholds
- Uppercase and lowercase character detection
- Numeric and special character detection
- Common password identification using a predefined password list
- Detection of excessive character repetition
- Detection of selected predictable password sequences
- Automatic strength classification into five categories
- Personalized password improvement recommendations
- Hidden password input using Python's getpass module
- Interactive command-line interface supporting multiple evaluations
- Local password processing without persistent storage
- Support for Windows, Linux, and macOS
- No external dependencies required

## Tech Stack

- Python 3
- Getpass
- Regular Expressions (re)
- String Processing
- Conditional Logic
- Command-Line Interface
- Git & GitHub

## Project Structure

```text
password-strength-analyzer/
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

Python cache files, virtual environments, environment configuration files, and temporary development artifacts are excluded from version control through `.gitignore`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Hinod3suuu/password-strength-analyzer.git
cd password-strength-analyzer
```

No additional Python packages are required.

## Usage

Run the application with:

```bash
python main.py
```

On Windows, the Python launcher can also be used:

```powershell
py main.py
```

The application displays an interactive password input prompt.

```text
=============================================
          PASSWORD STRENGTH ANALYZER
=============================================

Evaluate your password's strength.
Passwords are not stored or logged.

Enter password:
```

Password input is hidden using Python's `getpass` module to prevent characters from appearing in the terminal.

After entering a password, the application evaluates its characteristics and displays a detailed security report.

### Weak Password Example

A short numeric password containing a predictable sequence produces a low strength score.

Example:

```text
=============================================
          PASSWORD ANALYSIS RESULTS
=============================================

Password Strength: VERY WEAK
Strength Score:    5/100

---------------------------------------------
SECURITY CHECKS
---------------------------------------------
[FAIL] Minimum length (8 characters)
[FAIL] Recommended length (12 characters)
[FAIL] Uppercase letters
[FAIL] Lowercase letters
[PASS] Numbers
[FAIL] Special characters
[PASS] Not a common password
[PASS] No excessive repetition
[FAIL] No predictable sequences

---------------------------------------------
RECOMMENDATIONS
---------------------------------------------
1. Use at least 12 characters.
2. Avoid predictable sequences.
3. Include uppercase letters.
4. Include lowercase letters.
5. Include special characters.

=============================================
```

The example demonstrates how the application identifies insufficient password length, missing character categories, and predictable sequences.

### Strong Password Example

A longer password containing uppercase letters, lowercase letters, numbers, and special characters can achieve the maximum score when no predefined weaknesses are detected.

Example:

```text
=============================================
          PASSWORD ANALYSIS RESULTS
=============================================

Password Strength: VERY STRONG
Strength Score:    100/100

---------------------------------------------
SECURITY CHECKS
---------------------------------------------
[PASS] Minimum length (8 characters)
[PASS] Recommended length (12 characters)
[PASS] Uppercase letters
[PASS] Lowercase letters
[PASS] Numbers
[PASS] Special characters
[PASS] Not a common password
[PASS] No excessive repetition
[PASS] No predictable sequences

---------------------------------------------
RECOMMENDATIONS
---------------------------------------------
No immediate improvements suggested.

=============================================
```

The application allows additional passwords to be evaluated without restarting the program.

## Password Analysis Process

When a password is submitted, the application:

1. Accepts password input through the `getpass` module.
2. Verifies that the submitted password is not empty.
3. Calculates the password length.
4. Checks for uppercase and lowercase characters.
5. Identifies numeric and special characters.
6. Compares the password against a predefined list of common passwords.
7. Detects excessive repetition of identical characters.
8. Searches for selected predictable sequences.
9. Calculates a numerical strength score.
10. Applies penalties for detected weaknesses.
11. Classifies the password into a strength category.
12. Generates recommendations based on failed security checks.
13. Displays the analysis results in the terminal.

This provides a practical demonstration of rule-based password analysis and basic password security assessment.

## Strength Scoring System

The application calculates password strength using a weighted scoring system.

Password length contributes up to 40 points:

| Password Length | Points |
|---|---|
| Fewer than 8 characters | 5 |
| 8–11 characters | 20 |
| 12–15 characters | 30 |
| 16 or more characters | 40 |

Character variety contributes additional points:

| Character Category | Points |
|---|---|
| Uppercase letters | 15 |
| Lowercase letters | 15 |
| Numbers | 15 |
| Special characters | 15 |

The maximum score before penalties is 100 points.

Additional penalties are applied when weaknesses are detected:

| Security Weakness | Penalty |
|---|---|
| Common password | Score capped at 10 |
| Excessive character repetition | -10 |
| Predictable sequence | -15 |

The final score is restricted to the range of 0–100.

### Strength Classification

The calculated score determines the password's strength category.

| Score | Classification |
|---|---|
| 0–29 | VERY WEAK |
| 30–49 | WEAK |
| 50–69 | MODERATE |
| 70–84 | STRONG |
| 85–100 | VERY STRONG |

These classifications represent the application's rule-based assessment rather than a cryptographic measurement of password strength.

## Common Password Detection

The application maintains a predefined collection of commonly used passwords.

Examples include:

- password
- password123
- 123456
- 12345678
- qwerty
- admin
- letmein
- welcome

Password comparisons are performed without case sensitivity.

When a password matches an entry in the predefined collection, its score is capped at 10 points before applicable pattern penalties.

The current implementation uses a limited built-in collection rather than an external password breach database.

## Pattern Detection

The application uses regular expressions and string matching to identify selected password weaknesses.

### Character Repetition

The analyzer detects three or more identical consecutive characters.

Examples:

```text
aaa
111
!!!
```

Passwords containing excessive repetition receive a 10-point penalty.

### Predictable Sequences

The analyzer checks for selected predictable patterns.

Examples:

```text
1234
abcd
qwerty
password
```

Passwords containing these sequences receive a 15-point penalty.

Pattern detection is limited to the predefined rules and does not identify every possible predictable password structure.

## Security

The application processes passwords locally without requiring network access or external services.

Password input is handled through Python's `getpass` module, preventing entered characters from being displayed in the terminal under normal supported conditions.

The application does not intentionally write passwords to files, databases, or persistent logs.

No password information is transmitted to external servers.

However, password values are temporarily held in application memory during analysis.

The scoring system is intended for educational purposes and should not be treated as a comprehensive password security assessment.

A high score does not guarantee resistance against dictionary attacks, credential stuffing, or other password-related attacks.

For real-world account security, unique randomly generated passwords, reputable password managers, and multi-factor authentication are recommended.

## Limitations

- Password strength is estimated using predefined rules rather than statistical entropy calculations.
- Common password detection relies on a limited built-in password collection.
- The application does not check passwords against known data breach databases.
- Predictable sequence detection is limited to predefined patterns.
- Character variety is evaluated using basic character categories.
- The scoring system does not account for every form of password predictability.
- A maximum score does not guarantee that a password is secure.
- Passwords are analyzed individually without persistent history.
- Password recommendations are based on detected rule violations.
- The application does not perform password cracking or attack simulations.

## Future Improvements

Potential extensions include expanded common-password dictionaries, configurable password policies, entropy estimation, improved sequence detection, and more advanced password pattern recognition.

Additional improvements could include optional integration with password breach checking services, automated unit testing, configurable scoring weights, and more detailed security recommendations.

Further enhancements may include a graphical user interface, password generation functionality, and support for passphrase evaluation.

## Author

**Hinod3suuu**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.