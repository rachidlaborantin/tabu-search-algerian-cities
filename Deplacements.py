
wilayas = ["ADRAR", "CHLEF", "LAGHOUAT", "O. EL BOUAGHI", "BATNA",

        "BEJAIA", "BISKRA", "BECHAR", "BLIDA", "BOUIRA", "TAMANRASSET",

        "TEBESSA", "TLEMCEN", "TIARET", "TIZI-OUZOU", "ALGER", "DJELFA",

        "JUEL", "SETIF", "SAIDA"]


ADRAR =  [0, 1335, 1042, 1671, 1489, 1588, 1366,
          578, 1493, 1534, 1042, 1698, 1147, 1339, 1610,
            1543, 1153, 1614, 1477, 1100]

CHLEF = [1335, 0, 467, 600, 599, 396, 586,
         748, 159, 297, 2033, 809, 333, 168, 327,
         208, 334, 492, 480, 226]

LAGHOUAT = [1042, 467, 0, 708, 526, 708, 403,
             642, 346, 406, 1566, 735, 660, 291, 482,
             400, 111, 734, 597, 459]


O_EL_BOUAGHI = [1671, 600, 708, 0, 148, 311, 271,
                 1471, 519, 381, 1853, 117, 996, 662, 457,
                 500, 578, 215, 200, 881]

BATNA = [1489, 599, 526, 148, 0, 280, 123,
           1368, 490, 352, 1705, 209, 848, 514, 428,
           435, 453, 265, 169, 673]

BEJAIA = [1588, 396, 708, 311, 280, 0, 305,
             1183, 276, 136, 1887, 440, 729, 478, 133,
             263, 414, 96, 111, 637]

BISKRA = [1366, 586, 403, 271, 123, 305, 0,
             1230, 448, 358, 1582, 332, 835, 501, 434,
             425, 307, 331, 194, 660]


BECHAR = [578, 748, 642, 1471, 1368, 1183, 1230,
             0, 915, 1045, 1620, 1562, 569, 681, 1075,
             965, 753, 1214, 1077, 522]


BLIDA = [1493, 159, 346, 519, 490, 276, 448,
             915, 0, 138, 1930, 650, 492, 238, 168,
             50, 276, 372, 321, 397]

BOUIRA = [1534, 297, 406, 381, 352, 136, 358,
             1045, 138, 0, 1940, 498, 613, 339, 76,
             122, 294, 234, 183, 498]


TAMANRASSET = [1042, 2033, 1566, 1853, 1705, 1887, 1582,
                 1620, 1930, 1940, 0, 1849, 2226, 1856, 2016,
                 1970, 1677, 1913, 1776, 2025]


TEBESSA = [1698, 809, 735, 117, 209, 440, 332,
             1562, 650, 498, 1849, 0, 1057, 723, 637,
             634, 662, 344, 329, 852]


TLEMCEN = [1147, 333, 660, 996, 848, 729, 835,
             569, 492, 613, 2226, 1057, 0, 334, 689,
             540, 556, 825, 796, 190]

TIARET = [1339, 168, 291, 662, 514, 498, 501,
             681, 238, 339, 1856, 723, 334, 0, 415,
             340, 222, 588, 451, 159]


TIZI_OUZOU = [1610, 327, 482, 457, 428, 133, 434,
                 1075, 168, 76, 2016, 637, 689, 415, 0,
                 103, 373, 229, 259, 574]

ALGER = [1543, 208, 400, 500, 435, 263, 425,
             965, 50, 122, 1970, 634, 580, 340, 103,
             0, 275, 359, 300, 437]


DJELFA = [1153, 344, 111, 578, 453, 414, 307,
             753, 276, 294, 1677, 662, 556, 222, 370,
             275, 0, 461, 324, 381]

JUEL = [1614, 492, 734, 215, 265, 96, 331,
 1284, 372, 234, 1913, 344, 825, 588, 229,
 359, 461, 0, 137, 733]

SETIF = [1477, 480, 597, 200, 169, 111, 194,
 1077, 321, 183, 1776, 329, 796, 451, 259,
 300, 324, 137, 0, 610]

SAIDA = [1100, 236, 459, 881, 673, 637, 660,
 522, 397, 498, 2025, 852, 190, 159, 574,
 437, 381, 733, 610, 0]


listeWilayas = [ADRAR, CHLEF, LAGHOUAT, O_EL_BOUAGHI, BATNA,

        BEJAIA, BISKRA, BECHAR, BLIDA, BOUIRA, TAMANRASSET,

        TEBESSA, TLEMCEN, TIARET, TIZI_OUZOU, ALGER, DJELFA,

        JUEL, SETIF, SAIDA]


def Parcours():
    total = 0
    for i in range(len(listeWilayas)):
        for j in range(len(listeWilayas[i])):
            distance_parcourue = listeWilayas[i][j]
            total += distance_parcourue
            print("Parcours de " + str(distance_parcourue) +"km de " +
                  str(wilayas[i]) + " a " + str(wilayas[j]) )
        print("->TOTAL: " + str(total) + "km")
        print("**************************************************\n")

Parcours()




def SolutionInitiale():
    wilayas_de_depart = listeWilayas[0]
    matrix_creuse = 0
    distance_totale = 0

    for i in range(len(wilayas_de_depart)):
        if(i != 0):
            matrix_creuse = i
            print("Parcours de " + wilayas[0] + " a " + wilayas[i])
            distance_totale += wilayas_de_depart[i]

    print("TOTAL: " + str( (distance_totale + wilayas_de_depart[len(wilayas_de_depart) - 1]) ) + "km")

    return wilayas[0]




SolutionInitiale()