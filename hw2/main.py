GENERIC_ERROR_CODE = 1
KEYBOARD_INTERRUPT_ERROR_CODE = 11


def compound_interest(principle: float, rate: float, years: float) -> float:
    """
    Return Compound Interest of the given arguments.
    """
    return principal * (pow((1 + rate / 100), years)) - principle


if __name__ == "__main__":
    try:
        principal = float(input("Principle amount: "))
        time = float(input("Time: "))
        rate = float(input("Rate: "))
        si = compound_interest(principal, time, rate)
        print(f"Compound Interest: {si}")
    except KeyboardInterrupt as ke:
        print("\nExiting due to keyboard interrupt")
        exit(KEYBOARD_INTERRUPT_ERROR_CODE)
    except Exception as e:
        print(e)
        print("Exiting ...")
        exit(GENERIC_ERROR_CODE)
