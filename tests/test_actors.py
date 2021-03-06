from Queue import Empty

from cs143sim.actors import Buffer
from cs143sim.actors import Flow
from cs143sim.actors import Host
from cs143sim.actors import Link
from cs143sim.actors import DataPacket
from cs143sim.actors import RouterPacket
from cs143sim.actors import Router
from cs143sim.simulation import Controller
from cs143sim.simulation import ControlledEnvironment


def basic_buffer():
    return Buffer(env=ControlledEnvironment(controller=Controller()),
                  capacity=1, link=basic_link())


def basic_flow():
    return Flow(env=ControlledEnvironment(controller=Controller()),
                name='', source=basic_host(), destination=basic_host(),
                amount=1.0)


def basic_host():
    return Host(env=ControlledEnvironment(controller=Controller()),
                name='', address='')


def basic_link():
    return Link(env=ControlledEnvironment(controller=Controller()),
                name='', source=basic_host(), destination=basic_host(),
                delay=1.0, rate=1.0, buffer_capacity=1)


def basic_packet():
    #return Packet(source=basic_host(), destination=basic_host(), number=1,
    #              acknowledgement=object())
    return DataPacket(source=basic_host(), destination=basic_host(),
                      number=1, acknowledgement=object(), timestamp=0)


def basic_router_packet():
    return RouterPacket(source=basic_host(), timestamp=0, router_table={},
                        acknowledgement=False)


def basic_router():
    return Router(env=ControlledEnvironment(controller=Controller()),
                  name='', address='')


def buffer_overflow():
    buffer_capacity = 2
    number_of_packets = 3
    buffer_ = basic_buffer()
    buffer_.env.controller.packet_loss[buffer_.link] = []
    packets = []
    for _ in range(number_of_packets):
        packet_ = basic_packet()
        packet_.size = 1
        packets.append(packet_)
    buffer_.capacity = buffer_capacity
    for packet_ in packets:
        buffer_.add(packet_)
        print(buffer_.packets)
    buffer_packets = []
    while True:
        try:
            buffer_packets.append(buffer_.get(timeout=1))
        except Empty:
            break
    for i in range(number_of_packets):
        if i < buffer_capacity:
            assert packets[i] in buffer_packets
        else:
            assert packets[i] not in buffer_packets


def link_busy():
    link_ = basic_link()
    assert link_.buffer.capacity == 1
    packet_ = basic_packet()
    packet_.size = 1
    link_.busy = True
    link_.add(packet_)
    #assert packet_ in link_.buffer.packets


def router_initialize():
    router_ip_address = '1'
    router = basic_router()
    router.address = router_ip_address
    #router.default_gateway = '5'
    links = []
    number_of_links = 2
    
    link1_ = basic_link()
    link1_.destination = router
    link2_ = basic_link()
    link2_.source = router
    links.append(link1_)
    links.append(link2_)

    router.links = links
    assert link2_ in router.links
    assert link1_ == router.links[0]

    all_host_ip_addresses = ['11','12','13','14']
    router.initialize_routing_table(all_host_ip_addresses)


def router_forward():
    Dpacket = basic_packet()
    
    Dpacket.destination = 'H1'

    router = basic_router()

    link1_ = basic_link()
    link1_.destination = 'H1'

    router.table = {}
    router.table['H1'] = 5, 'R4'
    router.table['H2'] = 6, 'R5'
    router.table['H3'] = 7, 'R6'
    router.map_route(Dpacket)


def router_receive_update_packet():
    # packet_ = basic_packet()
    # link_1 = basic_link()
    # link_2 = basic_link()
    # router_ = basic_router()
    # router_.links.extend([link_1, link_2])
    # router_.do_things()

    Rpacket = basic_router_packet()
    
    Rpacket.source = 'R9'
    Rpacket.router_table['H1'] = 5, 'R4'
    Rpacket.router_table['H2'] = 6, 'R5'
    Rpacket.router_table['H3'] = 3, 'R3'

    router = basic_router()
    router.table = {}
    router.table['H1'] = 5, 'R4'
    router.table['H2'] = 6, 'R5'
    router.table['H3'] = 7, 'R6'
    router.update_router_table(Rpacket)
    assert router.table['H3'] == (4, 'R9')
    #=========== ===========
    Dpacket = basic_packet()


def router_send_update_packet():
    router = basic_router()
    router.address = 'R9'

    links = []
    number_of_links = 2
    
    link1_ = basic_link()
    link1_.destination = router
    link2_ = basic_link()
    link2_.source = router
    links.append(link1_)
    links.append(link2_)

    router.links = links

    router.table = {}
    router.table['H1'] = 5, 'R4'
    router.table['H2'] = 6, 'R5'
    router.table['H3'] = 7, 'R6'
    
    router.generate_router_packet()
    # assert len(link1_.buffer.packets) == 1
    
    pass


def test_buffer():
    basic_buffer()
    buffer_overflow()


def test_flow():
    basic_flow()


def test_host():
    basic_host()


def test_link():
    basic_link()
    link_busy()


def test_packet():
    basic_packet()


def test_router():
    basic_router()
    # router_initialize()
    # router_forward()
    # router_receive_update_packet()
    router_send_update_packet()
