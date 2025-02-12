# This program tells you what continent the country is 

while True: #infinate loop

    #user inputs name of country
    name = input("what is your country?  ").title()
    print("\n")

    # Cases to match
    match name:
        # African Cases
        case "Algeria" | "Angola" | "Benin" | "Botswana" | "Burkina Faso" | "Burundi" | "Cabo Verde" | "Cameroon" | "Central African Republic" |"Chad" | "Comoros" | "Democratic Republic of the Congo" |"D R Congo"|"The Congo"|"Congo"| "Djibouti" | "Egypt" |"Equatorial Guinea" | "Eritrea" | "Eswatini" | "Ethiopia" | "Gabon" | "Gambia" | "Ghana" | "Guinea" |  "Guinea-Bissau" | "Ivory Coast" | "Kenya" | "Lesotho" | "Liberia" | "Libya" | "Madagascar" | "Malawi" | "Mali" | "Mauritania" | "Mauritius" | "Morocco" | "Mozambique" | "Namibia" | "Niger" | "Nigeria" | "Republic of the Congo" | "Rwanda" | "São Tomé and Príncipe" | "Senegal" | "Seychelles" | "Sierra Leone" |    "Somalia" | "South Africa" | "South Sudan" | "Sudan" | "Tanzania" | "Togo" | "Tunisia" | "Uganda" | "Zambia" | "Zimbabwe":
            print(f"{name} is a country in Africa\n")
        # North american cases    
        case "Antigua and Barbuda" | "Bahamas" | "Barbados" | "Belize" | "Canada" | "Costa Rica" | "Cuba" | "Dominica" | "Dominican Republic" | "El Salvador" | "Grenada" | "Guatemala" | "Haiti" | "Honduras" | "Jamaica" | "Mexico" | "Nicaragua" | "Panama" | "Saint Kitts and Nevis" | "Saint Lucia" | "Saint Vincent and the Grenadines" | "Trinidad and Tobago" | "United States":
            print(f"{name} is a country in North America\n")
        # South America
        case "Argentina" | "Bolivia" | "Brazil" | "Chile" | "Colombia" | "Ecuador" | "Guyana" | "Paraguay" | "Peru" | "Suriname" | "Uruguay" | "Venezuela":
            print(f"{name} is a country in South America\n")
        # Europe
        case "England"|"Scotland"|"Wales"|"Northern Ireland"|"Republic Of Ireland"|"Holland"|"Albania" | "Andorra" | "Armenia" | "Austria" | "Azerbaijan" | "Belarus" | "Belgium" | "Bosnia and Herzegovina" |"Bulgaria" | "Croatia" | "Cyprus" | "Czech Republic" | "Denmark" | "Estonia" | "Finland" | "France" | "Georgia" |"Germany" | "Greece" | "Hungary" | "Iceland" | "Ireland" | "Italy" | "Kazakhstan" | "Latvia" | "Liechtenstein" |"Lithuania" | "Luxembourg" | "Malta" | "Moldova" | "Monaco" | "Montenegro" | "Netherlands" |"The Netherlands" | "North Macedonia" |"Norway" | "Poland" | "Portugal" | "Romania" | "Russia" | "San Marino" | "Serbia" | "Slovakia" | "Slovenia" |"Spain" | "Sweden" | "Switzerland" | "Turkey" | "Ukraine" | "United Kingdom" | "Vatican City":
            print(f"{name} is a country in Europe\n")
        # Asia
        case "Afghanistan" | "Bahrain" | "Bangladesh" | "Bhutan" | "Brunei" | "Cambodia" | "China" | "India" |"Indonesia" | "Iran" | "Iraq" | "Israel" | "Japan" | "Jordan" | "Kazakhstan" | "Kuwait" | "Kyrgyzstan" |"Laos" | "Lebanon" | "Malaysia" | "Maldives" | "Mongolia" | "Myanmar" | "Nepal" | "North Korea" | "Oman" |"Pakistan" | "Palestine" | "Philippines" | "Qatar" | "Saudi Arabia" | "Singapore" | "South Korea" | "Sri Lanka" |"Syria" | "Tajikistan" | "Thailand" | "Timor-Leste" | "Turkmenistan" | "United Arab Emirates" | "Uzbekistan" | "Vietnam" | "Yemen":
            print(f"{name} is country in Asia\n")
        # Oceania
        case "Australia" | "Fiji" | "Kiribati" | "Marshall Islands" | "Micronesia" | "Nauru" | "New Zealand" |"Palau" | "Papua New Guinea" | "Samoa" | "Solomon Islands" | "Tonga" | "Tuvalu" | "Vanuatu":
            print(f"{name} is a country in Oceania\n")
        # North Pole
        case "North Pole"|"The North Pole":
            print("The North Pole is not part of any country but is located in the Arctic Ocean.\n")
        # South Pole
        case "South Pole"|"The South Pole":
            print("The South Pole is Located in Antarctica, which is not a country but a continent governed by the Antarctic Treaty.\n")
        # Other cases
        case _:
            print(f"Sorry I dont recognise {name} as a country. Check the spelling and try again!\n")
    # Restart the loop message
    print("Lets try another country!\n")    
    