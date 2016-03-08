dbname = 'db.sqlite3'
rule = 'sudo iptables -t nat -I mac_check 2 -m mac --mac-source %s -j RETURN'
