from emo import Emo

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

class bunny(Emo):
    def __init__(self, iterable, emoji='bunny'):
        if emoji == 'bunny':
            super().__init__(iterable, bunny)
        elif emoji == 'bear':
            super().__init__(iterable, bear)
        else:
            # default to bunny
            super().__init__(iterable, bunny)
