INITIAL_RESULTS = [
    {
        "Company": "9ci",
        "Industry": "Software Development",
        "Address": "Chicago",
        "Phone": "********",
        "Website": "9ci.com",
        "Description": "9ci is a cutting-edge platform enabling B2B automation across enterprise resource workflows, offering invoice-to-cash, real-time payment tracking, and analytics."
    },
    {
        "Company": "Infivr",
        "Industry": "Software Development",
        "Address": "Chicago",
        "Phone": "********",
        "Website": "infivr.com",
        "Description": "Infivr builds immersive software solutions for AR/VR training and simulation across defense and education sectors, pioneering in virtualized user interfaces."
    }
]

EXTENDED_RESULTS = INITIAL_RESULTS + [
    {
        "Company": f"Company {i}",
        "Industry": "Software Development",
        "Address": "Chicago",
        "Phone": "********",
        "Website": f"example{i}.com",
        "Description": f"This is a detailed company description for Company {i}, focused on solving enterprise digital transformation using cloud-native tools and DevOps frameworks."
    }
    for i in range(3, 20)
]
