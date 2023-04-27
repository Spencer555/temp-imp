from django.db import models
from Authentication.models import User
from django.utils.text import slugify
from custom.custom_func import unique_slugify
from django.core.validators import RegexValidator
import os
from datetime import datetime

CarModelsAndMakes = [ 
    
    (
        "ACURA",
        (
            ("Acura ILX", "Acura ILX"),
            ("Acura TLX", "Acura TLX"),
            ("Acura RLX", "Acura RLX"),
            ("Acura NSX", "Acura NSX"),
            ("Acura RDX", "Acura RDX"),
            ("Acura MDX", "Acura MDX"),
        ),
    ),
    (
        "AUDI",
        (
            ("Audi A1", "Audi A1"),
            ("Audi A3", "Audi A3"),
            ("Audi A4", "Audi A4"),
            ("Audi A5", "Audi A5"),
            ("Audi A6", "Audi A6"),
            ("Audi A7", "Audi A7"),
            ("Audi A8", "Audi A8"),
            ("Audi Q2", "Audi Q2"),
            ("Audi Q3", "Audi Q3"),
            ("Audi Q5", "Audi Q5"),
            ("Audi Q7", "Audi Q7"),
            ("Audi Q8", "Audi Q8"),
            ("Audi TT", "Audi TT"),
            ("Audi R8", "Audi R8"),
            ("Audi E-TRON", "Audi E-TRON"),
        ),
    ),
    (
        "BMW",
        (
            ("BMW 1 Series", "BMW 1 Series"),
            ("BMW 2 Series", "BMW 2 Series"),
            ("BMW 3 Series", "BMW 3 Series"),
            ("BMW 4 Series", "BMW 4 Series"),
            ("BMW 5 Series", "BMW 5 Series"),
            ("BMW 6 Series", "BMW 6 Series"),
            ("BMW 7 Series", "BMW 7 Series"),
            ("BMW X1", "BMW X1"),
            ("BMW X2", "BMW X2"),
            ("BMW X3", "BMW X3"),
            ("BMW X4", "BMW X4"),
            ("BMW X5", "BMW X5"),
            ("BMW X6", "BMW X6"),
            ("BMW X7", "BMW X7"),
            ("BMW Z4", "BMW Z4"),
            ("BMW i3", "BMW i3"),
            ("BMW i8", "BMW i8"),
        ),
    ),
    (
        "BENTLEY",
        (
            ("Bentley Arnage", "Bentley Arnage"),
            ("Bentley Azure", "Bentley Azure"),
            ("Bentley Bentayga", "Bentley Bentayga"),
            ("Bentley Brooklands", "Bentley Brooklands"),
            ("Bentley Continental GT", "Bentley Continental GT"),
            ("Bentley Continental Flying Spur", "Bentley Continental Flying Spur"),
            ("Bentley Continental Supersports", "Bentley Continental Supersports"),
            ("Bentley Mulsanne", "Bentley Mulsanne"),
            ("Bentley Turbo R", "Bentley Turbo R"),
            ("Bentley Turbo S", "Bentley Turbo S"),
        ),
    ),
    (
        "BUICK",
        (
            ("Buick Cascada", "Buick Cascada"),
            ("Buick Enclave", "Buick Enclave"),
            ("Buick Encore", "Buick Encore"),
            ("Buick Encore GX", "Buick Encore GX"),
            ("Buick LaCrosse", "Buick LaCrosse"),
            ("Buick Regal", "Buick Regal"),
            ("Buick Verano", "Buick Verano"),
            ("Buick Century", "Buick Century"),
            ("Buick Electra", "Buick Electra"),
            ("Buick LeSabre", "Buick LeSabre"),
            ("Buick Lucerne", "Buick Lucerne"),
            ("Buick Park Avenue", "Buick Park Avenue"),
            ("Buick Rainier", "Buick Rainier"),
            ("Buick Reatta", "Buick Reatta"),
            ("Buick Rendezvous", "Buick Rendezvous"),
            ("Buick Riviera", "Buick Riviera"),
            ("Buick Roadmaster", "Buick Roadmaster"),
            ("Buick Skylark", "Buick Skylark"),
            ("Buick Special", "Buick Special"),
            ("Buick Terraza", "Buick Terraza"),
        ),
    ),
    (
        "CADILLAC",
        (
            ("Cadillac ATS", "Cadillac ATS"),
            ("Cadillac CT4", "Cadillac CT4"),
            ("Cadillac CT5", "Cadillac CT5"),
            ("Cadillac CTS", "Cadillac CTS"),
            ("Cadillac DTS", "Cadillac DTS"),
            ("Cadillac Eldorado", "Cadillac Eldorado"),
            ("Cadillac ELR", "Cadillac ELR"),
            ("Cadillac Escalade", "Cadillac Escalade"),
            ("Cadillac SRX", "Cadillac SRX"),
            ("Cadillac STS", "Cadillac STS"),
            ("Cadillac XLR", "Cadillac XLR"),
            ("Cadillac XT4", "Cadillac XT4"),
            ("Cadillac XT5", "Cadillac XT5"),
            ("Cadillac XT6", "Cadillac XT6"),
        ),
    ),
    (
        "CHEVROLET",
        (
            ("Chevrolet Bolt EV", "Chevrolet Bolt EV"),
            ("Chevrolet Camaro", "Chevrolet Camaro"),
            ("Chevrolet Colorado", "Chevrolet Colorado"),
            ("Chevrolet Corvette", "Chevrolet Corvette"),
            ("Chevrolet Cruze", "Chevrolet Cruze"),
            ("Chevrolet Equinox", "Chevrolet Equinox"),
            ("Chevrolet Express", "Chevrolet Express"),
            ("Chevrolet Impala", "Chevrolet Impala"),
            ("Chevrolet Malibu", "Chevrolet Malibu"),
            ("Chevrolet Silverado", "Chevrolet Silverado"),
            ("Chevrolet Sonic", "Chevrolet Sonic"),
            ("Chevrolet Spark", "Chevrolet Spark"),
            ("Chevrolet Suburban", "Chevrolet Suburban"),
            ("Chevrolet Tahoe", "Chevrolet Tahoe"),
            ("Chevrolet Traverse", "Chevrolet Traverse"),
            ("Chevrolet Blazer", "Chevrolet Blazer"),
            ("Chevrolet Trax", "Chevrolet Trax"),
            ("Chevrolet Blazer", "Chevrolet Blazer"),
            ("Chevrolet Trailblazer", "Chevrolet Trailblazer"),
            ("Chevrolet Cavalier", "Chevrolet Cavalier"),
            ("Chevrolet Celebrity", "Chevrolet Celebrity"),
            ("Chevrolet Citation", "Chevrolet Citation"),
            ("Chevrolet Classic", "Chevrolet Classic"),
            ("Chevrolet Colbat", "Chevrolet Colbat"),
            ("Chevrolet Corsica", "Chevrolet Corsica"),
            ("Chevrolet HHR", "Chevrolet HHR"),
            ("Chevrolet Lumina", "Chevrolet Lumina"),
            ("Chevrolet Monte Carlo", "Chevrolet Monte Carlo"),
            ("Chevrolet Nova", "Chevrolet Nova"),
        ),
    ),
    (
        "CHRYSLER",
        (
            ("Chrysler 200", "Chrysler 200"),
            ("Chrysler 300", "Chrysler 300"),
            ("Chrysler Pacifica", "Chrysler Pacifica"),
            ("Chrysler PT Cruiser", "Chrysler PT Cruiser"),
            ("Chrysler Sebring", "Chrysler Sebring"),
            ("Chrysler Town", "Chrysler Town"),
            ("Chrysler Aspen", "Chrysler Aspen"),
            ("Chrysler Crossfire", "Chrysler Crossfire"),
            ("Chrysler Concorde", "Chrysler Concorde"),
            ("Chrysler LHS", "Chrysler LHS"),
            ("Chrysler New Yorker", "Chrysler New Yorker"),
            ("Chrysler Voyager", "Chrysler Voyager"),
            ("Chrysler Imperial", "Chrysler Imperial"),
        ),
    ),
    (
        "DATSUN",
        (
            ("Datsun 210", "Datsun 210"),
            ("Datsun 240Z", "Datsun 240Z"),
            ("Datsun 260Z", "Datsun 260Z"),
            ("Datsun 280Z", "Datsun 280Z"),
            ("Datsun 310", "Datsun 310"),
            ("Datsun 510", "Datsun 510"),
            ("Datsun 620", "Datsun 620"),
            ("Datsun 720", "Datsun 720"),
            ("Datsun 810", "Datsun 810"),
            ("Datsun B210", "Datsun B210"),
            ("Datsun F10", "Datsun F10"),
            ("Datsun Maxima", "Datsun Maxima"),
            ("Datsun Pulsar", "Datsun Pulsar"),
            ("Datsun Skyline", "Datsun Skyline"),
            ("Datsun Sunny", "Datsun Sunny"),
        ),
    ),
    (
        "DODGE",
        (
            ("Dodge Challenger", "Dodge Challenger"),
            ("Dodge Charger", "Dodge Charger"),
            ("Dodge Grand Caravan", "Dodge Grand Caravan"),
            ("Dodge Journey", "Dodge Journey"),
            ("Dodge Neon", "Dodge Neon"),
            ("Dodge Nitro", "Dodge Nitro"),
            ("Dodge Ram", "Dodge Ram"),
            ("Dodge Viper", "Dodge Viper"),
            ("Dodge Avenger", "Dodge Avenger"),
            ("Dodge Caliber", "Dodge Caliber"),
            ("Dodge Caravan", "Dodge Caravan"),
            ("Dodge Colt", "Dodge Colt"),
            ("Dodge Dakota", "Dodge Dakota"),
            ("Dodge Dart", "Dodge Dart"),
            ("Dodge Diplomat", "Dodge Diplomat"),
            ("Dodge Intrepid", "Dodge Intrepid"),
            ("Dodge Magnum", "Dodge Magnum"),
            ("Dodge Monaco", "Dodge Monaco"),
            ("Dodge Polara", "Dodge Polara"),
            ("Dodge Raider", "Dodge Raider"),
            ("Dodge Shadow", "Dodge Shadow"),
            ("Dodge Spirit", "Dodge Spirit"),
            ("Dodge Stealth", "Dodge Stealth"),
            ("Dodge Stratus", "Dodge Stratus"),
        ),
    ),
    (
        "FERRARI",
        (
            ("Ferrari 212 Inter", "Ferrari 212 Inter"),
            ("Ferrari 225 S", "Ferrari 225 S"),
            ("Ferrari 250 GT", "Ferrari 250 GT"),
            ("Ferrari 250 Testa Rossa", "Ferrari 250 Testa Rossa"),
            ("Ferrari 275 GTB/4", "Ferrari 275 GTB/4"),
            ("Ferrari 288 GTO", "Ferrari 288 GTO"),
            ("Ferrari 308 GTB", "Ferrari 308 GTB"),
            ("Ferrari 328", "Ferrari 328"),
            ("Ferrari 330 P4", "Ferrari 330 P4"),
            ("Ferrari 348", "Ferrari 348"),
            ("Ferrari 360 Modena", "Ferrari 360 Modena"),
            ("Ferrari 365 GTB/4 Daytona", "Ferrari 365 GTB/4 Daytona"),
            ("Ferrari 365 GT4 2+2", "Ferrari 365 GT4 2+2"),
            ("Ferrari 365 GTC/4", "Ferrari 365 GTC/4"),
            ("Ferrari 365 GTS/4 Daytona Spyder", "Ferrari 365 GTS/4 Daytona Spyder"),
            ("Ferrari 456", "Ferrari 456"),
            ("Ferrari 458 Italia", "Ferrari 458 Italia"),
            ("Ferrari 488", "Ferrari 488"),
            ("Ferrari 512 BB", "Ferrari 512 BB"),
            ("Ferrari 550 Maranello", "Ferrari 550 Maranello"),
            ("Ferrari 575M Maranello", "Ferrari 575M Maranello"),
            ("Ferrari 599 GTB Fiorano", "Ferrari 599 GTB Fiorano"),
            ("Ferrari 612 Scaglietti", "Ferrari 612 Scaglietti"),
            ("Ferrari California", "Ferrari California"),
            ("Ferrari Dino 206 GT", "Ferrari Dino 206 GT"),
            ("Ferrari Enzo", "Ferrari Enzo"),
            ("Ferrari F12berlinetta", "Ferrari F12berlinetta"),
            ("Ferrari F355", "Ferrari F355"),
            ("Ferrari F40", "Ferrari F40"),
            ("Ferrari F430", "Ferrari F430"),
            ("Ferrari F50", "Ferrari F50"),
            ("Ferrari FF", "Ferrari FF"),
            ("Ferrari LaFerrari", "Ferrari LaFerrari"),
            ("Ferrari Mondial", "Ferrari Mondial"),
            ("Ferrari Portofino", "Ferrari Portofino"),
            ("Ferrari Roma", "Ferrari Roma"),
            ("Ferrari Testarossa", "Ferrari Testarossa"),
        ),
    ),
    (
        "FIAT",
        (
            ("Fiat 124 Spider", "Fiat 124 Spider"),
            ("Fiat 500", "Fiat 500"),
            ("Fiat 500 Abarth", "Fiat 500 Abarth"),
            ("Fiat 500L", "Fiat 500L"),
            ("Fiat 500X", "Fiat 500X"),
            ("Fiat 500e", "Fiat 500e"),
            ("Fiat 500C", "Fiat 500C"),
            ("Fiat 500L MPV", "Fiat 500L MPV"),
            ("Fiat Bravo", "Fiat Bravo"),
            ("Fiat Doblo", "Fiat Doblo"),
            ("Fiat Ducato", "Fiat Ducato"),
            ("Fiat Freemont", "Fiat Freemont"),
            ("Fiat Fullback", "Fiat Fullback"),
            ("Fiat Grande Punto", "Fiat Grande Punto"),
            ("Fiat Idea", "Fiat Idea"),
            ("Fiat Marea", "Fiat Marea"),
            ("Fiat Multipla", "Fiat Multipla"),
            ("Fiat Panda", "Fiat Panda"),
            ("Fiat Punto", "Fiat Punto"),
            ("Fiat Qubo", "Fiat Qubo"),
            ("Fiat Scudo", "Fiat Scudo"),
            ("Fiat Sedici", "Fiat Sedici"),
            ("Fiat Stilo", "Fiat Stilo"),
            ("Fiat Talento", "Fiat Talento"),
            ("Fiat Tipo", "Fiat Tipo"),
            ("Fiat Ulysse", "Fiat Ulysse"),
            ("Fiat Uno", "Fiat Uno"),
            ("Fiat X1/9", "Fiat X1/9"),
        ),
    ),
    (
        "FORD",
        (
            ("Ford models:", "Ford models:"),
            ("Ford Bronco", "Ford Bronco"),
            ("Ford C-Max", "Ford C-Max"),
            ("Ford Crown Victoria ", "Ford Crown Victoria "),
            ("Ford EcoSport", "Ford EcoSport"),
            ("Ford Edge", "Ford Edge"),
            ("Ford Escape", "Ford Escape"),
            ("Ford Escort ", "Ford Escort "),
            ("Ford Everest", "Ford Everest"),
            ("Ford Excursion ", "Ford Excursion "),
            ("Ford Expedition", "Ford Expedition"),
            ("Ford Explorer", "Ford Explorer"),
            ("Ford F-150", "Ford F-150"),
            ("Ford F-250", "Ford F-250"),
            ("Ford F-350", "Ford F-350"),
            ("Ford F-450", "Ford F-450"),
            ("Ford F-550", "Ford F-550"),
            ("Ford Fiesta", "Ford Fiesta"),
            ("Ford Five Hundred ", "Ford Five Hundred "),
            ("Ford Flex ", "Ford Flex "),
            ("Ford Focus ", "Ford Focus "),
            ("Ford Freestar ", "Ford Freestar "),
            ("Ford Freestyle ", "Ford Freestyle "),
            ("Ford Fusion", "Ford Fusion"),
            ("Ford Galaxy", "Ford Galaxy"),
            ("Ford GT", "Ford GT"),
            ("Ford Ka", "Ford Ka"),
            ("Ford Kuga", "Ford Kuga"),
            ("Ford Maverick ", "Ford Maverick "),
            ("Ford Mondeo", "Ford Mondeo"),
            ("Ford Mustang", "Ford Mustang"),
            ("Ford Puma", "Ford Puma"),
            ("Ford Ranger", "Ford Ranger"),
            ("Ford S-Max", "Ford S-Max"),
            ("Ford Taurus ", "Ford Taurus "),
            ("Ford Tempo ", "Ford Tempo "),
            ("Ford Thunderbird ", "Ford Thunderbird "),
            ("Ford Transit", "Ford Transit"),
            ("Ford Windstar ", "Ford Windstar "),
        ),
    ),
    (
        "FREIGHTLINER",
        (
            ("Freightliner Cascadia", "Freightliner Cascadia"),
            ("Freightliner Century Class", "Freightliner Century Class"),
            ("Freightliner Coronado", "Freightliner Coronado"),
            ("Freightliner Columbia", "Freightliner Columbia"),
            ("Freightliner M2 106", "Freightliner M2 106"),
            ("Freightliner M2 112", "Freightliner M2 112"),
            ("Freightliner 114SD", "Freightliner 114SD"),
            ("Freightliner 122SD", "Freightliner 122SD"),
            ("Freightliner Business Class M2", "Freightliner Business Class M2"),
            ("Freightliner Sprinter Van", "Freightliner Sprinter Van"),
        ),
    ),
    (
        "GMC",
        (
            ("GMC Acadia", "GMC Acadia"),
            ("GMC Canyon", "GMC Canyon"),
            ("GMC Envoy ", "GMC Envoy "),
            ("GMC Jimmy ", "GMC Jimmy "),
            ("GMC Safari ", "GMC Safari "),
            ("GMC Savana", "GMC Savana"),
            ("GMC Sierra 1500", "GMC Sierra 1500"),
            ("GMC Sierra 2500HD", "GMC Sierra 2500HD"),
            ("GMC Sierra 3500HD", "GMC Sierra 3500HD"),
            ("GMC Terrain", "GMC Terrain"),
            ("GMC Yukon", "GMC Yukon"),
            ("GMC Yukon XL", "GMC Yukon XL"),
        ),
    ),
    (
        "GENESIS",
        (
            ("Genesis G70", "Genesis G70"),
            ("Genesis G80", "Genesis G80"),
            ("Genesis G90", "Genesis G90"),
        ),
    ),
    (
        "HINO",
        (
            ("Hino 155", "Hino 155"),
            ("Hino 195", "Hino 195"),
            ("Hino 258", "Hino 258"),
            ("Hino 268", "Hino 268"),
            ("Hino 338", "Hino 338"),
            ("Hino 358", "Hino 358"),
            ("Hino 500 Series", "Hino 500 Series"),
            ("Hino 700 Series", "Hino 700 Series"),
        ),
    ),
    (
        "HONDA",
        (
            ("Honda Accord", "Honda Accord"),
            ("Honda Accord Hybrid", "Honda Accord Hybrid"),
            ("Honda Amaze", "Honda Amaze"),
            ("Honda Avancier", "Honda Avancier"),
            ("Honda Ballade", "Honda Ballade"),
            ("Honda Brio", "Honda Brio"),
            ("Honda BR-V", "Honda BR-V"),
            ("Honda City", "Honda City"),
            ("Honda Civic", "Honda Civic"),
            ("Honda Clarity", "Honda Clarity"),
            ("Honda CR-V", "Honda CR-V"),
            ("Honda CR-V Hybrid", "Honda CR-V Hybrid"),
            ("Honda CR-Z ", "Honda CR-Z "),
            ("Honda Crosstour ", "Honda Crosstour "),
            ("Honda E", "Honda E"),
            ("Honda Element ", "Honda Element "),
            ("Honda Fit", "Honda Fit"),
            ("Honda Fit/Jazz Hybrid", "Honda Fit/Jazz Hybrid"),
            ("Honda Freed", "Honda Freed"),
            ("Honda HR-V", "Honda HR-V"),
            ("Honda Insight", "Honda Insight"),
            ("Honda Integra ", "Honda Integra "),
            ("Honda Jade", "Honda Jade"),
            (
                "Honda Jazz (known as the Honda Fit in some markets)",
                "Honda Jazz (known as the Honda Fit in some markets)",
            ),
            ("Honda Legend", "Honda Legend"),
            ("Honda Mobilio", "Honda Mobilio"),
            ("Honda N-Box", "Honda N-Box"),
            ("Honda N-One", "Honda N-One"),
            ("Honda N-Van", "Honda N-Van"),
            ("Honda NSX", "Honda NSX"),
            ("Honda Odyssey", "Honda Odyssey"),
            ("Honda Passport", "Honda Passport"),
            ("Honda Pilot", "Honda Pilot"),
            ("Honda Prelude ", "Honda Prelude "),
            ("Honda Ridgeline", "Honda Ridgeline"),
            ("Honda S660", "Honda S660"),
            ("Honda Shuttle", "Honda Shuttle"),
            ("Honda StepWGN", "Honda StepWGN"),
            ("Honda UR-V", "Honda UR-V"),
            (
                "Honda Vezel (known as the Honda HR-V in some markets)",
                "Honda Vezel (known as the Honda HR-V in some markets)",
            ),
        ),
    ),
    (
        "HUMMER",
        (
            ("Hummer H1", "Hummer H1"),
            ("Hummer H2", "Hummer H2"),
            ("Hummer H3", "Hummer H3"),
            ("Hummer H3T", "Hummer H3T"),
        ),
    ),
    (
        "HYUNDAI",
        (
            ("Hyundai Accent", "Hyundai Accent"),
            ("Hyundai Accent Hatchback", "Hyundai Accent Hatchback"),
            ("Hyundai Alcazar", "Hyundai Alcazar"),
            ("Hyundai Elantra", "Hyundai Elantra"),
            ("Hyundai Elantra GT", "Hyundai Elantra GT"),
            ("Hyundai Elantra N", "Hyundai Elantra N"),
            ("Hyundai Entourage ", "Hyundai Entourage "),
            ("Hyundai Eon", "Hyundai Eon"),
            ("Hyundai Equus ", "Hyundai Equus "),
            ("Hyundai Genesis ", "Hyundai Genesis "),
            ("Hyundai Genesis Coupe ", "Hyundai Genesis Coupe "),
            ("Hyundai Getz ", "Hyundai Getz "),
            ("Hyundai Grand i10", "Hyundai Grand i10"),
            (
                "Hyundai Grandeur (known as the Azera in some markets)",
                "Hyundai Grandeur (known as the Azera in some markets)",
            ),
            ("Hyundai H-1", "Hyundai H-1"),
            ("Hyundai i10", "Hyundai i10"),
            ("Hyundai i20", "Hyundai i20"),
            ("Hyundai i30", "Hyundai i30"),
            ("Hyundai i40", "Hyundai i40"),
            ("Hyundai Ioniq", "Hyundai Ioniq"),
            ("Hyundai Kona", "Hyundai Kona"),
            ("Hyundai Kona Electric", "Hyundai Kona Electric"),
            ("Hyundai Matrix ", "Hyundai Matrix "),
            ("Hyundai Nexo", "Hyundai Nexo"),
            ("Hyundai Palisade", "Hyundai Palisade"),
            ("Hyundai Santa Cruz", "Hyundai Santa Cruz"),
            ("Hyundai Santa Fe", "Hyundai Santa Fe"),
            ("Hyundai Sonata", "Hyundai Sonata"),
            ("Hyundai Sonata Hybrid", "Hyundai Sonata Hybrid"),
            (
                "Hyundai Starex (known as the H-1 in some markets)",
                "Hyundai Starex (known as the H-1 in some markets)",
            ),
            ("Hyundai Terracan ", "Hyundai Terracan "),
            ("Hyundai Tucson", "Hyundai Tucson"),
            ("Hyundai Venue", "Hyundai Venue"),
            ("Hyundai Veracruz ", "Hyundai Veracruz "),
            ("Hyundai Verna", "Hyundai Verna"),
            (
                "Hyundai Xcent (known as the Grand i10 Sedan in some markets)",
                "Hyundai Xcent (known as the Grand i10 Sedan in some markets)",
            ),
        ),
    ),
    (
        "INFINITI",
        (
            ("Infiniti Q50", "Infiniti Q50"),
            ("Infiniti Q60", "Infiniti Q60"),
            (
                "Infiniti Q70 (known as the Infiniti M in some markets)",
                "Infiniti Q70 (known as the Infiniti M in some markets)",
            ),
            ("Infiniti QX30", "Infiniti QX30"),
            ("Infiniti QX50", "Infiniti QX50"),
            ("Infiniti QX55", "Infiniti QX55"),
            ("Infiniti QX60", "Infiniti QX60"),
            (
                "Infiniti QX70 (known as the Infiniti FX in some markets)",
                "Infiniti QX70 (known as the Infiniti FX in some markets)",
            ),
            ("Infiniti QX80", "Infiniti QX80"),
        ),
    ),
    (
        "IZUZU",
        (
            ("Isuzu Ascender ", "Isuzu Ascender "),
            (
                "Isuzu (Amigo known as the Isuzu MU in some markets)",
                "Isuzu Amigo (known as the Isuzu MU in some markets)",
            ),
            ("Isuzu Axiom ", "Isuzu Axiom "),
            ("Isuzu D-Max", "Isuzu D-Max"),
            ("Isuzu Hombre ", "Isuzu Hombre "),
            ("Isuzu i-Series ", "Isuzu i-Series "),
            ("Isuzu Impulse ", "Isuzu Impulse "),
            ("Isuzu Oasis ", "Isuzu Oasis "),
            (
                "Isuzu P up (known as the Isuzu KB in some markets)",
                "Isuzu P up (known as the Isuzu KB in some markets)",
            ),
            (
                "Isuzu Trooper (known as the Isuzu Bighorn in some markets)",
                "Isuzu Trooper (known as the Isuzu Bighorn in some markets) ",
            ),
            ("Isuzu VehiCROSS ", "Isuzu VehiCROSS "),
        ),
    ),
    (
        "JAGUAR",
        (
            ("Jaguar F-PACE", "Jaguar F-PACE"),
            ("Jaguar E-PACE", "Jaguar E-PACE"),
            ("Jaguar I-PACE", "Jaguar I-PACE"),
            ("Jaguar XE", "Jaguar XE"),
            ("Jaguar XF", "Jaguar XF"),
            ("Jaguar XJ ", "Jaguar XJ "),
            ("Jaguar XK ", "Jaguar XK "),
            ("Jaguar F-TYPE", "Jaguar F-TYPE"),
        ),
    ),
    (
        "JEEP",
        (
            ("Jeep models:", "Jeep models:"),
            ("Jeep Cherokee", "Jeep Cherokee"),
            ("Jeep Compass", "Jeep Compass"),
            ("Jeep Gladiator", "Jeep Gladiator"),
            ("Jeep Grand Cherokee", "Jeep Grand Cherokee"),
            ("Jeep Renegade", "Jeep Renegade"),
            ("Jeep Wrangler", "Jeep Wrangler"),
        ),
    ),
    (
        "KIA",
        (
            ("Kia models:", "Kia models:"),
            ("Kia Rio", "Kia Rio"),
            ("Kia Forte", "Kia Forte"),
            (
                "Kia Optima (known as K5 in some markets)",
                "Kia Optima (known as K5 in some markets),",
            ),
            ("Kia Stinger", "Kia Stinger"),
            ("Kia Cadenza", "Kia Cadenza"),
            ("Kia K900", "Kia K900"),
            ("Kia Soul", "Kia Soul"),
            (
                "Kia Niro (available as a hybrid, plug-in hybrid, and electric vehicle)",
                "Kia Niro (available as a hybrid, plug-in hybrid, and electric vehicle)",
            ),
            ("Kia Seltos", "Kia Seltos"),
            ("Kia Sportage", "Kia Sportage"),
            ("Kia Sorento", "Kia Sorento"),
            ("Kia Telluride", "Kia Telluride"),
        ),
    ),
    (
        "LAND ROVER",
        (
            ("Land Rover Defender", "Land Rover Defender"),
            ("Land Rover Discovery", "Land Rover Discovery"),
            ("Land Rover Discovery Sport", "Land Rover Discovery Sport"),
            ("Land Rover Range Rover", "Land Rover Range Rover"),
            ("Land Rover Range Rover Sport", "Land Rover Range Rover Sport"),
            ("Land Rover Range Rover Velar", "Land Rover Range Rover Velar"),
            ("Land Rover Range Rover Evoque", "Land Rover Range Rover Evoque"),
        ),
    ),
    (
        "LAMBORGHINI",
        (
            ("Lamborghini Huracán", "Lamborghini Huracán"),
            ("Lamborghini Aventador", "Lamborghini Aventador"),
            ("Lamborghini Urus", "Lamborghini Urus"),
            ("Lamborghini Diablo", "Lamborghini Diablo"),
            ("Lamborghini Murciélago", "Lamborghini Murciélago"),
            ("Lamborghini Countach", "Lamborghini Countach"),
            ("Lamborghini Gallardo", "Lamborghini Gallardo"),
            ("Lamborghini Veneno", "Lamborghini Veneno"),
            ("Lamborghini Sesto Elemento", "Lamborghini Sesto Elemento"),
            ("Lamborghini Reventón", "Lamborghini Reventón"),
            ("Lamborghini Miura", "Lamborghini Miura"),
            ("Lamborghini Espada", "Lamborghini Espada"),
            ("Lamborghini Jarama", "Lamborghini Jarama"),
            ("Lamborghini LM002", "Lamborghini LM002"),
        ),
    ),
    (
        "LEXUS",
        (
            ("Lexus ES", "Lexus ES"),
            ("Lexus IS", "Lexus IS"),
            ("Lexus LS", "Lexus LS"),
            ("Lexus LC", "Lexus LC"),
            ("Lexus RC", "Lexus RC"),
            ("Lexus UX", "Lexus UX"),
            ("Lexus NX", "Lexus NX"),
            ("Lexus RX", "Lexus RX"),
            ("Lexus GX", "Lexus GX"),
            ("Lexus LX", "Lexus LX"),
            ("Lexus LFA ", "Lexus LFA "),
        ),
    ),
    (
        "LINCOLN",
        (
            ("Lincoln Aviator", "Lincoln Aviator"),
            ("Lincoln Continental ", "Lincoln Continental "),
            ("Lincoln Corsair", "Lincoln Corsair"),
            ("Lincoln MKC ", "Lincoln MKC "),
            ("Lincoln MKS ", "Lincoln MKS "),
            ("Lincoln MKT ", "Lincoln MKT "),
            (
                "Lincoln MKX (renamed to Lincoln Nautilus)",
                "Lincoln MKX (renamed to Lincoln Nautilus)",
            ),
            (
                "Lincoln Nautilus (formerly known as Lincoln MKX)",
                "Lincoln Nautilus (formerly known as Lincoln MKX)",
            ),
            ("Lincoln Navigator", "Lincoln Navigator"),
            ("Lincoln Town Car ", "Lincoln Town Car "),
            ("Lincoln Zephyr ", "Lincoln Zephyr "),
        ),
    ),
    (
        "MACK",
        (
            ("Mack Anthem", "Mack Anthem"),
            ("Mack Granite", "Mack Granite"),
            ("Mack Pinnacle", "Mack Pinnacle"),
            ("Mack TerraPro", "Mack TerraPro"),
            ("Mack LR", "Mack LR"),
            ("Mack CH", "Mack CH"),
            ("Mack Vision", "Mack Vision"),
            ("Mack Metro Liner", "Mack Metro Liner"),
            ("Mack Super-Liner", "Mack Super-Liner"),
            ("Mack Titan", "Mack Titan"),
            ("Mack R Series ", "Mack R Series "),
            ("Mack DM Series ", "Mack DM Series "),
        ),
    ),
    (
        "MASERATI",
        (
            ("Maserati models:", "Maserati models:"),
            ("Maserati Ghibli", "Maserati Ghibli"),
            ("Maserati Levante", "Maserati Levante"),
            ("Maserati Quattroporte", "Maserati Quattroporte"),
            ("Maserati GranTurismo ", "Maserati GranTurismo "),
            ("Maserati GranCabrio ", "Maserati GranCabrio "),
        ),
    ),
    (
        "MCLAREN",
        (
            ("McLaren 540C", "McLaren 540C"),
            ("McLaren 570S", "McLaren 570S"),
            ("McLaren 570GT", "McLaren 570GT"),
            ("McLaren 600LT", "McLaren 600LT"),
            ("McLaren 620R", "McLaren 620R"),
            ("McLaren 720S", "McLaren 720S"),
            ("McLaren GT", "McLaren GT"),
            ("McLaren P1 ", "McLaren P1 "),
            ("McLaren Senna ", "McLaren Senna "),
        ),
    ),
    (
        "MERCEDES BENZ",
        (
            ("Mercedes Benz A-Class Sedan", "Mercedes Benz A-Class Sedan"),
            ("Mercedes Benz A-Class Hatchback", "Mercedes Benz A-Class Hatchback"),
            ("Mercedes Benz A-Class L Sedan", "Mercedes Benz A-Class L Sedan"),
            ("Mercedes Benz A-Class L Saloon", "Mercedes Benz A-Class L Saloon"),
            ("Mercedes Benz B-Class Hatchback", "Mercedes Benz B-Class Hatchback"),
            ("Mercedes Benz C-Class Sedan", "Mercedes Benz C-Class Sedan"),
            ("Mercedes Benz C-Class Coupe", "CMercedes Benz -Class Coupe"),
            ("Mercedes Benz C-Class Cabriolet", "Mercedes Benz C-Class Cabriolet"),
            ("Mercedes Benz C-Class Wagon", "Mercedes Benz C-Class Wagon"),
            ("Mercedes Benz CLA-Class Coupe", "Mercedes Benz CLA-Class Coupe"),
            (
                "Mercedes Benz CLA-Class Shooting Brake",
                "Mercedes Benz CLA-Class Shooting Brake",
            ),
            ("Mercedes Benz CLS-Class Coupe", "CMercedes Benz LS-Class Coupe"),
            (
                "Mercedes Benz CLS-Class Shooting Brake",
                "Mercedes Benz CLS-Class Shooting Brake",
            ),
            ("Mercedes Benz E-Class Sedan", "Mercedes Benz E-Class Sedan"),
            ("Mercedes Benz E-Class Coupe", "Mercedes Benz E-Class Coupe"),
            ("Mercedes Benz E-Class Cabriolet", "Mercedes Benz E-Class Cabriolet"),
            ("Mercedes Benz E-Class Wagon", "Mercedes Benz E-Class Wagon"),
            ("Mercedes Benz E-Class All-Terrain", "Mercedes Benz E-Class All-Terrain"),
            ("Mercedes Benz G-Class SUV", "Mercedes Benz G-Class SUV"),
            ("Mercedes Benz GLA-Class SUV", "Mercedes Benz GLA-Class SUV"),
            ("Mercedes Benz GLB-Class SUV", "Mercedes Benz GLB-Class SUV"),
            ("Mercedes Benz GLC-Class SUV", "Mercedes Benz GLC-Class SUV"),
            ("Mercedes Benz GLC-Class Coupe", "Mercedes Benz GLC-Class Coupe"),
            ("Mercedes Benz GLE-Class SUV", "Mercedes Benz GLE-Class SUV"),
            ("Mercedes Benz GLE-Class Coupe", "Mercedes Benz GLE-Class Coupe"),
            ("Mercedes Benz GLS-Class SUV", "Mercedes Benz GLS-Class SUV"),
            ("Mercedes Benz S-Class Sedan", "Mercedes Benz S-Class Sedan"),
            ("Mercedes Benz S-Class Coupe", "Mercedes Benz S-Class Coupe"),
            ("Mercedes Benz S-Class Cabriolet", "Mercedes Benz S-Class Cabriolet"),
            ("Mercedes Benz SL-Class Roadster", "Mercedes Benz SL-Class Roadster"),
            ("Mercedes Benz SLC-Class Roadster", "Mercedes Benz SLC-Class Roadster"),
            ("Mercedes Benz AMG GT Coupe", "Mercedes Benz AMG GT Coupe"),
            ("Mercedes Benz AMG GT Roadster", "Mercedes Benz AMG GT Roadster"),
            ("Mercedes Benz AMG GT 4-Door Coupe", "Mercedes Benz AMG GT 4-Door Coupe"),
            ("Mercedes Benz Maybach S-Class", "Mercedes Benz Maybach S-Class"),
        ),
    ),
    (
        "MAZDA",
        (
            (
                "Mazda2 (also known as Mazda Demio)",
                "Mazda2 (also known as Mazda Demio)",
            ),
            (
                "Mazda3 (also known as Mazda Axela)",
                "Mazda3 (also known as Mazda Axela)",
            ),
            (
                "Mazda5 (also known as Mazda Premacy)",
                "Mazda5 (also known as Mazda Premacy)",
            ),
            (
                "Mazda6 (also known as Mazda Atenza)",
                "Mazda6 (also known as Mazda Atenza)",
            ),
            (
                "Mazda MX-5 (also known as Mazda Miata or Eunos Roadster)",
                "Mazda MX-5 (also known as Mazda Miata or Eunos Roadster)",
            ),
            ("Mazda CX-3", "Mazda CX-3"),
            ("Mazda CX-30", "Mazda CX-30"),
            ("Mazda CX-5", "Mazda CX-5"),
            ("Mazda CX-7 ", "Mazda CX-7 "),
            ("Mazda CX-9", "Mazda CX-9"),
            ("Mazda RX-8 ", "Mazda RX-8 "),
            ("Mazda B-Series ", "Mazda B-Series "),
            ("Mazda MPV ", "Mazda MPV "),
            ("Mazda Tribute ", "Mazda Tribute "),
        ),
    ),
    (
        "MECURY",
        (
            ("MECURY Eight (1938-1951)", "MECURY Eight (1938-1951)"),
            ("MECURY Monterey (1950-1974, 1992-2007)", "MECURY Monterey (1950-1974, 1992-2007)"),
            ("MECURY Comet (1960-1977)", "MECURY Comet (1960-1977)"),
            ("MECURY Cougar (1967-1997, 1999-2002)", "MECURY Cougar (1967-1997, 1999-2002)"),
            ("MECURY Marquis (1967-1986)", "MECURY Marquis (1967-1986)"),
            ("MECURY Montego (1968-1976)", "MECURY Montego (1968-1976)"),
            ("MECURY Cyclone (1968-1971)", "MECURY Cyclone (1968-1971)"),
            ("MECURY Capri (1970-1977)", "MECURY Capri (1970-1977)"),
            ("MECURY Bobcat (1975-1980)", "MECURY Bobcat (1975-1980)"),
            ("MECURY Zephyr (1978-1983)", "MECURY Zephyr (1978-1983)"),
            ("MECURY Lynx (1981-1987)", "MECURY Lynx (1981-1987)"),
            ("MECURY Topaz (1983-1994)", "MECURY Topaz (1983-1994)"),
            ("MECURY Grand Marquis (1983-2011)", "MECURY Grand Marquis (1983-2011)"),
            ("MECURY Sable (1986-2005)", "MECURY Sable (1986-2005)"),
            ("MECURY Tracer (1987-1999)", "MECURY Tracer (1987-1999)"),
            ("MECURY Villager (1993-2002)", "MECURY Villager (1993-2002)"),
            ("MECURY Mountaineer (1997-2010)", "MECURY Mountaineer (1997-2010)"),
            ("MECURY Marauder (2003-2004)", "MECURY Marauder (2003-2004)"),
            ("MECURY Milan (2006-2011)", "MECURY Milan (2006-2011)"),
            ("MECURY Mariner (2005-2011)", "MECURY Mariner (2005-2011)"),
        ),
    ),
    (
        "MINI",
        (
            (
                "Mini Hatch (also known as Mini Cooper or Mini One)",
                "Mini Hatch (also known as Mini Cooper or Mini One)",
            ),
            ("Mini Convertible", "Mini Convertible"),
            ("Mini Clubman", "Mini Clubman"),
            ("Mini Countryman", "Mini Countryman"),
            ("Mini Coupe ", "Mini Coupe "),
            ("Mini Roadster ", "Mini Roadster "),
            ("Mini Paceman ", "Mini Paceman "),
        ),
    ),
    (
        "MITSUBISHI",
        (
            (
                "Mitsubishi Mirage (also known as Mitsubishi Space Star)",
                "Mitsubishi Mirage (also known as Mitsubishi Space Star)",
            ),
            (
                "Mitsubishi Attrage (also known as Mitsubishi Mirage G4)",
                "Mitsubishi Attrage (also known as Mitsubishi Mirage G4)",
            ),
            ("Mitsubishi Lancer", "Mitsubishi Lancer"),
            ("Mitsubishi Galant ", "Mitsubishi Galant "),
            ("Mitsubishi Eclipse Cross", "Mitsubishi Eclipse Cross"),
            ("Mitsubishi Outlander", "Mitsubishi Outlander"),
            (
                "Mitsubishi ASX (also known as Mitsubishi RVR or Outlander Sport)",
                "Mitsubishi ASX (also known as Mitsubishi RVR or Outlander Sport)",
            ),
            (
                "Mitsubishi Pajero (also known as Mitsubishi Montero or Shogun)",
                "Mitsubishi Pajero (also known as Mitsubishi Montero or Shogun)",
            ),
            (
                "Mitsubishi Delica (also known as Mitsubishi L300 or Starwagon)",
                "Mitsubishi Delica (also known as Mitsubishi L300 or Starwagon)",
            ),
            (
                "Mitsubishi Triton (also known as Mitsubishi L200)",
                "Mitsubishi Triton (also known as Mitsubishi L200)",
            ),
            (
                "Mitsubishi Fuso Canter (commercial vehicle)",
                "Mitsubishi Fuso Canter (commercial vehicle)",
            ),
        ),
    ),
    (
        "NISSAN",
        (
            (
                "Nissan Versa (also known as Nissan Tiida or Latio)",
                "Nissan Versa (also known as Nissan Tiida or Latio)",
            ),
            (
                "Nissan Sentra (also known as Nissan Sylphy)",
                "Nissan Sentra (also known as Nissan Sylphy)",
            ),
            ("Nissan Altima", "Nissan Altima"),
            ("Nissan Maxima", "Nissan Maxima"),
            ("Nissan Leaf (electric vehicle)", "Nissan Leaf (electric vehicle)"),
            ("Nissan Juke ", "Nissan Juke "),
            ("Nissan Kicks", "Nissan Kicks"),
            (
                "Nissan Rogue (also known as Nissan X-Trail)",
                "Nissan Rogue (also known as Nissan X-Trail)",
            ),
            ("Nissan Murano", "Nissan Murano"),
            ("Nissan Pathfinder", "Nissan Pathfinder"),
            ("Nissan Armada", "Nissan Armada"),
            (
                "Nissan Frontier (also known as Nissan Navara)",
                "Nissan Frontier (also known as Nissan Navara)",
            ),
            ("Nissan Titan", "Nissan Titan"),
            ("Nissan GT-R", "Nissan GT-R"),
            ("Nissan 370Z", "Nissan 370Z"),
        ),
    ),
    (
        "OLDSMOBILE",
        (
            ("Oldsmobile Curved Dash ", "Oldsmobile Curved Dash "),
            ("Oldsmobile Limited ", "Oldsmobile Limited "),
            ("Oldsmobile Model 44 ", "Oldsmobile Model 44 "),
            ("Oldsmobile Model 60 ", "Oldsmobile Model 60 "),
            ("Oldsmobile Model 66 ", "Oldsmobile Model 66 "),
            ("Oldsmobile Model 68 ", "Oldsmobile Model 68 "),
            ("Oldsmobile Model 90 ", "Oldsmobile Model 90 "),
            ("Oldsmobile Model F ", "Oldsmobile Model F "),
            ("Oldsmobile Series 60 ", "Oldsmobile Series 60 "),
            ("Oldsmobile Series 70 ", "Oldsmobile Series 70 "),
            ("Oldsmobile Series 80 ", "Oldsmobile Series 80 "),
            ("Oldsmobile Series 90 ", "Oldsmobile Series 90 "),
            ("Oldsmobile Series 88 ", "Oldsmobile Series 88 "),
            ("Oldsmobile Starfire ", "Oldsmobile Starfire "),
            ("Oldsmobile 442 ", "Oldsmobile 442 "),
            ("Oldsmobile Toronado ", "Oldsmobile Toronado "),
            ("Oldsmobile Cutlass ", "Oldsmobile Cutlass "),
            ("Oldsmobile Omega ", "Oldsmobile Omega "),
            ("Oldsmobile Achieva ", "Oldsmobile Achieva "),
            ("Oldsmobile Alero ", "Oldsmobile Alero "),
            ("Oldsmobile Aurora ", "Oldsmobile Aurora "),
            ("Oldsmobile Bravada ", "Oldsmobile Bravada "),
            ("Oldsmobile Silhouette ", "Oldsmobile Silhouette "),
        ),
    ),
    (
        "PLYMOUTH",
        (
            ("Plymouth Acclaim", "Plymouth Acclaim"),
            ("Plymouth Arrow Pickup", "Plymouth Arrow Pickup"),
            ("Plymouth Arrow Truck", "Plymouth Arrow Truck"),
            ("Plymouth Barracuda", "Plymouth Barracuda"),
            ("Plymouth Belvedere", "Plymouth Belvedere"),
            ("Plymouth Breeze", "Plymouth Breeze"),
            ("Plymouth Cambridge", "Plymouth Cambridge"),
            ("Plymouth Caravelle", "Plymouth Caravelle"),
            ("Plymouth Champ", "Plymouth Champ"),
            ("Plymouth Colt", "Plymouth Colt"),
            ("Plymouth Conquest", "Plymouth Conquest"),
            ("Plymouth Cranbrook", "Plymouth Cranbrook"),
            ("Plymouth Cricket", "Plymouth Cricket"),
            ("Plymouth Duster", "Plymouth Duster"),
            ("Plymouth Fury", "Plymouth Fury"),
            ("Plymouth Gran Fury", "Plymouth Gran Fury"),
            ("Plymouth Grand Voyager", "Plymouth Grand Voyager"),
            ("Plymouth Horizon", "Plymouth Horizon"),
            ("Plymouth Laser", "Plymouth Laser"),
            ("Plymouth Neon", "Plymouth Neon"),
            ("Plymouth Plaza", "Plymouth Plaza"),
            ("Plymouth Prowler", "Plymouth Prowler"),
            ("Plymouth Reliant", "Plymouth Reliant"),
            ("Plymouth Road Runner", "Plymouth Road Runner"),
            ("Plymouth Sapporo", "Plymouth Sapporo"),
            ("Plymouth Satellite", "Plymouth Satellite"),
            ("Plymouth Savoy", "Plymouth Savoy"),
            ("Plymouth Scamp", "Plymouth Scamp"),
            ("Plymouth Sundance", "Plymouth Sundance"),
            ("Plymouth Superbird", "Plymouth Superbird"),
            ("Plymouth TC3", "Plymouth TC3"),
            ("Plymouth Trailduster", "Plymouth Trailduster"),
            ("Plymouth Turismo", "Plymouth Turismo"),
            ("Plymouth Valiant", "Plymouth Valiant"),
            ("Plymouth VIP", "Plymouth VIP"),
            ("Plymouth Voyager", "Plymouth Voyager"),
        ),
    ),
    (
        "POLARIS",
        (
            ("Polaris Sportsman", "Polaris Sportsman"),
            ("Polaris Scrambler", "Polaris Scrambler"),
            ("Polaris Outlaw", "Polaris Outlaw"),
            ("Polaris Trail Boss", "Polaris Trail Boss"),
            ("Polaris Phoenix", "Polaris Phoenix"),
            ("Polaris Hawkeye", "Polaris Hawkeye"),
            ("Polaris Magnum", "Polaris Magnum"),
            ("Polaris Xplorer", "Polaris Xplorer"),
            ("Polaris Trail Blazer", "Polaris Trail Blazer"),
            ("Polaris Big Boss", "Polaris Big Boss"),
            ("Polaris Worker", "Polaris Worker"),
            ("Side-by-sides:", "Side-by-sides:"),
            ("Polaris RZR", "Polaris RZR"),
            ("Polaris Ranger", "Polaris Ranger"),
            ("Polaris General", "Polaris General"),
            ("Polaris ACE", "Polaris ACE"),
            ("Snowmobiles:", "Snowmobiles:"),
            ("Polaris INDY", "Polaris INDY"),
            ("Polaris Switchback", "Polaris Switchback"),
            ("Polaris RMK", "Polaris RMK"),
            ("Polaris Titan", "Polaris Titan"),
            ("Polaris Voyageur", "Polaris Voyageur"),
            ("Motorcycles:", "Motorcycles:"),
            ("Polaris Slingshot", "Polaris Slingshot"),
            ("Polaris Victory ", "Polaris Victory "),
        ),
    ),
    (
        "PONTIAC",
        (
            ("Pontiac 2+2", "Pontiac 2+2"),
            ("Pontiac Aztek", "Pontiac Aztek"),
            ("Pontiac Bonneville", "Pontiac Bonneville"),
            ("Pontiac Catalina", "Pontiac Catalina"),
            ("Pontiac Chieftain", "Pontiac Chieftain"),
            ("Pontiac Custom S", "Pontiac Custom S"),
            ("Pontiac Fiero", "Pontiac Fiero"),
            ("Pontiac Firebird", "Pontiac Firebird"),
            ("Pontiac G3", "Pontiac G3"),
            ("Pontiac G4", "Pontiac G4"),
            ("Pontiac G5", "Pontiac G5"),
            ("Pontiac G6", "Pontiac G6"),
            ("Pontiac G8", "Pontiac G8"),
            ("Pontiac Grand Am", "Pontiac Grand Am"),
            ("Pontiac Grand Prix", "Pontiac Grand Prix"),
            ("Pontiac GTO", "Pontiac GTO"),
            ("Pontiac LeMans", "Pontiac LeMans"),
            ("Pontiac Montana", "Pontiac Montana"),
            ("Pontiac Parisienne", "Pontiac Parisienne"),
            ("Pontiac Phoenix", "Pontiac Phoenix"),
            ("Pontiac Pursuit", "Pontiac Pursuit"),
            ("Pontiac Solstice", "Pontiac Solstice"),
            ("Pontiac Star Chief", "Pontiac Star Chief"),
            ("Pontiac Streamliner", "Pontiac Streamliner"),
            ("Pontiac Sunbird", "Pontiac Sunbird"),
            ("Pontiac Sunfire", "Pontiac Sunfire"),
            ("Pontiac Super Chief", "Pontiac Super Chief"),
            ("Pontiac Tempest", "Pontiac Tempest"),
            ("Pontiac Torrent", "Pontiac Torrent"),
            ("Pontiac Trans Am", "Pontiac Trans Am"),
            ("Pontiac Ventura", "Pontiac Ventura"),
            ("Pontiac Vibe", "Pontiac Vibe"),
        ),
    ),
    (
        "RAM",
        (
            ("Ram models:", "Ram models:"),
            ("Ram 1500", "Ram 1500"),
            ("Ram 2500", "Ram 2500"),
            ("Ram 3500", "Ram 3500"),
            ("Ram 4500", "Ram 4500"),
            ("Ram 5500", "Ram 5500"),
            ("Ram C/V Tradesman", "Ram C/V Tradesman"),
            ("Ram Dakota ", "Ram Dakota "),
            ("Ram ProMaster", "Ram ProMaster"),
            ("Ram ProMaster City", "Ram ProMaster City"),
        ),
    ),
    (
        "ROLLS ROYCE",
        (
            ("Rolls-Royce 10 hp", "Rolls-Royce 10 hp"),
            ("Rolls-Royce 15 hp", "Rolls-Royce 15 hp"),
            ("Rolls-Royce 20 hp", "Rolls-Royce 20 hp"),
            ("Rolls-Royce 20/25", "Rolls-Royce 20/25"),
            ("Rolls-Royce 25/30", "Rolls-Royce 25/30"),
            ("Rolls-Royce Camargue", "Rolls-Royce Camargue"),
            ("Rolls-Royce Corniche", "Rolls-Royce Corniche"),
            ("Rolls-Royce Corniche II", "Rolls-Royce Corniche II"),
            ("Rolls-Royce Corniche III", "Rolls-Royce Corniche III"),
            ("Rolls-Royce Corniche IV", "Rolls-Royce Corniche IV"),
            ("Rolls-Royce Corniche V", "Rolls-Royce Corniche V"),
            ("Rolls-Royce Dawn", "Rolls-Royce Dawn"),
            ("Rolls-Royce Ghost", "Rolls-Royce Ghost"),
            ("Rolls-Royce Ghost II", "Rolls-Royce Ghost II"),
            ("Rolls-Royce Ghost III", "Rolls-Royce Ghost III"),
            ("Rolls-Royce Phantom", "Rolls-Royce Phantom"),
            ("Rolls-Royce Phantom II", "Rolls-Royce Phantom II"),
            ("Rolls-Royce Phantom III", "Rolls-Royce Phantom III"),
            ("Rolls-Royce Phantom IV", "Rolls-Royce Phantom IV"),
            ("Rolls-Royce Phantom V", "Rolls-Royce Phantom V"),
            ("Rolls-Royce Phantom VI", "Rolls-Royce Phantom VI"),
            ("Rolls-Royce Phantom VII", "Rolls-Royce Phantom VII"),
            ("Rolls-Royce Phantom VIII", "Rolls-Royce Phantom VIII"),
            ("Rolls-Royce Silver Cloud", "Rolls-Royce Silver Cloud"),
            ("Rolls-Royce Silver Dawn", "Rolls-Royce Silver Dawn"),
            ("Rolls-Royce Silver Ghost", "Rolls-Royce Silver Ghost"),
            ("Rolls-Royce Silver Shadow", "Rolls-Royce Silver Shadow"),
            ("Rolls-Royce Silver Spirit", "Rolls-Royce Silver Spirit"),
            ("Rolls-Royce Silver Spur", "Rolls-Royce Silver Spur"),
            ("Rolls-Royce Silver Wraith", "Rolls-Royce Silver Wraith"),
            ("Rolls-Royce Sweptail", "Rolls-Royce Sweptail"),
            ("Rolls-Royce Tourer", "Rolls-Royce Tourer"),
            ("Rolls-Royce Wraith", "Rolls-Royce Wraith"),
        ),
    ),
    (
        "SAAB",
        (
            ("Saab 92 (1949–1956)", "Saab 92 (1949–1956)"),
            ("Saab 93 (1955–1960)", "Saab 93 (1955–1960)"),
            ("Saab 95 (1959–1978)", "Saab 95 (1959–1978)"),
            ("Saab 96 (1960–1980)", "Saab 96 (1960–1980)"),
            ("Saab 99 (1968–1984)", "Saab 99 (1968–1984)"),
            ("Saab Sonett (1966–1974)", "Saab Sonett (1966–1974)"),
            ("Saab 900 (1978–1993)", "Saab 900 (1978–1993)"),
            ("Saab 9000 (1984–1998)", "Saab 9000 (1984–1998)"),
            ("Saab 9-2X (2004–2006)", "Saab 9-2X (2004–2006)"),
            ("Saab 9-3 (1998–2012)", "Saab 9-3 (1998–2012)"),
            ("Saab 9-4X (2011)", "Saab 9-4X (2011)"),
            ("Saab 9-5 (1997–2012)", "Saab 9-5 (1997–2012)"),
        ),
    ),
    (
        "SATURN",
        (
            ("Saturn S-Series (1991–2002)", "Saturn S-Series (1991–2002)"),
            ("Saturn L-Series (2000–2005)", "Saturn L-Series (2000–2005)"),
            ("Saturn Vue (2002–2010)", "Saturn Vue (2002–2010)"),
            ("Saturn Ion (2003–2007)", "Saturn Ion (2003–2007)"),
            ("Saturn Sky (2007–2010)", "Saturn Sky (2007–2010)"),
            ("Saturn Outlook (2007–2010)", "Saturn Outlook (2007–2010)"),
            ("Saturn Aura (2007–2010)", "Saturn Aura (2007–2010)"),
            ("Saturn Astra (2008–2009)", "Saturn Astra (2008–2009)"),
        ),
    ),
    (
        "SCION",
        (
            ("Scion xA (2004-2006)", "Scion xA (2004-2006)"),
            ("Scion xB (2004-2015)", "Scion xB (2004-2015)"),
            ("Scion tC (2005-2016)", "Scion tC (2005-2016)"),
            ("Scion xD (2008-2014)", "Scion xD (2008-2014)"),
            ("Scion iQ (2011-2015)", "Scion iQ (2011-2015)"),
            ("Scion FR-S (2013-2016)", "Scion FR-S (2013-2016)"),
            ("Scion iM (2016)", "Scion iM (2016)"),
            ("Scion iA (2016)", "Scion iA (2016)"),
        ),
    ),
    (
        "SMART",
        (
            ("Smart Fortwo (1998-present)", "Smart Fortwo (1998-present)"),
            (
                "Smart Forfour (2004-2006, 2014-present)",
                "Smart Forfour (2004-2006, 2014-present)",
            ),
            ("Smart Roadster (2003-2005)", "Smart Roadster (2003-2005)"),
            ("Smart Crossblade (2002)", "Smart Crossblade (2002)"),
            ("Smart City-Coupe (1998-2004)", "Smart City-Coupe (1998-2004)"),
            ("Smart City-Cabriolet (2000-2004)", "Smart City-Cabriolet (2000-2004)"),
            (
                "Smart Fortwo Cabriolet (2000-present)",
                "Smart Fortwo Cabriolet (2000-present)",
            ),
            (
                "Smart Fortwo Electric Drive (2007-present)",
                "Smart Fortwo Electric Drive (2007-present)",
            ),
            (
                "Smart Fortwo Brabus (2002-present)",
                "Smart Fortwo Brabus (2002-present)",
            ),
        ),
    ),
    (
        "SUBARU",
        (
            ("Subaru 1500 (1954–1955)", "Subaru 1500 (1954–1955)"),
            ("Subaru 360 (1958–1971)", "Subaru 360 (1958–1971)"),
            ("Subaru Sambar (1961–present)", "Subaru Sambar (1961–present)"),
            ("Subaru R-2 (1969–1972)", "Subaru R-2 (1969–1972)"),
            ("Subaru Leone (1971–1994)", "Subaru Leone (1971–1994)"),
            ("Subaru BRAT (1978–1994)", "Subaru BRAT (1978–1994)"),
            ("Subaru XT (1985–1991)", "Subaru XT (1985–1991)"),
            ("Subaru Legacy (1989–present)", "Subaru Legacy (1989–present)"),
            ("Subaru Impreza (1992–present)", "Subaru Impreza (1992–present)"),
            ("Subaru Alcyone SVX (1991–1996) ", "Subaru Alcyone SVX (1991–1996)"),
            ("Subaru Forester (1997–present)", "Subaru Forester (1997–present)"),
            ("Subaru Outback (1994–present)", "Subaru Outback (1994–present)"),
            ("Subaru Baja (2002–2006)", "Subaru Baja (2002–2006)"),
            ("Subaru Tribeca (2005–2014)", "Subaru Tribeca (2005–2014)"),
            ("Subaru WRX (1992–present)", "Subaru WRX (1992–present)"),
            ("Subaru XV Crosstrek (2013–2015)", "Subaru XV Crosstrek (2013–2015)"),
            ("Subaru Ascent (2018–present)", "Subaru Ascent (2018–present)"),
            ("Subaru BRZ (2012–present)", "Subaru BRZ (2012–present)"),
            ("Subaru Crosstrek (2018–present)", "Subaru Crosstrek (2018–present)"),
            ("Subaru Levorg (2014–present)", "Subaru Levorg (2014–present)"),
        ),
    ),
    (
        "SUZUKI",
        (
            ("Suzuki Aerio", "Suzuki  Aerio"),
            ("Suzuki Alto", "Suzuki  Alto"),
            ("Suzuki Baleno", "Suzuki  Baleno"),
            ("Suzuki Cappuccino", "Suzuki  Cappuccino"),
            ("Suzuki Carry", "Suzuki  Carry"),
            ("Suzuki Celerio", "Suzuki  Celerio"),
            ("Suzuki Cultus", "Suzuki  Cultus"),
            ("Suzuki Equator", "Suzuki  Equator"),
            ("Suzuki Escudo", "Suzuki  Escudo"),
            ("Suzuki Esteem", "Suzuki  Esteem"),
            ("Suzuki Every", "Suzuki  Every"),
            ("Suzuki Forenza", "Suzuki  Forenza"),
            ("Suzuki Fronte", "Suzuki  Fronte"),
            ("Suzuki Grand Vitara", "Suzuki Grand Vitara"),
            ("Suzuki Ignis", "Suzuki  Ignis"),
            ("Suzuki Jimny", "Suzuki  Jimny"),
            ("Suzuki Kizashi", "Suzuki  Kizashi"),
            ("Suzuki Lapin", "Suzuki  Lapin"),
            ("Suzuki LJ", "Suzuki  LJ"),
            ("Suzuki MR Wagon", "Suzuki MR Wagon"),
            ("Suzuki Reno", "Suzuki  Reno"),
            ("Suzuki Samurai", "Suzuki  Samurai"),
            ("Suzuki Sidekick", "Suzuki  Sidekick"),
            ("Suzuki Solio", "Suzuki  Solio"),
            ("Suzuki Splash", "Suzuki  Splash"),
            ("Suzuki Swift", "Suzuki  Swift"),
            ("Suzuki SX4", "Suzuki  SX4"),
            ("Suzuki Verona", "Suzuki  Verona"),
            ("Suzuki Vitara", "Suzuki  Vitara"),
            ("Suzuki Wagon R+", "Suzuki Wagon R+"),
        ),
    ),
    (
        "TESLA",
        (
            ("Tesla Model S", "Tesla Model S"),
            ("Tesla Model X", "Tesla Model X"),
            ("Tesla Model 3", "Tesla Model 3"),
            ("Tesla Model Y", "Tesla Model Y"),
            ("Tesla Roadster (2022)", "Tesla Roadster (2022)"),
        ),
    ),
    (
        "TOYOTA",
        (
            ("Toyota 86", "Toyota 86"),
            ("Toyota 4Runner", "Toyota 4Runner"),
            ("Toyota Avalon", "Toyota Avalon"),
            ("Toyota Avalon Hybrid", "Toyota Avalon Hybrid"),
            ("Toyota C-HR", "Toyota C-HR"),
            ("Toyota Camry", "Toyota Camry"),
            ("Toyota Camry Hybrid", "Toyota Camry Hybrid"),
            ("Toyota Corolla", "Toyota Corolla"),
            ("Toyota Corolla Hatchback", "Toyota Corolla Hatchback"),
            ("Toyota Corolla Hybrid", "Toyota Corolla Hybrid"),
            ("Toyota GR Supra", "Toyota GR Supra"),
            ("Toyota Highlander", "Toyota Highlander"),
            ("Toyota Highlander Hybrid", "Toyota Highlander Hybrid"),
            ("Toyota Land Cruiser", "Toyota Land Cruiser"),
            ("Toyota Mirai", "Toyota Mirai"),
            ("Toyota Prius", "Toyota Prius"),
            ("Toyota Prius Prime", "Toyota Prius Prime"),
            ("Toyota RAV4", "Toyota RAV4"),
            ("Toyota RAV4 Hybrid", "Toyota RAV4 Hybrid"),
            ("Toyota Sequoia", "Toyota Sequoia"),
            ("Toyota Sienna", "Toyota Sienna"),
            ("Toyota Tacoma", "Toyota Tacoma"),
            ("Toyota Tundra", "Toyota Tundra"),
            ("Toyota Venza", "Toyota Venza"),
            ("Toyota Yaris", "Toyota Yaris"),
            ("Toyota Yaris Hatchback", "Toyota Yaris Hatchback"),
        ),
    ),
    (
        "VOLKSWAGEN",
        (
            ("Volkswagen Amarok", "Volkswagen Amarok"),
            ("Volkswagen Arteon", "Volkswagen Arteon"),
            ("Volkswagen Atlas", "Volkswagen Atlas"),
            ("Volkswagen Beetle", "Volkswagen Beetle"),
            ("Volkswagen Bora", "Volkswagen Bora"),
            ("Volkswagen Caddy", "Volkswagen Caddy"),
            ("Volkswagen California", "Volkswagen California"),
            ("Volkswagen Caravelle", "Volkswagen Caravelle"),
            ("Volkswagen CC", "Volkswagen CC"),
            ("Volkswagen Corrado", "Corrado"),
            ("Volkswagen Crafter", "Crafter"),
            ("Volkswagen CrossFox", "CrossFox"),
            ("Volkswagen e-Golf", "e-Golf"),
            ("Volkswagen Eos", "Volkswagen Eos"),
            ("Volkswagen Fox", "Volkswagen Fox"),
            ("Volkswagen Golf", "Volkswagen Golf"),
            ("Volkswagen Golf Alltrack", "Volkswagen Golf Alltrack"),
            ("Volkswagen Golf GTI", "Volkswagen Golf GTI"),
            ("Volkswagen Golf R", "GVolkswagen olf R"),
            ("Volkswagen Golf SportWagen", "Volkswagen Golf SportWagen"),
            ("Volkswagen ID.3", "Volkswagen ID.3"),
            ("Volkswagen ID.4", "Volkswagen ID.4"),
            ("Volkswagen Jetta", "Volkswagen Jetta"),
            ("Volkswagen K70", "Volkswagen K70"),
            ("Volkswagen Karmann Ghia", "Volkswagen Karmann Ghia"),
            ("Volkswagen Lupo", "Volkswagen Lupo"),
            ("Volkswagen Multivan", "Volkswagen Multivan"),
            ("Volkswagen New Beetle", "Volkswagen New Beetle"),
            ("Volkswagen Passat", "Volkswagen Passat"),
            ("Volkswagen Phaeton", "Volkswagen Phaeton"),
            ("Volkswagen Polo", "Volkswagen Polo"),
            ("Volkswagen Rabbit", "Volkswagen Rabbit"),
            ("Volkswagen Santana", "Volkswagen Santana"),
            ("Volkswagen Scirocco", "Volkswagen Scirocco"),
            ("Volkswagen Sharan", "Volkswagen Sharan"),
            ("Volkswagen T-Cross", "Volkswagen T-Cross"),
            ("Volkswagen T-Roc", "Volkswagen T-Roc"),
            ("Volkswagen Tiguan", "Volkswagen Tiguan"),
            ("Volkswagen Touareg", "Volkswagen Touareg"),
            ("Volkswagen Touran", "Volkswagen Touran"),
            ("Volkswagen Transporter", "Volkswagen Transporter"),
            ("Volkswagen up!", "Volkswagen up!"),
        ),
    ),
    (
        "VOLVO",
        (
            ("Volvo 120 Series", "Volvo 120 Series"),
            ("Volvo 140 Series", "Volvo 140 Series"),
            ("Volvo 164", "Volvo 164"),
            ("Volvo 1800", "Volvo 1800"),
            ("Volvo 200 Series", "Volvo 200 Series"),
            ("Volvo 300 Series", "Volvo 300 Series"),
            ("Volvo 400 Series", "Volvo 400 Series"),
            ("Volvo 480", "Volvo 480"),
            ("Volvo 66", "Volvo 66"),
            ("Volvo 700 Series", "Volvo 700 Series"),
            ("Volvo 800 Series", "Volvo 800 Series"),
            ("Volvo 850", "Volvo 850"),
            ("Volvo 900 Series", "Volvo 900 Series"),
            ("Volvo C30", "Volvo C30"),
            ("Volvo C70", "Volvo C70"),
            ("Volvo Cross Country", "Volvo Cross Country"),
            ("Volvo P1800", "Volvo P1800"),
            ("Volvo S40", "Volvo S40"),
            ("Volvo S60", "Volvo S60"),
            ("Volvo S70", "Volvo S70"),
            ("Volvo S80", "Volvo S80"),
            ("Volvo S90", "Volvo S90"),
            ("Volvo V40", "Volvo V40"),
            ("Volvo V50", "Volvo V50"),
            ("Volvo V60", "Volvo V60"),
            ("Volvo V70", "Volvo V70"),
            ("Volvo V90", "Volvo V90"),
            ("Volvo XC40", "Volvo XC40"),
            ("Volvo XC60", "Volvo XC60"),
            ("Volvo XC70", "Volvo XC70"),
            ("Volvo XC90", "Volvo XC90"),
        ),
    ),
    (
        "WINNEBAGO",
        (
            ("Winnebago Adventurer", "Winnebago Adventurer"),
            ("Winnebago Aspect", "Winnebago Aspect"),
            ("Winnebago Brave", "Winnebago Brave"),
            ("Winnebago Chieftain", "Winnebago Chieftain"),
            ("Winnebago Era", "Winnebago Era"),
            ("Winnebago Forza", "Winnebago Forza"),
            ("Winnebago Grand Tour", "Winnebago Grand Tour"),
            ("Winnebago Horizon", "Winnebago Horizon"),
            ("Winnebago Intent", "Winnebago Intent"),
            ("Winnebago Journey", "Winnebago Journey"),
            ("Winnebago Minnie Winnie", "Winnebago Minnie Winnie"),
            ("Winnebago Navion", "Winnebago Navion"),
            ("Winnebago Outlook", "Winnebago Outlook"),
            ("Winnebago Paseo", "Winnebago Paseo"),
            ("Winnebago Revel", "Winnebago Revel"),
            ("Winnebago Sightseer", "Winnebago Sightseer"),
            ("Winnebago Solei", "Winnebago Solei"),
            ("Winnebago Spirit", "Winnebago Spirit"),
            ("Winnebago Sunova", "Winnebago Sunova"),
            ("Winnebago Sunstar", "Winnebago Sunstar"),
            ("Winnebago Tour", "Winnebago Tour"),
            ("Winnebago Travato", "Winnebago Travato"),
            ("Winnebago Trend", "Winnebago Trend"),
            ("Winnebago View", "Winnebago View"),
        ),
    ),
]

