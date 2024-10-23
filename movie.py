# the content of the movie database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
# http://www.gustavus.edu/+max/concrete-abstractions.html

# the Scheme file, Revision 1.3 as of 2005/12/20 14:09:37, has been reformated for
# Python. The original file is available as
# http://www.gustavus.edu/academics/mcs/max/concabs/code/movie.scm

# list of tuples w/ following format (the first tuple in the list is also annotated):
# each tuple contains title, director, year and actors/actresses
# `[(title, director, year, [actress_one, actor_two, ...]), ...]`
from typing import List, Tuple

movie_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "amarcord",  # title
        "federico fellini",  # director
        1974,  # year
        [
            "magali noel",
            "bruno zanin",
            "pupella maggio",
            "armando drancia",
        ],  # actors/actresses
    ),
    (
        "the big easy",
        "jim mcbride",
        1987,
        [
            "dennis quaid",
            "ellen barkin",
            "ned beatty",
            "lisa jane persky",
            "john goodman",
            "charles ludlam",
        ],
    ),
    (
        "boyz n the hood",
        "john singleton",
        1991,
        [
            "cuba gooding jr.",
            "ice cube",
            "larry fishburne",
            "tyra ferrell",
            "morris chestnut",
        ],
    ),
    (
        "dead again",
        "kenneth branagh",
        1991,
        [
            "kenneth branagh",
            "emma thompson",
            "andy garcia",
            "derek jacobi",
            "hanna schygulla",
        ],
    ),
    (
        "the godfather",
        "francis ford coppola",
        1972,
        ["marlon brando", "al pacino", "james caan", "robert duvall", "diane keaton"],
    ),
    (
        "an american in paris",
        "vincente minnelli",
        1952,
        ["gene kelley", "leslie caron", "oscar levant", "nina foch", "george guetary"],
    ),
    (
        "casablanca",
        "michael curtiz",
        1942,
        [
            "humphrey bogart",
            "ingrid bergman",
            "paul henreid",
            "claude rains",
            "sydney greenstreet",
            "peter lorre",
            "s z sakall",
            "conrad veidt",
            "dooley wilson",
        ],
    ),
    (
        "citizen kane",
        "orson welles",
        1941,
        [
            "orson welles",
            "joseph cotten",
            "dorothy comingore",
            "ray collins",
            "george coulouris",
            "agnes moorehead",
            "ruth warrick",
        ],
    ),
    (
        "gone with the wind",
        "victor fleming",
        1939,
        [
            "clark gable",
            "vivien leigh",
            "leslie howard",
            "olivia de havilland",
            "hattie mcdaniel",
            "butterfly mcqueen",
        ],
    ),
    (
        "lawrence of arabia",
        "david lean",
        1962,
        [
            "peter otoole",
            "alec guinness",
            "anthony quinn",
            "jack hawkins",
            "jose ferrer",
            "omar sharif",
            "anthony quayle",
            "claude rains",
            "arthur kennedy",
            "donald wolfit",
        ],
    ),
    (
        "the manchurian candidate",
        "john frankenheimer",
        1962,
        [
            "frank sinatra",
            "laurence harvey",
            "janet leigh",
            "angela lansbury",
            "henry silva",
            "james gregory",
            "leslie parrish",
            "john mcgiver",
            "khigh dhiegh",
            "james edwards",
        ],
    ),
    (
        "metropolis",
        "fritz lang",
        1926,
        [
            "alfred abel",
            "gustay frohlich",
            "brigitte helm",
            "rudolf kleinrogge",
            "heinrich george",
        ],
    ),
    (
        "othello",
        "orson welles",
        1952,
        [
            "orson welles",
            "michael mac liammoir",
            "robert coote",
            "suzanne cloutier",
            "faye compton",
            "doris dowling",
            "michael laurence",
        ],
    ),
    (
        "spartacus",
        "stanley kubrick",
        1960,
        [
            "kirk douglas",
            "laurence olivier",
            "jean simmons",
            "charles laughton",
            "peter ustinov",
            "john gavin",
            "tony curtis",
            "woody strode",
        ],
    ),
    (
        "a star is born",
        "george cuckor",
        1954,
        [
            "judy garland",
            "james mason",
            "jack carson",
            "tommy noonan",
            "charles bickford",
        ],
    ),
    (
        "after the rehearsal",
        "ingmar bergman",
        1984,
        ["erland josephson", "ingrid thulin", "lena olin", "nadja palmstjerna-weiss"],
    ),
    (
        "amadeus",
        "milos forman",
        1984,
        [
            "f murray abraham",
            "tom hulce",
            "elizabeth berridge",
            "simon callow",
            "roy dotrice",
            "christine ebersole",
            "jeffrey jones",
        ],
    ),
    (
        "blood simple",
        "joel coen",
        1985,
        [
            "john getz",
            "frances mcdormand",
            "dan hedaya",
            "m emmet walsh",
            "samm-art williams",
        ],
    ),
    (
        "chinatown",
        "roman polanski",
        1974,
        [
            "jack nicholson",
            "faye dunaway",
            "john huston",
            "perry lopez",
            "john hillerman",
            "darrell zwerling",
            "diane ladd",
            "roman polanski",
        ],
    ),
    (
        "the cotton club",
        "francis ford coppola",
        1984,
        [
            "richard gere",
            "gregory hines",
            "diane lane",
            "lonette mckee",
            "bob hoskins",
            "james remar",
            "fred gwynne",
        ],
    ),
    (
        "the crying game",
        "neil jordan",
        1992,
        [
            "stephen rea",
            "jaye davidson",
            "forest whitaker",
            "miranda richardson",
            "adrian dunbar",
            "breffini mckenna",
            "joe savino",
        ],
    ),
    (
        "the day of the jackal",
        "fred zinnemann",
        1973,
        [
            "edward fox",
            "terence alexander",
            "michel auclair",
            "alan badel",
            "tony britton",
            "denis carey",
            "olga georges-picot",
            "cyril cusack",
        ],
    ),
    (
        "diva",
        "jean-jacques beineix",
        1981,
        [
            "wilhelmenia wiggins fernandez",
            "frederic andrei",
            "richard bohringer",
            "thay an luu",
            "jacques fabbri",
            "chantal deruaz",
        ],
    ),
    (
        "the dresser",
        "peter yates",
        1984,
        ["albert finney", "tom courtenay", "edward fox", "zena walker"],
    ),
    (
        "el norte",
        "gregory nava",
        1983,
        [
            "zaide silvia gutierrez",
            "david villalpando",
            "ernesto gomez cruz",
            "alicia del lago",
            "trinidad silva",
        ],
    ),
    (
        "the exorcist",
        "william friedkin",
        1973,
        [
            "ellen burstyn",
            "linda blair",
            "jason miller",
            "max von sydow",
            "kitty winn",
            "lee j cobb",
        ],
    ),
    (
        "a fish called wanda",
        "michael chrichton",
        1988,
        [
            "john cleese",
            "jamie lee curtis",
            "kevin kline",
            "michael palin",
            "maria aitken",
            "tom georgeson",
            "patricia hayes",
        ],
    ),
    (
        "flirting",
        "john duigan",
        1992,
        [
            "noah taylor",
            "thandie newton",
            "nicole kidman",
            "bartholomew rose",
            "felix nobis",
            "josh picker",
            "kiri paramore",
        ],
    ),
    ("gates of heaven", "errol morris", 1978, []),
    (
        "house of games",
        "david mamet",
        1987,
        [
            "lindsay crouse",
            "joe mantegna",
            "mike nussman",
            "lilia skala",
            "j t walsh",
            "jack wallace",
        ],
    ),
    (
        "iceman",
        "fred schepisi",
        1984,
        ["timothy hutton", "john lone", "lindsay crouse"],
    ),
    (
        "jaws",
        "steven spielberg",
        1975,
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ],
    ),
    (
        "johnny got his gun",
        "dalton trumbo",
        1971,
        [
            "timothy bottoms",
            "kathy fields",
            "jason robards",
            "diane varsi",
            "donald sutherland",
            "eduard franz",
        ],
    ),
    (
        "local hero",
        "bill forsyth",
        1983,
        [
            "burt lancaster",
            "peter reigert",
            "peter capaldi",
            "fulton mckay",
            "denis lawson",
        ],
    ),
    (
        "malcolm x",
        "spike lee",
        1992,
        [
            "denzel washington",
            "angela basset",
            "albert hall",
            "al freeman jr",
            "delroy lindo",
            "spike lee",
        ],
    ),
    (
        "gladiator",
        "ridley scott",
        2000, 
        [
            "russell crowe", 
            "joaquin phoenix", 
            "connie nielsen", 
            "oliver reed", 
            "richard harris"
         ]
    ),
    (
        "memento", 
        "christopher nolan", 
        2000, 
        [
            "guy pearce", 
            "carrie-anne moss", 
            "joe pantoliano", 
            "mark boone junior"
        ]
    ),
    (
        "the lord of the rings: the fellowship of the ring", 
        "peter jackson", 
        2001, 
        [
            "elijah wood", 
            "ian mckellen", 
            "viggo mortensen", 
            "sean astin", 
            "cate blanchett"
        ]
    ),
    (
        "the dark knight", 
        "christopher nolan",
        2008, 
        [
            "christian bale", 
            "heath ledger", 
            "aaron eckhart", 
            "maggie gyllenhaal", 
            "gary oldman"
        ]
    ),
    (
        "slumdog millionaire", 
        "danny boyle", 
        2008, 
        [
            "dev patel", 
            "freida pinto", 
            "anil kapoor", 
            "irrfan khan"
        ]
    ),
    (
        "avatar", 
        "james cameron", 
        2009, 
        [
            "sam worthington", 
            "zoe saldaña", 
            "sigourney weaver", 
            "stephen lang", 
            "giovanni ribisi"
        ]
    ),
    (
        "inception", 
        "christopher nolan", 
        2010, 
        [
            "leonardo dicaprio", 
            "joseph gordon-levitt", 
            "ellen page", 
            "tom hardy", 
            "marion cotillard"
        ]
    ),
    (
        "black swan", 
        "darren aronofsky", 
        2010, 
        [
            "natalie portman", 
            "mila kunis", 
            "vincent cassel", 
            "barbara hershey"
        ]
    ),
    (
        "the social network", 
        "david fincher", 
        2010, 
        [
            "jesse eisenberg", 
            "andrew garfield", 
            "justin timberlake", 
            "armie hammer"
        ]
        ),
    (
        "drive", 
        "nicolas winding refn",
        2011, 
        [
            "ryan gosling", 
            "carey mulligan", 
            "bryan cranston", 
            "albert brooks"
        ]
    ),
    (
        "the artist", 
        "michel hazanavicius", 
        2011, 
        [
            "jean dujardin", 
            "bérénice bejo", 
            "john goodman", 
            "james cromwell"
        ]
    ),
    (
        "django unchained", 
        "quentin tarantino", 
        2012, 
        [
            "jamie foxx", 
            "christoph waltz", 
            "leonardo dicaprio", 
            "kerry washington", 
            "samuel l. jackson"
        ]
    ),
    (
        "gravity", 
        "alfonso cuarón", 
        2013, 
        [
            "sandra bullock", 
            "george clooney", 
            "ed harris"
        ]
    ),
    (
        "12 years a slave", 
        "steve mcqueen", 
        2013, 
        [
            "chiwetel ejiofor", 
            "michael fassbender", 
            "lupita nyong'o", 
            "brad pitt", 
            "paul dano"
        ]
    ),
    (
        "mad max: fury road", 
        "george miller", 
        2015, 
        [
            "tom hardy", 
            "charlize theron", 
            "nicholas hoult", 
            "hugh keays-byrne"
        ]
    ),
    (
        "the revenant", 
        "alejandro g. iñárritu", 
        2015, 
        [
            "leonardo dicaprio", 
            "tom hardy", 
            "domhnall gleeson", 
            "will poulter"
        ]
    ),
    (
        "la la land", 
        "damien chazelle", 
        2016, 
        [
            "ryan gosling", 
            "emma stone", 
            "john legend", 
            "rosemarie dewitt"
        ]
    ),
    (
        "moonlight", 
        "barry jenkins", 
        2016, 
        [
            "mahershala ali", 
            "naomie harris", 
            "trevante rhodes", 
            "andré holland"
        ]
    ),
    (
        "get out", 
        "jordan peele", 
        2017, 
        [
            "daniel kaluuya", 
            "allison williams", 
            "bradley whitford", 
            "catherine keener"
        ]
    ),
    (
        "parasite", 
        "bong joon-ho", 
        2019, 
        [
            "song kang-ho", 
            "lee sun-kyun", 
            "cho yeo-jeong", 
            "choi woo-shik"
        ]
    ),
]