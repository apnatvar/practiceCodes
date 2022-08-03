def arithmetic_arranger(problems, check=False):
    if len(problems) > 5:
      return "Error: Too many problems."
    sTop = ""
    sMiddle = ""
    sline = ""
    sBottom =""
    for problem in problems:
      problem = problem.split()
      num = problem[0]
      func = problem[1]
      den = problem[2]
      try:
        if int(num) > 9999 or int(den)>9999:
          return "Error: Numbers cannot be more than four digits."
      except:
        return "Error: Numbers must only contain digits."
      if func=='+':
        answer = str(int(num) + int(den))
      elif func=='-':
        answer = str(int(num) - int(den))
      else:
        return "Error: Operator must be '+' or '-'."
      length = len(num)
      if length < len(den):
        length = len(den)
      length += 2
      if length < len(answer):
        length = len(answer)
      num = num.rjust(length, " ")
      den = den.rjust(abs(length-2), " ")
      den = func + " " + den
      answer = answer.rjust(length, " ")
      sTop += num + "    "
      sMiddle += den + "    "
      emptyString = "".rjust(length, "-")
      sline += emptyString + "    "
      sBottom += answer + "    "
    finalString = sTop[:-4] + '''
''' + sMiddle[:-4] + '''
''' + sline[:-4]
    if check:
      finalString += '''
''' + sBottom[:-4]
    return finalString
