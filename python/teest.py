def score_jumsu():
  print("학점계산기를 실행합니다.")
  
  your_score = eval(input("점수 입력:"))
  print(type(your_score))

  if str(type(your_score)) == "<class 'int'>" or str(type(your_score)) == "<class 'float'>":
    score = float(your_score)
    
    grade = 0
    if (1.0>=score >= 0.9):
        grade='A'
        print("학점계산을 실행합니다")
        print("===============")
        print (grade)
        print("===============")        
            
    elif (0.9>score >= 0.8):
        grade='B'
        print("학점계산을 실행합니다")
        print("===============")
        print (grade)
        print("===============")      

    elif (0.8>score >= 0.7):
        grade='C'
        print("학점계산을 실행합니다")
        print("===============")
        print (grade)
        print("===============")      

    elif (0.7>score >= 0.6):
        grade='D'
        print("학점계산을 실행합니다")
        print("===============")
        print (grade)
        print("===============")      

    elif (0.6>score>=0.0):
        grade='F'
        print("학점계산을 실행합니다")
        print("===============")
        print (grade)
        print("===============")      
                
    else:
      print("bad score")


  else:
    print("bad score")



score_jumsu()