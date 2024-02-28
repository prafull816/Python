# WAF to find in which line of th e file does the word "learning" occure first/
# print -1 if word not fund

def check_for_line():
    word = "practice"  
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
      while data:
        data = f.readline()
        if(word in data):
            print(line_no)
            return
        line_no +=1


    return -1

check_for_line()