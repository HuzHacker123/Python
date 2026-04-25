Comment=input("Enter your comment: ")
spam_Texts=["make a lot of money","buy now","click this","subscribe this","free gift"]
if any(text in Comment.lower() for text in spam_Texts):
    print("This is a spam comment")