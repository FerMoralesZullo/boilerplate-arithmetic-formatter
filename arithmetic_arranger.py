def arithmetic_arranger(problems, show_answers=False):
    # Verificar el número de problemas
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = {"line1": [], "line2": [], "line3": [], "answers": []}

    for problem in problems:
        # Dividir el problema en operando1, operador y operando2
        operand1, operator, operand2 = problem.split()

        # Verificar que el operador sea válido
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"

        # Verificar que los operandos contengan solo dígitos
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits"

        # Verificar que los operandos tengan como máximo cuatro dígitos
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits"

        # Determinar la longitud total del problema
        length = max(len(operand1), len(operand2)) + 2

        # Crear las líneas superior e intermedia con operador y operandos
        arranged_problems["line1"].append(operand1.rjust(length))
        arranged_problems["line2"].append(operator + operand2.rjust(length - 1))

        # Crear la línea intermedia con guiones
        arranged_problems["line3"].append("-" * length)

        if show_answers:
            # Calcular respuestas y agregarlas a la lista de respuestas
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            arranged_problems["answers"].append(answer.rjust(length))

    # Crear la cadena final combinando las líneas
    result = "\n".join(
        [
            "    ".join(arranged_problems["line1"]),
            "    ".join(arranged_problems["line2"]),
            "    ".join(arranged_problems["line3"]),
        ]
    )

    # Agregar respuestas si es necesario
    if show_answers:
        result += "\n" + "    ".join(arranged_problems["answers"])

    return result


if __name__ == '__main__':
    arithmetic_arranger()