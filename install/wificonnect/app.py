import subprocess
import time
from flask import Flask, render_template, request, redirect, url_for, flash



def check_wifi():
    try:
        result = subprocess.check_output(["nmcli", "--terse", "connection", "show"], capture_output=True, text=True)
        wifi_connections = [line.split(':')[1] for line in result.stdout.splitlines() if "Wired" not in line and "Hotspot" not in line][0]
        if wifi_connections:
            print(f"Connected to WiFi network: {wifi_connections}")
            subprocess.run(["systemctl stop wificonnect"])
    except Exception as e:
        pass


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

adhoc_network_ssid = "Miniprintbox"  # Change this to your desired adhoc network SSID

# Delete existing adhoc network
connection_names = subprocess.run(["nmcli", "--terse", "connection", "show"], capture_output=True, text=True)
hotspot_connections = [line.split(':')[0] for line in connection_names.stdout.splitlines() if "802-11-wireless" in line and "Hotspot" in line]

    # Disconnect and delete "Hotspot" connections
for connection in hotspot_connections:
    subprocess.run(["nmcli", "connection", "down", connection])
    subprocess.run(["nmcli", "connection", "delete", connection])




# Function to scan available Wi-Fi networks and create an adhoc network
def scan_and_create_adhoc(ssid, password):
    try:
        result = subprocess.check_output(["nmcli", "-t", "-f", "SSID", "device", "wifi", "list"])
        print(result)
        networks = result.decode("utf-8").strip().split('\n')
        networks = [network.strip() for network in networks]
        time.sleep(5) #allow time to scan for wifi networks



        # Create the adhoc network
        subprocess.run(["nmcli", "device", "wifi", "hotspot", "ssid", ssid, "password", password], check=True)
        time.sleep(5)  # Wait for a few seconds to ensure the adhoc network is ready

        return networks
    except Exception as e:
        return [str(e)]

# Function to stop the adhoc network
def stop_adhoc_network():
    try:
        connection_names = subprocess.run(["nmcli", "--terse", "connection", "show"], capture_output=True, text=True)
        hotspot_connections = [line.split(':')[0] for line in connection_names.stdout.splitlines() if "Hotspot" in line]

        # Disconnect and delete "Hotspot" connections
        for connection in hotspot_connections:
            subprocess.run(["nmcli", "connection", "down", connection])
            subprocess.run(["nmcli", "connection", "delete", connection])
        return True
    except Exception as e:
        return False

# Function to connect to an existing Wi-Fi network
def connect_to_wifi(ssid, password):
    try:
        time.sleep(5)
        subprocess.run(["nmcli", "device", "wifi", "connect", ssid, "password", password], check=True)
        if check_internet_connectivity():
            flash("Connected to {} successfully! Internet connection is working.".format(ssid))
            subprocess.run(["systemctl stop wificonnect"])

    except Exception as e:
        return False


# Function to check internet connectivity using ping
def check_internet_connectivity():
    try:
        subprocess.run(["ping", "-c", "1", "1.1.1.1"])
        subprocess.run(["systemctl stop wificonnect"])
        return True
    except Exception as e:
        return False

# Scan available Wi-Fi networks and create the adhoc network
networks = scan_and_create_adhoc(adhoc_network_ssid, "letsprint")  # Change the password as needed

@app.route('/')
def index():
    return render_template('index.html', networks=networks)

@app.route('/connect', methods=['POST'])
def connect():
    selected_network = request.form.get('network')
    password = request.form.get('password')

    if not selected_network:
        flash("Please select a WiFi network.")
        return redirect(url_for('index'))

    if not password:
        flash("Please enter a password.")
        return redirect(url_for('index'))

    # Stop the adhoc network (if running)
    stop_adhoc_network()

    if networks:
        # Attempt to connect to the selected network
        success = connect_to_wifi(selected_network, password)

        if success:
            flash(f"Connected to {selected_network} successfully!")

            # Check internet connectivity
            if check_internet_connectivity():
                flash("Internet connection is working.")
            else:
                flash("No internet connection.")

        else:
            flash(f"Failed to connect to {selected_network}. Check the password.")
    else:
        flash("Failed to scan available networks. Check the configuration.")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4298)

