from ticket import Ticket
from vip import VIP
from normal import Normal
from lower_stateroom import LowerStateroom
from superior_stateroom import SuperiorStateroom

def main():
    ticket = Ticket(100)
    vip_ticket = VIP(100, 50)
    normal_ticket = Normal(100)
    lower_stateroom = LowerStateroom(100, 50, "Lower Deck")
    superior_stateroom = SuperiorStateroom(100, 50, 30)

    print(f'Valor do ingresso comum: R${ticket.get_value()}')
    print(f'Valor do ingresso VIP: R${vip_ticket.get_value()}')
    print(f'Valor do ingresso normal: R${normal_ticket.get_value()}')
    print(f'Valor do Lower Stateroom: R${lower_stateroom.get_value()}')
    print(f'Valor do Superior Stateroom: R${superior_stateroom.get_value()}')

    lower_stateroom.print_location()

if __name__ == "__main__":
    main()
