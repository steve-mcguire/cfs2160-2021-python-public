def validate_email_bad(email, domain):
    if email.count("@") == 1:
        email_split = email.split("@")
        if len(email_split[0]) > 0:
            if email_split[1] == domain:
                print(email + " is valid")
            else:
                print(email + "is not valid at " + domain)
        else:
            print("Your email username is not valid")
    else:
        print("Email does nto contain a single @")


#print(validate_email_bad("abcd@hud.ac.ukg", "hud.ac.uk"))

def validate_email_better(email, domain):
    if email.count("@") == 1:
        email_split = email.split("@")
        if len(email_split[0]) > 0:
            if email_split[1] == domain:
                return email + " is valid"
            else:
                return email + "is not valid at " + domain
        else:
            return "Your email username is not valid"
    else:
        return "Email does nto contain a single @"


#print(validate_email_better("abcd@hud.ac.ukg", "hud.ac.uk"))


def validate_email_brilliant(email, domain):
    '''
    Checks an email has username and correct domain
    :param email:
    :param domain:
    :return:
    '''
    if email.count("@") == 1:
        email_split = email.split("@")
        if len(email_split[0]) > 0:
            if email_split[1] == domain:
                return True
            else:
                raise Exception(email + " is not valid at " + domain)
        else:
            raise Exception("Your email username is not valid")
    else:
        raise Exception("Email does not contain a single @")


try:
    user_email = "abcd@hud.ac.com"
    valid_domain = "hud.ac.uk"
    if validate_email_brilliant(user_email, valid_domain):
        print(user_email + " is valid at " + valid_domain)
except Exception as e:
    print("ERROR " + str(e))

