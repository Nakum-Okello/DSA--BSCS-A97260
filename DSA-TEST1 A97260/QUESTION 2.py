catholic_martyrs = [
    "Achileo Kiwanuka",
    "Adolphus Ludigo-Mukasa",
    "Ambrosius Kibuuka",
    "Anatoli Kiriggwajjo",
    "Andrew Kaggwa",
    "Antanansio Bazzekuketta",
    "Bruno Sserunkuuma",
    "Charles Lwanga",
    "Denis Ssebuggwawo Wasswa",
    "Gonzaga Gonza",
    "Gyavira Musoke",
    "Yowana Mukiibi",
    "Yusufu Lugalama",
    "Zakayo Lubega",
    "James Buuzaabalyaawo",
    "John Maria Muzeeyi",
    "Joseph Mukasa Kizito",
    "Lukka Baanabakintu",
    "Matiya Mulumba",
    "Mbaga Tuzinde",
    "Mugagga Lubowa",
    "Mukasa Kiriwawanvu",
    "Nowa Mawaggali",
    "Ponsiano Ngondwe"
]

anglican_martyrs = [
    "Aaron Lubega",
    "Apollo Kivebulaya",
    "Eria Sebukyala",
    "Fredrick Kizza",
    "George Kizza",
    "James Hannington",
    "Janani Luwum",
    "Joseph Balikuddembe",
    "Kizito Mark Kakumba",
    "Matia Mulumba",
    "Nuhu Mbegu",
    "Robert Munyagayirwa",
    "Samwiri Mukasa",
    "Yefusa Namayanja",
    "Yohana Mukasa",
    "Yosefu Lugalama",
    "Yowana Kitaka",
    "Yowana Maria Mukasa"
]
# Identify and remove duplicates
catholic_martyrs = list(set(catholic_martyrs))
anglican_martyrs = list(set(anglican_martyrs))

#lists updated without duplicates
print(catholic_martyrs)
print(anglican_martyrs)


# Corrected function to determine the group of a martyr based on their name
# Updated function to determine the group of a martyr based on a partial match of the name
def martyr_count(name):
    # Lists of Catholic and Anglican martyrs (without duplicates)
    catholic_martyrs = [
        "Achileo Kiwanuka", "Adolphus Ludigo-Mukasa", "Ambrosius Kibuuka",
        "Anatoli Kiriggwajjo", "Andrew Kaggwa", "Antanansio Bazzekuketta",
        "Bruno Sserunkuuma", "Charles Lwanga", "Denis Ssebuggwawo Wasswa",
        "Gonzaga Gonza", "Gyavira Musoke", "Yowana Mukiibi", "Yusufu Lugalama",
        "Zakayo Lubega", "James Buuzaabalyaawo", "John Maria Muzeeyi",
        "Joseph Mukasa Kizito", "Lukka Baanabakintu", "Matiya Mulumba",
        "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa Kiriwawanvu",
        "Nowa Mawaggali", "Ponsiano Ngondwe"
    ]

    anglican_martyrs = [
        "Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza",
        "George Kizza", "James Hannington", "Janani Luwum", "Joseph Balikuddembe",
        "Kizito Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu", "Robert Munyagayirwa",
        "Samwiri Mukasa", "Yefusa Namayanja", "Yohana Mukasa", "Yosefu Lugalama",
        "Yowana Kitaka", "Yowana Maria Mukasa"
    ]

    # Check for a partial match in either list
    similar_catholic_martyrs = [m for m in catholic_martyrs if name.lower() in m.lower()]
    similar_anglican_martyrs = [m for m in anglican_martyrs if name.lower() in m.lower()]

    # Determine the group based on the partial match
    if similar_catholic_martyrs:
        return "Catholic"
    elif similar_anglican_martyrs:
        return "Anglican"
    else:
        return "Unknown"

# Prompt the user to input a name
user_input = input("Enter a martyr's name: ")

# Using the function to determine the group based on a partial match
martyr_group = martyr_count(user_input)

# Display the result
print(f"The martyr belongs to the {martyr_group} group.")


def is_uganda_martyr(name):
    # Lists of Catholic and Anglican martyrs (without duplicates)
    catholic_martyrs = [
        "Achileo Kiwanuka", "Adolphus Ludigo-Mukasa", "Ambrosius Kibuuka",
        "Anatoli Kiriggwajjo", "Andrew Kaggwa", "Antanansio Bazzekuketta",
        "Bruno Sserunkuuma", "Charles Lwanga", "Denis Ssebuggwawo Wasswa",
        "Gonzaga Gonza", "Gyavira Musoke", "Yowana Mukiibi", "Yusufu Lugalama",
        "Zakayo Lubega", "James Buuzaabalyaawo", "John Maria Muzeeyi",
        "Joseph Mukasa Kizito", "Lukka Baanabakintu", "Matiya Mulumba",
        "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa Kiriwawanvu",
        "Nowa Mawaggali", "Ponsiano Ngondwe"
    ]

    anglican_martyrs = [
        "Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza",
        "George Kizza", "James Hannington", "Janani Luwum", "Joseph Balikuddembe",
        "Kizito Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu", "Robert Munyagayirwa",
        "Samwiri Mukasa", "Yefusa Namayanja", "Yohana Mukasa", "Yosefu Lugalama",
        "Yowana Kitaka", "Yowana Maria Mukasa"
    ]

    # Convert input name to lowercase for case-insensitive comparison
    name_lower = name.lower()

    # Check for a match in both lists
    catholic_match = any(name_lower in martyr.lower() for martyr in catholic_martyrs)
    anglican_match = any(name_lower in martyr.lower() for martyr in anglican_martyrs)

    return catholic_match and anglican_match

# Prompt the user to input a name
user_input = input("Enter a name to check for a match with Uganda Martyrs: ")

# Using the function to determine if there's a match
is_match = is_uganda_martyr(user_input)

# Display the result
print(f"Does the input match names of the Uganda Martyrs in both lists? {is_match}")
