import subprocess

def test_speed():
    speedtest_cmd = "speedtest-cli --bytes --simple"
    process = subprocess.Popen(speedtest_cmd.split(), stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output

output = test_speed()
print(output)