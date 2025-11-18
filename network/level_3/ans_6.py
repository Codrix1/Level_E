
import psutil

def get_active_connections():
    # Get the active TCP connections
    connections = psutil.net_connections(kind='tcp')
    connection_details = []

    for conn in connections:

        local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
        foreign_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        
        state = conn.status
        

        pid = conn.pid
        process_name = None
        if pid:
            try:
                process = psutil.Process(pid)
                process_name = process.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                process_name = "N/A"

        connection_details.append({
            "Local Address": local_address,
            "Foreign Address": foreign_address,
            "State": state,
            "PID": pid,
            "Process Name": process_name,
        })

    return connection_details

def display_connections(connections):
    print(f"{'Local Address':<30} {'Foreign Address':<30} {'State':<15} {'PID':<10} {'Process Name':<25}")
    print("=" * 120)
    for conn in connections:
        print(f"{conn['Local Address']:<30} {conn['Foreign Address']:<30} {conn['State']:<15} {conn['PID']:<10} {conn['Process Name']}")

if __name__ == "__main__":
    active_connections = get_active_connections()
    display_connections(active_connections)