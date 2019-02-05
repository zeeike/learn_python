monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

#Print out the value from dictionary given the key
print(monthConversions["Aug"])
print(monthConversions.get("Jul"))
print(monthConversions.get("Luv","Not a valid key"))