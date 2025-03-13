import pandas as pd

# Load the Excel file
file_path = "ip.xlsx"  # Update with the correct path if needed

# Read the Excel file without headers
df = pd.read_excel(file_path, header=None)

# Function to extract and format the IP, port, and protocol
def format_ip_port_protocol(row):
    parts = str(row[0]).split(" / ")  # Split based on " / "
    if len(parts) == 3:
        ip, port, protocol = parts
        return f"{ip}:{port} [{protocol.upper()}]"
    return None

# Apply the function to extract and format the data
df['Formatted'] = df.apply(format_ip_port_protocol, axis=1)

# Drop empty values and display the result
df = df[['Formatted']].dropna()

# Save the output to a new Excel file
df.to_excel("Formatted_IPs.xlsx", index=False)

# Print the output
print(df)
