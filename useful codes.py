class pyautogui_examples:
  def windows():
    # import win32gui
    hwnd = win32gui.GetForegroundWindow()  # active window
    bbox = win32gui.GetWindowRect(hwnd)  # bounding rectangle
    # add here how to get title
  def adding_hotkeys:
    # import keyboard
    functionName = lambda: print("Example")
    hotkey = 'ctrl+shift+q' 
    keyboard.add_hotkey(hotkey, functionName)

    
def handlingException():
  try:
    pass
  except Exception as e:
    print("Capture error:" e)
  
class regular_expressions:
  space_vertical = r'\n\v\f\r\u2028\u2029'
  space_horizontal = ''
  alldigits = r'\d'
  allalpha = r'[A-z]'
  alpha_lowercase = r'[a-z]'
  alpha_uppercase = r'[A-Z]'
  allalpha_and_digits = r'\w'
  function = {"re.escape": "Use to escape all characters"}
  def __init__():
    defs = {
      "re.escape", "to match literal counterpart of the string"}
  def isMatch(regex: str, string: str) -> bool:
    return bool(re.search(regex, string))

class string_manipulation:
  def stringBetween():
    x = "/watch?v=kTh0forT2Sg&list=PLw2faK8_QKfmSs0Xp8ycOXgZSXzM0pLWK&index=1"
    start = 'asdf=5;'
    end = '123jasd'
    s = 'asdf=5;iwantthis123jasd'
    str_between = lambda s, a, z: s[s.find(a)+len(a):s.rfind(z)]
    print(str_between(x, "watch?v=", "&list="))
  
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
