import allfn as af

d = {
    "ş": {"type": "tam-sayı", "value": "8"},
    "ç": {"type": "tam-sayı", "value": "2"},
    "a": {"type": "reel-sayı", "value": "5,0"},
    "b": {"type": "reel-sayı", "value": "3,0"},
    "c": {"type": "reel-sayı", "value": "2,1"},
    "t": {"type": "metin", "value": "!balalalab!"},
    "m": {"type": "metin", "value": "!ala!"},
    "k": {"type": "metin", "value": "!2,1!"},
}

operators = ["artı", "eksi", "çarp", "bölü"]
exp = "!1! artı !,0!"


def expression_calculator(expression, d):
    expression_words_list = expression.split()
    while len(expression_words_list) != 1:
        word_index = 1
        operator = expression_words_list[word_index]
        if operator.lower() in operators:
            operator = expression_words_list[word_index]
            first_operand = expression_words_list[word_index - 1]
            second_operand = expression_words_list[word_index + 1]
            operator = operator.lower()
            if first_operand.lower() in d and second_operand.lower() in d:
                first_operand = first_operand.lower()
                second_operand = second_operand.lower()
                type1 = d[first_operand]["type"]
                type2 = d[second_operand]["type"]
                value1 = d[first_operand]["value"]
                value2 = d[second_operand]["value"]

                params = (type1, type2, value1, value2, d, expression_words_list, word_index)

                if operator == "artı":
                    result = af.add(*params)
                elif operator == "eksi":
                    result = af.subtract(*params)
                elif operator == "çarp":
                    result = af.multiply(*params)
                elif operator == "bölü":
                    result = af.divide(*params)

                if result == "runtime":
                    return "runtime"
                if result == "compile":
                    return "runtime"

                else:
                    expression_words_list = result
            elif (first_operand.lower() not in d) and (second_operand.lower() not in d):
                type1 = af.operand_type_definition(first_operand, d)
                type2 = af.operand_type_definition(second_operand, d)
                value1 = first_operand
                value2 = second_operand
                if type1 == "compile" or type2 == "compile":
                    return "compile"

                params = (type1, type2, value1, value2, d, expression_words_list, word_index)

                if operator == "artı":
                    result = af.add(*params)
                elif operator == "eksi":
                    result = af.subtract(*params)
                elif operator == "çarp":
                    result = af.multiply(*params)
                elif operator == "bölü":
                    result = af.divide(*params)

                if result == "runtime":
                    return "runtime"
                if result == "compile":
                    return "compile"
                else:
                    expression_words_list = result
            elif first_operand.lower() in d and second_operand.lower() not in d:
                type1 = d[first_operand]["type"]
                type2 = af.operand_type_definition(second_operand, d)
                value1 = d[first_operand]["value"]
                value2 = second_operand
                if type2 == "compile":
                    return "compile"

                params = (type1, type2, value1, value2, d, expression_words_list, word_index)

                if operator == "artı":
                    result = af.add(*params)
                elif operator == "eksi":
                    result = af.subtract(*params)
                elif operator == "çarp":
                    result = af.multiply(*params)
                elif operator == "bölü":
                    result = af.divide(*params)

                if result == "runtime":
                    return "runtime"
                if result == "compile":
                    return "compile"
                else:
                    expression_words_list = result
            else:
                return "compile"
        else:
            return "compile"

    return expression_words_list[0]


print(expression_calculator(exp, d))
print(d)


"""
Programı başlat. 
<var> bir <type> olsun.
#############################    <var> değeri <expr> olsun.
<expr> yazdır.
<expr>. satıra zıpla.
Programı bitir.
"""


# line = "İ değeri A artı 5 çarp 3 olsun."
# words_list = line.split()
# words_list = words_list[:3-1] + ["A+5"] + words_list[3+2:]
# print(words_list)
