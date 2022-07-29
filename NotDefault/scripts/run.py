from brownie import accounts, NotDefault, Exp
from rich import print as rp

def main():
    rp('[bold green]------------ Supremacy Inc. ------------[/]')
    rp('[bold green]-------------- VyperPunk --------------[/]\n')
    deployer = accounts[0]
    hacker = accounts.at('0xc95C558dAA63b1A79331B2AB4a2a7af375384d3B', force=True)

    notdefault = NotDefault.deploy({
        'from': deployer
    })

    Exp.deploy(notdefault, {
        'from': hacker
    })

    ##############################
    #     Write Exp code here    #
    #         /\_/\   /          #
    #    ____/ o o \             #
    #  /~____  =ø= /             #
    # (______)__m_m)             #
    ##############################
    
    rp('[bold green]-------------- End --------------[/]')
