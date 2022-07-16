class regular_expressions:
  space_vertical = r'\n\v\f\r\u2028\u2029'
  space_horizontal = ''
  alldigits = r'\d'
  allalpha = r'[A-z]'
  alpha_lowercase = r'[a-z]'
  alpha_uppercase = r'[A-Z]'
  allalpha_and_digits = r'\w'
  function = {"re.escape": "Use to escape all characters"}
  
  def isMatch(regex: str, string: str) -> bool:
    return bool(re.search(regex, string))

  
def reading_file(directory):
  with open(directory) as f:
    text = f.read()
    