# Create your models here.

Rate = (
    ('Per Hour', 'Per Hour'),
    ('Per Day', 'Per Day'),
    ('Per Week', 'Per Week'),
    ('Per Month', 'Per Month'),
)

Condition = (
    ('New', 'New'),
    ('Local Used', 'Local Used'),
    ('Foriegn Used', 'Foriegn Used'),
)
Steering = (
    ('Right', 'Right'),
    ('Left', 'Left'),
)

Fuels = (
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('Electric', 'Electric'),
    ('Solar', 'Solar'),
    ('Hybrid', 'Hybrid'),

)

Transmissions = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
    ('Semi Automatic', 'Semi Automatic'),
    ('Continious Variable Transmission', 'Continious Variable Transmission'),

)

Countries = (
    ("Afghanistan", "Afghanistan"),
    ("Åland Islands", "Åland Islands"),
    ("Albania", "Albania"),
    ("Algeria", "Algeria"),
    ("American Samoa" , "American Samoa"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Anguilla", "Anguilla"),
    ("Antarctica", "Antarctica"),
    ("Antigua and Barbuda" , "Antigua and Barbuda"),
    ("Argentina", "Argentina"),
    ("Armenia", "Armenia"),
    ("Aruba", "Aruba"),
    ("Australia", "Australia"),
    ("Austria", "Austria"),
    ("Azerbaijan", "Azerbaijan"),
    ("Bahamas", "Bahamas"),
    ("Bahrain", "Bahrain"),
    ("Bangladesh", "Bangladesh"),
    ("Barbados", "Barbados"),
    ("Belarus", "Belarus"),
    ("Belgium", "Belgium"),
    ("Belize", "Belize"),
    ("Benin", "Benin"),
    ("Bermuda", "Bermuda"),
    ("Bhutan", "Bhutan"),
    ("Bolivia", "Bolivia"),
    ("Bonaire, Sint Eustatius and Saba", "Bonaire, Sint Eustatius and Saba"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Botswana", "Botswana"),
    ("Bouvet Island", "Bouvet Island"),
    ("Brazil", "Brazil"),
    ("British Indian Ocean Territory", "British Indian Ocean Territory"),
    ("Brunei Darussalam", "Brunei Darussalam"),
    ("Bulgaria", "Bulgaria"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burundi", "Burundi"),
    ("Cabo Verde", "Cabo Verde"),
    ("Cambodia", "Cambodia"),
    ("Cameroon", "Cameroon"),
    ("Canada", "Canada"),
    ("Cayman Islands", "Cayman Islands"),
    ("Central African Republic", "Central African Republic"),
    ("Chad", "Chad"),
    ("Chile", "Chile"),
    ("China", "China"),
    ("Christmas Island", "Christmas Island"),
    ("Cocos (Keeling) Islands", "Cocos (Keeling) Islands"),
    ("Colombia", "Colombia"),
    ("Comoros", "Comoros"),
    ("Congo", "Congo"),
    ("Congo (the Democratic Republic of the)", "Congo (the Democratic Republic of the)"),
    ("Cook Islands", "Cook Islands"),
    ("Costa Rica", "Costa Rica"),
    ("Côte d'Ivoire", "Côte d'Ivoire"),
    ("Croatia", "Croatia"),
    ("Cuba", "Cuba"),
    ("Curaçao", "Curaçao"),
    ("Cyprus", "Cyprus"),
    ("Czechia", "Czechia"),
    ("Denmark", "Denmark"),
    ("Djibouti", "Djibouti"),
    ("Dominica", "Dominica"),
    ("Dominican Republic", "Dominican Republic"),
    ("Ecuador", "Ecuador"),
    ("Egypt", "Egypt"),
    ("El Salvador", "El Salvador"),
    ("Equatorial Guinea", "Equatorial Guinea"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonia"),
    ("Eswatini", "Eswatini"),
    ("Ethiopia", "Ethiopia"),
    ("Falkland Islands (Malvinas)", "Falkland Islands (Malvinas)"),
    ("Faroe Islands", "Faroe Islands"),
    ("Fiji", "Fiji"),
    ("Finland", "Finland"),
    ("France", "France"),
    ("French Guiana", "French Guiana"),
    ("French Polynesia", "French Polynesia"),
    ("French Southern Territories", "French Southern Territories"),
    ("Gabon", "Gabon"),
    ("Gambia", "Gambia"),
    ("Georgia", "Georgia"),
    ("Germany", "Germany"),
    ("Ghana", "Ghana"),
    ("Gibraltar", "Gibraltar"),
    ("Greece", "Greece"),
    ("Greenland", "Greenland"),
    ("Grenada", "Grenada"),
    ("Guadeloupe", "Guadeloupe"),
    ("Guam", "Guam"),
    ("Guatemala", "Guatemala"),
    ("Guernsey", "Guernsey"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bissau"),
    ("Guyana", "Guyana"),
    ("Haiti", "Haiti"),
    ("Heard Island and McDonald Islands", "Heard Island and McDonald Islands"),
    ("Holy See", "Holy See"),
    ("Honduras", "Honduras"),
    ("Hong Kong", "Hong Kong"),
    ("Hungary", "Hungary"),
    ("Iceland", "Iceland"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Iran", "Iran"),
    ("Iraq", "Iraq"),
    ("Ireland", "Ireland"),
    ("Isle of Man", "Isle of Man"),
    ("Israel", "Israel"),
    ("Italy", "Italy"),
    ("Jamaica", "Jamaica"),
    ("Japan", "Japan"),
    ("Jersey", "Jersey"),
    ("Jordan", "Jordan"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kenya", "Kenya"),
    ("Kiribati", "Kiribati"),
    ("Korea (the Democratic People's Republic of)", "Korea (the Democratic People's Republic of)"),
    ("Korea (the Republic of)", "Korea (the Republic of)"),
    ("Kuwait", "Kuwait"),
    ("Kyrgyzstan", "Kyrgyzstan"),
    ("Lao People's Democratic Republic", "Lao People's Democratic Republic"),
    ("Latvia", "Latvia"),
    ("Lebanon", "Lebanon"),
    ("Lesotho", "Lesotho"),
    ("Liberia", "Liberia"),
    ("Libya", "Libya"),
    ("Liechtenstein", "Liechtenstein"),
    ("Lithuania", "Lithuania"),
    ("Luxembourg", "Luxembourg"),
    ("Macao", "Macao"),
    ("Madagascar", "Madagascar"),
    ("Malawi", "Malawi"),
    ("Malaysia", "Malaysia"),
    ("Maldives", "Maldives"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Marshall Islands", "Marshall Islands"),
    ("Martinique", "Martinique"),
    ("Mauritania", "Mauritania"),
    ("Mauritius", "Mauritius"),
    ("Mayotte", "Mayotte"),
    ("Mexico", "Mexico"),
    ("Micronesia", "Micronesia"),
    ("Moldova", "Moldova"),
    ("Monaco", "Monaco"),
    ("Mongolia", "Mongolia"),
    ("Montenegro", "Montenegro"),
    ("Montserrat", "Montserrat"),
    ("Morocco", "Morocco"),
    ("Mozambique", "Mozambique"),
    ("Myanmar", "Myanmar"),
    ("Namibia", "Namibia"),
    ("Nauru", "Nauru"),
    ("Nepal", "Nepal"),
    ("Netherlands", "Netherlands"),
    ("New Caledonia", "New Caledonia"),
    ("New Zealand", "New Zealand"),
    ("Nicaragua", "Nicaragua"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigeria"),
    ("Niue", "Niue"),
    ("Norfolk Island", "Norfolk Island"),
    ("North Macedonia", "North Macedonia"),
    ("Northern Mariana Islands", "Northern Mariana Islands"),
    ("Norway", "Norway"),
    ("Oman", "Oman"),
    ("Pakistan", "Pakistan"),
    ("Palau", "Palau"),
    ("Palestine", "Palestine"),
    ("Panama", "Panama"),
    ("Papua New Guinea", "Papua New Guinea"),
    ("Paraguay", "Paraguay"),
    ("Peru", "Peru"),
    ("Philippines", "Philippines"),
    ("Pitcairn", "Pitcairn"),
    ("Poland", "Poland"),
    ("Portugal", "Portugal"),
    ("Puerto Rico", "Puerto Rico"),
    ("Qatar", "Qatar"),
    ("Réunion", "Réunion"),
    ("Romania", "Romania"),
    ("Russian Federation", "Russian Federation"),
    ("Rwanda", "Rwanda"),
    ("Saint Barthélemy", "Saint Barthélemy"),
    ("Saint Helena, Ascension and Tristan da Cunha", "Saint Helena, Ascension and Tristan da Cunha"),
    ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
    ("Saint Lucia", "Saint Lucia"),
    ("Saint Martin (French part)", "Saint Martin (French part)"),
    ("Saint Pierre and Miquelon", "Saint Pierre and Miquelon"),
    ("Saint Vincent and the Grenadines", "Saint Vincent and the Grenadines"),
    ("Samoa", "Samoa"),
    ("San Marino", "San Marino"),
    ("Sao Tome and Principe", "Sao Tome and Principe"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Senegal", "Senegal"),
    ("Serbia", "Serbia"),
    ("Seychelles", "Seychelles"),
    ("Sierra Leone", "Sierra Leone"),
    ("Singapore", "Singapore"),
    ("Sint Maarten (Dutch part)", "Sint Maarten (Dutch part)"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Solomon Islands", "Solomon Islands"),
    ("Somalia", "Somalia"),
    ("South Africa", "South Africa"),
    ("South Georgia and the South Sandwich Islands", "South Georgia and the South Sandwich Islands"),
    ("South Sudan", "South Sudan"),
    ("Spain", "Spain"),
    ("Sri Lanka", "Sri Lanka"),
    ("Sudan", "Sudan"),
    ("Suriname", "Suriname"),
    ("Svalbard and Jan Mayen", "Svalbard and Jan Mayen"),
    ("Sweden", "Sweden"),
    ("Switzerland", "Switzerland"),
    ("Syria", "Syria"),
    ("Taiwan", "Taiwan"),
    ("Tajikistan", "Tajikistan"),
    ("Tanzania", "Tanzania"),
    ("Thailand", "Thailand"),
    ("Timor-Leste", "Timor-Leste"),
    ("Togo", "Togo"),
    ("Tokelau", "Tokelau"),
    ("Tonga", "Tonga"),
    ("Trinidad and Tobago", "Trinidad and Tobago"),
    ("Tunisia", "Tunisia"),
    ("Turkey", "Turkey"),
    ("Turkmenistan", "Turkmenistan"),
    ("Turks and Caicos Islands", "Turks and Caicos Islands"),
    ("Tuvalu", "Tuvalu"),
    ("Uganda", "Uganda"),
    ("Ukraine", "Ukraine"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("United Kingdom of Great Britain and Northern Ireland", "United Kingdom of Great Britain and Northern Ireland"),
    ("United States Minor Outlying Islands", "United States Minor Outlying Islands"),
    ("United States of America", "United States of America"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistan", "Uzbekistan"),
    ("Vanuatu", "Vanuatu"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Virgin Islands (British)", "Virgin Islands (British)"),
    ("Virgin Islands (U.S.)", "Virgin Islands (U.S.)"),
    ("Wallis and Futuna", "Wallis and Futuna"),
    ("Western Sahara", "Western Sahara"),
    ("Yemen", "Yemen"),
    ("Zambia", "Zambia"),
    ("Zimbabwe", "Zimbabwe"),

)

Regions = (
   ('VOLTA ',  'VOLTA '),
   ('BRONG AHAFO ',  'BRONG AHAFO '),
   ('OTI ',  'OTI '),
   ('CENTRAL ',  'CENTRAL '),
   ('EASTERN ',  'EASTERN '),
   ('GREATER ACCRA ',  'GREATER ACCRA '),
   ('NORTH EAST ',  'NORTH EAST '),
   ('NORTHERN ',  'NORTHERN '),
   ('SAVANNAH ',  'SAVANNAH '),
   ('UPPER EAST ',  'UPPER EAST '),
   ('UPPER WEST ',  'UPPER WEST '),
   ('WESTERN ',  'WESTERN '),
   ('WESTERN NORTH ',  'WESTERN NORTH '),
   ('BONO EAST  ',  'BONO EAST  '),
   ('AHAFO ',  'AHAFO '),
   ('ASHANTI ',  'ASHANTI '),
)
  

def accessories_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('accessories', timestamp, filename)

def lists_accessories_images_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('accessories_images', timestamp, filename)

def list_rental_images_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('list_rental_images_path', timestamp, filename)


 
from django.core.validators import RegexValidator

class YearField(models.CharField):
    default_validators = [RegexValidator(r'^\d{4}$', 'Enter a valid year.')]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 4
        super().__init__(*args, **kwargs)

def ship_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('ship_car', timestamp, filename)

def ship_images_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('ship_car_images', timestamp, filename)


def sell_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('sell_car', timestamp, filename)

def sell_images_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('sell_car_images', timestamp, filename)


def rental_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('rental_car', timestamp, filename)

def rental_images_path(instance, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join('rental_car_images', timestamp, filename)


 
# Create your models here.
class LetUsSellYourCar(models.Model):
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    your_name = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to=sell_path)
    description =  models.TextField()
    title =  models.CharField(max_length = 150)
    condition = models.CharField(max_length = 150, choices=Condition)
    mileage = models.PositiveIntegerField()
    location = models.CharField(max_length = 100)
    steering = models.CharField(max_length = 100, choices=Steering)
    color = models.CharField(max_length = 100)
    transmission = models.CharField(max_length = 100, choices=Transmissions)
    fuel = models.CharField(max_length = 100, choices=Fuels)
    interior_color = models.CharField(max_length = 100) 
    year_manufactured = YearField()
    registered = models.BooleanField(default=False)
    duty_paid = models.BooleanField(default=False)
    accessories = models.TextField()
    price =  models.DecimalField(decimal_places=2, max_digits=10)
    image_1 = models.ImageField(upload_to=sell_images_path, null=True, blank=True)
    image_2 = models.ImageField(upload_to=sell_images_path, null=True, blank=True)
    image_3 = models.ImageField(upload_to=sell_images_path, null=True, blank=True)
    image_4 = models.ImageField(upload_to=sell_images_path, null=True, blank=True)
    anything_u_want_to_tell_us = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=100, choices=Regions)
    makes_and_model = models.CharField(max_length = 150, choices=CarModelsAndMakes)
    slug = models.SlugField(blank=True, null=True, editable=False)
    attended_to = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Let Us Sell Your Car"



    def __str__(self):
        return f'{self.your_name} - {self.makes_and_model}'
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.your_name))
        super().save(*args, **kwargs)


 





# Create your models here.
class ShipCarForUsSell(models.Model):
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)   
    your_name = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to=ship_path)
    description =  models.TextField()
    title =  models.CharField(max_length = 150)
    condition = models.CharField(max_length = 150, choices=Condition)
    mileage = models.PositiveIntegerField()
    location = models.CharField(max_length = 100)
    steering = models.CharField(max_length = 100, choices=Steering)
    color = models.CharField(max_length = 100)
    transmission = models.CharField(max_length = 100, choices=Transmissions)
    country = models.CharField(max_length = 100, choices=Countries)
    fuel = models.CharField(max_length = 100, choices=Fuels)
    interior_color = models.CharField(max_length = 100)
    year_manufactured = YearField()
    registered = models.BooleanField(default=False)
    duty_paid = models.BooleanField(default=False)
    accessories = models.TextField()
    price =  models.DecimalField(decimal_places=2, max_digits=10)
    image_1 = models.ImageField(upload_to=ship_images_path, null=True, blank=True)
    image_2 = models.ImageField(upload_to=ship_images_path, null=True, blank=True)
    image_3 = models.ImageField(upload_to=ship_images_path, null=True, blank=True)
    image_4 = models.ImageField(upload_to=ship_images_path, null=True, blank=True)
    attended_to = models.BooleanField(default=False)
    anything_u_want_to_tell_us = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    makes_and_model = models.CharField(max_length = 150, choices=CarModelsAndMakes)
    slug = models.SlugField(blank=True, null=True, editable=False)

    class Meta:
        verbose_name_plural = "Ship Car For Us Sell"



    def __str__(self):
        return f'{self.your_name} {self.makes_and_model}'
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.your_name))
        super().save(*args, **kwargs)








class ContactUsForEnquires(models.Model):
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)     
    name = models.CharField(max_length = 100)
    enquiry = models.TextField()
    attended_to = models.BooleanField(default=False)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Contact Us For Enquires"

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)




 
class CarRental(models.Model):
    car = models.CharField(max_length = 150)
    description = models.TextField()
    rate = models.DecimalField(decimal_places = 2, max_digits=10)
    per = models.CharField(max_length = 100, choices=Rate)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length = 100)
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)     
    color = models.CharField(max_length = 100)
    interior_color = models.CharField(max_length = 100)
    accessories = models.TextField()
    main_image = models.ImageField(upload_to=rental_path)
    region = models.CharField(max_length=100, choices=Regions)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True) 
 


    def __str__(self):
        return f'{self.car}'
    
    class Meta:
        verbose_name_plural = "Car Rentals"

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.car))
        super().save(*args, **kwargs)


     
     
