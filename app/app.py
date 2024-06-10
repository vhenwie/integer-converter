class Converter:
    def __init__(self, input_decimal: str) -> None:
        try:
            self.input_decimal = int(input_decimal)
        except ValueError:
            print("Not a valid decimal number.")
            main()

    def calculate(self, input_val: int, operation_int: int) -> dict:
        result: int = input_val // operation_int
        remainder: int = input_val % operation_int

        return {
            "result": result,
            "remainder": remainder
        }

    def print_result(self, result: tuple, factor: int) -> None:
        reversed_result: str = ""

        for i in range(len(result) - 1, -1, -1):
            reversed_result = reversed_result + str(result[i])

        match factor:
            case 8:
                base = "Octal"
            case 16:
                base = "Hexadecimal"
            case 2:
                base = "Binary"
            case _:
                base = "Not valid"

        print(f'> {base}: {reversed_result}')

    def convert(self, factor: int) -> None:

        if factor not in [8, 16, 2]:
            print("Not a valid factor.")
            main()

        target_value: tuple = []
        to_convert: dict = {
            "result": self.input_decimal,
            "remainder": 0
        }

        while True:
            to_convert = self.calculate(to_convert["result"], factor)
            target_value.append(to_convert["remainder"])
            if to_convert["result"] == 0:
                break

        if factor == 16:
            target_len = len(target_value)

            if target_len % 2 == 1:
                target_value.append(0)

            for i in range(target_len):
                match target_value[i]:
                    case 10:
                        target_value[i] = "A"
                    case 11:
                        target_value[i] = "B"
                    case 12:
                        target_value[i] = "C"
                    case 13:
                        target_value[i] = "D"
                    case 14:
                        target_value[i] = "E"
                    case 15:
                        target_value[i] = "F"

        self.print_result(target_value, factor)


def main() -> None:
    my_decimal = input("Enter a decimal value: ")
    my_handler = Converter(my_decimal)

    my_handler.convert(8)
    my_handler.convert(16)
    my_handler.convert(2)


if __name__ == '__main__':
    main()
