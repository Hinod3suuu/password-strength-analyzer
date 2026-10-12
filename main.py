import getpass
import re


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
}


def analyze_password(password):
    score = 0
    suggestions = []
    checks = {}

    # Check password length
    length = len(password)

    checks["Minimum length (8 characters)"] = length >= 8
    checks["Recommended length (12 characters)"] = length >= 12

    if length >= 16:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        score += 5
        suggestions.append("Use at least 12 characters.")

    # Check character variety
    checks["Uppercase letters"] = bool(re.search(r"[A-Z]", password))
    checks["Lowercase letters"] = bool(re.search(r"[a-z]", password))
    checks["Numbers"] = bool(re.search(r"\d", password))
    checks["Special characters"] = bool(
        re.search(r"[^A-Za-z0-9]", password)
    )

    for check in [
        "Uppercase letters",
        "Lowercase letters",
        "Numbers",
        "Special characters",
    ]:
        if checks[check]:
            score += 15

    # Detect common passwords
    is_common = password.lower() in COMMON_PASSWORDS

    checks["Not a common password"] = not is_common

    if is_common:
        score = min(score, 10)
        suggestions.append("Avoid commonly used passwords.")

    # Detect repeated characters
    has_repetition = bool(re.search(r"(.)\1{2,}", password))

    checks["No excessive repetition"] = not has_repetition

    if has_repetition:
        score -= 10
        suggestions.append("Avoid repeating characters.")

    # Detect predictable sequences
    sequences = [
        "1234",
        "abcd",
        "qwerty",
        "password",
    ]

    has_sequence = any(
        sequence in password.lower()
        for sequence in sequences
    )

    checks["No predictable sequences"] = not has_sequence

    if has_sequence:
        score -= 15
        suggestions.append("Avoid predictable sequences.")

    # Generate improvement suggestions
    if length < 12 and length >= 8:
        suggestions.append("Consider using at least 12 characters.")

    if not checks["Uppercase letters"]:
        suggestions.append("Include uppercase letters.")

    if not checks["Lowercase letters"]:
        suggestions.append("Include lowercase letters.")

    if not checks["Numbers"]:
        suggestions.append("Include numbers.")

    if not checks["Special characters"]:
        suggestions.append("Include special characters.")

    # Keep score within valid range
    score = max(0, min(score, 100))

    # Determine strength
    if score >= 85:
        strength = "VERY STRONG"
    elif score >= 70:
        strength = "STRONG"
    elif score >= 50:
        strength = "MODERATE"
    elif score >= 30:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"

    return score, strength, checks, suggestions


def display_results(score, strength, checks, suggestions):
    print("\n" + "=" * 45)
    print("          PASSWORD ANALYSIS RESULTS")
    print("=" * 45)

    print(f"\nPassword Strength: {strength}")
    print(f"Strength Score:    {score}/100")

    print("\n" + "-" * 45)
    print("SECURITY CHECKS")
    print("-" * 45)

    for check, passed in checks.items():
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {check}")

    print("\n" + "-" * 45)
    print("RECOMMENDATIONS")
    print("-" * 45)

    if suggestions:
        for index, suggestion in enumerate(suggestions, 1):
            print(f"{index}. {suggestion}")
    else:
        print("No immediate improvements suggested.")

    print("\n" + "=" * 45)


def main():
    print("=" * 45)
    print("          PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    print("\nEvaluate your password's strength.")
    print("Passwords are not stored or logged.\n")

    while True:
        password = getpass.getpass("Enter password: ")

        if not password:
            print("\n[ERROR] Password cannot be empty.")
            continue

        score, strength, checks, suggestions = analyze_password(
            password
        )

        display_results(score, strength, checks, suggestions)

        choice = input("\nAnalyze another password? (y/n): ")
        choice = choice.strip().lower()

        if choice != "y":
            print("\nThank you for using Password Strength Analyzer!")
            break

        print()


if __name__ == "__main__":
    main()