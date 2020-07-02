# Validating Math Class Score
math_score = 0

while math_score == 0:
    math_input = int(raw_input('Enter the score you received for Math: '))
    if math_input < 0 or math_input > 100:
        print 'No valid score. Insert again.'
    else:
        math_score += math_input

# Validating English Class Score
english_score = 0

while english_score == 0:
    english_input = int(raw_input('Enter the score you received for English: '))
    if english_input < 0 or english_input > 100:
        print 'No valid score. Insert again.'
    else:
        english_score += english_input

# Validating PE Class Score
pe_score = 0

while pe_score == 0:
    pe_input = int(raw_input('Enter the score you received for PE: '))
    if pe_input < 0 or pe_input > 100:
        print 'No valid score. Insert again.'
    else:
        pe_score += pe_input

# Validating Science Class Score
science_score = 0

while science_score == 0:
    science_input = int(raw_input('Enter the score you received for Science: '))
    if science_input < 0 or science_input > 100:
        print 'No valid score. Insert again.'
    else:
        science_score += science_input

# Validating Art Class Score
art_score = 0

while art_score == 0:
    art_input = int(raw_input('Enter the score you received for Art: '))
    if art_input < 0 or art_input > 100:
        print 'No valid score. Insert again.'
    else:
        art_score += art_input

def calc_grade(grade):
    if 93 <= grade <= 100:
        return 'A'
    elif 90 <= grade < 93:
        return 'A-'
    elif 87 <= grade < 90:
        return 'B+'
    elif 83 <= grade < 87:
        return 'B'
    elif 80 <= grade < 83:
        return 'B-'
    elif 77 <= grade < 80:
        return 'C+'
    elif 73 <= grade < 77:
        return 'C'
    elif 70 <= grade < 73:
        return 'C-'
    elif 67 <= grade < 70:
        return 'D+'
    elif 63 <= grade < 67:
        return 'D'
    elif 60 <= grade < 63:
        return 'D-'
    else:
        return 'F'
    
print 'Your Math score is '+ str(math_score) + ', you got a ' + str(calc_grade(math_score)) + '.'
print 'Your English score is '+ str(english_score) + ', you got a ' + str(calc_grade(english_score)) + '.'
print 'Your PE score is '+ str(pe_score) + ', you got a ' + str(calc_grade(pe_score)) + '.'
print 'Your Science score is '+ str(science_score) + ', you got a ' + str(calc_grade(science_score)) + '.'
print 'Your Art score is '+ str(art_score) + ', you got a ' + str(calc_grade(art_score)) + '.'
