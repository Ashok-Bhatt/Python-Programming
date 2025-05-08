choice="0"
while True:
    choice=input("\nEnter '0' for encoding the secret code language, enter '1' for decoding the secret code language or enter anything else to end the service:")
    if choice=="0":
        code=input("\nEnter the statement in your secret code language:")
        list1=code.split(" ")
        list2=[]
        for i in list1:
            if len(i)<3:
                list2.append(i[::-1])
            else:
                reverse1=i[::-1]
                final=reverse1[0]+i[:-1]
                random_alphabet=[chr(character) for character in range(65,91)]+[chr(character) for character in range(97,123)]
                import random
                begin=""
                end=""
                for rand in range(3):
                    begin=begin+random.choice(random_alphabet)
                    end=end+random.choice(random_alphabet)
                final=begin+final[::-1]+end
                list2.append(final)
            encode_message=""
            for j in list2:
                encode_message=encode_message+j+" "
        print("\nThe encoded message is given by:",encode_message)
    elif choice=="1":
        code=input("\nEnter the statement in your secret code language:")
        list1=code.split(" ")
        list2=[]
        for i in list1:
            if len(i)<3:
                list2.append(i[::-1])
            else:
                real=i[3:-3]
                reverse2=real[::-1]
                initial=reverse2[1:]+reverse2[0]
                list2.append(initial)
            decode_message=""
            for j in list2:
                decode_message=decode_message+j+" "
        print("T\nhe decoded message is given by:",decode_message)
    else:
        print("\nThanks for using our secret code language. May you will use this language in upcoming future.")
        break