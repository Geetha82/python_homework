
# Task 1: Diary

import traceback

try:
   # Open a file called diary.txt for appending
   with open("diary.txt", "a") as diary_file:
      first_prompt = True

      while True:
         
         #f irst prompt say, "What happened today? "
         if first_prompt:
            user_input = input("What happened today? ")
            first_prompt = False

            # all subsequent prompts say "What else? "
         else:
            user_input = input("What else? ")

            # write the line recieved to diary.txt, with a newline (\n) at the end
            diary_file.write(user_input + "\n")

            # When "done for now" is received, write to diary.txt and exit the loop

            if user_input.lower() == "done for now" :
               break
         

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

