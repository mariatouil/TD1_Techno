import argparse
import sys

from Game import Game


def make_argparser():

    parser = argparse.ArgumentParser(description='Command Ligne Interface.')

    parser.add_argument('--config', action='store_true', default=False,
                        help='run game configuration')

def main(args):
    """Main function
    """
    parser = make_argparser()
    opts = parser.parse_args(args)

    game = Game()
    
    if opts.config:
        game.config()

if __name__ == "__main__":
    ret = main(sys.argv[1:])
    sys.exit(ret)