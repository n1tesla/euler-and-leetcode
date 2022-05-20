def number_letter_counts():
    words = [
        (1, 'one', ''),
        (2, 'two', ''),
        (3, 'three', ''),
        (4, 'four', ''),
        (5, 'five', ''),
        (6, 'six', ''),
        (7, 'seven', ''),
        (8, 'eight', ''),
        (9, 'nine', ''),
        (10, 'ten', ''),
        (11, 'eleven', ''),
        (12, 'twelve', ''),
        (13, 'thirteen', ''),
        (14, 'fourteen', ''),
        (15, 'fifteen', ''),
        (16, 'sixteen', ''),
        (17, 'seventeen', ''),
        (18, 'eighteen', ''),
        (19, 'nineteen', ''),
        (20, 'twenty', ''),
        (30, 'thirty', ''),
        (40, 'forty', ''),
        (50, 'fifty', ''),
        (60, 'sixty', ''),
        (70, 'seventy', ''),
        (80, 'eighty', ''),
        (90, 'ninety', ''),
        (100, 'hundred', 'and'),
        (1000, 'thousand', 'and'),
    ]

    words_dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:
                'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
                70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}

    size_of_number=0

    for i in range(1,1000):

        if i<20:
            print(words_dict[i])
            size_of_number += len(words_dict[i])

        elif (i>=20) and (len(str(i))==2):
            decimal=i-i%10
            remainder=i%10
            if remainder!=0:
                print(words_dict[decimal]+'-'+words_dict[remainder])
                size_of_number+=len(words_dict[decimal]+'-'+words_dict[remainder])
            else:
                print(words_dict[decimal])
                size_of_number+=len(words_dict[decimal])

        elif len(str(i))==3:
            hundred=(i-i%100)/100
            full_decimal=i%100
            remainder = i % 10
            decimal=i%100-remainder
            if full_decimal==0:
                print(words_dict[hundred]+' hundred')
                size_of_number+=len(words_dict[hundred]+' hundred')
            else:
                if 0<full_decimal<20:
                    print(words_dict[hundred]+' hundred'+' and '+words_dict[full_decimal])
                    size_of_number+=len(words_dict[hundred]+' hundred'+' and '+words_dict[full_decimal])

                elif full_decimal>=20:
                    if remainder!=0:
                        print(words_dict[hundred]+' hundred'+' and '+words_dict[decimal]+'-'+words_dict[remainder])
                        size_of_number+=len(words_dict[hundred]+' hundred'+' and '+words_dict[decimal]+'-'+words_dict[remainder])
                    else:
                        print(words_dict[hundred] + ' hundred' + ' and ' + words_dict[decimal])
                        size_of_number += len(words_dict[hundred] + ' hundred' + ' and ' + words_dict[decimal])

    return size_of_number



if __name__=='__main__':
    print(number_letter_counts())