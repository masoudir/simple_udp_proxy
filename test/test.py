from simple_udp_proxy import simple_udp_proxy as px

px.is_verbose = True
px.is_log_enabled = True


proxy = px.UdpProxy(in_port=14553, out_port=1220, buf_size=1024)

while True:
    pass