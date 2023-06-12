# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)

regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,}"
