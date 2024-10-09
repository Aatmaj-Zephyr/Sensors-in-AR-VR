import socket
def format_number_to_hex(number):
    # Convert the number to hexadecimal and remove the '0x' prefix
    hex_value = format(number, '08x')
   
    # Split the hex string into pairs of two characters
    hex_pairs = [hex_value[i:i+2] for i in range(0, len(hex_value), 2)]
   
    # Join the pairs with a space to match the format
    formatted_hex = ' '.join(hex_pairs)
   
    return formatted_hex

def send_mbox_udp_request(a,b,c):
    a=int(a*300000/100)
    b=int(b*300000/100)
    c=int(c*300000/100)
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # The target IP and port (change as per your setup)
    target_ip = '255.255.255.255'  # Broadcast IP
    target_port = 7408  # Target port
    sock.bind(('0.0.0.0', 8410))

    # Construct the UDP packet payload (hex to bytes)
    # Payload taken from the provided dump
    payload = bytes.fromhex(
        '55 AA 00 00 13 01 00 01 FF FF FF FF 00 00 00 01 00 00 00 0A'+ format_number_to_hex(a) +format_number_to_hex(b)+format_number_to_hex(c)+
        '00 01 86 A0 00 01 86 A0 00 01 86 A0 00 00 00 00 00 00'
    )

    # Send the UDP packet to the target IP and port
    try:
        # Enable broadcasting mode if required
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Send the UDP packet
        sock.sendto(payload, (target_ip, target_port))
        print(f"UDP packet sent to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Failed to send UDP packet: {e}")
    finally:
        # Close the socket
        sock.close()

# Call the function to send the UDP packet
send_mbox_udp_request(80,80,80)
