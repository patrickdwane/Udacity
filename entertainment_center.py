"""
list of Top10 Singles (Nov11) that feed into fresh_tomatoes.py file
"""
import media
import fresh_tomatoes

ROCKABYE =      media.Song("1",
                            "Rockabye (feat. Sean Paul)",
                            "Clean Bandit & Anne-Marie",
                            "http://s.mxmcdn.net/images-storage/albums4/4/2/9/1/1/2/35211924_350_350.jpg",
                            "https://www.youtube.com/watch?v=2F3YbB9hu6c",
                            "New Entry this Week!",
                            False, None)

SHOUT_OUT_TO_MY_EX = media.Song("2",
                            "Shout Out To My Ex",
                            "Little Mix",
                            "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRrYW6cRQVXPrMl2vJCC80_PGQHwB1a3OrgSo5VMi5nVdIDq3U_5Q",
                            "https://www.youtube.com/watch?v=o04PXpriWTg",
                            " ",
                            False, None)

SAY_YOU_WONT_LET_GO = media.Song("3",
                            "Say You Won't Let Go",
                            "James Arthur",
                            "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTAxCrO3wlcDcrycjPNcb-eIorWBarDtn8MxAc-P4lqSMuT69NqYQ",
                            "https://www.youtube.com/watch?v=kWehLbsIKbs",
                            " ",
                            False, None)

STARBOY =        media.Song("4",
                            "Starboy (feat. Daft Punk)",
                            "The Weeknd",
                            "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRm5rOMgcc04cSzJQH_z9zjkyl79VdTscgRG4sGLBDBF0me1cqc",
                            "https://www.youtube.com/watch?v=z0BuVC7j1og",
                            " ",
                            True, None)

TWENTYFOURK_MAGIC = media.Song("5",
                            "24K Magic",
                            "Bruno Mars",
                            "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTuWcDYUAdgkJm2S2_mHC0bs_srwy35d0GfiT1m-9AY0vUinRNG",
                            "https://www.youtube.com/watch?v=KkupLU5kdTc",
                            " ",
                            False, None)

SENSUAL =         media.Song("6",
                            "Sensual",
                            "NEIKED",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL36MyNgjibh5bMJmx3Pkdwgf2DdVeovuTvYVyOdp0-MDjTeNmqw",
                            "https://www.youtube.com/watch?v=UQbyGTKSzpI",
                            " ",
                            True, None)

DONT_WANNA_KNOW = media.Song("7",
                            "Don't Wanna Know (feat. Kendrick Lamar)",
                            "Maroon 5",
                            "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRKm7BchD3XTlYlIDyKEDdC1N0LgYKWw9QyEvsiG5yPD03DVhdU",
                            "https://www.youtube.com/watch?v=OxPv8mSTv9U",
                            " ",
                            False, None)

CLOSER =         media.Song("8",
                            "Closer (feat. Halsey)",
                            "The Chainsmokers",
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwShSalfIBJHUyGtC8dIZHp12-tcm7huyTPsNdSs0uglslkYV-HA",
                            "https://www.youtube.com/watch?v=agFMqNB9BYM",
                            " ",
                            False, None)

STARVING =         media.Song("9",
                            "Starving (feat. Zedd)",
                            "Hailee Steinfeld & Grey",
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRF4u7zlXSKQcrJkpu-w3nETqdzDoEoy6JY-YeqbDOKpAh4TZ38",
                            "https://www.youtube.com/watch?v=43slUlACaEs",
                            " ",
                            False, None)

THE_GREATEST =      media.Song("10",
                            "The Greatest (feat. Kendrick Lamar)",
                            "Sia",
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQQ0H9rWyUM1cWHTSe8gfaDDGVkMFe_B2mZjCLrr4KutK1SnzAy",
                            "https://www.youtube.com/watch?v=yrqcQzPBREU",
                            " ",
                            False, None)

songs = [ROCKABYE, SHOUT_OUT_TO_MY_EX, SAY_YOU_WONT_LET_GO, STARBOY,
          TWENTYFOURK_MAGIC, SENSUAL, DONT_WANNA_KNOW, CLOSER,
          STARVING, THE_GREATEST]

fresh_tomatoes.open_songs_page(songs)