class CarRentalImage(models.Model):
    image = models.ImageField(upload_to=rental_images_path)
    car =  models.ForeignKey(CarRental, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.car.car}'
    
    class Meta:
        verbose_name_plural = "Car Rental Images"

    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.car.car))
        super().save(*args, **kwargs)


     
     
     
class RentCar(models.Model):
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 100)
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    email = models.EmailField()
    car = models.ForeignKey(CarRental, on_delete=models.CASCADE)
    region = models.CharField(max_length=100, choices=Regions)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    attended_to = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)


  

    
#    
   

class ListCarRental(models.Model):
    car = models.CharField(max_length = 150)
    description = models.TextField()
    rate = models.DecimalField(decimal_places = 2, max_digits=10)
    per = models.CharField(max_length = 100, choices=Rate)
    location = models.CharField(max_length = 100)
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)     
    color = models.CharField(max_length = 100)
    interior_color = models.CharField(max_length = 100)
    accessories = models.TextField()
    main_image = models.ImageField(upload_to=rental_path)
    email =  models.EmailField()
    region = models.CharField(max_length=100, choices=Regions)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True) 
    image_1 = models.ImageField(upload_to=list_rental_images_path, null=True, blank=True)
    image_2 = models.ImageField(upload_to=list_rental_images_path, null=True, blank=True)
    image_3 = models.ImageField(upload_to=list_rental_images_path, null=True, blank=True)
    image_4 = models.ImageField(upload_to=list_rental_images_path, null=True, blank=True)
    approved = models.BooleanField(default=False)
          


    def __str__(self):
        return f'{self.car}'
    
    class Meta:
        verbose_name_plural = "List Car Rentals"

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.car))
        super().save(*args, **kwargs)


# Create your models here.
class ListAccessories(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    main_image = models.ImageField(upload_to=accessories_path)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(blank=True, null=True, editable=False)
    
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    region = models.CharField(max_length=100, choices=Regions)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    image_1 = models.ImageField(upload_to=lists_accessories_images_path, null=True, blank=True)
    image_2 = models.ImageField(upload_to=lists_accessories_images_path, null=True, blank=True)
    image_3 = models.ImageField(upload_to=lists_accessories_images_path, null=True, blank=True)
    image_4 = models.ImageField(upload_to=lists_accessories_images_path, null=True, blank=True)
    approved = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "List Accessories"

    def __str__(self):
        return f'{self.name}'
    
    

    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)
        
        


class RequestDrivingSch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=100, choices=Regions)
    budget = models.DecimalField(decimal_places = 2, max_digits=10)
    anything_else = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.location}'
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)



 


class ListDrivingSch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    driving_sch_name = models.CharField(max_length=100)
    services_offered = models.TextField()
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{1,3}?\s?\-?[0-9]{1,15}$',
        message="Phone number must be entered in the format: '+999 999999999'. Up to 15 digits allowed."
    )
    contact_no = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) 
    region = models.CharField(max_length=100, choices=Regions)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.location}'
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)


