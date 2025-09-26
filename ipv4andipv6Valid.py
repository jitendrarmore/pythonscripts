import re
def ip4AndIPv6Validation(ip):
    pattern = re.compile(
        r'''
        ^(
            (?:
                (25[0-5]|
                2[0-4][0-9]|
                1[0-9]{2}|
                [1-9][0-9]?|0)\.){3}
                (25[0-5]|
                2[0-4][0-9]|
                1[0-9]{2}|
                [1-9][0-9]?|0)
        | 
        (
        #ipv6
            ([0-9a-fA-F]{1,4}:){7}
            ([0-9a-fA-F]{1,4})
        )
        )$
        ''', re.VERBOSE
    )


    # pattern = re.compile(r'''
    #     ^(
    #         # IPv4
    #         (?:
    #             (25[0-5]|               # 250-255
    #             2[0-4][0-9]|            # 200-249
    #             1[0-9]{2}|              # 100-199
    #             [1-9][0-9]?|            # 1-99
    #             0)                      # 0
    #             \.
    #         ){3}
    #         (25[0-5]|
    #          2[0-4][0-9]|
    #          1[0-9]{2}|
    #          [1-9][0-9]?|0)
    #     |
    #
    #         # IPv6
    #         (
    #         ([0-9a-fA-F]{1,4}:){7}
    #         ([0-9a-fA-F]{1,4})
    #         )
    #     )$
    #         ''', re.VERBOSE)

    if pattern.match(ip) and '.' in ip:
        print("IPv4")
    elif pattern.match(ip) and ':' in ip:
        print("IPv6")
    else:
        print("Neither")

ip4AndIPv6Validation("192.168.1.1")



