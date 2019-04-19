from random import randint

def get_match_data():
    """
    Match data
    """

    match = [
        ("Simmons", 3),
        ("Patel", 4),
        ("Rayudu", 12),
        ("Rohit", 24),
        ("Krunal", 53),
        ("Pollard", 7),
        ("Hardik", 10),
        ("Karn", 1),
        ("Johnson", 13),
        ("Rahane", 44),
        ("Tripathi", 3),
        ("Smith", 51),
        ("Dhoni", 10),
        ("Tiwary", 7),
        ("Christian", 4),
        ("Sundar", 0),
        ("p17", 0),
        ("p18", 0),
        ("p19", 0),
        ("p20", 0),
        ("p21", 0),
        ("p22", 0),
    ]


    return match


def gen_ratings():
    """
    Generate ratings
    """

    scores = [
        ("Simmons", 3),
        ("Patel", 4),
        ("Rayudu", 12),
        ("Rohit", 24),
        ("Krunal", 53),
        ("Pollard", 7),
        ("Hardik", 10),
        ("Karn", 1),
        ("Johnson", 13),
        ("Rahane", 44),
        ("Tripathi", 3),
        ("Smith", 51),
        ("Dhoni", 10),
        ("Tiwary", 7),
        ("Christian", 4),
        ("Sundar", 0),
        ("p17", 0),
        ("p18", 0),
        ("p19", 0),
        ("p20", 0),
        ("p21", 0),
        ("p22", 0),
    ]

    return [(player_x, randint(1350, 1750)) for player_x, score_x in scores]


def get_current_ratings():
    """
    Current ratings
    """

    ratings = [('Simmons', 1689), ('Patel', 1611), ('Rayudu', 1644), ('Rohit', 1563), ('Krunal', 1688), ('Pollard', 1486), ('Hardik', 1401), ('Karn', 1453), ('Johnson', 1652), ('Rahane', 1699), ('Tripathi', 1463), ('Smith', 1580), ('Dhoni', 1417), ('Tiwary', 1689), ('Christian', 1432), ('Sundar', 1505), ('p17', 1612), ('p18', 1388), ('p19', 1585), ('p20', 1399), ('p21', 1372), ('p22', 1466)]

    return {player: rating for player, rating in ratings}


def calc_run_matrix(match):

    run_matrix = {}
    for player_x, score_x in match:
        for player_y, score_y in match:
            if not run_matrix.get(player_x):
                run_matrix[player_x] = {}

            run_matrix[player_x][player_y] = 0

            if score_x == score_y:
                run_matrix[player_x][player_y] = 0.5

            if score_x > score_y:
                run_matrix[player_x][player_y] = 1

    return run_matrix



def f_matrix(match):

    f_matrix = {}
    for player_x, score_x in match:
        for player_y, score_y in match:
            if not f_matrix.get(player_x):
                f_matrix[player_x] = {}

            f_matrix[player_x][player_y] = 32

    return f_matrix

def exp_matrix(match):
    """
    ExpA(result) = 10^(A old rating/400) / ( 10^(A old rating/400) + 10^(B old rating/400) )
    """

    ratings = get_current_ratings()

    exp_matrix = {}
    for player_x, score_x in match:
        ratin_player_x = ratings.get(player_x, 1500)

        for player_y, score_y in match:
            if not exp_matrix.get(player_x):
                exp_matrix[player_x] = {}

            ratin_player_y = ratings.get(player_y, 1500)

            exp_player_x = 10 ** (ratin_player_x/400)
            exp_player_y = 10 ** (ratin_player_y/400)

            exp_matrix[player_x][player_y] = round(exp_player_x / (exp_player_x + exp_player_y), 2)

    return exp_matrix


def calc_new_ratings(match):
    """
    New Rating A = Old Rating A + sum(k * (result A - ExpA(result)))

    """
    res_matrix_inst = calc_run_matrix(match)
    f_matrix_inst = f_matrix(match)
    exp_matrix_inst = exp_matrix(match)
    ratings = get_current_ratings()

    new_ratings = {}
    for player_x, score_x in match:
        ratin_player_x = ratings.get(player_x, 1500)

        rating_delta = 0
        for player_y, score_y in match:
            rating_delta += f_matrix_inst[player_x][player_y] * (res_matrix_inst[player_x][player_y] - exp_matrix_inst[player_x][player_y])

        rating_delta = round(rating_delta / (len(match) - 1), 0)

        new_ratings[player_x] = ratin_player_x + rating_delta


    return new_ratings



# calc_run_matrix(get_match_data())
