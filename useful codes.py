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
    

class using_json:
  filename = "student.json"
   def opening():
      with open(filename,'w') as f:
        json.dump(var, f, indent =4)
   def saving():
      with open(filename) as f:
        return json.load(f)    

def multithreading():
  # import threading
  def function_name(argument):
    print(argument)
  t1 = threading.Thread(target=function_name, args='argument')
  t1.start()
