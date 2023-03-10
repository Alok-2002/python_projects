def kbc():
    print("\n-----Welcome To Kaun Banega Crorepati-----\n")
    print("\n-----Round 1 Starts-----\n")


    questions = ["1. Who is the Prime Minister of India ?","2. Where is Taj Mahal located ?","3. On Which Day Independence Day is Celebrated ?","4. Who was the First President of India ?","5. Who was the First Prime Minister Of India ?","6. Who is the Chief Of Defence Staff ?","7. Which one is a Union Territory of the following ?","8. Who is the Parent Company Of Google ?","9. Who is the Richest Person In the World ?","10. What is Full form of C.B.I ?"]
    first_option = ["A. Dr. Manmohan Singh","A. Delhi","A. 26th January","A. A.P.J Abdul Kalam","A. Swami Vivekanda","A. Lt General Anil Chauhan","A. Daman & Diu ","A. Alphabet","A. Bill Gates","A. Central Bank Of India"]
    second_option = ["B. Shri Narendra Modi","B. Indore","B. 26th November","B. Dr. Rajendra Prasad","B. Pandit Jawaharlal Nehru","B. General Manoj Pandey","B. New Delhi","B. Microsoft","B. Elon Musk","B. Crime Branch Of India"]
    third_option = ["C. Rahul Gandhi","C. Mumbai","C. 15th August","C. Sarvepalli Radhakrishnan","C. Lal Bahadur Shastri","C. General Manoj Mukund","C. Mumbai","C. Apple","C. Bernard Arnault & Family","C. Central Bureau Of Investigation"]
    fourth_option=["D. Droupadi Murmu","D. Agra","D. 25th December","D. Zakir Hussain","D. Indira Gandhi  ","D. General Bipin Rawat","D. Hyderabad","D. Amazon ","D. Jeff Bezos","D. Corporate Bussiness Intelligence"]
    answers = ["B","D","C","B","B","A","A","A","C","C"]
    answerlist = []
    Correct_Answers = 0
    prize_money=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
    total_amount=0
    a = 0
    Round = 1
    while a < len ( questions ) :
        print(questions[a])
        print(first_option[a])
        print(second_option[a])
        print(third_option[a])
        print(fourth_option[a])
        
        User = input("Enter Your Answer : ").upper()
        if User == answers[a] :
            
            print("Congratulations.......Aapka answer sahi hai aap jeet chuke hai Rs.",prize_money[a])
            print(" ")
            Correct_answers = 1
#             for i in range(0,len(prize_money)):
#                 total_amount = total_amount + prize_money[i]
            
#             print("You've Won a Total of Rs.",total)
                
            
        else:
            print("Sorry Your Answer is Wrong.......Better Luck Next Time :-) ")
            print(" ")
            break
        a = a + 1
        if a % 5 == 0 :
            print ("Congratulations......Aapka %s Round pura ho gaya hai."%Round)
            
            print (" ")
            Round = Round+1
        answerlist.append(User)
    print("You've Won A Total of Rs.",total_amount)
#     return total_amount

# kbc()


