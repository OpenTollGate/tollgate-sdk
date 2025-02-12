import json
import subprocess
import os
import pytest
import re
import time

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
# Get the absolute path to the parent directory of tests
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGGREGATE_INFO_SCRIPT = os.path.join(BASE_DIR, "aggregate_info.py")


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

def run_with_timeout(command, timeout=30):
    """Run a command with timeout and return the result"""
    try:
        start_time = time.time()
        
        # Setup environment with PYTHONPATH
        env = os.environ.copy()
        env['PYTHONPATH'] = BASE_DIR  # Add the project root to PYTHONPATH
        
        print(f"\nDebug information:")
        print(f"BASE_DIR: {BASE_DIR}")
        print(f"PYTHONPATH being set to: {BASE_DIR}")
        print(f"Script path: {AGGREGATE_INFO_SCRIPT}")
        print(f"Script exists: {os.path.exists(AGGREGATE_INFO_SCRIPT)}")
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,  # Pass the modified environment
            cwd=BASE_DIR  # Run from project root
        )
        end_time = time.time()
        print(f"Command took {end_time - start_time:.2f} seconds to execute")
        return result
    except subprocess.TimeoutExpired as e:
        print(f"Command timed out after {timeout} seconds")
        print(f"Partial stdout: {e.stdout if e.stdout else 'None'}")
        print(f"Partial stderr: {e.stderr if e.stderr else 'None'}")
        raise

def test_aggregate_info_simple(setup_teardown):
    # Add debug prints
    print(f"\nChecking if directories exist:")
    print(f"ARCH_DIR exists: {os.path.exists(ARCH_DIR)}")
    print(f"FEEDS_CONF exists: {os.path.exists(FEEDS_CONF)}")
    print(f"FEEDS_PARENT exists: {os.path.exists(FEEDS_PARENT)}")
    
    # Print directory contents
    print("\nDirectory contents:")
    print(f"ARCH_DIR contents: {os.listdir(ARCH_DIR)}")
    print(f"FEEDS_PARENT contents: {os.listdir(FEEDS_PARENT)}")
    
    # Run with shorter timeout and debug info
    try:
        command = ["python3", AGGREGATE_INFO_SCRIPT, ARCH_DIR, FEEDS_CONF, FEEDS_PARENT]
        print(f"\nExecuting command: {' '.join(command)}")
        
        result = run_with_timeout(command, timeout=300)
        
        print(f"\nCommand exit code: {result.returncode}")
        print(f"Command stdout: {result.stdout[:500]}...")  # Print first 500 chars
        print(f"Command stderr: {result.stderr[:500]}...")  # Print first 500 chars
        
        # Clean and parse output
        output_json = re.sub(r"^[\s\S]*?{", "{", result.stdout)
        data = json.loads(output_json)
        
        # Assertions
        assert "binaries" in data, "Missing 'binaries' in output"
        assert "target_info" in data, "Missing 'target_info' in output"
        assert "feed_info" in data, "Missing 'feed_info' in output"
        
        # Check binaries
        binaries = data["binaries"]
        print(f"\nFound binaries: {binaries}")
        assert "dummy_package_1.ipk" in binaries
        assert "dummy_package_2.ipk" in binaries
        
        # Check other fields
        assert isinstance(data["target_info"], dict)
        assert isinstance(data["feed_info"], dict)
        assert len(data["feed_info"]) > 0
        
    except Exception as e:
        print(f"\nTest failed with error: {str(e)}")
        print(f"Current working directory: {os.getcwd()}")
        # Print environment variables that might be relevant
        print("\nRelevant environment variables:")
        for env_var in ['PATH', 'PYTHONPATH', 'PWD']:
            print(f"{env_var}: {os.environ.get(env_var, 'Not set')}")
        raise
