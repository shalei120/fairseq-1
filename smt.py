import os

import argparse
name2sh = {
    # 'deenbet-dec': ['deen_bet_dec', 'de-en-BET-dec'],
    # 'deenbet-dec-dm': ['deen_bet_dec-dm','de-en-BET-dec=dm'],
    # 'deenbet-enc': ['deen_bet_enc','de-en-BET-enc'],
    # 'deenbet-enc-dm': ['deen_bet_enc-dm','de-en-BET-enc=dm'],
    # 'deenbet-encdec': ['deen_bet_encdec','de-en-BET-encdec'],
    # 'deenbet-encdec-dm': ['deen_bet_encdec-dm','de-en-BET-encdec=dm'],
    # 'endebet-dec': ['ende_bet_dec','en-de-BET-dec'],
    'endebet-dec-dm': ['ende_bet_dec-dm','en-de-BET-dec=dm'],

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
            os.system('echo "password" | sudo -S rm -r ./checkpoints/' + tasksh[1])


    elif choose == 'submit':
        for taskname, tasksh in name2sh.items():
            os.system('sh submitdgx.sh -n '+ taskname + ' -m '+tasksh[0])

