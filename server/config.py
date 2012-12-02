ConfigCategories = {
	"Computer Science":[
		"Algorithm",
		"Java",
		"Web Application",
		"C++",
        "Python",
	],
	"House Care":[
		"Gardening",
		"Plumbing",
		"Electricity",
		"cleaning",
		"House Keeping"
	],
	"Personal Service":[
		"Baby sitting",
		"Parcel Fetching"
	],
	"International":[
		"English",
		"Spannish",
		"French",
		"Russian"
	]
}

ConfigProfils = [
	{
		"Email":"sei7787@gmail.com",
		"FirstName" : "Leo",
		"LastName" : "Sei",
		"Address" : "3 rue des jeuneurs,75002 Paris France",
		"Image": "https://secure.gravatar.com/avatar/73d252f886f31843cf263b869e5bcef2",
		"Involvement":545,
		"TimeCredit":3,
		"Headline" : "This is just me",
		"Skills":[
			"Web Application",
			"English",
			"French"
		],
        "Friends":[
            "alexandre.hajjar@gmail.com",
        ],
	},
	{
		"Email":"test@example.com",
		"FirstName" : "Leo",
		"LastName" : "Sei",
		"Address" : "3 rue des jeuneurs,75002 Paris France",
		"Image": "https://secure.gravatar.com/avatar/73d252f886f31843cf263b869e5bcef2",
		"Involvement":545,
		"TimeCredit":3,
		"Headline" : "This is just me",
		"Skills":[
			"Web Application",
			"English",
			"French",
			"House Keeping"
		]
	},
	{
		"Email":"alexandre.hajjar@gmail.com",
		"FirstName" : "Alex",
		"LastName" : "Hajjar",
		"Address" : "1 rue Waikiki, Honolulu",
        "Image": "http://en.gravatar.com/avatar/c4855961632635e313ced8253004558b",
		"Involvement":823,
		"TimeCredit":14,
        "Headline" : ":P",
		"Skills":[
			"Web Application",
			"French",
		],
        "Friends":[
            "sei7787@gmail.com"
        ],
	},
	{
		"Email":"augustin.riedinger@gmail.com",
		"FirstName" : "Augustin",
		"LastName" : "Riedinger",
		"Address" : "21 rue servan, 75011 Paris",
        "Image": "http://en.gravatar.com/avatar/bc22b26eca68dab55ec4fe491495951e",
		"Involvement":450,
		"TimeCredit":24,
        "Headline" : "I <3 Hackathons",
		"Skills":[
			"Web Application",
			"French",
			"House Keeping",
			"English"
		]
	}
]

ConfigServices = [
{
	"Title" : "Garden my plants",
	"Description" : "I'll be out for a week, could you water my plants",
	"TimeNeeded":4,
	"StartDate":"2012-12-02",
	"EndDate" : "2013-01-03",
	"Skill" : "House Keeping",
	"Geoloc" : True,
	"Requester" : "alexandre.hajjar@gmail.com",
	"Comments":[
		{
			"Comment":"For how long will you be out",
			"Owner":"sei7787@gmail.com"
		},
		{
			"Comment":"probably 2 weeks",
			"Owner":"alexandre.hajjar@gmail.com"
		},
	]
},
{
    "Title" : "AngelHack",
    "Description" : "Make an awesome web app, win, get thousands, get fame, get billions, retire.",
    "TimeNeeded" : 24,
    "StartDate" : "2012-10-01",
    "EndDate" : "2012-12-02",
    "Skill" : "Web Application",
    "Geoloc" : True,
    "Requester": "sei7787@gmail.com",
},
{
    "Title" : "Talk French to make some noise",
    "Description": "This is stupid",
    "TimeNeeded" : 3,
    "StartDate" : "2012-09-02",
    "EndDate" : "2012-09-26",
    "Skill" : "French",
    "Geoloc" : True,
    "Requester" : "test@example.com",
    "Responder" : "alexandre.hajjar@gmail.com",
},
{
    "Title" : "Do a web app for my business", 
    "Description" : "Use Python and AppEngine for a simple web app",
    "TimeNeeded" : 5,
    "StartDate" : "2012-12-22",
    "EndDate" : "2013-01-14",
    "Skill" : "Web Application",
    "Geoloc" : False,
    "Requester" : "test@example.com",
},
{
    "Title" : "Be a master at Python", 
    "Description" : "Walk through Python Challenge up to level 23",
    "TimeNeeded" : 10,
    "StartDate" : "2012-12-12",
    "EndDate" : "2013-02-04",
    "Skill" : "Python",
    "Geoloc" : False,
    "Requester" : "sei7787@gmail.com",
},
]

ServiceApplicants = [
    {
        "Service" : "Garden my plants",
        "Applicant" : "test@example.com",
        "Date" : "2012-12-04"
    },
    {
        "Service" : "AngelHack",
        "Applicant" : "alexandre.hajjar@gmail.com",
        "Date" : "2012-11-01"
    }
]
