import os

import argparse
name2sh = {
    'deenbet-dec': 'deen_bet_dec',
    'deenbet-dec-dm': 'deen_bet_dec-dm',
    'deenbet-enc': 'deen_bet_enc',
    'deenbet-enc-dm': 'deen_bet_enc-dm',
    'deenbet-encdec': 'deen_bet_encdec',
    'deenbet-encdec-dm': 'deen_bet_encdec-dm',

}



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--choose', '-c')
    cmdargs = parser.parse_args()

    if cmdargs.choose is None:
        pass
    else:
        choose = cmdargs.choose

    if choose == 'del':

        for taskname, tasksh in name2sh.items():
            os.system('runai delete '+ taskname)


    elif choose == 'submit':
        for taskname, tasksh in name2sh.items():
            os.system('sh submitdgx.sh -n '+ taskname + ' -m '+tasksh)

