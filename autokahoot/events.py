from enum import IntEnum


class Events(IntEnum):
    UNKNOWN = 0
    GET_READY = 1
    START_QUESTION = 2
    GAME_OVER = 3
    TIME_UP = 4
    PLAY_AGAIN = 5
    ANSWER_SELECTED = 6
    ANSWER_RESPONSE = 7
    REVEAL_ANSWER = 8
    START_QUIZ = 9
    RESET_CONTROLLER = 10
    SUBMIT_FEEDBACK = 11
    FEEDBACK = 12
    REVEAL_RANKING = 13
    USERNAME_ACCEPTED = 14
    USERNAME_REJECTED = 15
    REQUEST_RECOVERY_DATA_FROM_PLAYER = 16
    SEND_RECOVERY_DATA_TO_CONTROLLER = 17
    JOIN_TEAM_MEMBERS = 18
    JOIN_TEAM_MEMBERS_RESPONSE = 19
    START_TEAM_TALK = 20
    SKIP_TEAM_TALK = 21
    IFRAME_CONTROLLER_EVENT = 31
    SERVER_IFRAME_EVENT = 32
    STORY_BLOCK_GET_READY = 40
    REACTION_SELECTED = 41
    REACTION_RESPONSE = 42
    GAME_BLOCK_START = 43
    GAME_BLOCK_END = 44
    GAME_BLOCK_ANSWER = 45
    SUBMIT_2FA = 50
    INCORRECT_2FA = 51
    CORRECT_2FA = 52
    RESET_2FA = 53
