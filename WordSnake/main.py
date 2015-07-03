# WordSnake

# Note: Ctrl+Shift+F10 runs the function you're currently on
# Shift+F10 runs the last function you had selected (SUPER USEFUL!)

import snake


def main():
    input_words = "SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE"
    input_words = input_words.split()
    snake_ = snake.Snake(input_words)
    snake_.printShape()

    return


if __name__ == '__main__':
    main()