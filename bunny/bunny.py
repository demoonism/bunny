from .emo import Emo

bear = (['|￣￣￣￣￣￣￣￣|',
         '|    TRAINING    |',
         '|     epoch      |',
         '| ＿＿＿_＿＿＿＿|',
         '        ||',
         '  ʕ•͡ᴥ•ʔ ||',
         '  /   づ'])

bunny = (['|￣￣￣￣￣￣￣￣|',
          '|    TRAINING    |',
          '|     epoch      |',
          '| ＿＿＿_＿＿＿＿|',
          ' (\__/) ||',
          ' (•ㅅ•) || ',
          ' / 　 づ'])

cat = (['|￣￣￣￣￣￣￣￣|',
        '|    TRAINING    |',
        '|     epoch      |',
        '| ＿＿＿_＿＿＿＿|',
        './\…/\.  ||',
        '=‘•..•’= ||',
        '.♥**♥  づ',
        '(.\. .)♥¸.•*°☼'])


class Bunny(Emo):
    def __init__(self, iterable, emoji='bunny'):
        if emoji == 'bunny':
            super().__init__(iterable, bunny)
        elif emoji == 'bear':
            super().__init__(iterable, bear)
        elif emoji == 'cat':
            super().__init__(iterable, cat)
        else:
            # default to bunny
            super().__init__(iterable, bunny)
