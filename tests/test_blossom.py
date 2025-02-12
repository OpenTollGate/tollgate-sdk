
import pytest
import subprocess
import json
import os
import hashlib
import tempfile
import shutil
from nostr.event import Event
from nostr.key import PrivateKey
from nostr.relay_manager import RelayManager
import time
import ssl

# Constants
SCRIPT_PATH = "../blossom_upload.py"
TEST_FILE_CONTENT = "This is a test file for blossom upload."
SECRETS_FILE = "../blossom_secrets.json"


def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


@pytest.fixture(scope="module")
def test_environment(tmpdir_factory):
    """
    Sets up the test environment:
    1. Creates a temporary directory.
    2. Creates a test file with known content.
    """
    tmpdir = tmpdir_factory.mktemp("test_env")

    # Create test file
    test_file = tmpdir.join("test_file.txt")
    test_file.write(TEST_FILE_CONTENT)
    original_hash = calculate_sha256(str(test_file))

    return {
        "test_file": str(test_file),
        "original_hash": original_hash,
        "tmpdir": str(tmpdir),
    }


def test_blossom_command_exists():
    """Check if the 'blossom' command is available in the PATH."""
    try:
        subprocess.run(["blossom", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        pytest.fail("The 'blossom' command is not in the PATH.  Make sure it is installed correctly.")


def test_secrets_file_exists():
    """Check if the secrets file exists if NOSTR_SECRET_KEY is not set."""
    if "NOSTR_SECRET_KEY" not in os.environ:
        secrets_path = os.path.join(os.path.dirname(__file__), SECRETS_FILE)
        if not os.path.exists(secrets_path):
            pytest.fail(
                f"The 'NOSTR_SECRET_KEY' environment variable is not set, and the secrets file '{secrets_path}' does not exist.  "
                f"Make sure the secrets file is in the same directory as the test, or set the environment variable."
            )


def test_blossom_upload(test_environment):
    """
    Tests the blossom_upload.py script.
    """
    test_file = test_environment["test_file"]
    original_hash = test_environment["original_hash"]
    tmpdir = test_environment["tmpdir"]

    # Set environment variable (if not already set)
    if "NOSTR_SECRET_KEY" not in os.environ:
        # Attempt to read the secret key from blossom_secrets.json
        try:
            secrets_path = os.path.join(os.path.dirname(__file__), SECRETS_FILE)
            with open(secrets_path) as f:
                secrets = json.load(f)
                secret_key = secrets['secret_key']
                os.environ["NOSTR_SECRET_KEY"] = secret_key
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            pytest.fail(f"Error reading secrets file: {str(e)}")

    # Run the script
    script_path = os.path.join(os.path.dirname(__file__), SCRIPT_PATH)
    result = subprocess.run(
        ["python3", script_path, test_file],
        capture_output=True,
        text=True,
        cwd=tmpdir,
    )

    # Assert that the script ran successfully
    assert result.returncode == 0, f"Script failed: {result.stderr}"

    assert original_hash in result.stdout, f"Hash not found in output: {result}"


def test_nostr_publish():
    """Tests publishing a note using the nostr library."""
    note_content = "This is a test note published again using the nostr library."

    # Load secrets
    secrets_path = os.path.join(os.path.dirname(__file__), SECRETS_FILE)
    with open(secrets_path) as f:
        secrets = json.load(f)
        secret_key_hex = secrets['secret_key_hex']
        relays = secrets['relays']

    print(secret_key_hex)

    # Create a private key object
    private_key = PrivateKey(bytes.fromhex(secret_key_hex))

    # Create an event
    event = Event(content=note_content, public_key=private_key.public_key.hex())
    private_key.sign_event(event)

    successful_publish = False
    
    # Try each relay individually
    for relay_url in relays:
        try:
            # Initialize relay manager with single relay
            relay_manager = RelayManager()
            relay_manager.add_relay(relay_url)
            
            relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})
            time.sleep(1.25)  # give the relay time to connect
            
            # Attempt to publish
            relay_manager.publish_event(event)
            time.sleep(1)  # wait for publishing
            
            successful_publish = True
            print(f"Successfully published to {relay_url}")
            
        except Exception as e:
            print(f"Failed to publish to {relay_url}: {str(e)}")
        
        finally:
            try:
                relay_manager.close_connections()
            except:
                pass
        
        # Break if we've had a successful publish
        if successful_publish:
            break
    
    # Assert that at least one relay worked
    assert successful_publish, "Failed to publish to any relay"
