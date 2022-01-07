class Ping:
    TABLE = "Ping"

    class Columns:
        EVENT_TIME = "EventTime"
        IP = "IP"
        DOMAIN_NAME = "DomainName"
        IP_DESCRIPTION = "IPDescription"
        RESPONSE_TIME = "ResponseTime"
        PACKET_LOSS = "PacketLoss"

        ALL = [EVENT_TIME, IP, DOMAIN_NAME, IP_DESCRIPTION, RESPONSE_TIME, PACKET_LOSS]