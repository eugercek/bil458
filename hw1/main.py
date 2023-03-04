GENERIC_ERROR_CODE = 1
KEYBOARD_INTERRUPT_ERROR_CODE = 11


def simple_interest(principle: float, rate: float, years: float) -> float:
    """
    Return Simple Interest of the given arguments.
    Be aware that principle, the money that borrower have, is not included in the returned value.
    """
    return (principle * rate * years) / 100


if __name__ == "__main__":
    try:
        principal = float(input("Principle amount: "))
        time = float(input("Time: "))
        rate = float(input("Rate: "))
        si = simple_interest(principal, time, rate)
        print(f"Simple Interest: {si}")
    except KeyboardInterrupt as ke:
        print("\nExiting due to keyboard interrupt")
        exit(KEYBOARD_INTERRUPT_ERROR_CODE)
    except Exception as e:
        print(e)
        print("Exiting ...")
        exit(GENERIC_ERROR_CODE)
