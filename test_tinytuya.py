import tinytuya
import base64


# get data, rememeber to create your own data.txt and write the below info in order
with open("data.txt", "r") as f:
    DEVICE_ID = f.readline(). replace('\n', '')
    LOCAL_KEY = f.readline(). replace('\n', '')
    DEVICE_IP = f.readline(). replace('\n', '')
DP_ID = 51


# create base64 string
def control_lamp(white_switch, RGB_switch, white_brightness, RGB_brightness, RGB_color_white_level, RGB_color, white_temperature):
    control_string = ["0" for _ in range(12 * 8)]
    control_string[13] = "1"
    if (white_switch):
        control_string[15] = "1"
    if (RGB_switch):
        control_string[14] = "1"
    control_string[64:80] = list(format(white_brightness, f"0{16}b"))
    control_string[48:64] = list(format(RGB_brightness, f"0{16}b"))
    control_string[32:48] = list(format(RGB_color_white_level, f"0{16}b"))
    control_string[16:32] = list(format(RGB_color, f"0{16}b"))
    control_string[80:96] = list(format(white_temperature, f"0{16}b"))
    binary_number = int("".join(control_string), 2)
    binary_bytes = binary_number.to_bytes((len(control_string) + 7) // 8, byteorder='big')
    base64_encoded = base64.b64encode(binary_bytes).decode("utf-8")
    return base64_encoded


base64_string = control_lamp(True, True, 1000, 600, 600, 400, 200)
print(base64_string)

# Connect to the Tuya device
device = tinytuya.OutletDevice(DEVICE_ID, DEVICE_IP, LOCAL_KEY)
device.set_version(3.4)  # Ensure the correct protocol version

# Send the decoded data to the specific DP
response = device.set_value(DP_ID, base64_string)

# Print response
print("Response:", response)
