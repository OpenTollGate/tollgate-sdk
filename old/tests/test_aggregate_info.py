import json
import subprocess
import os
import pytest
import re

# Define constants for file paths
SDK_DIR = "/tmp/test_packages/openwrt-sdk-23.05.0-aarch64_cortex-a53"
IPK_DIR = SDK_DIR + "/packages"
ARCH_DIR = IPK_DIR + "/aarch64_cortex-a53"
os.makedirs(ARCH_DIR, exist_ok=True)
FEEDS_PARENT = SDK_DIR # "/tmp"
MAKEDIR = os.path.join(FEEDS_PARENT, "feeds/custom/dummy/")
os.makedirs(os.path.dirname(MAKEDIR), exist_ok=True)
MAKEFILE = os.path.join(MAKEDIR, "Makefile")
FEEDS_CONF = os.path.join(SDK_DIR, "feeds.conf")
AGGREGATE_INFO_SCRIPT = "aggregate_info.py"

@pytest.fixture(scope="module")
def setup_teardown():
    # Setup: Create dummy files and directories
    os.makedirs(os.path.dirname(IPK_DIR), exist_ok=True)
    os.makedirs(ARCH_DIR, exist_ok=True)
    with open(os.path.join(ARCH_DIR, "dummy_package_1.ipk"), "w") as f:
        f.write("")
    with open(os.path.join(ARCH_DIR, "dummy_package_2.ipk"), "w") as f:
        f.write("")
    with open(FEEDS_CONF, "w") as f:
        f.write("""src-git base git://github.com/openwrt/packages\n""")
        f.write("""src-link custom /usr/lib/openwrt/custom-feeds/packages\n""")

    with open(MAKEFILE, "w") as f:
        f.write("""PKG_SOURCE_URL:=https://github.com/OpenTollGate/tollgate-module-relay-go.git\n""")
        f.write("""PKG_SOURCE_VERSION:=main\n""")
    
    # Yield control to the test function
    yield

    # Teardown: Remove the created files and directories
    import shutil
    os.remove(FEEDS_CONF)
    shutil.rmtree(SDK_DIR)


def test_blossom_installed():
    result = subprocess.run(["blossom", "--version"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "debug" in result.stdout

def test_aggregate_info_simple(setup_teardown):
    import re

    # Run the aggregate_info.py script and capture the output
    command = ["python3", AGGREGATE_INFO_SCRIPT, ARCH_DIR, FEEDS_CONF, FEEDS_PARENT]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    output_json = result.stdout

    # Remove log messages from the beginning of the JSON output
    output_json = re.sub(r"^[\s\S]*?{", "{", output_json)


    print("Command:" + str(command))
    print("Result:" + str(result))
    print("Output json:" + str(output_json))

    # Load the JSON output
    data = json.loads(output_json)
    print("Data:" + str(data))
    
    assert "binaries" in data
    assert "target_info" in data
    assert "feed_info" in data

    # Check if the dummy packages are listed in the binaries
    assert "dummy_package_1.ipk" in data["binaries"]
    assert "dummy_package_2.ipk" in data["binaries"]

    # Basic check for target_info (adjust based on expected default values)
    assert isinstance(data["target_info"], dict)

    assert isinstance(data["feed_info"], dict)
    assert len(data["feed_info"]) > 0
    #assert "feed_info" in data

    # Check if the dummy packages are listed in the binaries
    #assert "dummy_package_1.ipk" in data["binaries"]
    #assert "dummy_package_2.ipk" in data["binaries"]

    # Basic check for target_info (adjust based on expected default values)
    #assert isinstance(data["target_info"], dict)

    # Check for feed_info entries
    #assert isinstance(data["feed_info"], list)
    #assert len(data["feed_info"]) > 0
