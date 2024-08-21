import os

from distutils.util import strtobool

# Gives a list of companies
dummyUsers = {
    "companies": [
        {
            "name": "Infineon Technologies AG",
            "location": "Munich, Bavaria, Germany",
            "description": "Infineon Technologies is a leading German semiconductor manufacturer specializing in automotive, industrial, and multi-market sectors. The company is known for producing microcontrollers, sensors, power semiconductors, and security solutions. Infineon's products are widely used in automotive electronics, industrial power control, and digital security solutions, making it a key player in the global semiconductor industry.",
        },
        {
            "name": "Apple Inc.",
            "location": "Cupertino, California, USA",
            "description": "Apple is a global technology company known for its innovative products such as the iPhone, iPad, Mac computers, and Apple Watch. The company also offers software, services, and digital content.",
        },
        {
            "name": "Microsoft Corporation",
            "location": "Redmond, Washington, USA",
            "description": "Microsoft is a multinational technology company that develops, manufactures, licenses, and sells software, electronics, and personal computers. It's best known for Windows, Office Suite, and Azure.",
        },
    ]
}

def getDummyCompanies():
    return dummyUsers["companies"]